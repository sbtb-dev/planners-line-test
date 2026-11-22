# Fixture 26: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> A residency: one sign in a dockside district for eight weeks. You supply one flat design. We bill per player-minute, one minute a player spends in the district while the sign is in render range. We do not quote a rate for views. We set a floor and a cap on billable minutes. If minutes fall below the floor, we extend the term at no charge. Our servers log the minutes. Your team can check the method.

## Answer

# Offer: sign in a dockside district

**1. What it is**

| # | Part |
|---|---|
| 1 | One sign, one flat design, eight weeks, billed per player-minute |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Unplaced. Format: display. The price basis differs. | Not yet. The seller must show a currency or a record for player-minutes. | N-9, M-01 |

The sign is a standard creative in a slot, so it is display. The price is counted on player-minutes. That is not the display price basis. The unit is not the same unit, so the first sentence of the rule does not place it.

The floor, the cap, and the free extension are deal terms. They do not change the unit (N-2).

**3. What has no native line**

Nothing here is a brand's presence inside play. The design is flat. Route stated: neither. The seller's servers log the minutes. The seller is the host, not a third party. No comparison is stated. A minute count is media engagement.

**4. What to confirm**

- Does the seller also count viewable impressions for the sign?
- The definition of a player-minute and of render range.
- Who counts the minutes. Can a party that is not the host check the method?
- How the floor and the cap are set.
- The terms of the free extension.
- Whether the sign is an in-game display unit or something else.
- Any attention or time claim. It is the seller's claim.

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "One sign in a dockside district for eight weeks, with one flat design supplied by the brand, billed per player-minute",
     "format": "display",
     "unplaced": true,
     "reason": "The sign is a standard creative in a slot (display, M-01). The seller counts the price on player-minutes, not on the display price basis. The price basis differs, so it is a new unit with no currency or record.",
     "cite": ["N-9", "M-01"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "Whether the seller also counts viewable impressions for the sign (the display price basis)",
    "The definition of a player-minute, and of render range",
    "Who counts the minutes. The seller's servers are the host, not a third party.",
    "Whether any party that is not the host can check the method, and how",
    "How the floor and the cap on billable minutes are set",
    "The terms of the free extension if minutes fall below the floor",
    "Whether the sign is an in-game display unit or something else, such as an object the brand builds",
    "Any attention or time claim. It is the seller's claim and is compared inside the display line."
  ],
  "instructions_in_input": [],
  "notes": "The floor, the cap, and the free extension are deal terms. They do not change the unit (N-2). The flat design shows a standard creative, so the item is not a brand's presence inside play. A count of minutes is media engagement unless a comparison comes with it."
}
```
