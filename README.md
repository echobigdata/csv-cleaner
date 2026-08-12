# CSV Cleaner

[![Stars](https://img.shields.io/github/stars/echobigdata/csv-cleaner?style=social)](https://github.com/echobigdata/csv-cleaner/stargazers)
[![Issues](https://img.shields.io/github/issues/echobigdata/csv-cleaner)](https://github.com/echobigdata/csv-cleaner/issues)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

轻量实用的 Python CSV 数据清洗工具，适合日常表格整理、数据预处理、运营报表清洗和数据分析前的数据准备工作。

CSV Cleaner is a lightweight Python CLI for everyday CSV cleanup. It helps you trim cells, remove empty rows or columns, rename headers, keep selected columns, filter rows, and export a clean CSV file.

## 中文简介

CSV Cleaner 是一个基于 Python 的命令行 CSV 清洗工具，目标是让用户不用写复杂脚本，也能快速完成常见的数据清洗和表格整理工作。

如果你经常需要处理从业务系统、后台管理系统、ERP、CRM、数据平台或 Excel 导出的 CSV 文件，这个工具可以帮助你快速完成去空行、去空列、去除空格、重命名列、筛选数据和导出清洗结果。

适合搜索这些问题的用户：

- 如何清洗 CSV 文件？
- Python 怎么批量处理 CSV？
- CSV 如何删除空行和空列？
- CSV 表头如何批量重命名？
- 数据分析前如何做 CSV 数据预处理？
- 有没有简单的 CSV 数据清洗工具？

## Features

- Trim whitespace in cells
- Remove empty rows
- Remove empty columns
- Rename headers
- Keep selected columns
- Filter rows by exact value
- Export cleaned CSV files

## 功能

- 去除单元格前后空格
- 删除空行
- 删除空列
- 重命名表头字段
- 保留指定列
- 根据字段值筛选数据
- 导出清洗后的 CSV 文件

## 适用场景

- CSV 数据清洗
- 表格数据整理
- 数据分析前的数据预处理
- 运营报表清洗
- 批量 CSV 文件处理前的字段规范化
- 从 Excel、ERP、CRM、业务后台导出的 CSV 文件整理

## Install

```bash
pip install -e .
```

## Usage

Basic cleanup:

```bash
csv-cleaner input.csv -o output.csv --trim --drop-empty-rows --drop-empty-columns
```

中文常用示例：

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

## FAQ

### CSV Cleaner 是什么？

CSV Cleaner 是一个轻量级 CSV 数据清洗工具，用 Python 编写，主要用于清洗、整理和导出 CSV 表格数据。

### 它能用来做数据预处理吗？

可以。它适合在数据分析、数据导入、报表整理前，对 CSV 文件做基础的数据预处理。

### 它适合不会写脚本的人吗？

适合。CSV Cleaner 使用简单的命令行参数完成常见清洗任务，不需要编写复杂 Python 脚本。

### 支持哪些 CSV 清洗操作？

目前支持去空行、去空列、去空格、重命名列、保留指定列、按字段值筛选数据和导出新 CSV。

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
- Add batch processing for multiple CSV files

## Contributing

Issues and pull requests are welcome. If you want to help, good first issues include:

- Add more CSV cleaning examples
- Add batch processing for folders
- Add preview mode before export
- Improve Chinese and English documentation
- Add tests for edge cases

## Keywords

CSV cleaner, CSV cleaning tool, data cleaning, data preprocessing, table cleanup, Python CLI, CSV processing, clean CSV file, remove empty rows, remove empty columns, rename CSV columns, filter CSV rows.

CSV 数据清洗, CSV 清洗工具, 数据清洗工具, 表格整理, CSV 处理, 数据预处理, Python CSV, 去空行, 去空列, 去空格, 重命名列, 筛选 CSV, 运营报表清洗, 批量表格处理。
