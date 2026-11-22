# Fixture 09: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> We propose a mobile-gaming line. Mobile gaming has higher attention, so it needs its own benchmark.

## Answer

# Proposed-line result: mobile-gaming line

**Result: Placed.** Cite F-1 and N-2.

A line named for a venue or an audience holds units that already have lines (F-1). A claim of higher attention does not change this. Attention is a property of the delivery. It is compared within the line (N-2). So a mobile-gaming line needs no benchmark of its own.

| Part | Line | Cite |
|---|---|---|
| Proposed mobile-gaming line | Place each unit in its own line | F-1, N-2 |

The proposal states no units. I cannot place each unit yet.

## What to confirm
- The units sold in the line, each with its format.
- The price basis of each unit.
- Whether any price is counted on attention or time in place of the format's own price basis (N-9). If yes, the price basis differs. Name the format.
- Whether the line includes a brand's presence inside play (M-27). It has no native line.

This result applies to the description given. It is not a verdict on any seller or buy.

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "proposed_line",
  "items": [
    {"item": "Proposed mobile-gaming line", "unplaced": true,
     "reason": "The proposal names a venue and an audience, not a unit. Its units are not stated, so each unit cannot be placed yet. A claim of higher attention does not change the unit.",
     "cite": ["F-1", "N-2"]}
  ],
  "result": {"value": "Placed", "cite": ["F-1", "N-2"]},
  "to_confirm": [
    "The units sold in the line, each with its format",
    "The price basis of each unit",
    "Whether any price is counted on attention or time in place of the format's own price basis (N-9)",
    "Whether the line includes a brand's presence inside play (M-27)"
  ],
  "notes": "Place each unit in its own line once the units are known. Attention is compared within the line."
}
```
