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

## Results, run 2026-11-21

Run by subagents on three model tiers (Opus, Haiku, Fable), not by hand. All three are from the same vendor as the attackers and the first judges, so this is a weaker check than a different vendor's models. Each cell is one run. Judges read the prompt from a one-file copy.

### Prompt 0.2.2 (before the fix)

| File | Opus | Haiku | Fable |
|---|---|---|---|
| S1-proposal-1.md | A | B | B. Said 0.2.2 has no offer-form rule for this case. |
| S1-proposal-2.md | Excluded | C | B/C. Named two readings (A and B) and said the text does not choose. |

The Opus run on proposal 2 said it had seen the 0.3.0 branch's commit message. That is information outside the prompt file. Its answer is not clean, so it is not counted. I could not find out how it saw the message.

On 0.2.2, the three tiers gave A, B and C on the same facts. The gap was real. It was not only one judge's error.

### Prompt 0.3.0 (after the fix)

| File | Opus | Haiku | Fable |
|---|---|---|---|
| S1-proposal-1.md | B | B | B |
| S1-proposal-2.md | B | B | B |

All six runs placed the format in Display, left the unit unplaced (notes 2, 6, 7 and 9), found no route, labeled player-minutes media engagement, and did not move the sign to "a brand's presence inside play." This is the reading B result that the repo owner confirmed.

### Limits

- One run per cell.
- All models are from one vendor.
- Both texts are the original attack texts. A seller who has read note 9 would write new ones.
