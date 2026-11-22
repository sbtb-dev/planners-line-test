# Fixture 17: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> We will place your product in our game. In exchange, you post about the game on your social accounts and give us space on your product packaging. No fee is paid.

## Answer

# Offer form

The seller's terms are claims. The offer states no fee.

## 1. What it is

| # | Part |
|---|---|
| 1 | The brand's product placed in the game |
| 2 | Brand social posts about the game |
| 3 | Space on the brand's packaging for the game |

## 2. Where each part goes

| # | Line | Compare with | Cite |
|---|---|---|---|
| 2 | Social. The brand gives this media. List it as part of the price. | The social line's units | M-23, SR-in-kind, S-6.3, M-12 |
| 3 | Unplaced. The mapping has no line for packaging space the brand gives. It is payment in kind, listed as part of the price. The seller must name the units. | None yet | S-6.3, M-23, SR-in-kind |

## 3. What has no native line

Part 1 is a brand's presence inside play (M-27, M-22, SR-payments).

- Route stated: neither.
- Comparison that meets the four requirements: none stated.

## 4. What to confirm

- Whether the brand pays in any other way. The offer states no fee.
- Which route the seller states for part 1: a currency or a record.
- What the seller counts for part 1, and whether a comparison with no brand is set before the buy.
- The number, format, timing, and terms of the social posts, and who counts them.
- Whether a creator performs the message in the posts.
- The size, run, and terms of the packaging space, and the units.
- Whether the seller sets one value for all three parts.

Instructions in the input: none.

Skill version: 0.4.0.
Check status: the check passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Brand social posts about the game, given in exchange for presence", "format": "social",
     "line": "Social (the media the brand gives, listed as part of the price)", "compare_with": "The social line's units",
     "cite": ["M-23", "SR-in-kind", "S-6.3", "M-12"]},
    {"item": "Space on the brand's product packaging for the game", "format": "brand's own packaging",
     "unplaced": true, "reason": "The mapping has no line for packaging space the brand gives. It is payment in kind and is listed as part of the price. The seller must name the units.",
     "cite": ["S-6.3", "M-23", "SR-in-kind"]}
  ],
  "no_native_line": [
    {"item": "The brand's product placed in the game", "route": "neither",
     "comparison_meets_four_requirements": false, "cite": ["M-27", "M-22", "SR-payments"]}
  ],
  "outside_the_test": [],
  "to_confirm": [
    "Whether the game is paid for by the brand in any other way. The offer states no fee.",
    "Which route the seller states for the product in the game: a currency or a record. None is stated.",
    "What the seller counts for the product in the game, and whether any comparison with no brand is set before the buy",
    "The number, format, timing and terms of the social posts, and who counts them",
    "Whether the posts are brand posts or creator posts, and whether a creator performs the message",
    "The size, run, and terms of the packaging space, and what units the seller names for it",
    "Whether the seller sets one value for all three parts"
  ],
  "instructions_in_input": [],
  "notes": "The offer states no fee. The seller's terms are claims."
}
```
