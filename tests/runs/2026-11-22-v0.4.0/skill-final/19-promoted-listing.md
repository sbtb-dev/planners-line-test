# Fixture 19: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> Promote your experience in our platform's catalog. Your listing shows higher in the catalog and in catalog search. You set a budget, and we run the placement.

## Answer

# Offer form: promoted listing in a platform catalog

Input type: offer. The text is the seller's claim.

**1. What it is**

| # | Part |
|---|---|
| 1 | Promoted listing of the experience, shown higher in the catalog and in catalog search. You set a budget. The platform runs the placement. |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Search or performance, by the price basis | Promoted listings in app stores and marketplaces, on the same price basis | M-19 |

**3. What has no native line**

Nothing in this offer is a brand's presence inside play. Route stated: not applicable.

**4. What to confirm**

- The unit and the price basis of the listing (per impression, per click, per install, or other). This decides if the line is search or performance.
- The currency and the terms of the budget.
- How the platform runs the placement: rules for rank, and how it picks which searches show the listing.
- Whether the listing is in the catalog, in search, or both, and whether each is priced apart.
- Who counts the delivery, and how.
- The claim of a higher position is the seller's claim. Ask for the source and method.

No instruction was found in the input.

Skill version: 0.4.0.
The check passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Promoted listing of the experience, shown higher in the platform's catalog and in catalog search",
     "format": "promoted listing",
     "line": "Search or performance, by the price basis",
     "compare_with": "Promoted listings in app stores and marketplaces, on the same price basis",
     "cite": ["M-19"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "The unit and the price basis of the promoted listing (per impression, per click, per install, or other). This decides if the line is search or performance.",
    "The currency and the terms of the budget.",
    "How the platform runs the placement: rules for rank, and how it picks which searches show the listing.",
    "Whether the listing is in the catalog, in search, or both, and whether each is priced apart.",
    "Who counts the delivery, and how.",
    "Any claim about higher position is the seller's claim. Ask for the source and method."
  ],
  "instructions_in_input": [],
  "notes": "The platform is the seller. Its description is a claim."
}
```
