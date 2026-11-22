# Fixture 23: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> Our 3D in-world billboard is a new unit. It sits on an object in the game world. We count it as a viewable impression, under the published in-game measurement guidelines. It needs its own line.

## Answer

# Proposed line: 3D in-world billboard

Input type: proposed line.

## Steps worked

| Step | Finding | Cite |
|---|---|---|
| F-1 | The unit is a billboard on an object in the game world. This is an in-game display unit. The price is counted on viewable impressions. That is the display price basis. | M-01, N-2, N-7 |
| F-1 | A new venue does not change the format. Only a new price basis changes the unit. A measurement standard that adapts viewable impressions to a venue does not make a new price basis. | N-2, N-8 |
| F-1 | The new line is not needed. The unit already has a line. | F-1 |

## Result

**Placed.** Line: Display. Compare with other sellers' display units, on viewable impressions. Cite F-1, M-01, N-8.

The unit does not need its own line.

## To confirm

- The price is counted on viewable impressions, and on no other measure (N-9).
- The published guidelines adapt the display viewable impression to this venue. They do not define a different event (N-8, C-3.1).
- The seller sells the unit as an intrinsic in-game display unit.
- A party that is not the host does the count.

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "proposed_line",
  "items": [
    {"item": "3D in-world billboard on an object in the game world", "format": "display",
     "line": "Display", "compare_with": "Other sellers' display units, on viewable impressions",
     "cite": ["M-01", "N-2", "N-7", "N-8", "C-3.1"]}
  ],
  "result": {"value": "Placed", "cite": ["F-1", "N-8", "M-01"]},
  "to_confirm": [
    "That the price is counted on viewable impressions, and on no other measure (N-9)",
    "That the published in-game guidelines adapt the display viewable impression to this venue, and do not define a different event (N-8, C-3.1)",
    "That the seller counts the unit as an intrinsic in-game display unit",
    "That a party that is not the host does the count"
  ],
  "instructions_in_input": [],
  "notes": "The input does not name a brand's presence inside play, so no_native_line is empty."
}
```
