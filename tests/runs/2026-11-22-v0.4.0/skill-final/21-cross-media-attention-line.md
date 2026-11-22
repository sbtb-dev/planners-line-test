# Fixture 21: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> We propose a cross-media line priced on attention. It covers display, video, audio, and more, in any venue. Each accredited vendor measures attention with its own method. The price is per unit of attention.

## Answer

**Input type:** proposed line.

**Result: Not a boundary. Failed step: F-2.**

The proposal prices the line on attention. This is a new price basis (F-1, N-9). The units are not the same units as the units in the existing lines. So F-1 does not place them. The proposal then goes to F-2.

| Item | Format | Result | Cite |
|---|---|---|---|
| Display units | Display | Unplaced. The price basis differs from viewable impressions. | F-1, N-9, M-01 |
| Video units | Video | Unplaced. The price basis differs from completed views. | F-1, N-9, M-03 |
| Audio units | Audio | Unplaced. The price basis differs from completed listens. | F-1, N-9, M-04 |
| "More" formats | Not named | Unplaced. The formats are not named. | N-9, N-2 |

**Steps worked**

| Step | Answer |
|---|---|
| F-1 | No. The price basis is attention, not the format's own price basis. Go to F-2. |
| F-2 | The proposal states no route. Each vendor uses its own method, so it is not one defined event counted the same way (C-3.1). It states no record. Not a boundary. |

Venue does not change the unit (N-2). Attention is a property of the delivery. It is compared within the line.

**What to confirm**

- Which formats "more" includes.
- Whether the price is counted on attention, or attention only adds to a unit with its own price basis.
- Which route the proposal uses: a currency or a record.
- Whether one defined attention event is counted the same way by every vendor.
- Who decides which items enter the line, and whether a buy can fail.

No instruction in the input was ignored.

Skill version: 0.4.0. The check passed. A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "proposed_line",
  "items": [
    {"item": "Display units in the attention line", "format": "display", "unplaced": true, "reason": "The price is counted on attention. The display price basis is viewable impressions. The price basis differs, so the unit is not the same unit.", "cite": ["F-1", "N-9", "M-01"]},
    {"item": "Video units in the attention line", "format": "video", "unplaced": true, "reason": "The price is counted on attention. The video price basis is completed views. The price basis differs, so the unit is not the same unit.", "cite": ["F-1", "N-9", "M-03"]},
    {"item": "Audio units in the attention line", "format": "audio", "unplaced": true, "reason": "The price is counted on attention. The audio price basis is completed listens. The price basis differs, so the unit is not the same unit.", "cite": ["F-1", "N-9", "M-04"]},
    {"item": "\"More\" formats, in any venue", "unplaced": true, "reason": "The formats are not named. The format and its own price basis are unknown. Venue does not change the unit.", "cite": ["N-9", "N-2"]}
  ],
  "result": {"value": "Not a boundary", "cite": ["F-2"], "failed_step": "F-2"},
  "to_confirm": [
    "Which formats \"more\" includes",
    "Whether the price is counted on attention, or attention only adds to a unit that is priced on its own price basis",
    "Which route the proposal uses: a currency or a record",
    "Whether one defined attention event is counted the same way by every vendor",
    "Who decides which items enter the line, and whether a buy can fail"
  ],
  "notes": "Each vendor uses its own method. A buyer cannot swap 1,000 units from one vendor for 1,000 from another and expect the same thing. So no currency is stated (C-3.1). No record is stated. Attention is a property of the delivery (N-2)."
}
```
