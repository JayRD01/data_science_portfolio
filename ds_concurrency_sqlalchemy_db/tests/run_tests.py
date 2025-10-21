#!/usr/bin/env python3
"""
Generic unittest runner (stdlib only)

Covers:
  - tests/unit/
  - tests/integration/

Features:
  - Discovery across both roots
  - Filename pattern filtering (e.g., test_*.py)
  - Verbosity, failfast, buffer
  - Optional randomized order with seed
  - Compact summary
"""

import argparse
import random
import sys
import time
import unittest
from pathlib import Path


DEFAULT_ROOTS = [
    Path("tests") / "unit",
    Path("tests") / "integration",
]


def flatten_suite(suite: unittest.TestSuite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from flatten_suite(item)
        else:
            yield item


def shuffle_suite(suite: unittest.TestSuite, seed: int | None) -> unittest.TestSuite:
    tests = list(flatten_suite(suite))
    if seed is not None:
        rnd = random.Random(seed)
        rnd.shuffle(tests)
    return unittest.TestSuite(tests)


def discover_from_roots(pattern: str, roots: list[Path]) -> unittest.TestSuite:
    loader = unittest.defaultTestLoader
    discovered = []
    for root in roots:
        if root.exists():
            discovered.append(loader.discover(start_dir=str(root), pattern=pattern))
    # Fallback: discover from tests/ if specific roots missing
    if not discovered and Path("tests").exists():
        discovered.append(loader.discover(start_dir="tests", pattern=pattern))
    # Last resort: current directory
    if not discovered:
        discovered.append(loader.discover(start_dir=".", pattern=pattern))
    return unittest.TestSuite(discovered)


def parse_args(argv):
    p = argparse.ArgumentParser(description="Generic unittest runner")
    p.add_argument("--suite", choices=["unit", "integration", "all"], default="all",
                   help="Subset to run (default: all)")
    p.add_argument("--pattern", default="test_*.py",
                   help='Filename pattern (default: "test_*.py")')
    p.add_argument("--verbosity", "-v", type=int, default=2,
                   help="Verbosity for TextTestRunner (default: 2)")
    p.add_argument("--failfast", action="store_true",
                   help="Stop on first failure/error")
    p.add_argument("--buffer", action="store_true",
                   help="Buffer stdout/stderr during tests")
    p.add_argument("--seed", type=int, default=None,
                   help="Shuffle tests with reproducible seed")
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(argv or sys.argv[1:])

    if args.suite == "unit":
        roots = [Path("tests") / "unit"]
    elif args.suite == "integration":
        roots = [Path("tests") / "integration"]
    else:
        roots = DEFAULT_ROOTS

    suite = discover_from_roots(pattern=args.pattern, roots=roots)
    suite = shuffle_suite(suite, seed=args.seed)

    runner = unittest.TextTestRunner(
        verbosity=args.verbosity,
        failfast=args.failfast,
        buffer=args.buffer,
        descriptions=True,
    )

    start = time.time()
    result = runner.run(suite)
    duration = time.time() - start

    total = result.testsRun
    failed = len(result.failures)
    errored = len(result.errors)
    skipped = len(result.skipped)

    print("\n" + "-" * 60)
    print("SUMMARY")
    print(f"  Suite:        {args.suite}")
    print(f"  Roots:        {', '.join(str(p) for p in roots)}")
    print(f"  Pattern:      {args.pattern}")
    print(f"  Seed:         {args.seed if args.seed is not None else '-'}")
    print(f"  Ran:          {total} test(s) in {duration:.2f}s")
    print(f"  Failures:     {failed}")
    print(f"  Errors:       {errored}")
    print(f"  Skipped:      {skipped}")
    print("-" * 60 + "\n")

    sys.exit(0 if result.wasSuccessful() else 1)


if __name__ == "__main__":
    main()
