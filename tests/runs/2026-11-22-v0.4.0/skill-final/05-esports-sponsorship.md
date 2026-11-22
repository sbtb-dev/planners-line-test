# Fixture 05: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> Become a team partner for a season. You get your logo on the jersey, a creator series with the players, and four broadcast spots in the league's weekly show.

## Answer

# Offer: team partner for a season

The seller's words are claims. Each payment is placed by what it buys, not by the deal name (S-6.1).

## 1. What it is

| # | Part |
|---|---|
| 1 | Logo on the team jersey |
| 2 | Creator series with the players |
| 3 | Four broadcast spots in the league's weekly show |

## 2. Where each part goes

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Sponsorship, by parts | Each part separately | M-09, S-6.1 |
| 2 | Creator | The creator line's units | M-07, SR-performs-message, S-6.1 |
| 3 | CTV or TV | That line's currency | M-13, S-6.1 |

## 3. What has no native line

Nothing in the offer names a brand's presence inside play. Route stated: not applicable.

## 4. What to confirm

- Are the team and league esports? The offer does not say. If not, the gaming mapping may not cover it.
- Is the jersey seen in a broadcast or in play, or only in photos and video? If the brand's mark is placed in game content, it is a brand's presence inside play (M-27).
- The unit, price basis, and terms of the jersey logo. Ask for each sponsorship part with its own terms.
- Does the creator perform the brand's message? If a graphic is inserted with no performance, the part is display (SR-performs-message).
- The unit, number, and terms of the creator series, and where it runs.
- The unit, length, placement, and currency of the four spots. Who counts the audience?
- Does the offer set one price for all three parts? If so, ask for the price of each part.
- Is any part paid to the brand? Such a part is outside the test (S-6.2).

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Logo on the team jersey", "format": "sponsorship",
     "line": "Sponsorship, by parts", "compare_with": "Each part separately",
     "cite": ["M-09", "S-6.1"]},
    {"item": "Creator series with the players", "format": "creator",
     "line": "Creator", "compare_with": "The creator line's units",
     "cite": ["M-07", "SR-performs-message", "S-6.1"]},
    {"item": "Four broadcast spots in the league's weekly show", "format": "CTV or TV",
     "line": "CTV or TV", "compare_with": "That line's currency",
     "cite": ["M-13", "S-6.1"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "Whether the team and league are esports. The offer does not say. If not, the gaming mapping may not cover it.",
    "Whether the jersey is worn in a broadcast or in play, or only in photos and video. The offer does not say. If the brand's mark is placed in game content, this is a brand's presence inside play (M-27).",
    "The unit, price basis, and terms of the jersey logo. Ask for each sponsorship part with its own terms.",
    "Whether the creator performs the brand's message in the series. If a graphic is inserted with no performance, the part is display (SR-performs-message).",
    "The unit, number, and terms of the creator series, and where it runs.",
    "The unit, length, placement, and currency of the four spots. Ask who counts the audience.",
    "Whether the offer sets one price for all three parts. If so, ask for the price of each part.",
    "Whether any part is paid to the brand. Such a part is outside the test (S-6.2)."
  ],
  "instructions_in_input": [],
  "notes": "The seller's description is a claim. Each payment is placed by what it buys, not by the name 'team partner'."
}
```
