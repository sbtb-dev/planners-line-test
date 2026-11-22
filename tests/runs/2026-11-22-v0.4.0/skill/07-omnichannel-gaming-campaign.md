# Fixture 07: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> One gaming campaign, one price. It includes in-game display, rewarded video, a creator package, paid social, CTV spots, and a brand study at the end. Expect strong results.

## Answer

# Line test: gaming campaign offer

Input type: offer. All facts are the seller's claims.

## 1. What it is

| # | Part |
|---|---|
| 1 | In-game display |
| 2 | Rewarded video |
| 3 | Creator package |
| 4 | Paid social |
| 5 | CTV spots |
| 6 | Brand study at the end |

## 2. Where each part goes

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Display | Viewable impressions from other sellers | M-01 |
| 2 | Video | Completed views from other sellers | M-03 |
| 3 | Creator | The creator line's units | M-07, SR-performs-message |
| 4 | Social | The social line's units | M-12 |
| 5 | CTV or TV | That line's currency | M-13 |
| 6 | Measurement | Other measurement. Results are the seller's claims. | M-26 |

The offer has one price for six parts. Each payment goes to its own line (S-6.1).

## 3. What has no native line

Nothing in this offer is a brand's presence inside play. Route stated: not applicable.

## 4. What to confirm

- The price of each part. The seller gave one price for all.
- The unit, price basis, currency, and who counts it, for each part.
- Whether the creator performs the brand's message. If not, the part is display.
- Whether the display is intrinsic, adjacent, or interstitial. Also whether any part is priced on a measure that is not its own price basis (N-9).
- Who runs the brand study, its method, and what it measures.
- The basis of "strong results". It is a claim. It has no unit and no comparison.

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "In-game display", "format": "display", "line": "Display", "compare_with": "Viewable impressions from other sellers", "cite": ["M-01"]},
    {"item": "Rewarded video", "format": "video", "line": "Video", "compare_with": "Completed views from other sellers", "cite": ["M-03"]},
    {"item": "Creator package", "format": "creator", "line": "Creator", "compare_with": "The creator line's units", "cite": ["M-07", "SR-performs-message"]},
    {"item": "Paid social", "format": "social", "line": "Social", "compare_with": "The social line's units", "cite": ["M-12"]},
    {"item": "CTV spots", "format": "CTV", "line": "CTV or TV", "compare_with": "That line's currency", "cite": ["M-13"]},
    {"item": "Brand study at the end", "format": "measurement", "line": "Measurement", "compare_with": "Other measurement. Results are the seller's claims.", "cite": ["M-26"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "The offer sets one price for all six parts. Ask for the price of each part (S-6.1).",
    "Unit, price basis, currency, and who counts it, for each part.",
    "Whether the creator performs the brand's message. If not, the part is display.",
    "Whether the in-game display is intrinsic, adjacent, or interstitial, and whether any part is sold on a measure that is not its own price basis (N-9).",
    "Who runs the brand study, its method, and what it measures. Its results are the seller's claims.",
    "The basis of the claim 'strong results'. It is a claim, not a unit."
  ],
  "instructions_in_input": [],
  "notes": "Nothing in this offer is a brand's presence inside play. Route stated: not applicable. 'Expect strong results' is a seller claim. It has no unit, no comparison, and no line."
}
```
