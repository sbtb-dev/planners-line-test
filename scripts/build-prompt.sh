#!/usr/bin/env bash
# Kept so that older instructions still work. The prompt and the skill come from
# the same sources, so this runs the whole build. See scripts/build.sh.
set -euo pipefail

exec "$(dirname "${BASH_SOURCE[0]}")/build.sh" "$@"
