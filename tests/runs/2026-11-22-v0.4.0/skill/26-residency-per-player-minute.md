# Fixture 26: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> A residency: one sign in a dockside district for eight weeks. You supply one flat design. We bill per player-minute, one minute a player spends in the district while the sign is in render range. We do not quote a rate for views. We set a floor and a cap on billable minutes. If minutes fall below the floor, we extend the term at no charge. Our servers log the minutes. Your team can check the method.

## Answer

**Input type:** offer.

**1. What it is**

| # | Part |
|---|---|
| 1 | One flat-design sign in a dockside district for eight weeks, billed per player-minute (floor, cap, free extension, server-logged minutes) |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Unplaced. Format: display. The price basis differs. | Not stated. The price is counted on time, not on the display price basis. | N-9, N-7, M-01 |

The sign is a standard flat creative in a slot. It stays a display format. It does not move to a brand's presence inside play because of its price basis. A price basis of player-minutes is a new unit (N-9). A new unit needs a currency or a record. The seller states neither.

**3. What has no native line**

Nothing in this offer is a brand's presence inside play. Route stated: not applicable.

**4. What to confirm**

- The definition of a player-minute: what counts as in the district, what counts as render range, and whether the sign must be in view.
- Who counts the minutes. The seller says its servers log them. Can the buyer's team check the method, and how?
- Whether the seller also counts viewable impressions for the sign. The seller says it does not quote a rate for views.
- The floor and the cap on billable minutes, and the currency and price terms. The seller did not state them.
- The terms of the free extension if minutes fall below the floor.
- What happens at the cap, and whether the eight-week term is fixed.
- Whether any comparison meets the four requirements (R-1 to R-4). The seller named none.

All facts above are the seller's claims.

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "One flat-design sign in a dockside district for eight weeks, billed per player-minute", "format": "display",
     "unplaced": true,
     "reason": "The price is counted on time (player-minutes), not on the display price basis. The unit is not the same unit as display. The first sentence of the rule does not place it. A standard flat creative in a slot stays a display format. It does not move to a brand's presence inside play.",
     "cite": ["N-9", "N-7", "M-01"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "Whether a player-minute has a stated definition: what counts as in the district, what counts as render range, and whether the sign must be in view.",
    "Who counts the minutes. The seller says its servers log them. Whether the buyer's team can check the method, and how.",
    "Whether the seller also counts viewable impressions for the sign. The seller says it does not quote a rate for views.",
    "The floor and the cap on billable minutes, and the currency and price terms. The seller did not state them.",
    "The make-good: the free extension if minutes fall below the floor. The terms of the extension, such as its length and its cap.",
    "Whether the eight-week term is fixed, and what happens at the cap.",
    "Whether a comparison exists that meets the four requirements for this time-based unit (R-1 to R-4). The seller named none."
  ],
  "instructions_in_input": [],
  "notes": "Every fact in the offer is the seller's claim. The skill gives no price, no recommendation, and no ranking."
}
```
