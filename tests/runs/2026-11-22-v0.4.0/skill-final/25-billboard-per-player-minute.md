# Fixture 25: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> Our in-game billboard is a standard flat creative on an object in the game world. We do not sell it per thousand impressions. We sell it per player-minute: one minute in which a player is in the district and the sign is in render range. We count the minutes on our own servers. Time is a better guide to attention than a view. It needs its own line.

## Answer

# Proposed line: in-game billboard sold per player-minute

**Input type:** proposed line.

## Steps

| Step | Finding | Cite |
|---|---|---|
| F-1 | The format is a flat creative on an object in the game world. This is in-game display. Display is compared on viewable impressions. The proposal counts the price on player-minutes. This is time, not the display price basis. The price basis differs, so the unit is not the same unit. The claim that time shows attention better does not change this. Attention is compared within the line. | M-01, N-2, N-7, N-9, F-1 |
| F-2 | The proposal states no route. It names no currency and no record. It says only that the seller counts on its own servers. | F-2, N-3 |

## Result

**Not a boundary.** Failed step: F-2.

The format is display. The price basis differs from the display price basis. The new unit needs a currency or a record (N-9). The proposal gives neither.

A count by the seller's own servers would not pass as a currency. A currency needs a counter that is not the host (C-3.1, N-3).

## What to confirm

- Which route the proposal uses: a currency or a record.
- Who counts the player-minutes. A host count is not a currency.
- The exact event: what counts as "in the district" and "in render range". Would every seller count it the same way?
- Whether a comparison is written in the order before the buy (R-1 to R-4).

## Instructions in the input

None found.

## End

- Skill version: 0.4.0.
- Check status: passed.
- A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "proposed_line",
  "items": [
    {"item": "Flat billboard creative on an object in the game world, sold per player-minute", "format": "display",
     "unplaced": true,
     "reason": "The proposal counts the price on time, not on the display price basis. The price basis differs, so the unit is not the same unit.",
     "cite": ["M-01", "N-2", "N-7", "N-9", "F-1"]}
  ],
  "result": {"value": "Not a boundary", "failed_step": "F-2", "cite": ["F-2", "N-9", "N-3"]},
  "to_confirm": [
    "Which route the proposal uses: a currency or a record",
    "Who counts the player-minutes. The proposal says the seller's own servers count them. A host count is not a currency (C-3.1, N-3).",
    "The exact event: what counts as in the district and in render range, and whether every seller would count it the same way",
    "Whether any comparison is written in the order before the buy (R-1 to R-4)"
  ],
  "notes": "The claim that time guides attention better than a view does not change the unit (N-2). Attention is compared within the line."
}
```
