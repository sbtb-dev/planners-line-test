# Source: Overwolf offer, read 23 November 2026

This file records the full offer behind `input.md`, and the 0.5.2 answer. Every fact is the seller's claim. Short quotes are the seller's words.

The facts come from the change prompt for version 0.6.0. The repository owner read the pages on 23 November 2026. The author of this file did not open them.

The CMO's LinkedIn post about the new ad identity (November 2026) is context only. It is not part of the offer, so this file leaves it out.

## Sources

- Overwolf Ads home page: <https://www.overwolf.com/ads>
- Case study index: <https://www.overwolf.com/ads/case-studies/>
- Wendy's case: <https://www.overwolf.com/ads/case-studies/wendys/>
- Pringles case: <https://www.overwolf.com/ads/case-studies/pringles/>
- Epic Games case: <https://www.overwolf.com/ads/case-studies/epic-games/>

## What the seller sells (ads home page)

| Product | Seller's description |
|---|---|
| Standard Media | IAB display and video in "premium, high-attention placements" |
| Custom Media | Takeovers, skins, and similar assets that make the brand "part of the screen" |
| Custom Activations | Challenges, tournaments, and achievement rewards built around the brand |

Other claims on the home page:

- **Placement:** "matched to the game, the context and the player." The page does not say how in-game moments are detected.
- **Signals:** session length, time of day, hardware, and which games and genres a person plays.
- **Scale:** 113M consumers, 5,000+ games under one contract, and about 15 named titles, including Fortnite, Call of Duty, Apex Legends, and Roblox.
- **Measurement:** "measured on business impact"; installs and players won back, "traced to the campaign."
- **Buying:** the only path stated is "Talk to our team." The page names no programmatic route, PMP, CPM, price basis, or measurement partner.
- **Tagline:** "Your Audience. In-Game. Every Game." The word "playtime" does not appear on the page.

## Case: Wendy's x Takis Fuego

- Games: Fortnite, Marvel Rivals, and R.E.P.O. The seller calls it Marvel Rivals' first rewarded challenge.
- Mechanic: players opted in to a Wendy's in-game challenge and stayed in play to unlock rewards. Overwolf amplified it with "high-visibility ad units," formats not named.
- Rewards: not described. The page does not say who granted them.
- Reported results: 46M+ impressions; 48K hours of challenge gameplay; CTR 23x an undefined benchmark; 21% purchase intent; 11% brand consideration. No baseline, no provider, and no control is given.
- Creators joined the challenge and shared their play.

## Case: Pringles

- Games: Fortnite and Apex Legends, in the UK, France, Germany, and Poland.
- Mechanic: "Moment-Triggered Ads" and "Rewarded-Moments Triggered Ads." The example is a custom Pringles message on screen each time a player scores a kill. The creative was video, written for each game.
- Rewards: "in-game rewards" for achievements. The page does not say what they were or who granted them.
- Reported results: 96% video viewability against a 68.7% benchmark; 89% completion rate against a 66.2% benchmark; "thousands of hours" of engagement; brand lift from an ad-effectiveness survey, with no numbers and no named provider. No control is given.
- Price basis: not stated.

## Case: Epic Games (Fortnite Chapter 7 Season 3)

- Goal: acquire new Fortnite players in the UK, Germany, the US, Poland, Brazil, and Spain, aimed at people who do not play Fortnite.
- Formats: video and display (skyscrapers), placed in Overwolf companion and tracker apps (for example, Marvel Rivals Tracker, Apex Legends Tracker, CurseForge, and Insights Capture) and next to gameplay.
- Targeting: Overwolf's "proprietary targeting solutions." The criteria are not described.
- Attribution: Overwolf served the impression, matched the player in its own platform, detected the Fortnite install, and linked the install to the impression. No other party counted.
- Reported results: 160,864 new installs, "100%" attributed to an impression; 92% viewability; +3% action intent lift, with no baseline or method. No holdout is described.
- Price basis: not stated.

## The 0.5.2 answer, for comparison

The run placed the offer as follows. The check passed.

| Item | Line | Cite | What the run got wrong or did not flag |
|---|---|---|---|
| Standard display in apps | Display | M-02, N-7 | — |
| Standard video | Video | M-03 | — |
| Rewarded video | Video | M-03, N-2 | Called the reward a term. N-2 does not list rewards. Not flagged. |
| Moment-triggered messages | Display or video | M-01, M-03, N-2 | M-01 cited. M-02 fits an overlay better. |
| Takeovers and skins | Display | M-02, N-7 | Whether "skins" are in-game items (M-27) left to "to confirm." Correct. |
| Targeting signals | Targeting on the carrying line | M-24, SR-targeting | — |
| Tournaments | Experiential, by parts | M-17 | — |
| Reward codes or items | Promotions | M-16 | — |
| Epic acquisition buy | Display or video, unless priced per install and counted by a non-host | M-02, M-03, M-18, N-5, N-9 | Took Overwolf as the host. The glossary does not decide this. Not flagged. |
| Brand studies | Measurement | M-26 | — |
| Wendy's challenge | `no_native_line`, route "neither" | M-27, R-1, R-3 | No row names a challenge set from an overlay. Placed by judgment. Not flagged. |

## Three gaps that this case found

1. **Host.** The glossary said the host is "the party that runs the venue." Overwolf serves ads in its own overlay, on top of games that other companies run. Under one reading, Overwolf is not the host, so its own count of Fortnite installs is "a party that is not the host" (N-5). Version 0.6.0 defines more than one host (N-10).
2. **A brand's objectives inside play.** The Wendy's challenge fits none of the cases that M-27 names. Version 0.6.0 adds M-28.
3. **Rewards.** The skill did not say whether a reward is a term or changes the unit. Version 0.6.0 adds N-11.
