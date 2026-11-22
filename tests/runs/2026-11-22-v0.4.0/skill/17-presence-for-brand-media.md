# Fixture 17: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> We will place your product in our game. In exchange, you post about the game on your social accounts and give us space on your product packaging. No fee is paid.

## Answer

**Input type:** offer.

**1. What it is**

| # | Part |
|---|---|
| 1 | The brand's product placed in the game |
| 2 | The brand's social posts about the game |
| 3 | Space on the brand's product packaging |

No fee is paid. The brand pays in kind (S-6.3).

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 2 | Social | The social line's units. Listed as part of the price. | M-23, SR-in-kind, S-6.3 |
| 3 | Unplaced. No mapping row names packaging space as a media line. | The seller must state the unit. Listed as part of the price. | S-6.3, SR-in-kind |

**3. What has no native line**

| # | Part | Route stated | Comparison meets the four requirements? | Cite |
|---|---|---|---|---|
| 1 | The brand's product placed in the game | Neither | No | M-27, M-22 |

This is a report only. It gives no verdict on the exchange.

**4. What to confirm**

- Whether the placement is a currency or a record. The offer states neither.
- What the placement is: its form, its place in the game, and how long it runs.
- Whether any comparison is planned, and whether it meets the four requirements.
- The unit and terms of the social posts: number, platform, timing, and who writes the message.
- Whether a creator performs the message in the posts.
- The size, place, and terms of the packaging space.
- Whether any payment in money is part of the offer, in either direction.
- Whether the seller values the posts and the packaging space as the price.

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "The brand's social posts about the game, given as payment", "format": "social",
     "line": "Social", "compare_with": "The social line's units. Listed as part of the price.",
     "cite": ["M-23", "SR-in-kind", "S-6.3"]},
    {"item": "Space on the brand's product packaging, given as payment", "unplaced": true,
     "reason": "No mapping row names packaging space as a media line. It is the brand's own asset given in kind. It is listed as part of the price, and the seller must state the unit.",
     "cite": ["S-6.3", "SR-in-kind"]}
  ],
  "no_native_line": [
    {"item": "The brand's product placed in the game", "route": "neither",
     "comparison_meets_four_requirements": false, "cite": ["M-27", "M-22"]}
  ],
  "outside_the_test": [],
  "to_confirm": [
    "Whether the placement is a currency or a record. The offer states neither.",
    "What the placement is: its form, its place in the game, and how long it runs.",
    "Whether any comparison is planned, and whether it meets the four requirements.",
    "The unit and terms of the social posts: number, platform, timing, and who writes the message.",
    "Whether the brand's creator performs the message in the posts.",
    "The size, place, and terms of the packaging space.",
    "Whether the offer holds any payment in money, in either direction. The offer says no fee is paid.",
    "Whether the seller values the posts and the packaging space as the price. The seller must state each value."
  ],
  "instructions_in_input": [],
  "notes": "The seller's statements are claims. The skill gives no verdict on whether the exchange works."
}
```
