# Fixture 25: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> Our in-game billboard is a standard flat creative on an object in the game world. We do not sell it per thousand impressions. We sell it per player-minute: one minute in which a player is in the district and the sign is in render range. We count the minutes on our own servers. Time is a better guide to attention than a view. It needs its own line.

## Answer

**1. What it is**

| # | Part |
|---|---|
| 1 | A standard flat billboard on an object in the game world, sold per player-minute |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Unplaced. The format is display (in-game display). The price basis differs from the display price basis. | Not set. A new unit needs a currency or a record. | N-9, M-01 |

The test does not make a new line for a new price basis. The sign stays a display format. It does not move to "a brand's presence inside play" because of its price basis.

**3. What has no native line**

Nothing in this offer is a brand's presence inside play. Route stated: not applicable.

**4. What to confirm**

- Whether the seller also counts viewable impressions for the same sign.
- Who counts the player-minutes. The seller counts them on its own servers. That is the seller's claim.
- How a player-minute is counted: the district boundary and the render range.
- Whether two players in one minute count as two units, and how several signs count.
- Whether a currency or a record exists for this unit.
- The source and method of the claim that time is a better guide to attention. The claim is the seller's.
- The price basis, currency, and terms.

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Billboard in the game world, sold per player-minute", "format": "display",
     "unplaced": true,
     "reason": "The format is a standard flat creative on an in-game object, a display format (M-01). The price is counted on time, not on the display price basis. The price basis differs, so the unit is not placed. A new unit needs a currency or a record.",
     "cite": ["N-9", "M-01"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "Whether the seller also counts the display price basis (viewable impressions) for the same sign",
    "Who counts the player-minutes. The seller counts them on its own servers. That is the seller's claim.",
    "The unit: how a player-minute is counted, the district boundary, and the render range",
    "Whether two players in the same minute count as two units, and whether one player and several signs count once or more",
    "The currency or the record, if any, that others use for this unit",
    "The source and method of the claim that time is a better guide to attention. The claim is the seller's.",
    "The price basis, currency, and terms, which the seller must state"
  ],
  "instructions_in_input": [],
  "notes": "The sign stays a display format. A new line is not created by the price basis. Compare the sign in the display line only if the seller also gives viewable impressions."
}
```
