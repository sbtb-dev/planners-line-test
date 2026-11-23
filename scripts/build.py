#!/usr/bin/env python3
"""Build everything that is generated from the source files.

Run it through scripts/build.sh. Steps, in order:
1. Check data/mapping.yaml against the source files.
2. Render the mapping table in mapping/MAPPING.md.
3. Build prompt/PROMPT.md.
4. Copy the source files into skill/planners-line-test/ (references/ and data/).
5. Write skill/planners-line-test/MANIFEST.txt.
6. Write dist/planners-line-test-<VERSION>-claude-skill.zip
   and dist/planners-line-test-<VERSION>-chatgpt-plugin.zip.
7. Run scripts/test_check.py.

Standard library only. No network. Running it twice changes no file.
"""
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.join(ROOT, "skill", "planners-line-test")
NAME = "planners-line-test"

BEGIN = "<!-- BEGIN GENERATED TABLE -->"
END = "<!-- END GENERATED TABLE -->"
ROW_FIELDS = ("id", "sold_as", "line", "compare_on", "support", "second_rules",
              "differs_from_iab", "status")

# Order of the files in prompt/PROMPT.md.
PROMPT_SOURCES = [
    "prompt/INSTRUCTIONS.md",
    "line-test/RULE.md",
    "mapping/README.md",
    "mapping/MAPPING.md",
    "forms/OFFER_FORM.md",
    "forms/PROPOSED_LINE_FORM.md",
]
# Source file -> file in skill/planners-line-test/references/.
REFERENCES = [
    ("prompt/INSTRUCTIONS.md", "INSTRUCTIONS.md"),
    ("line-test/RULE.md", "RULE.md"),
    ("mapping/README.md", "MAPPING_README.md"),
    ("mapping/MAPPING.md", "MAPPING.md"),
    ("forms/OFFER_FORM.md", "OFFER_FORM.md"),
    ("forms/PROPOSED_LINE_FORM.md", "PROPOSED_LINE_FORM.md"),
    ("GLOSSARY.md", "GLOSSARY.md"),
]
# Files that may cite IDs. Every ID in them must exist in the data file.
ID_SCAN_FILES = [
    "README.md", "CONTRIBUTING.md", "GLOSSARY.md", "prompt/INSTRUCTIONS.md",
    "line-test/RULE.md", "line-test/APPLIED.md", "mapping/README.md",
    "mapping/MAPPING.md", "forms/OFFER_FORM.md", "forms/PROPOSED_LINE_FORM.md",
]
ID_TOKEN = re.compile(r"\b(M-\d{2}|N-\d|C-\d\.\d|R-\d|S-\d\.\d|SR-[a-z]+(?:-[a-z]+)*|F-\d)\b")


class BuildError(Exception):
    pass


def path(rel):
    return os.path.join(ROOT, *rel.split("/"))


def read(rel):
    with open(path(rel), encoding="utf-8") as handle:
        return handle.read()


