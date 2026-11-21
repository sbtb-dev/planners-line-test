# The mapping

Read [the notes on scope, support labels, and second rules](README.md) first.

| Sold as gaming | Line | Compare on | Support |
|---|---|---|---|
| In-game display: intrinsic, adjacent, interstitial | Display | Viewable impressions | IAB (display matrix) |
| Overlays and app inventory | Display | Viewable impressions | Test, direct |
| In-game video, rewarded video, in-stream | Video | Completed views | IAB (video matrix) |
| In-game audio | Audio | Completed listens | IAB (audio matrix) |
| Platform formats sold as "immersive" (image, video, portal units) | Display or video | The matching line's unit | Test, direct |
| Playable ad | Display, video, or performance, by the price basis of the buy | The matching line's unit | Test, after a second rule. Differs: IAB lists playables under Custom. |
| Creator package: mentions or integrations the creator performs | Creator | The creator line's units | Test, after a second rule |
| Automated overlay in a live stream | Display | Viewable impressions | Test, after a second rule |
| Sponsorship and rights: esports teams, leagues, tournaments | Sponsorship, by parts | Each part separately | Test for the line, practice for the method. Differs: IAB lists sponsorship as a display, video, and custom format. |
| A retailer's onsite placements and hubs | Retail media | That retailer's other onsite units, and other retailers' onsite units | Test, direct |
| A retailer's offsite media sold with its gaming audience data | Display or video, by format | That line's units. The data is targeting. | Test, after a second rule |
| Paid social inside a package | Social | The social line's units | Test, direct |
| CTV inside a gaming campaign; esports broadcast spots | CTV or TV | That line's currency | Test, direct |
| Screens at venues, conventions, launch events | Out-of-home | The out-of-home line's units | Test, direct |
| Sponsored content on gaming publishers | Branded content | That line's units | Test, direct |
| Sweepstakes, codes, sampling | Promotions | Cost per entry or redemption | Test, direct |
| Launch events, tournaments, play spaces | Experiential, by parts | Each part separately | Test for the line, practice for the method |
| Install offers, offerwalls, shoppable links | Performance | Cost per install or action | Test, direct |
| Promoted listings in a platform's own catalog of games or experiences | Search or performance, by the price basis | Promoted listings in app stores and marketplaces, on the same price basis | Test, direct |
| Game IP licensed for the brand's products or packaging | Licensing | Royalty, guarantee, term, and territory | Test for the line, practice for the method |
| Game IP licensed for use in the brand's ads | Production | Other rights and production quotes | Extension |
| The brand's marks placed inside play, under any deal name, including a license | No native line | See the row for a brand's presence inside play | Test, after a second rule |
| The brand's media given in exchange for presence | That media's line | Listed as part of the price | Test, after a second rule |
| A gaming audience segment sold on another line | That line's targeting | That line's other segments, on the same units | Test, after a second rule |
| Construction of a build | Production | Other production quotes | Extension |
| A seller-supplied brand study | Measurement | Other measurement. Results are the seller's claims. | Extension |
| **A brand's presence inside play:** branded worlds, integrations, skins, digital goods, branded games, and a brand's products or marks placed in game content | **No native line** | **The second sentence of the rule: a currency or a record** | See below |

Two items are outside the test (rule, section 6.2): a fee paid to the brand for its marks to appear in a game, and the brand's share of sales of branded digital goods. Any build the brand pays for is production. Any presence is placed by the row for a brand's presence inside play.

## The item with no native line

The IAB framework lists counts for these formats in its custom matrix: impressions, visitors, engagement, session duration, UGC equipment, and skin retention. The repo owner read the framework on 19 November 2026. The framework names these counts. It does not define one event that every seller counts the same way. So the counts do not pass the exchange check (reading note 3, and check 3.1 in the [rule](../line-test/RULE.md)).

Most of these counts are also counts of media engagement. None comes with a comparison.

The framework refers readers to MRC guidelines for measurement. It names the *Intrinsic In-Game Advertising Measurement Guidelines 2.0* as the primary guideline for gaming platforms. The repo owner read the public-comment version of those guidelines (released 14 June 2022). The repo owner had read only the public-comment version when this was first written. A final version is described below.

What that version says:

- **It defines impressions and viewable impressions.** It covers ads on in-game objects (dynamic, static, and hardcoded), in-game video, and advergames. An impression counts when the ad has loaded and begins to render. A viewable display impression needs 50% of pixels in view for one continuous second (pages 6, 8, 14).
- **It leaves out engagement.** It says it "does not include" engagement, interaction attributes, and outcomes, and it names them as possible future work (pages 7 and 23).
- **It allows a counter that is not the host.** It describes measurement "within or external to" the game, and it strongly encourages third-party audits (pages 7 and 33).

What this means for the mapping:

- An impression of a standard creative on an in-game object is a defined event. It goes to display or video (first row of the table above, and the first row of the table below).
- The custom counts (visitors, session duration, engagement, UGC equipment, skin retention) are not defined there. They are media engagement counts, and no comparison comes with them.
- A planner who finds a final text or another document that defines these counts should report it as a correction.

A final version of the guidelines is public. It is dated August 2022. It was read on 20 November 2026. The reading above covers the public-comment version only. The final version keeps the viewable display impression test (50% of pixels in view for one continuous second, section 3.2). It adds conditions for in-game ads: a minimum of 1.5% of screen coverage (section 3.2.2), an ad angle of no more than 55 degrees, which it recommends and lets measurers change if empirically supported (section 3.2.3), and a rule that an ad with less than 50% of the creative visible because of occlusion is not counted as viewable (section 3.2.4). It still says it does not include engagement and outcomes (section 1). The mapping's result does not change. Whether the added conditions define a different event is open. Reading note 8 and the exchange check (3.1) decide it.

## Three places for a brand's presence inside play

| The offer states | Where it goes |
|---|---|
| A standard creative in a slot inside the world | Display or video (the first sentence of the rule) |
| A record in the order, with a comparison that meets the four requirements | A line by the record route. See the [register](../register/BOUNDARIES.md). |
| Neither | Production plus delivery, on partnership terms. Engagement counts are reported as media engagement. |
