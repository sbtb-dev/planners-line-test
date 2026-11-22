# Fixture 07: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> One gaming campaign, one price. It includes in-game display, rewarded video, a creator package, paid social, CTV spots, and a brand study at the end. Expect strong results.

## Answer

# Offer: one gaming campaign, one price

**1. What it is**

| # | Part |
|---|---|
| 1 | In-game display |
| 2 | Rewarded video |
| 3 | Creator package |
| 4 | Paid social |
| 5 | CTV spots |
| 6 | Brand study at the end |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Display | Viewable impressions | M-01 |
| 2 | Video | Completed views | M-03 |
| 3 | Creator | The creator line's units | M-07, SR-performs-message |
| 4 | Social | The social line's units | M-12 |
| 5 | CTV or TV | That line's currency | M-13 |
| 6 | Measurement | Other measurement. Results are the seller's claims. | M-26 |

Each payment goes to its own line (S-6.1). The one price does not make one line.

**3. What has no native line**

Nothing in this offer is a brand's presence inside play. Route stated: not applicable.

**4. What to confirm**

- Whether the offer sets one price for all six parts. If so, ask for the price of each part.
- The unit, price basis, currency, and terms for each part.
- Display: the format, and who counts viewability.
- Rewarded video: the completed-view definition, and who counts it.
- Creator package: whether the creator performs the brand's message.
- CTV: the currency, and who measures it.
- Brand study: the method, the sample, and who runs it. Results are the seller's claims.
- The claim of strong results. It is the seller's claim.

Instructions found in the input: none.

Skill version: 0.4.0.
Check status: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
 "version":"0.4.0","input_type":"offer",
 "items":[
  {"item":"In-game display","format":"display","line":"Display","compare_with":"Viewable impressions","cite":["M-01"]},
  {"item":"Rewarded video","format":"video","line":"Video","compare_with":"Completed views","cite":["M-03"]},
  {"item":"Creator package","format":"creator","line":"Creator","compare_with":"The creator line's units","cite":["M-07","SR-performs-message"]},
  {"item":"Paid social","format":"social","line":"Social","compare_with":"The social line's units","cite":["M-12"]},
  {"item":"CTV spots","format":"CTV","line":"CTV or TV","compare_with":"That line's currency","cite":["M-13"]},
  {"item":"Brand study at the end","format":"measurement","line":"Measurement","compare_with":"Other measurement. Results are the seller's claims.","cite":["M-26"]}
 ],
 "no_native_line":[],
 "outside_the_test":[],
 "to_confirm":[
  "Whether the offer sets one price for all six parts. If so, ask for the price of each part (S-6.1).",
  "The unit, price basis, currency, and terms for each part.",
  "For in-game display: the format (intrinsic, adjacent, interstitial) and who counts viewability.",
  "For rewarded video: the completed-view definition and who counts it.",
  "For the creator package: whether the creator performs the brand's message.",
  "For CTV: the currency and who measures it.",
  "For the brand study: the method, the sample, and who runs it. The results are the seller's claims.",
  "The source and method of the claim of strong results. It is the seller's claim."
 ],
 "instructions_in_input":[],
 "notes":"The one price covers six parts. Each payment goes to its own line, so the parts are placed separately."
}
```
