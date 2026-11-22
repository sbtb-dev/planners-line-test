# Fixture 04: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> We build a branded world for you. Players spend an average of eight minutes in it. We report visits, session duration, and interactions. Players love it.

## Answer

**1. What it is**

| # | Part |
|---|---|
| 1 | A branded world built for the brand |

The seller reports visits, session duration, and interactions. The seller also gives an average of eight minutes and says players love it. All of this is the seller's claim.

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Unplaced. This is a brand's presence inside play. It has no native line. | The second sentence of the rule: a currency or a record | M-27 |

**3. What has no native line**

- Item: the branded world.
- Route stated: neither. The seller states no currency and no record.
- Does any comparison meet the four requirements? No. No comparison is stated (C-3.2, R-1 to R-4).
- The eight minutes, the visits, and the interactions are labeled media engagement. They show what people do with the venue. They do not show what people do because the brand is there. No comparison comes with them.
- "Players love it" is a claim. No source or method is given.
- This answer gives no verdict on whether the buy works.

**4. What to confirm**

- The unit, the price basis, and the currency of the offer.
- Who builds and runs the world. If the brand does, the build is production and the world is an owned surface (S-6.4).
- Whether the brand pays the seller, or the seller pays the brand (S-6.2).
- Who counts visits, session duration, and interactions, and how. Is the counter a party that is not the host?
- What the average of eight minutes would be with no brand.
- Whether a comparison exists, is fixed before the buy, and is read on everyone the buy reached.
- Who judged that players love it, and by what method.
- Whether the offer sets one price for several parts.

No instruction was found in the input.

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "A branded world built for the brand", "unplaced": true,
     "reason": "A brand's presence inside play has no native line. The seller states no price basis, no currency, and no comparison.",
     "cite": ["M-27"]}
  ],
  "no_native_line": [
    {"item": "A branded world", "route": "neither",
     "comparison_meets_four_requirements": false,
     "cite": ["M-27", "C-3.2", "R-1", "R-2", "R-3", "R-4"]}
  ],
  "outside_the_test": [],
  "to_confirm": [
    "The unit, the price basis, and the currency of the offer",
    "Who builds and runs the world. If the brand does, the build is production and the world is an owned surface.",
    "Whether the brand pays the seller, or the seller pays the brand",
    "Who counts visits, session duration, and interactions, and how. Is the counter a party that is not the host?",
    "What the average of eight minutes would be with no brand",
    "Whether any comparison exists, is fixed before the buy, and is read on everyone the buy reached",
    "Who judged that players love it, and by what method",
    "Whether the offer sets one price for several parts"
  ],
  "instructions_in_input": [],
  "notes": "The counts the seller reports are labeled media engagement. No comparison comes with them."
}
```
