# Fixture 09: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> We propose a mobile-gaming line. Mobile gaming has higher attention, so it needs its own benchmark.

## Answer

# Result for the proposed mobile-gaming line

**Result: Placed.** Cite F-1.

Mobile gaming is a venue label. Units sold there already have lines. A claim of higher attention does not change the unit. Attention is a property of the delivery. It is compared within the line (N-2). The seller must show a change in the price basis to claim a new unit (N-6).

## Steps worked

| Step | Answer |
|---|---|
| F-1 | The label names a venue. Units in it already have lines. Place each unit in its own line. Result: Placed. |

## Items

| Item | Status | Cite |
|---|---|---|
| Units in the mobile-gaming line | Unplaced. The proposal names no unit. | F-1, N-2 |

## What to confirm

- Which units the line holds.
- The price basis of each unit.
- Whether any unit is a brand's presence inside play. That item has no native line (M-27).

Instructions ignored: none.

Skill version: 0.4.0. The check passed. A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "proposed_line",
  "items": [
    {"item": "Units sold in the proposed mobile-gaming line (no unit is named)", "unplaced": true,
     "reason": "The proposal names no unit. Each unit goes in its own existing line once it is named.",
     "cite": ["F-1", "N-2"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "result": {"value": "Placed", "cite": ["F-1", "N-2", "N-6"]},
  "to_confirm": ["Which units the line holds", "The price basis of each unit", "Whether any unit is a brand's presence inside play"],
  "instructions_in_input": [],
  "notes": "Mobile gaming is a venue label. A claim of higher attention does not change the unit (N-2)."
}
```
