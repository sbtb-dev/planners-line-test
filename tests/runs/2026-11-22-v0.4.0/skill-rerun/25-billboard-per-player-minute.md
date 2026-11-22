# Fixture 25: rerun through the skill (final build), v0.4.0

Input given:

> Our in-game billboard is a standard flat creative on an object in the game world. We do not sell it per thousand impressions. We sell it per player-minute: one minute in which a player is in the district and the sign is in render range. We count the minutes on our own servers. Time is a better guide to attention than a view. It needs its own line.

## Answer

# Proposed line: a player-minute line for a flat billboard

**Result: Not a boundary. Failed step: F-3.**

| Step | Finding | Cite |
|---|---|---|
| F-1 | The sign is a standard flat creative. Its format is display. The price is counted on player-minutes, not on the display price basis. This claims a new price basis. The unit is not the same unit, so the item is not placed in the display line. Go to F-2. | F-1, N-9, N-7, M-01 |
| F-2 | The proposal names a count: minutes counted on your own servers. It names no comparison. | F-2, N-3 |
| F-3 | A currency needs a counter that is not the host. Your servers are the host. Other sellers do not count the same event. A buyer cannot swap units across sellers. The count is not a currency. | F-3, C-3.1 |

"Time is a better guide to attention" does not change this. Attention is a property of the delivery. It is compared within the line (N-2). The seller must show a change in the price basis (N-6).

**What to confirm**
- Does a party that is not the host count the player-minutes?
- Do other sellers count the same event the same way?
- Is any comparison fixed before the buy? It must hold the venue constant, be read on everyone reached, and count only the difference as the brand's.
- What is the exact definition of the minute (district, render range)?

This result applies to the description given. It is not a verdict on any seller or on any buy.

- Skill version: 0.4.0.
- Check status: passed (see below).
- A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "proposed_line",
  "items": [
    {"item": "Flat billboard on an object in the game world, sold per player-minute", "format": "display",
     "unplaced": true,
     "reason": "The format is display (M-01). The price is counted on player-minutes, not on the display price basis. This claims a new price basis, so the unit is not the same unit.",
     "cite": ["F-1", "N-9", "N-2", "N-7", "M-01"]}
  ],
  "result": {"value": "Not a boundary", "failed_step": "F-3", "cite": ["F-3", "F-2", "N-3", "C-3.1", "N-6"]},
  "to_confirm": [
    "Whether any party that is not the host counts the player-minutes",
    "Whether other sellers count the same event the same way, so that a buyer can swap units",
    "Whether any comparison is fixed before the buy: the venue held constant, read on everyone reached, only the difference counted as the brand's",
    "The exact definition of the minute: player in the district, sign in render range, and how the render range is set"
  ],
  "notes": "Time is a property of the delivery. It is compared within the line (N-2). The count is made on the seller's own servers, so the counter is the host."
}
```
