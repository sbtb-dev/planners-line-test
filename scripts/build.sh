#!/usr/bin/env bash
# Build all generated files: the mapping table, prompt/PROMPT.md, the skill folder,
# its manifest, and dist/planners-line-test-<VERSION>.zip. Then run the check tests.
# The work is done in scripts/build.py. Python 3.9 or later. No network.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

export PYTHONDONTWRITEBYTECODE=1
exec python3 scripts/build.py "$@"
