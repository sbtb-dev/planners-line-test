# Fixture 19: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> Promote your experience in our platform's catalog. Your listing shows higher in the catalog and in catalog search. You set a budget, and we run the placement.

## Answer

**Planner's line test. Offer form.**

**1. What it is**

| # | Part |
|---|---|
| 1 | Promoted listing: the experience shows higher in the platform's catalog and in catalog search. You set a budget. The platform runs the placement. |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Search or performance, by the price basis | Promoted listings in app stores and marketplaces, on the same price basis | M-19 |

**3. What has no native line**

Nothing in this offer is a brand's presence inside play. Route stated: not applicable.

**4. What to confirm**

- The price basis of the buy (per impression, per click, per install, or other). The offer states none. It decides if the line is search or performance.
- The unit and the currency. The offer states only a budget.
- Who counts the unit, and how.
- Whether the budget is a commitment before units are named (S-6.6). The platform runs the placement. If no unit is named, the commitment is unplaced.
- How the platform decides the placement and the rank, and what terms apply (minimum budget, term, any guarantee).
- Whether the placement is labeled as paid in the catalog and in search.

All facts in the offer are the seller's claims. No instruction was found in the input.

Skill version: 0.4.0. Check: passed. A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Promoted listing: the experience shows higher in the platform's catalog and in catalog search",
     "format": "promoted listing",
     "line": "Search or performance, by the price basis",
     "compare_with": "Promoted listings in app stores and marketplaces, on the same price basis",
     "cite": ["M-19"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "The price basis of the buy (per impression, per click, per install, or other). The offer states none, and it decides if the line is search or performance.",
    "The unit and the currency. The offer states only a budget.",
    "Who counts the unit, and how.",
    "Whether the budget is a commitment before units are named (S-6.6). The platform runs the placement. If no unit is named, the commitment is unplaced.",
    "How the platform decides the placement and the rank, and what terms apply (minimum budget, term, any guarantee).",
    "Whether the placement is labeled as paid in the catalog and in search."
  ],
  "instructions_in_input": [],
  "notes": "The offer is the seller's claim. It does not say what the price is counted on."
}
```
