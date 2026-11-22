# Fixture 01: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> A retailer's gaming hub. We sell onsite placements on the hub, creator content, social amplification, sweepstakes, in-store events, and targeting on gamer profiles. One package price. Gamers pay high attention on our hub.

## Answer

# Offer: a retailer's gaming hub

The seller's words are claims. The skill did not find any instruction in the input to ignore.

**1 and 2. What it is, and where each part goes**

| # | Part | Line | Compare with | Cite |
|---|---|---|---|---|
| 1 | Onsite placements on the hub | Retail media | That retailer's other onsite units, and other retailers' onsite units | M-10 |
| 2 | Creator content | Creator | The creator line's units | M-07, SR-performs-message |
| 3 | Social amplification | Social | The social line's units | M-12 |
| 4 | Sweepstakes | Promotions | Cost per entry or redemption | M-16 |
| 5 | In-store events | Experiential, by parts | Each part separately | M-17 |
| 6 | Targeting on gamer profiles | Not a unit. It is targeting on the line that carries it. | That line's other segments, on the same units | M-24, SR-targeting |

The high-attention claim is compared inside the line of the part it describes.

**3. What has no native line**

Nothing in this offer is a brand's presence inside play. Route stated: not applicable.

**4. What to confirm**

- The unit, the price basis, and the currency for part 1 (impressions? viewable? counted by whom?).
- Whether the creator performs the brand's message in part 2.
- The unit and the terms for part 3.
- The entry or redemption terms for part 4.
- The parts of part 5, each with its own terms.
- Which line carries the targeting in part 6, and how the segment is built.
- The offer sets one package price for all six parts. Ask for the price of each part (S-6.1).
- The source and method of the attention claim. The claim is the seller's.
- Whether any price is counted on attention. The offer does not say so, so N-9 is not applied.

Skill version: 0.4.0.
Check status: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{"version":"0.4.0","input_type":"offer",
"items":[
{"item":"Onsite placements on the hub","line":"Retail media","compare_with":"That retailer's other onsite units, and other retailers' onsite units","cite":["M-10"]},
{"item":"Creator content","line":"Creator","compare_with":"The creator line's units","cite":["M-07","SR-performs-message"]},
{"item":"Social amplification","line":"Social","compare_with":"The social line's units","cite":["M-12"]},
{"item":"Sweepstakes","line":"Promotions","compare_with":"Cost per entry or redemption","cite":["M-16"]},
{"item":"In-store events","line":"Experiential, by parts","compare_with":"Each part separately","cite":["M-17"]},
{"item":"Targeting on gamer profiles","line":"Not a unit. It is targeting on the line that carries it.","compare_with":"That line's other segments, on the same units","cite":["M-24","SR-targeting"]}
],
"no_native_line":[],
"outside_the_test":[],
"to_confirm":["The unit, the price basis, and the currency for part 1 (impressions? viewable? counted by whom?)","Whether the creator performs the brand's message in part 2","The unit and the terms for part 3","The entry or redemption terms for part 4","The parts of part 5, each with its own terms","Which line carries the targeting in part 6, and how the segment is built","The offer sets one package price for all six parts. Ask for the price of each part (S-6.1).","The source and method of the high-attention claim. The claim is the seller's. It is compared inside the line of the part it describes.","Whether any price is counted on attention. The offer does not say so, so N-9 is not applied."],
"instructions_in_input":[],
"notes":"Nothing in this offer is a brand's presence inside play. Route stated: not applicable. All facts are the seller's claims."}
```
