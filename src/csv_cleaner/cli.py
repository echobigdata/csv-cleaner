from __future__ import annotations

import argparse
from pathlib import Path

from .processor import clean_csv


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="csv-cleaner",
        description="Clean CSV files with simple, practical rules.",
    )
    parser.add_argument("input", type=Path, help="Input CSV file")
    parser.add_argument("-o", "--output", type=Path, required=True, help="Output CSV file")
    parser.add_argument("--trim", action="store_true", help="Trim whitespace from cells")
    parser.add_argument("--drop-empty-rows", action="store_true", help="Remove rows with no data")
    parser.add_argument(
        "--drop-empty-columns",
        action="store_true",
        help="Remove columns that are empty across all rows",
    )
    parser.add_argument(
        "--keep-columns",
        type=str,
        help="Comma-separated list of columns to keep",
    )
    parser.add_argument(
        "--rename",
        action="append",
        default=[],
        help='Rename a column using "old:new" or "old=new". Can be repeated.',
    )
    parser.add_argument(
        "--filter",
        action="append",
        default=[],
        help='Keep rows where "column=value". Can be repeated.',
    )
    parser.add_argument(
        "--encoding",
        default="utf-8-sig",
        help="File encoding for input and output",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    keep_columns = None
    if args.keep_columns:
        keep_columns = [column.strip() for column in args.keep_columns.split(",")]

    stats = clean_csv(
        args.input,
        args.output,
        trim=args.trim,
        drop_empty_rows=args.drop_empty_rows,
        drop_empty_columns=args.drop_empty_columns,
        keep_columns=keep_columns,
        rename_rules=args.rename,
        filter_rules=args.filter,
        encoding=args.encoding,
    )
    print(f"Saved {stats['rows']} rows and {stats['columns']} columns to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
