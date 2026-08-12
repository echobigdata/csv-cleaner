# Roadmap

These are real, useful issues for the project.

## 1. Add preview before export

**Goal:** Show a small sample of the cleaned result before writing the output file.

**Why it matters:** Users can confirm the cleanup rules before saving changes.

**Acceptance criteria:**

- Preview the first N cleaned rows
- Show selected columns and applied filters
- Do not write the output file unless the user confirms

## 2. Add batch processing for folders

**Goal:** Clean multiple CSV files in a folder with one command.

**Why it matters:** Useful for recurring reports and exported datasets.

**Acceptance criteria:**

- Accept a folder path as input
- Process all `.csv` files in the folder
- Write cleaned files to an output folder

## 3. Add date normalization

**Goal:** Normalize common date formats into one consistent format.

**Why it matters:** Better for downstream analysis and imports.

**Acceptance criteria:**

- Support common date formats
- Let users choose the output format
- Handle invalid values gracefully

## 4. Add number normalization

**Goal:** Normalize numeric values with commas, currency symbols, and blanks.

**Why it matters:** Makes CSV data easier to analyze.

**Acceptance criteria:**

- Strip currency symbols and separators
- Preserve empty values when needed
- Support configurable decimal format

## 5. Add optional web UI

**Goal:** Provide a simple browser-based interface for CSV cleaning.

**Why it matters:** Lowers the barrier for non-technical users.

**Acceptance criteria:**

- Upload a CSV file
- Configure basic cleanup rules in the browser
- Download the cleaned file
