#!/usr/bin/env python3
"""Check one answer from the planner's line test skill.

Usage: python3 scripts/check.py <answer-file>

Standard library only. No network. Python 3.9 or later.
Prints one line per error. Exit code 0 if there are none, 1 if there are any.
The check finds format errors. It does not show that an answer is right.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(HERE)
DATA_FILE = os.path.join(SKILL_DIR, "data", "mapping.yaml")
SKILL_FILE = os.path.join(SKILL_DIR, "SKILL.md")

INPUT_TYPES = ("offer", "proposed_line")
RESULTS = ("Placed", "Not a boundary", "A boundary on paper")
ROUTES = ("currency", "record", "neither")

# A currency symbol, or a currency code, next to a number.
PRICE_TEXT = re.compile(
    r"[$€£¥₹]\s*\d|\d\s*[$€£¥₹]"
    r"|\b(?:USD|EUR|GBP)\s*\d|\d\s*(?:USD|EUR|GBP)\b"
)
# A field name that holds a price, a cost, or a rate. The last word of the name
# decides, so "unit_cost" is flagged and "price_basis" is not. Words such as
# "cost per install" in a text value are not flagged: only names of fields.
PRICE_KEY_WORDS = {"price", "prices", "cost", "costs", "rate", "rates", "cpm", "fee", "fees"}


def parse_value(text):
    """Every value in the data file is a JSON string or a JSON list."""
    return json.loads(text)


def load_data(path=DATA_FILE):
    """Read data/mapping.yaml. The file uses a small subset of YAML:
    top-level keys, list items that start with '  - ', and JSON values."""
    data = {"rows": [], "others": []}
    section = None
    item = None
    with open(path, encoding="utf-8") as handle:
        for number, raw in enumerate(handle, 1):
            line = raw.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if not line.startswith(" "):
                key, _, value = line.partition(":")
                if key in ("rows", "others"):
                    section = key
                    item = None
                else:
                    data[key] = parse_value(value.strip())
                continue
            match = re.match(r"^(  - |    )([a-z_]+): (.*)$", line)
            if not match or section is None:
                raise ValueError("%s line %d: cannot read %r" % (path, number, line))
            lead, key, value = match.groups()
            if lead == "  - ":
                item = {}
                data[section].append(item)
            if item is None:
                raise ValueError("%s line %d: value before a list item" % (path, number))
            item[key] = parse_value(value)
    return data


def skill_version(path=SKILL_FILE):
    """The version is the 'version' key under 'metadata' in the SKILL.md frontmatter."""
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    front = text.split("---")[1] if text.startswith("---") else ""
    match = re.search(r'^\s+version:\s*"?([^"\s]+)"?\s*$', front, re.M)
    return match.group(1) if match else None


def id_status(data):
    """Map every ID in the data file to its status."""
    return {entry["id"]: entry.get("status", "active") for entry in data["rows"] + data["others"]}


def check_answer(answer, data, version):
    errors = []
    statuses = id_status(data)

    def err(message):
        errors.append(message)

    def check_cites(where, cites, required):
        if cites is None:
            if required:
                err("%s: no citation" % where)
            return
        if not isinstance(cites, list) or not all(isinstance(c, str) for c in cites):
            err("%s: 'cite' must be a list of IDs" % where)
            return
        if required and not cites:
            err("%s: no citation" % where)
        for cite in cites:
            if cite not in statuses:
                err("%s: cited ID %s does not exist" % (where, cite))
            elif statuses[cite] != "active":
                err("%s: cited ID %s is retired" % (where, cite))

    if not isinstance(answer, dict):
        return ["Format: the answer must be a JSON object"]

    # Format and version
    for field in ("version", "input_type", "items", "to_confirm"):
        if field not in answer:
            err("Format: required field '%s' is missing" % field)
    if "version" in answer and answer["version"] != version:
        err("Version: the answer says %r, the skill is %r" % (answer["version"], version))
    input_type = answer.get("input_type")
    if "input_type" in answer and input_type not in INPUT_TYPES:
        err("Input type: %r is not 'offer' or 'proposed_line'" % (input_type,))

    # Items: placements and unplaced items
    items = answer.get("items")
    if "items" in answer and not isinstance(items, list):
        err("Format: 'items' must be a list")
        items = []
    for index, item in enumerate(items or [], 1):
        where = "items[%d]" % index
        if not isinstance(item, dict):
            err("%s: must be an object" % where)
            continue
        if not item.get("item"):
            err("%s: field 'item' is missing" % where)
        if item.get("unplaced") is True:
            if item.get("line"):
                err("%s: an unplaced item must not also have a line" % where)
            if not str(item.get("reason", "")).strip():
                err("%s: an unplaced item needs a reason" % where)
            check_cites(where + " (unplaced)", item.get("cite"), True)
        elif item.get("line"):
            check_cites(where, item.get("cite"), True)
        else:
            err("%s: the item has neither a line nor 'unplaced': true" % where)
            check_cites(where, item.get("cite"), False)

    # Brand's presence inside play
    for index, entry in enumerate(answer.get("no_native_line", []), 1):
        where = "no_native_line[%d]" % index
        if not isinstance(entry, dict):
            err("%s: must be an object" % where)
            continue
        if entry.get("route") not in ROUTES:
            err("%s: 'route' must be one of %s" % (where, ", ".join(ROUTES)))
        if not isinstance(entry.get("comparison_meets_four_requirements"), bool):
            err("%s: 'comparison_meets_four_requirements' must be true or false" % where)
        check_cites(where, entry.get("cite"), True)

    # Items outside the test
    for index, entry in enumerate(answer.get("outside_the_test", []), 1):
        where = "outside_the_test[%d]" % index
        if not isinstance(entry, dict):
            err("%s: must be an object" % where)
            continue
        check_cites(where, entry.get("cite"), True)

    # Result of a proposed line
    result = answer.get("result")
    if input_type == "proposed_line" and result is None:
        err("Results: a proposed line needs a 'result'")
    if result is not None:
        if not isinstance(result, dict):
            err("Results: 'result' must be an object with 'value' and 'cite'")
        else:
            value = result.get("value")
            if value not in RESULTS:
                err("Results: %r is not one of %s" % (value, ", ".join(RESULTS)))
            check_cites("result", result.get("cite"), True)
            if value == "Not a boundary":
                step = result.get("failed_step")
                if step not in ("F-2", "F-3", "F-4"):
                    err("Results: 'Not a boundary' needs 'failed_step' F-2, F-3, or F-4")
            if value == "A boundary on paper" and not answer.get("in_practice"):
                err("Results: 'A boundary on paper' needs 'in_practice'")

    # Confirm list
    if "to_confirm" in answer and not isinstance(answer["to_confirm"], list):
        err("Confirm list: 'to_confirm' must be a list")

    # Instructions found in the input
    found = answer.get("instructions_in_input", [])
    if not isinstance(found, list):
        err("Format: 'instructions_in_input' must be a list")
        found = []
    for index, entry in enumerate(found, 1):
        where = "instructions_in_input[%d]" % index
        if not isinstance(entry, dict) or not entry.get("instruction"):
            err("%s: must be an object with 'instruction' and 'action'" % where)
        elif "ignor" not in str(entry.get("action", "")).lower():
            err("%s: the answer must say that the instruction was ignored" % where)

    # No prices
    for path, key, text in walk(answer):
        if path.endswith(".instruction"):
            continue  # a quote of the input. The answer only reports it.
        words = [w for w in re.split(r"[^a-z]+", key.lower()) if w] if key else []
        if words and words[-1] in PRICE_KEY_WORDS:
            err("No prices: field name %r at %s names a price, cost, or rate" % (key, path))
        if text is not None and PRICE_TEXT.search(text):
            err("No prices: a currency amount appears at %s" % path)

    return errors


def walk(node, path="answer"):
    """Yield (path, key, text) for every dict key and every string value."""
    if isinstance(node, dict):
        for key, value in node.items():
            yield (path + "." + str(key), str(key), None)
            for found in walk(value, path + "." + str(key)):
                yield found
    elif isinstance(node, list):
        for index, value in enumerate(node):
            for found in walk(value, "%s[%d]" % (path, index)):
                yield found
    elif isinstance(node, str):
        yield (path, None, node)


def main(argv):
    if len(argv) != 2:
        print("usage: python3 scripts/check.py <answer-file>")
        return 2
    try:
        with open(argv[1], encoding="utf-8") as handle:
            answer = json.load(handle)
    except (OSError, ValueError) as problem:
        print("Format: cannot read the answer as JSON (%s)" % problem)
        return 1
    errors = check_answer(answer, load_data(), skill_version())
    for message in errors:
        print(message)
    if errors:
        print("%d error(s). Correct the answer and run the check again." % len(errors))
        return 1
    print("Check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
