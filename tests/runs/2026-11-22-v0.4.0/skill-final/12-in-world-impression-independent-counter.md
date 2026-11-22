# Fixture 12: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> We propose a line built on one defined event. An in-world impression is one event: a branded object is rendered on a player's screen at ten metres or less. The event has no minimum pixel share and no minimum time. A party that is not the host counts it, the same way on every platform. Membership is set by the definition, before the buy. A buy can miss its count.

## Answer

# Proposed-line result

**Result: A boundary on paper (F-5).**

## Steps worked

| Step | Finding | Cite |
|---|---|---|
| F-1 | A brand's object inside game content has no native line. The event has no minimum pixel share and no minimum time. It is not the viewable impression of the display line. The price basis differs. Go to F-2. | M-27, N-9, F-1 |
| F-2 | The proposal states a route: a currency. It names one defined event and a counter that is not the host. | F-2, N-3 |
| F-3 | On paper, the exchange check can pass. The event is defined, and the same on every platform. | F-3, C-3.1 |
| F-4 | The definition sorts items before the buy. A buy can miss its count. | F-4, N-4 |
| F-5 | The description passes all steps. | F-5 |

## Items

| Item | Status | Cite |
|---|---|---|
| In-world impression (branded object on screen at ten metres or less) | Unplaced in an existing line. Price basis differs. | M-27, N-9 |

## Brand presence inside play

| Item | Route stated | Comparison meets the four requirements | Cite |
|---|---|---|---|
| A branded object in game content | Currency | No. No comparison is stated. | M-27 |

## What must be shown in practice

- A counter that is not the host counts the same event, the same way, on every platform.
- A buyer can swap 1,000 from one seller for 1,000 from another.
- A buy has missed its count in a real case.

## What to confirm

- Who writes and holds the definition. Can the seller change it?
- Who counts. Is it not the host, and not paid by the host?
- How "branded object" is defined, and how ten metres is measured on each platform.
- That the count is the same on every platform.
- What happens when a buy misses its count, and who decides.
- The unit, the price basis, and the terms of the buy.

A count of this event supports a price for exposure only (N-5). It does not support a price for response.

This result applies to the description given. It is not a verdict on any seller or buy.

Skill version: 0.4.0.
Check status: the check passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "proposed_line",
  "items": [
    {"item": "In-world impression: a branded object rendered on a player's screen at ten metres or less", "format": "A brand's presence inside play (branded object in game content)",
     "unplaced": true,
     "reason": "The event has no minimum pixel share and no minimum time, so it is not the viewable impression of the display line. The price basis differs. A brand's mark in game content has no native line.",
     "cite": ["M-27", "N-9", "F-1"]}
  ],
  "no_native_line": [
    {"item": "A branded object rendered in game content", "route": "currency",
     "comparison_meets_four_requirements": false, "cite": ["M-27"]}
  ],
  "result": {"value": "A boundary on paper", "cite": ["F-5"]},
  "in_practice": "Show that a counter that is not the host counts the same defined event, the same way, on every platform, and that two sellers' counts can be swapped one for one. Show that a buy has missed its count in a real case.",
  "to_confirm": [
    "Who writes and holds the definition, and whether the seller can change it",
    "Who the counting party is, and that it is not the host and not paid by the host",
    "How a branded object is defined, and how ten metres is measured on each platform",
    "That the count is the same on every platform, tested by exchange of 1,000 from one seller for 1,000 from another",
    "What happens when a buy misses its count, and who decides it",
    "The unit, the price basis, and the terms of the buy"
  ],
  "notes": "Route stated: currency. F-2 passes. F-3: on paper, the exchange check (C-3.1) can pass, because the event is defined and counted by a party that is not the host. F-4: membership is set by the definition before the buy, and a buy can fail (N-4). This is not a record route, so the four requirements (R-1 to R-4) are not met and no comparison is stated. A count of this event supports a price for exposure only (N-5)."
}
```
