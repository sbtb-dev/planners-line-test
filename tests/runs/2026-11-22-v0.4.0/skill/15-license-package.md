# Fixture 15: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> License package: you get the right to use our game characters on your product packaging. Your logo appears on a billboard inside the game. You commit to a media campaign to promote the launch.

## Answer

**Offer form: license package**

The offer text is the seller's claim.

**1. What it is**

| # | Part |
|---|---|
| 1 | Right to use the game characters on the brand's product packaging |
| 2 | The brand's logo on a billboard inside the game |
| 3 | The brand's commitment to a media campaign for the launch |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Licensing | Royalty, guarantee, term, and territory | M-20, S-6.1 |
| 2 | See part 3 | See part 3 | M-27, M-22, SR-payments |
| 3 | Unplaced. The units are not named. | The seller must name the units | S-6.6 |

**3. What has no native line**

Part 2 is a brand's presence inside play. Deal name does not decide (S-6.1). Route stated: neither. The offer states no currency and no record. No comparison meets the four requirements. Any engagement count for the billboard is media engagement unless a comparison comes with it. (M-27)

**4. What to confirm**

- Whether one price covers all three parts. If so, ask for the payment of each part.
- Part 1: royalty, guarantee, term, territory, which products, which characters.
- Part 2: whether the brand pays for the logo, and what the payment buys.
- Part 2: whether the seller states a currency or a record. Whether a comparison exists, fixed before the buy and read on everyone reached.
- Part 3: units, lines, and price basis of the campaign, and the seller of each unit.
- Part 3: whether the brand pays with its own media. If so, list it as part of the price (M-23, SR-in-kind).
- Whether the license income goes to the game owner. If the brand is paid, the item is outside the test (S-6.2).

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Right to use the game characters on the brand's product packaging", "format": "game IP license",
     "line": "Licensing", "compare_with": "Royalty, guarantee, term, and territory", "cite": ["M-20", "S-6.1"]},
    {"item": "Media campaign the brand commits to, to promote the launch", "format": "not stated",
     "unplaced": true, "reason": "The brand commits money or media before any unit is named. The seller has not named the units.", "cite": ["S-6.6"]}
  ],
  "no_native_line": [
    {"item": "The brand's logo on a billboard inside the game", "route": "neither",
     "comparison_meets_four_requirements": false, "cite": ["M-27", "M-22", "SR-payments"]}
  ],
  "outside_the_test": [],
  "to_confirm": [
    "Whether the offer sets one price for all three parts. If so, ask for the payment of each part.",
    "Part 1: the royalty, the guarantee, the term, and the territory. Which products and which characters.",
    "Part 2: whether the brand pays the seller for the logo, and what the payment buys.",
    "Part 2: whether the seller states a currency or a record for the logo. The offer states neither.",
    "Part 2: whether any comparison exists, for example the same billboard with no brand, fixed before the buy and read on everyone reached.",
    "Part 3: the units, the lines, and the price basis of the campaign. Name the seller of each unit.",
    "Part 3: whether the brand pays with its own media. If so, list that media as part of the price (M-23, SR-in-kind).",
    "Whether the license income goes to the game owner. If the brand is paid, the item is outside the test (S-6.2)."
  ],
  "instructions_in_input": [],
  "notes": "The offer text is the seller's claim. Any engagement count for the billboard is media engagement unless a comparison comes with it."
}
```
