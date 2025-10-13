"""
All-in-one Integration Test Template (stdlib only)

- Focus: real boundaries you control (temp dirs/files, local SQLite).
- Pattern: AAA (Arrange → Act → Assert), deterministic inputs, clear asserts.
- Naming convention for tests:
  test___<function_under_test>___<scenario>____<expected_result>
"""

import unittest
import tempfile
from pathlib import Path
import sqlite3


# =========================
# Code under test (examples)
# =========================

def process_file(input_path: str, output_path: str) -> int:
    """
    Read a text file, trim whitespace, drop blank lines,
    write the count of non-empty lines to output, and return that count.
    Side effect: creates/overwrites output_path with the number.
    """
    inp = Path(input_path)
    out = Path(output_path)
    lines = inp.read_text(encoding="utf-8").splitlines()
    non_empty = [ln.strip() for ln in lines if ln.strip()]
    out.write_text(str(len(non_empty)), encoding="utf-8")
    return len(non_empty)


def run_job(db_path: str) -> int:
    """
    Open a SQLite DB, ensure a table exists, insert one row ("ok"),
    and return total rows in the table.
    Side effect: mutates database state at db_path.
    """
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
        conn.execute("INSERT INTO items(name) VALUES (?)", ("ok",))
        conn.commit()
        total = conn.execute("SELECT COUNT(*) FROM items").fetchone()[0]
        return total
    finally:
        conn.close()


def io_pipeline(input_text: str, work_dir: str) -> Path:
    """
    Simple pipeline:
      1) Write input_text -> input.txt
      2) process_file(input.txt -> count.txt)
      3) write summary -> report.txt
    Returns the Path to report.txt
    """
    wd = Path(work_dir)
    wd.mkdir(parents=True, exist_ok=True)

    inp = wd / "input.txt"
    out_count = wd / "count.txt"
    report = wd / "report.txt"

    inp.write_text(input_text, encoding="utf-8")
    count = process_file(str(inp), str(out_count))
    report.write_text(f"Non-empty lines: {count}\n", encoding="utf-8")
    return report


# =========================
# Integration tests
# =========================

class TestIntegration(unittest.TestCase):

    # ============================================================
    # INTEGRATION TEST — FILE I/O (single component with real FS)
    # Scope: process_file using a real temporary directory (no mocks)
    # Entry point: process_file()
    # Purpose: verify return value + side effect (output file content)
    # ============================================================
    def test___process_file___ignores_blank_and_whitespace_lines____writes_correct_count(self):
        # ARRANGE — build an isolated workspace with controlled input data
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            inp = td / "in.txt"
            out = td / "out.txt"
            # Includes blank lines and whitespace-only lines; expected non-empty = 3
            inp.write_text("a\n\n  b \n   \n c\n", encoding="utf-8")

            # ACT — run the real function against the real filesystem
            count = process_file(str(inp), str(out))

            # ASSERT — verify both the return value and the side effect on disk
            self.assertEqual(count, 3, "Should count exactly 3 non-empty trimmed lines")
            self.assertTrue(out.exists(), "Output file must be created")
            self.assertEqual(out.read_text(encoding="utf-8"), "3")

    # ============================================================
    # INTEGRATION TEST — SQLITE (lightweight local DB)
    # Scope: run_job touches a real SQLite file and persists state
    # Entry point: run_job()
    # Purpose: verify table creation + insert + persisted rows
    # ============================================================
    def test___run_job___empty_db_file____creates_table_and_inserts_row(self):
        # ARRANGE — new temp DB path ensures a clean slate
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "app.db"

            # ACT — run the job which should create table and insert "ok"
            total_after_insert = run_job(str(db))

            # ASSERT — total rows >= 1 and row content matches expectation
            self.assertGreaterEqual(total_after_insert, 1, "Should have at least 1 row after run_job()")

            # Extra verification: open a fresh connection and check data persisted
            conn = sqlite3.connect(db)
            try:
                rows = conn.execute("SELECT name FROM items ORDER BY id").fetchall()
            finally:
                conn.close()
            self.assertIn(("ok",), rows, "Inserted row with name='ok' should be present")

    # ============================================================
    # INTEGRATION TEST — END-TO-END PIPELINE (multi-step over FS)
    # Scope: io_pipeline orchestrates multiple steps and artifacts
    # Entry point: io_pipeline()
    # Purpose: verify presence + consistency of all produced files
    # ============================================================
    def test___io_pipeline___writes_input_counts_and_report____artifacts_are_consistent(self):
        # ARRANGE — deterministic input text; expected non-empty lines = 3
        text = "alpha\n\n beta \n \n\ngamma\n"
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)

            # ACT — execute the full pipeline (write input -> count -> report)
            report_path = io_pipeline(text, str(td))

            # ASSERT — all artifacts exist and their contents align
            self.assertTrue((td / "input.txt").exists(), "input.txt should exist")
            self.assertTrue((td / "count.txt").exists(), "count.txt should exist")
            self.assertTrue(report_path.exists(), "report.txt should exist")

            count_txt = (td / "count.txt").read_text(encoding="utf-8")
            report_txt = report_path.read_text(encoding="utf-8")
            self.assertEqual(count_txt, "3", "count.txt must store the numeric count")
            self.assertIn("Non-empty lines: 3", report_txt, "report.txt must summarize the same count")


# =========================
# Runner
# =========================

if __name__ == "__main__":
    # Verbose for clarity; runs only this file’s tests.
    unittest.main(verbosity=2)
