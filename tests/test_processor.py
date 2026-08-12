from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from csv_cleaner.processor import clean_csv


class CleanCsvTests(unittest.TestCase):
    def test_basic_cleanup(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            input_file = tmp_path / "input.csv"
            output_file = tmp_path / "output.csv"
            input_file.write_text(
                "name,city,status\n Alice , Beijing ,active\n,,\nBob,Shanghai,inactive\n",
                encoding="utf-8",
            )

            stats = clean_csv(
                input_file,
                output_file,
                trim=True,
                drop_empty_rows=True,
                rename_rules=["city:location"],
                filter_rules=["status=active"],
            )

            self.assertEqual(stats["rows"], 1)
            self.assertEqual(stats["columns"], 3)
            self.assertEqual(
                output_file.read_text(encoding="utf-8-sig").splitlines(),
                ["name,location,status", "Alice,Beijing,active"],
            )


if __name__ == "__main__":
    unittest.main()
