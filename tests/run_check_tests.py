#!/usr/bin/env python3
"""Run skill/planners-line-test/scripts/check.py on every fixture in tests/check_fixtures/.

Pass fixtures must exit 0. Fail fixtures must exit 1 and print the message in their
field "_expect_error". A fixture can set "version" to "@VERSION". The runner then
writes the current version from the VERSION file into a temporary copy.

Run: python3 -B tests/run_check_tests.py
Standard library only. No network."""
import glob
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECK = os.path.join(ROOT, "skill", "planners-line-test", "scripts", "check.py")
FIXTURES = os.path.join(ROOT, "tests", "check_fixtures")


def run_fixture(file, version):
    with open(file, encoding="utf-8") as handle:
        answer = json.load(handle)
    if isinstance(answer, dict) and answer.get("version") == "@VERSION":
        answer["version"] = version
    with tempfile.TemporaryDirectory() as folder:
        copy = os.path.join(folder, "answer.json")
        with open(copy, "w", encoding="utf-8") as handle:
            json.dump(answer, handle)
        result = subprocess.run([sys.executable, "-B", CHECK, copy], capture_output=True, text=True)
    return answer, result


def main():
    with open(os.path.join(ROOT, "VERSION"), encoding="utf-8") as handle:
        version = handle.read().strip()
    failures = []
    count = 0
    for kind, expected_code in (("pass", 0), ("fail", 1)):
        for file in sorted(glob.glob(os.path.join(FIXTURES, kind, "*.json"))):
            count += 1
            name = "%s/%s" % (kind, os.path.basename(file))
            answer, result = run_fixture(file, version)
            if result.returncode != expected_code:
                failures.append("%s: exit code %d, expected %d\n%s" % (
                    name, result.returncode, expected_code, result.stdout))
            elif kind == "fail":
                expect = answer.get("_expect_error") if isinstance(answer, dict) else None
                if not expect:
                    failures.append("%s: a fail fixture needs '_expect_error'" % name)
                elif expect not in result.stdout:
                    failures.append("%s: expected message %r not in output:\n%s" % (
                        name, expect, result.stdout))
    if count == 0:
        failures.append("no fixtures found in %s" % FIXTURES)
    for failure in failures:
        print("FAIL " + failure)
    print("%d fixture(s), %d failure(s)." % (count, len(failures)))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
