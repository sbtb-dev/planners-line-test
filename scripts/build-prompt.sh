#!/usr/bin/env bash
# Build prompt/PROMPT.md from the source files.
# Order: instructions, rule, mapping files, forms.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

version="$(tr -d '[:space:]' < VERSION)"
out="prompt/PROMPT.md"

sources=(
  prompt/INSTRUCTIONS.md
  line-test/RULE.md
  mapping/README.md
  mapping/MAPPING.md
  forms/OFFER_FORM.md
  forms/PROPOSED_LINE_FORM.md
)

for f in "${sources[@]}"; do
  [ -f "$f" ] || { echo "missing source: $f" >&2; exit 1; }
done

{
  echo "<!-- Generated file. Do not edit by hand. -->"
  echo "# Prompt for the planner's line test, applied to gaming media"
  echo
  echo "Version: ${version}. Generated file."
  echo
  echo "Paste everything below the line into your model."
  echo
  echo "---"
  for f in "${sources[@]}"; do
    echo
    # Pasted text has no files to link to. Turn relative links into plain text.
    sed -E 's/\[([^]]+)\]\(([^h)][^)]*)\)/\1/g' "$f"
  done
} > "$out"

echo "wrote $out (version ${version})"
