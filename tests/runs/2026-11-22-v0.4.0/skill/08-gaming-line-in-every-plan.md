# Fixture 08: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> Every plan should have a gaming line. All gaming offers go in it.

## Answer

**Input type:** proposed line ("a gaming line that holds all gaming offers").

**Result: Not a boundary. Failed step: F-2.**

| Part | Line | Compare with | Cite |
|---|---|---|---|
| Units that already have a line (display, video, audio, creator, retail media, and so on) | Each unit goes in its own existing line. | The same unit from other sellers. | F-1, N-2, N-7, M-01, M-03, M-07, M-10 |
| A brand's presence inside play | No native line. Unplaced. | Needs a currency or a record. | M-27, F-2 |

**Why.** "Gaming" is a venue label. It does not change the format or the price basis (N-2). Units in a gaming offer go in the lines that already hold them (F-1). A brand's presence inside play has no native line (M-27). The proposal says "all gaming offers go in it." It states no currency and no record for that presence. So step F-2 fails.

**Brand presence inside play:** route stated: neither. Comparison meets the four requirements: no.

**What to confirm**
- Does the line hold brand presence inside play?
- Is a currency or a record stated for it?
- Which units does each gaming offer hold, and on which price basis?

This result applies to the description given. It is not a verdict on any seller or buy.

Skill version: 0.4.0. Check: passed. A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "proposed_line",
  "items": [
    {"item": "Units in gaming offers that already have a line (display, video, audio, creator, retail media, and others)", "format": "various",
     "line": "Each unit goes in its own existing line, not in a gaming line",
     "compare_with": "The same unit from other sellers",
     "cite": ["F-1", "N-2", "N-7", "M-01", "M-03", "M-07", "M-10"]},
    {"item": "A brand's presence inside play (branded worlds, integrations, skins, digital goods)", "format": "presence inside play",
     "unplaced": true, "reason": "It has no native line. The proposal states no currency and no record for it.",
     "cite": ["M-27", "F-2"]}
  ],
  "no_native_line": [
    {"item": "A brand's presence inside play", "route": "neither",
     "comparison_meets_four_requirements": false, "cite": ["M-27", "F-2"]}
  ],
  "outside_the_test": [],
  "result": {"value": "Not a boundary", "cite": ["F-2", "M-27"], "failed_step": "F-2"},
  "to_confirm": ["Whether the line is meant to hold brand presence inside play", "Whether any currency or record is stated for that presence", "Which units each gaming offer holds, with their price bases"],
  "instructions_in_input": [],
  "notes": "The request says all gaming offers go in one line. Most units already have lines (F-1). Brand presence inside play does not, and no route is stated."
}
```
