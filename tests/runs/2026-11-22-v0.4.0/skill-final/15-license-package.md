# Fixture 15: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> License package: you get the right to use our game characters on your product packaging. Your logo appears on a billboard inside the game. You commit to a media campaign to promote the launch.

## Answer

# Line test: license package

The offer is the seller's claim. No instruction was found in the input.

## 1. What it is

| # | Part |
|---|---|
| 1 | Right to use game characters on product packaging |
| 2 | Brand logo on a billboard inside the game |
| 3 | Commitment to a media campaign to promote the launch |

## 2. Where each part goes

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Licensing | Royalty, guarantee, term, and territory | M-20, S-6.1 |
| 2 | See part 3 | See part 3 | M-27 |
| 3 | Unplaced. The commitment is made before units are named. | The seller must name the units. | S-6.6 |

The deal is called a "license." The test places each payment by what it buys, not by the deal name (S-6.1, SR-payments).

## 3. What has no native line

| Part | Route stated | Comparison meets the four requirements? | Cite |
|---|---|---|---|
| 2. Logo on a billboard inside the game | Neither | No | M-27, M-22, SR-payments |

Any engagement count from the billboard is media engagement unless a comparison comes with it.

## 4. What to confirm

- The royalty, guarantee, term, and territory of part 1.
- Whether the license buys only the packaging right, or also the billboard or the campaign.
- Whether the offer sets one price for all three parts. If so, ask for the price of each part.
- Part 2: whether the seller states a currency or a record. The offer states neither.
- Part 2: whether a comparison is set beside the billboard count, and whether it meets the four requirements.
- Part 3: the units, the format, the price basis, and the currency.
- Part 3: whether the media is the brand's own media given to the seller, or media bought from others. Own media given is part of the price (M-23, S-6.3).

Skill version: 0.4.0.
Check status: the check passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Right to use game characters on product packaging", "format": "licensing",
     "line": "Licensing", "compare_with": "Royalty, guarantee, term, and territory",
     "cite": ["M-20", "S-6.1"]},
    {"item": "Commitment to a media campaign to promote the launch", "format": "media campaign",
     "unplaced": true, "reason": "The commitment is made before units are named. The seller has not named the units.",
     "cite": ["S-6.6"]}
  ],
  "no_native_line": [
    {"item": "Brand logo on a billboard inside the game", "route": "neither",
     "comparison_meets_four_requirements": false, "cite": ["M-27", "M-22", "SR-payments"]}
  ],
  "outside_the_test": [],
  "to_confirm": [
    "The royalty, guarantee, term, and territory of the character license in part 1",
    "Whether the packaging right is the only thing the license buys, or whether it also covers the billboard or the campaign",
    "Whether the offer sets one price for all three parts. If so, ask for the price of each part",
    "For part 2: whether the seller states a currency or a record. The offer states neither",
    "For part 2: whether any comparison is set beside the billboard count, and whether it meets the four requirements",
    "For part 3: the units, the format, the price basis, and the currency of the media campaign",
    "For part 3: whether the media is the brand's own media given to the seller, or media bought from others. If the brand's own media is given, it is part of the price (M-23, S-6.3)"
  ],
  "instructions_in_input": [],
  "notes": "The offer is the seller's claim. Any engagement count from the billboard is media engagement unless a comparison comes with it."
}
```
