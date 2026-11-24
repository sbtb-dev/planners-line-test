#!/usr/bin/env python3
"""Compare one answer with the expected values of a placement case.

Usage: python3 scripts/compare_case.py <answer.json> <expected.json>

Standard library only. No network. Python 3.9 or later.

For each expected item, the script reports: found or missing; line match or
mismatch; required cites present or absent; hosts and counter match or mismatch.
It does not judge anything else. Every expected value is an object with a "value"
and a "status". Names are compared after trimming spaces and ignoring case.

An expected item has:
  item_key      a phrase that must appear in the answer's "item" text
  line          value: a string, or a list of strings (any one matches). A line
                matches if the expected text appears in the answer's line.
                "unplaced" means the item is unplaced. "no_native_line" means the
                item is in no_native_line.
  line_not      value: a list of texts that must not appear in the answer's line
  route         value: the expected route of a no_native_line entry
  cites         value: a list. Each element is an ID that must appear, or a list
                of IDs of which at least one must appear.
  hosts         value: a list. Each element is a name that must appear in the
                answer's hosts, or a list of names of which one must appear.
  counter       value: a string, or a list of strings (any one matches)
Fields other than item_key are optional. Only the fields that are present are checked.
Exit code: 0 if every check matches, 1 if any does not.
"""
import json
import sys


def norm(text):
    return str(text).strip().lower()


def value_of(field):
    return field["value"] if isinstance(field, dict) and "value" in field else field


def as_list(value):
    return value if isinstance(value, list) else [value]


def find_entry(answer, key):
    """Return (section, entry) for the first entry whose item text holds the key."""
    for section in ("items", "no_native_line"):
        for entry in answer.get(section, []) or []:
            if isinstance(entry, dict) and norm(key) in norm(entry.get("item", "")):
                return section, entry
    return None, None


def check_line(expected, section, entry):
    want = [norm(x) for x in as_list(value_of(expected))]
    if section == "no_native_line":
        return "no_native_line" in want
    if entry.get("unplaced") is True:
        return "unplaced" in want
    line = norm(entry.get("line", ""))
    return any(w in line for w in want if w not in ("unplaced", "no_native_line"))


def compare(answer, expected):
    lines = []
    bad = 0
    for spec in expected.get("items", []):
        key = spec["item_key"]
        section, entry = find_entry(answer, key)
        if entry is None:
            lines.append("%-14s missing" % key)
            bad += 1
            continue
        parts = ["found"]
        if "line" in spec:
            ok = check_line(spec["line"], section, entry)
            parts.append("line " + ("match" if ok else "MISMATCH (answer: %s)" % (
                "unplaced" if entry.get("unplaced") else entry.get("line", section))))
            bad += not ok
        if "line_not" in spec:
            line = norm(entry.get("line", ""))
            hit = [x for x in as_list(value_of(spec["line_not"])) if norm(x) in line]
            parts.append("line_not " + ("MISMATCH (%s)" % ", ".join(hit) if hit else "match"))
            bad += bool(hit)
        if "route" in spec:
            ok = norm(entry.get("route", "")) in [norm(x) for x in as_list(value_of(spec["route"]))]
            parts.append("route " + ("match" if ok else "MISMATCH (answer: %s)" % entry.get("route")))
            bad += not ok
        if "cites" in spec:
            cites = {norm(c) for c in entry.get("cite", []) if isinstance(c, str)}
            absent = []
            for need in value_of(spec["cites"]):
                options = [norm(n) for n in as_list(need)]
                if not any(o in cites for o in options):
                    absent.append(" or ".join(as_list(need)))
            parts.append("cites " + ("present" if not absent else "ABSENT (%s)" % ", ".join(absent)))
            bad += bool(absent)
        if "hosts" in spec:
            hosts = {norm(h) for h in entry.get("hosts", []) if isinstance(h, str)}
            absent = []
            for need in value_of(spec["hosts"]):
                if not any(norm(n) in hosts for n in as_list(need)):
                    absent.append(" or ".join(as_list(need)))
            parts.append("hosts " + ("match" if not absent else "MISMATCH (absent: %s)" % ", ".join(absent)))
            bad += bool(absent)
        if "counter" in spec:
            ok = norm(entry.get("counter", "")) in [norm(x) for x in as_list(value_of(spec["counter"]))]
            parts.append("counter " + ("match" if ok else "MISMATCH (answer: %s)" % entry.get("counter")))
            bad += not ok
        lines.append("%-14s %s" % (key, "; ".join(parts)))
    return lines, bad


def main(argv):
    if len(argv) != 3:
        print("usage: python3 scripts/compare_case.py <answer.json> <expected.json>")
        return 2
    try:
        with open(argv[1], encoding="utf-8") as handle:
            answer = json.load(handle)
        with open(argv[2], encoding="utf-8") as handle:
            expected = json.load(handle)
    except (OSError, ValueError) as problem:
        print("cannot read a file as JSON (%s)" % problem)
        return 2
    lines, bad = compare(answer, expected)
    drafts = sum(1 for spec in expected.get("items", []) for field in spec.values()
                 if isinstance(field, dict) and field.get("status") == "draft")
    for line in lines:
        print(line)
    print("%d item(s) with a difference. %d expected value(s) still draft." % (bad, drafts))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
