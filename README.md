# CSV Cleaner

轻量实用的 CSV 数据清洗工具，适合日常表格整理、数据预处理和简单的数据清洗任务。
支持去空行、去空列、去除空格、重命名列、筛选数据和导出清洗后的 CSV 文件。

CSV Cleaner is a lightweight Python CLI for everyday CSV cleanup.
It helps you trim cells, remove empty rows or columns, rename headers, keep
only the columns you need, and filter rows before exporting a clean file.

## 中文简介

CSV Cleaner 是一个基于 Python 的命令行 CSV 清洗工具，目标是让用户不用写复杂脚本，
也能快速完成常见的数据清洗和表格整理工作。

它适合处理运营数据、导出的业务报表、数据分析前的 CSV 预处理、批量表格清洗等场景。

## Features

- Trim whitespace in cells
- Remove empty rows
- Remove empty columns
- Rename headers
- Keep selected columns
- Filter rows by exact value

## 功能

- 去除单元格前后空格
- 删除空行
- 删除空列
- 重命名表头字段
- 保留指定列
- 根据字段值筛选数据
- 导出清洗后的 CSV 文件

## Install

```bash
pip install -e .
```

## Usage

```bash
csv-cleaner input.csv -o output.csv --trim --drop-empty-rows --drop-empty-columns
```

常用中文示例：

```bash
csv-cleaner data.csv -o cleaned.csv --trim --drop-empty-rows --drop-empty-columns
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

## Project Structure

```text
csv-cleaner/
  src/csv_cleaner/
  tests/
  pyproject.toml
  README.md
  LICENSE
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

## Keywords

CSV cleaner, CSV cleaning tool, data cleaning, table cleanup, Python CLI,
CSV 数据清洗, 数据清洗工具, 表格整理, CSV 处理, 数据预处理, 去空行, 去空列, 重命名列
