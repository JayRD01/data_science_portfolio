"""
Unit Test Template (stdlib only) — generic patterns most software uses.

How you'd normally split this in a real project:
  src/app/logic.py          -> sanitize_ids()
  src/app/timebox.py        -> bucket_by_part_of_day()
  src/app/transport.py      -> transport_get(), fetch_settings()
  tests/unit/test_logic.py
  tests/unit/test_timebox.py
  tests/unit/test_transport.py
  
  - Naming convention for tests:
  test___<function_under_test>___<scenario>____<expected_result>

Here everything lives in one file for learning/demo purposes.
"""

import unittest
from unittest.mock import patch
from datetime import datetime
import json


# =========================
# CODE UNDER TEST (GENERIC)
# =========================

# ---- Case A: Pure business logic (deterministic, no I/O) ----
def sanitize_ids(seq):
    """
    Return a sorted list of unique positive integer IDs.
    Reject non-integers and non-positive values.
    """
    if seq is None:
        return []  # graceful
    clean = []
    for x in seq:
        if not isinstance(x, int):
            raise TypeError("All IDs must be integers")
        if x > 0:
            clean.append(x)
    return sorted(set(clean))


# ---- Case B: Time-dependent logic (reads current clock) ----
def bucket_by_part_of_day():
    """
    Map current hour to a coarse "part of day" bucket.
    morning: 05:00–11:59, afternoon: 12:00–17:59, night: otherwise
    """
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "morning"
    if 12 <= hour < 18:
        return "afternoon"
    return "night"


# ---- Case C: External dependency via indirection (network, DB, etc.) ----
def transport_get(url: str) -> str:
    """
    Placeholder for an external call (HTTP, DB query, etc.).
    Intentionally unimplemented so we can patch it in tests.
    """
    raise NotImplementedError("Implement transport_get or patch it in tests.")

def fetch_settings(url: str):
    """
    Pull JSON via transport_get and validate a minimal schema.
    Expected keys: version (str), features (list).
    """
    raw = transport_get(url)
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("settings must be a JSON object")
    if "version" not in data or "features" not in data:
        raise ValueError("missing required keys: version, features")
    if not isinstance(data["version"], str) or not isinstance(data["features"], list):
        raise ValueError("invalid types for version/features")
    return data


# =========================
# UNIT TESTS
# =========================

# ------------------------------------------------------------
# 1) PURE LOGIC: happy path, boundaries, and error handling
#    No mocks. Small, fast, deterministic.
# ------------------------------------------------------------
class TestLogic(unittest.TestCase):

    def test___sanitize_ids___duplicates_and_mixed_signs____returns_unique_sorted_positive(self):
        result = sanitize_ids([3, 1, 2, 2, -5, 0, 3, 7])
        self.assertEqual(result, [1, 2, 3, 7])

    def test___sanitize_ids___none_input____returns_empty_list(self):
        self.assertEqual(sanitize_ids(None), [])

    def test___sanitize_ids___non_integer_present____raises_type_error(self):
        with self.assertRaises(TypeError):
            sanitize_ids([1, "2", 3])

    def test___sanitize_ids___table_of_small_inputs____stable_expectations(self):
        # Subtests give you a quick “poor man’s parametrization”
        cases = [
            ([], []),
            ([0, -1, -2], []),
            ([5], [5]),
            ([2, 2, 2], [2]),
        ]
        for seq, expected in cases:
            with self.subTest(seq=seq):
                self.assertEqual(sanitize_ids(seq), expected)


# ------------------------------------------------------------
# 2) TIME-DEPENDENT: patch where datetime is USED
#    We patch this module’s datetime, then configure now().return_value.hour
# ------------------------------------------------------------
class TestTimebox(unittest.TestCase):

    @patch(__name__ + ".datetime")
    def test___bucket_by_part_of_day___10am____returns_morning(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        self.assertEqual(bucket_by_part_of_day(), "morning")

    @patch(__name__ + ".datetime")
    def test___bucket_by_part_of_day___3pm____returns_afternoon(self, mock_datetime):
        mock_datetime.now.return_value.hour = 15
        self.assertEqual(bucket_by_part_of_day(), "afternoon")

    @patch(__name__ + ".datetime")
    def test___bucket_by_part_of_day___23pm____returns_night(self, mock_datetime):
        mock_datetime.now.return_value.hour = 23
        self.assertEqual(bucket_by_part_of_day(), "night")


# ------------------------------------------------------------
# 3) EXTERNAL DEPENDENCY: patch the indirection (transport_get)
#    Control the payloads with return_value and assert behavior.
# ------------------------------------------------------------
class TestTransport(unittest.TestCase):

    @patch(__name__ + ".transport_get")
    def test___fetch_settings___valid_json____returns_validated_dict(self, mock_get):
        mock_get.return_value = json.dumps({"version": "1.0.0", "features": ["x", "y"]})
        data = fetch_settings("any://settings")
        self.assertEqual(data["version"], "1.0.0")
        self.assertEqual(data["features"], ["x", "y"])

    @patch(__name__ + ".transport_get")
    def test___fetch_settings___malformed_json____raises_json_decode_error(self, mock_get):
        mock_get.return_value = "not-json"
        with self.assertRaises(Exception):
            fetch_settings("any://settings")

    @patch(__name__ + ".transport_get")
    def test___fetch_settings___missing_keys____raises_value_error(self, mock_get):
        mock_get.return_value = json.dumps({"version": "1.0.0"})  # no features
        with self.assertRaises(ValueError):
            fetch_settings("any://settings")


# =========================
# RUNNER
# =========================
if __name__ == "__main__":
    unittest.main(verbosity=2)
