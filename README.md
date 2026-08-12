# CSV Cleaner

CSV Cleaner is a lightweight command-line tool for everyday CSV cleanup.
It helps you trim data, remove empty rows or columns, rename headers, keep
only the columns you need, and filter rows before exporting a clean file.

## Features

- Remove empty rows
- Remove empty columns
- Trim whitespace in cells
- Rename headers
- Keep selected columns
- Filter rows by exact value

## Install

```bash
pip install -e .
```

## Usage

```bash
csv-cleaner input.csv -o output.csv --trim --drop-empty-rows --drop-empty-columns
```

Rename columns:

```bash
csv-cleaner input.csv -o output.csv --rename "old_name:new_name" --rename "city:location"
```

Keep only some columns:

```bash
csv-cleaner input.csv -o output.csv --keep-columns "name,email,city"
```

Filter rows:

```bash
csv-cleaner input.csv -o output.csv --filter "status=active" --filter "country=CN"
```

## Example

```bash
csv-cleaner data.csv -o cleaned.csv --trim --drop-empty-rows --rename "full_name:name"
```

## Development

```bash
python -m unittest
```

## Roadmap

- Add preview mode
- Add column type hints
- Add date and number normalization
- Add optional web UI
