# Fixture 05: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> Become a team partner for a season. You get your logo on the jersey, a creator series with the players, and four broadcast spots in the league's weekly show.

## Answer

**Offer form: team partner for a season**

All facts below are the seller's claims.

**1. What it is**

| # | Part |
|---|---|
| 1 | Logo on the jersey for a season |
| 2 | Creator series with the players |
| 3 | Four broadcast spots in the league's weekly show |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Sponsorship, by parts | Each part separately | M-09, S-6.1 |
| 2 | Creator | The creator line's units | M-07, SR-performs-message |
| 3 | CTV or TV | That line's currency | M-13 |

Each payment goes to its own line, not to the name of the deal. Any attention claim is compared inside the line of the part it describes.

**3. What has no native line**

Nothing in this offer is a brand's presence inside play. Route stated: not applicable.

**4. What to confirm**

- Whether the team and league are esports. The offer does not say. Rows M-09 and M-13 are written for esports. Parts 1 and 3 depend on this.
- Part 1: the parts of the sponsorship rights, and the terms of each. Is the logo worn in play, or only on a team item?
- Part 2: do the players perform the brand's message? If the brand's graphic is shown and the players do not perform it, the item is display.
- Part 2: the unit, the price basis, and the number of episodes.
- Part 3: the unit, the price basis, the currency, and who counts the audience for the four spots.
- Does the offer set one price for all three parts? If so, ask for the price of each part.
- The currency and terms of the whole offer.
- The source and method of any attention or reach claim.

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Logo on the jersey for a season", "format": "sponsorship",
     "line": "Sponsorship, by parts", "compare_with": "Each part separately",
     "cite": ["M-09", "S-6.1"]},
    {"item": "Creator series with the players", "format": "creator",
     "line": "Creator", "compare_with": "The creator line's units",
     "cite": ["M-07", "SR-performs-message"]},
    {"item": "Four broadcast spots in the league's weekly show", "format": "broadcast spot",
     "line": "CTV or TV", "compare_with": "That line's currency",
     "cite": ["M-13"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "Whether the team and league are esports. The offer does not say. Rows M-09 and M-13 are written for esports, so the placement of parts 1 and 3 depends on this.",
    "Part 1: the parts of the sponsorship rights, and the terms of each. State whether the jersey logo is worn in play or only on a team item.",
    "Part 2: whether the players perform the brand's message. If the brand's graphic is shown without the player performing it, the item is display.",
    "Part 2: the unit, the price basis, and the number of episodes.",
    "Part 3: the unit, the price basis, the currency, and who counts the audience, for the four spots.",
    "Whether the offer sets one price for all three parts. If so, ask for the price of each part (each payment goes to its own line).",
    "The currency and terms of the whole offer. The offer does not state them.",
    "Any attention or reach claim the seller makes. The claim is the seller's, and it is compared inside the line of the part it describes."
  ],
  "instructions_in_input": [],
  "notes": "The offer states no label such as gaming. The placement uses the mapping rows for sponsorship, creator, and broadcast spots. All facts in the offer are the seller's claims. The version of the map applied is 0.4.0."
}
```
