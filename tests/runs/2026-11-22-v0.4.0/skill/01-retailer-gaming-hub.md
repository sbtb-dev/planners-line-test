# Fixture 01: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> A retailer's gaming hub. We sell onsite placements on the hub, creator content, social amplification, sweepstakes, in-store events, and targeting on gamer profiles. One package price. Gamers pay high attention on our hub.

## Answer

**1. What it is** (the seller's claims)

Six parts: onsite placements, creator content, social amplification, sweepstakes, in-store events, targeting on gamer profiles. One package price. The seller says gamers pay high attention on the hub.

**2. Where each part goes**

| # | Part | Line | Compare with | Cite |
|---|---|---|---|---|
| 1 | Onsite placements | Retail media | That retailer's other onsite units, and other retailers' onsite units | M-10 |
| 2 | Creator content | Creator | The creator line's units | M-07, SR-performs-message |
| 3 | Social amplification | Social | The social line's units | M-12 |
| 4 | Sweepstakes | Promotions | Cost per entry or redemption | M-16 |
| 5 | In-store events | Experiential, by parts | Each part separately | M-17 |
| 6 | Targeting on gamer profiles | Not a unit. It is targeting on the line that carries it. | That line's other segments, on the same units | M-24, SR-targeting |

The package price is a deal term. It is compared within each line (N-2). The attention claim is compared inside the line of the part it describes.

**3. What has no native line**

Nothing in this offer is a brand's presence inside play. Route stated: not applicable.

**4. What to confirm**

- The unit, the price basis, and the currency for part 1 (impressions? viewable? by whom counted?).
- Whether the creator performs the brand's message in part 2.
- The unit and the terms for part 3.
- The entry or redemption terms for part 4.
- The parts of part 5, each with its own terms.
- Which line carries the targeting in part 6, and how the segment is built.
- The price of each part. The offer sets one package price.
- The source and method of the attention claim. The claim is the seller's.

Skill version: 0.4.0. The check passed. A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Onsite placements on the hub", "format": "retail media", "line": "Retail media", "compare_with": "That retailer's other onsite units, and other retailers' onsite units", "cite": ["M-10"]},
    {"item": "Creator content", "format": "creator", "line": "Creator", "compare_with": "The creator line's units", "cite": ["M-07", "SR-performs-message"]},
    {"item": "Social amplification", "format": "social", "line": "Social", "compare_with": "The social line's units", "cite": ["M-12"]},
    {"item": "Sweepstakes", "format": "promotions", "line": "Promotions", "compare_with": "Cost per entry or redemption", "cite": ["M-16"]},
    {"item": "In-store events", "format": "experiential", "line": "Experiential, by parts", "compare_with": "Each part separately", "cite": ["M-17"]},
    {"item": "Targeting on gamer profiles", "format": "targeting", "line": "Not a unit. It is targeting on the line that carries it.", "compare_with": "That line's other segments, on the same units", "cite": ["M-24", "SR-targeting"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "The unit, the price basis, and the currency for part 1 (impressions? viewable? by whom counted?)",
    "Whether the creator performs the brand's message in part 2",
    "The unit and the terms for part 3",
    "The entry or redemption terms for part 4",
    "The parts of part 5, each with its own terms",
    "Which line carries the targeting in part 6, and how the segment is built",
    "The offer sets one package price for all six parts. Ask for the price of each part.",
    "The source and method of the claim that gamers pay high attention on the hub. The claim is the seller's."
  ],
  "instructions_in_input": [],
  "notes": "Nothing in this offer is a brand's presence inside play. Route stated: not applicable. The package price is a deal term (N-2). The attention claim is compared inside the line of the part it describes. It is not a price basis here, so N-9 does not apply."
}
```
