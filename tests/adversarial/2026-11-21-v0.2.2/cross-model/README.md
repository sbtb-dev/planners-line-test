# Cross-model pack

These files hold the proposals graded Rule gap. No attack was graded Break.

## How to run

1. Build the prompt: `scripts/build-prompt.sh`. Confirm `prompt/PROMPT.md` shows the current version.
2. Open a fresh session in each model you want to test. Give it no file access.
3. Paste the contents of `prompt/PROMPT.md`. Then paste the line `INPUT:`. Then paste the proposal text from one file below.
4. Copy the answer into the table.

## What to record

The correct result is not fixed for these two. They test a rule gap (see REPORT.md, section 4). Record which of these each model gives:

| Code | Meaning |
|---|---|
| A | Placed in display, with the price basis under "what to confirm" |
| B | Not placed in display. The price basis is called different. No route stated. |
| C | Presence inside play, no native line |
| D | Other. Write it down. |

| File | Model | Code | Notes |
|---|---|---|---|
| S1-proposal-1.md | | | |
| S1-proposal-2.md | | | |

If models split between A and B, the rule needs a decision before a fixture can be written.
