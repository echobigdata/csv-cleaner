from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class RenameRule:
    source: str
    target: str


@dataclass(frozen=True)
class FilterRule:
    column: str
    expected: str


def _normalize_cell(value: str | None, trim: bool) -> str:
    if value is None:
        return ""
    return value.strip() if trim else value


def _parse_rename_rules(raw_rules: Iterable[str]) -> list[RenameRule]:
    rules: list[RenameRule] = []
    for raw in raw_rules:
        if ":" in raw:
            source, target = raw.split(":", 1)
        elif "=" in raw:
            source, target = raw.split("=", 1)
        else:
            raise ValueError(f"Invalid rename rule: {raw!r}")
        source = source.strip()
        target = target.strip()
        if not source or not target:
            raise ValueError(f"Invalid rename rule: {raw!r}")
        rules.append(RenameRule(source=source, target=target))
    return rules


def _parse_filter_rules(raw_rules: Iterable[str]) -> list[FilterRule]:
    rules: list[FilterRule] = []
    for raw in raw_rules:
        if "=" not in raw:
            raise ValueError(f"Invalid filter rule: {raw!r}")
        column, expected = raw.split("=", 1)
        column = column.strip()
        expected = expected.strip()
        if not column:
            raise ValueError(f"Invalid filter rule: {raw!r}")
        rules.append(FilterRule(column=column, expected=expected))
    return rules


def clean_csv(
    input_path: str | Path,
    output_path: str | Path,
    *,
    trim: bool = False,
    drop_empty_rows: bool = False,
    drop_empty_columns: bool = False,
    keep_columns: list[str] | None = None,
    rename_rules: Iterable[str] = (),
    filter_rules: Iterable[str] = (),
    encoding: str = "utf-8-sig",
) -> dict[str, int]:
    input_path = Path(input_path)
    output_path = Path(output_path)
    rename_rules_parsed = _parse_rename_rules(rename_rules)
    filter_rules_parsed = _parse_filter_rules(filter_rules)

    with input_path.open("r", encoding=encoding, newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV file has no header row")

        fieldnames = list(reader.fieldnames)
        rename_map = {rule.source: rule.target for rule in rename_rules_parsed}
        fieldnames = [rename_map.get(name, name) for name in fieldnames]

        if keep_columns is not None:
            keep_set = {column.strip() for column in keep_columns if column.strip()}
            fieldnames = [name for name in fieldnames if name in keep_set]
        else:
            keep_set = None

        rows: list[dict[str, str]] = []
        for raw_row in reader:
            row = {
                rename_map.get(column, column): _normalize_cell(value, trim)
                for column, value in raw_row.items()
            }

            if keep_set is not None:
                row = {column: value for column, value in row.items() if column in keep_set}

            if filter_rules_parsed:
                matched = True
                for rule in filter_rules_parsed:
                    if _normalize_cell(row.get(rule.column), trim) != rule.expected:
                        matched = False
                        break
                if not matched:
                    continue

            if drop_empty_rows and all(value == "" for value in row.values()):
                continue

            rows.append(row)

    if drop_empty_columns and rows:
        non_empty_columns = {
            column
            for column in fieldnames
            if any(row.get(column, "") != "" for row in rows)
        }
        fieldnames = [column for column in fieldnames if column in non_empty_columns]
        rows = [{column: row.get(column, "") for column in fieldnames} for row in rows]
    else:
        rows = [{column: row.get(column, "") for column in fieldnames} for row in rows]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding=encoding, newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return {"rows": len(rows), "columns": len(fieldnames)}