def write(rel, text):
    """Write a file only if the text changed. Returns True if it changed."""
    full = path(rel)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    if os.path.exists(full) and read(rel) == text:
        return False
    with open(full, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return True


def load_check_module():
    spec = importlib.util.spec_from_file_location("check", os.path.join(SKILL, "scripts", "check.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def plain_links(text):
    """Pasted text has no files to link to. Turn relative links into plain text."""
    return re.sub(r"\[([^\]]+)\]\(([^h)][^)]*)\)", r"\1", text)


def drop_markers(text):
    return "".join(l for l in text.splitlines(True) if l.strip() not in (BEGIN, END) and
                   not l.startswith("<!-- Generated from data/mapping.yaml"))


# 1. Validate the data file ------------------------------------------------

def validate(check, data, version):
    problems = []
    seen = set()
    for row in data["rows"]:
        for field in ROW_FIELDS:
            if field not in row:
                problems.append("row %s: field '%s' is missing" % (row.get("id", "?"), field))
        if row.get("status") not in ("active", "retired"):
            problems.append("row %s: status must be 'active' or 'retired'" % row.get("id"))
        if not re.match(r"^M-\d{2,}$", str(row.get("id"))):
            problems.append("row id %r is not of the form M-01" % row.get("id"))
    for entry in data["others"]:
        for field in ("id", "title", "status"):
            if field not in entry:
                problems.append("entry %s: field '%s' is missing" % (entry.get("id", "?"), field))
    for entry in data["rows"] + data["others"]:
        if entry.get("id") in seen:
            problems.append("duplicate ID %s" % entry.get("id"))
        seen.add(entry.get("id"))
    sr_ids = {e["id"] for e in data["others"] if e["id"].startswith("SR-")}
    for row in data["rows"]:
        for sr in row.get("second_rules", []):
            if sr not in sr_ids:
                problems.append("row %s: unknown second rule %s" % (row["id"], sr))
    active = {e["id"] for e in data["rows"] + data["others"] if e.get("status") == "active"}
    retired = {e["id"] for e in data["rows"] + data["others"] if e.get("status") == "retired"}

    # The IDs in the source files must match the data file, both ways.
    def found(rel, pattern):
        return set(re.findall(pattern, read(rel), re.M))
    in_rule = found("line-test/RULE.md", r"\[((?:N|C|R|S)-[0-9.]+)\]")
    in_sr = found("mapping/README.md", r"\[(SR-[a-z-]+)\]")
    in_form = found("forms/PROPOSED_LINE_FORM.md", r"^\| (F-\d+) \|")
    from_data = {e["id"] for e in data["others"] if e["status"] == "active"}
    for label, ids in (("RULE.md", in_rule), ("mapping/README.md", in_sr),
                       ("PROPOSED_LINE_FORM.md", in_form)):
        for missing in sorted(ids - from_data):
            problems.append("%s has ID %s that is not active in the data file" % (label, missing))
    for missing in sorted(from_data - (in_rule | in_sr | in_form)):
        problems.append("ID %s is in the data file but not in the source text" % missing)
    # Every ID that any file cites must exist and must not be retired.
    for rel in ID_SCAN_FILES:
        for token in sorted(set(ID_TOKEN.findall(read(rel)))):
            if token not in active:
                problems.append("%s cites %s, which %s" % (
                    rel, token, "is retired" if token in retired else "does not exist"))
    return problems


def render_table(data):
    lines = ["| ID | Sold as gaming | Line | Compare on | Support |",
             "|---|---|---|---|---|"]
    for row in data["rows"]:
        if row["status"] != "active":
            continue
        support = row["support"]
        if row["differs_from_iab"]:
            support += ". Differs: " + row["differs_from_iab"]
        lines.append("| %s | %s | %s | %s | %s |" % (
            row["id"], row["sold_as"], row["line"], row["compare_on"], support))
    return "\n".join(lines)


# 2. Render the mapping table ----------------------------------------------

def render_mapping(data):
    text = read("mapping/MAPPING.md")
    pattern = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.S)
    if len(pattern.findall(text)) != 1:
        raise BuildError("mapping/MAPPING.md needs exactly one pair of table markers")
    block = (BEGIN + "\n<!-- Generated from data/mapping.yaml. Do not edit by hand. -->\n\n" +
             render_table(data) + "\n" + END)
    changed = write("mapping/MAPPING.md", pattern.sub(lambda m: block, text))
    ids = re.findall(r"^\| (M-\d+) \|", read("mapping/MAPPING.md"), re.M)
    wanted = [r["id"] for r in data["rows"] if r["status"] == "active"]
    if ids != wanted:
        raise BuildError("the rendered table does not match the data file")
    return changed


# 3. Prompt ------------------------------------------------------------------

def build_prompt(version):
    parts = [
        "<!-- Generated file. Do not edit by hand. -->\n",
        "# Prompt for the planner's line test, applied to gaming media\n",
        "\n",
        "Version: %s. Generated file.\n" % version,
        "\n",
        "Paste everything below the line into your model. Then paste the offer or the proposed line after it, marked with a label such as INPUT:.\n",
        "\n",
        "---\n",
    ]
    for rel in PROMPT_SOURCES:
        parts.append("\n")
        parts.append(plain_links(drop_markers(read(rel))))
    return write("prompt/PROMPT.md", "".join(parts))


# 4. Skill folder -------------------------------------------------------------

def header(rel, version, comment):
    text = "Generated file. Do not edit by hand. Source: %s. Version: %s." % (rel, version)
    return ("<!-- %s -->\n\n" % text) if comment == "html" else ("# %s\n" % text)


def build_skill(version):
    changed = False
    skill_md = os.path.join(SKILL, "SKILL.md")
    if not os.path.exists(skill_md):
        raise BuildError("skill/planners-line-test/SKILL.md is missing")
    text = read("skill/planners-line-test/SKILL.md")
    new = re.sub(r'^(  version: ")[^"]*(")', lambda m: m.group(1) + version + m.group(2), text, flags=re.M)
    new = re.sub(r'^(  "version": ")[^"]*(")', lambda m: m.group(1) + version + m.group(2), new, flags=re.M)
    new = re.sub(r"^Skill version: .*$", "Skill version: %s." % version, new, flags=re.M)
    if "Skill version: %s." % version not in new or ('version: "%s"' % version) not in new:
        raise BuildError("SKILL.md must have a metadata version line and a 'Skill version:' line")
    changed |= write("skill/planners-line-test/SKILL.md", new)
    for src, name in REFERENCES:
        body = plain_links(drop_markers(read(src)))
        changed |= write("skill/planners-line-test/references/" + name,
                         header(src, version, "html") + body)
    changed |= write("skill/planners-line-test/data/mapping.yaml",
                     header("data/mapping.yaml", version, "yaml") + read("data/mapping.yaml"))
    return changed


# 5 and 6. Manifest and zip ---------------------------------------------------

def skill_files():
    found = []
    for folder, dirs, files in os.walk(SKILL):
        dirs[:] = sorted(d for d in dirs if d != "__pycache__")
        for name in sorted(files):
            if name in (".DS_Store", "MANIFEST.txt"):
                continue
            full = os.path.join(folder, name)
            found.append(os.path.relpath(full, SKILL).replace(os.sep, "/"))
    return sorted(found)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def manifest_text(version, commit=None):
    entries = []
    for rel in skill_files():
        with open(os.path.join(SKILL, *rel.split("/")), "rb") as handle:
            entries.append((rel, sha256(handle.read())))
    overall = sha256(("\n".join(sorted(h for _, h in entries)) + "\n").encode("ascii"))
    lines = ["planners-line-test skill manifest", "Version: %s" % version]
    if commit:
        lines.append("Source commit: %s" % commit)
    lines += ["", "SHA-256 of each file:"]
    lines += ["%s  %s" % (h, rel) for rel, h in entries]
    lines += ["", "SHA-256 of the sorted list of file hashes (one hash per line): %s" % overall]
    return "\n".join(lines) + "\n"


def git_commit():
    try:
        out = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True,
                             text=True, check=True)
        return out.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def build_zip(version):
    """The zip is deterministic: sorted entries, a fixed time stamp. Its manifest also
    names the commit the build came from. The committed manifest does not, because
    a commit cannot hold its own hash."""
    out = path("dist/%s-%s-claude-skill.zip" % (NAME, version))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    members = [(rel, None) for rel in skill_files()]
    commit = git_commit()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as archive:
        names = sorted([rel for rel, _ in members] + ["MANIFEST.txt"])
        for rel in names:
            if rel == "MANIFEST.txt":
                data = manifest_text(version, commit).encode("utf-8")
            else:
                with open(os.path.join(SKILL, *rel.split("/")), "rb") as handle:
                    data = handle.read()
            info = zipfile.ZipInfo("%s/%s" % (NAME, rel), date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, data)
    return out


def build_plugin_zip(version):
    """A second zip for hosts that load plugins (ChatGPT, Codex). It holds the same
    skill files under skills/<name>/ and a plugin manifest in .codex-plugin/ and
    .claude-plugin/. The Claude.ai zip stays as it is."""
    out = path("dist/%s-%s-chatgpt-plugin.zip" % (NAME, version))
    description = ("Places an offer sold on a label such as gaming in a media-plan line, "
                   "or tests a proposed line. Cites IDs, lists facts to confirm. "
                   "Does not price, recommend, or rate sellers.")
    base = {"name": NAME, "version": version, "description": description,
            "author": {"name": "SBTB", "url": "https://github.com/sbtb-dev"},
            "homepage": "https://github.com/sbtb-dev/planners-line-test",
            "repository": "https://github.com/sbtb-dev/planners-line-test",
            "license": "CC-BY-4.0", "keywords": ["media planning", "advertising"],
            "skills": "./skills/"}
    codex = dict(base, interface={
        "displayName": "Planner's line test",
        "shortDescription": "Place an offer sold on a label in a media-plan line.",
        "longDescription": description,
        "developerName": "SBTB",
        "category": "Productivity",
        "capabilities": ["Read"],
    })
    codex_text = json.dumps(codex, indent=2) + "\n"
    claude_text = json.dumps(base, indent=2) + "\n"
    commit = git_commit()
    entries = {}
    for rel in skill_files():
        with open(os.path.join(SKILL, *rel.split("/")), "rb") as handle:
            entries["skills/%s/%s" % (NAME, rel)] = handle.read()
    entries["skills/%s/MANIFEST.txt" % NAME] = manifest_text(version, commit).encode("utf-8")
    entries[".codex-plugin/plugin.json"] = codex_text.encode("utf-8")
    entries[".claude-plugin/plugin.json"] = claude_text.encode("utf-8")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as archive:
        for name in sorted(entries):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, entries[name])
    return out


# Main ---------------------------------------------------------------------------

def main():
    version = read("VERSION").strip()
    check = load_check_module()
    data = check.load_data(path("data/mapping.yaml"))

    print("1. checking data/mapping.yaml")
    problems = validate(check, data, version)
    if problems:
        raise BuildError("data file and source files do not match:\n  " + "\n  ".join(problems))
    print("2. rendering the mapping table")
    render_mapping(data)
    print("3. building prompt/PROMPT.md")
    build_prompt(version)
    print("4. copying the source files into the skill folder")
    build_skill(version)
    print("5. writing MANIFEST.txt")
    write("skill/planners-line-test/MANIFEST.txt", manifest_text(version))
    print("6. writing the zip")
    out = build_zip(version)
    build_plugin_zip(version)
    print("7. running scripts/test_check.py")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    result = subprocess.run([sys.executable, "-B", path("scripts/test_check.py")], cwd=ROOT, env=env)
    if result.returncode != 0:
        raise BuildError("scripts/test_check.py failed")
    print("built version %s: %s" % (version, os.path.relpath(out, ROOT)))


if __name__ == "__main__":
    try:
        main()
    except BuildError as problem:
        print("BUILD FAILED: %s" % problem, file=sys.stderr)
        sys.exit(1)
