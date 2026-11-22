# Fixture 12: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> We propose a line built on one defined event. An in-world impression is one event: a branded object is rendered on a player's screen at ten metres or less. The event has no minimum pixel share and no minimum time. A party that is not the host counts it, the same way on every platform. Membership is set by the definition, before the buy. A buy can miss its count.

## Answer

# Proposed-line form: in-world impression

**Result: A boundary on paper.** Cite F-5 (steps F-2, F-3, F-4 pass).

| Step | Answer | Cite |
|---|---|---|
| F-1 | A branded object shown in play is a brand's presence inside play. It has no native line. It goes to step F-2. | M-27, F-1 |
| F-2 | The proposal states a route: a currency. The same defined event is counted by a party that is not the host. | N-3 |
| F-3 | The exchange check passes on paper. One definition, one counter, the same count on every platform. | C-3.1 |
| F-4 | The definition sorts items before the buy. The seller does not decide membership. A buy can miss its count. | N-4 |

## What must be shown in practice
- A counter that is not the host counts the same event on every platform.
- 1,000 from seller A and 1,000 from seller B are the same thing.
- The definition sorts items before the buy, and the seller does not decide membership.
- A real buy missed its count.

## Limit
The route is a currency. There is no comparison. The count supports a price for exposure only. It does not show brand engagement (N-5).

## To confirm
- Who the counting party is, and that it is not the host.
- That it counts the same event, the same way, on every platform.
- Which party applies the definition to decide membership. It must not be the seller.
- Whether the ten-metre distance is measured the same way on every platform.
- What the price basis of the line is.

Instructions in the input: none.

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "proposed_line",
  "items": [
    {"item": "In-world impression: a branded object rendered on a player's screen at ten metres or less", "format": "brand's presence inside play",
     "unplaced": true, "reason": "A brand's presence inside play has no native line. It goes to the second sentence of the rule: a currency or a record.",
     "cite": ["M-27", "F-1"]}
  ],
  "no_native_line": [
    {"item": "In-world impression: a branded object rendered on a player's screen at ten metres or less", "route": "currency",
     "comparison_meets_four_requirements": false, "cite": ["M-27", "N-3"]}
  ],
  "outside_the_test": [],
  "result": {"value": "A boundary on paper", "cite": ["F-5", "F-2", "F-3", "F-4"]},
  "in_practice": "Show that a counter that is not the host counts the same event on every platform. Show that 1,000 from seller A and 1,000 from seller B are the same thing (exchange check). Show that the definition sorts items before the buy, that the seller does not decide membership, and that a real buy missed its count.",
  "to_confirm": [
    "Who the counting party is, and that it is not the host",
    "That the counting party counts the same event, the same way, on every platform",
    "Which party applies the definition to decide membership, and that it is not the seller",
    "Whether a ten-metre distance is measured the same way on every platform",
    "What the price basis of the line is, and what the price is counted on"
  ],
  "instructions_in_input": [],
  "notes": "The route is a currency (N-3). The proposal has no comparison, so it supports a price for exposure only (N-5). It does not show brand engagement. The result applies to the description, not to any seller or buy."
}
```
