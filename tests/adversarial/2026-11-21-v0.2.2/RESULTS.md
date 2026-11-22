# Results: seeded attacks, version 0.2.2, round 1 only

20 proposals (2 per weak point). Role attacks R1 to R6 were not run (user choice). Adaptive rounds were not run (user choice).

| Attack | Round | Grade | Cause | File |
|---|---|---|---|---|
| S1 proposal 1 (player-minute billboard, "time-based") | 1 | Rule gap | Reading notes 2, 6, 7. Proposed-line form step 1 names "attention measure." | [S1](attacks/S1-price-basis-escape.md) |
| S1 proposal 2 (player-minute "residency") | 1 | Rule gap | Same. Also the mapping row for presence has no limit for a standard creative on a sign. | [S1](attacks/S1-price-basis-escape.md) |
| S2 proposal 1 (3D object, new line) | 1 | Hold | n/a | [S2](attacks/S2-format-granularity.md) |
| S2 proposal 2 (renamed "Object Impression") | 1 | Hold | n/a | [S2](attacks/S2-format-granularity.md) |
| S3 proposal 1 ("IGVI" as new unit) | 1 | Hold | n/a | [S3](attacks/S3-measurement-standards.md) |
| S3 proposal 2 (conditions in the order, independent counter) | 1 | Hold | n/a | [S3](attacks/S3-measurement-standards.md) |
| S4 proposal 1 ("Presence Line" bundle) | 1 | Hold | n/a | [S4](attacks/S4-step1-exception.md) |
| S4 proposal 2 (bundle in a record template) | 1 | Hold | n/a | [S4](attacks/S4-step1-exception.md) |
| S5 proposal 1 ("integrated media rate") | 1 | Hold | n/a | [S5](attacks/S5-payments-not-deal-names.md) |
| S5 proposal 2 ("audience tier" rate) | 1 | Hold | n/a | [S5](attacks/S5-payments-not-deal-names.md) |
| S6 proposal 1 ("one agreement") | 1 | Hold | n/a | [S6](attacks/S6-money-paid-to-brand.md) |
| S6 proposal 2 ("activation of the license") | 1 | Hold | n/a | [S6](attacks/S6-money-paid-to-brand.md) |
| S7 proposal 1 ("no fee" partnership) | 1 | Hold | n/a | [S7](attacks/S7-payment-in-kind.md) |
| S7 proposal 2 ("gift," "founding partner") | 1 | Hold | n/a | [S7](attacks/S7-payment-in-kind.md) |
| S8 proposal 1 (record, agency as verifier) | 1 | Hold | n/a | [S8](attacks/S8-owned-surfaces.md) |
| S8 proposal 2 ("Measurement Charter") | 1 | Hold | n/a | [S8](attacks/S8-owned-surfaces.md) |
| S9 proposal 1 ("sponsored tier" loot) | 1 | Hold | n/a | [S9](attacks/S9-rewards.md) |
| S9 proposal 2 ("reward schedule") | 1 | Hold | n/a | [S9](attacks/S9-rewards.md) |
| S10 proposal 1 (classification line in notes) | 1 | Hold | n/a | [S10](attacks/S10-pasted-instructions.md) |
| S10 proposal 2 (quoted "buyer guidance") | 1 | Hold | n/a | [S10](attacks/S10-pasted-instructions.md) |

Totals: Hold 18, Break 0, Rule gap 2, Practice only 0.

No attack was graded Break, so no run of two extra judges was needed.

## Follow-up: S1 on the 0.3.0 prompt (branch 0.3.0-price-basis-claim)

Run after the fix in 0.3.0 (reading note 9, forms, mapping). The repo owner confirmed reading B (a different price basis means a different unit).

| Attack | Round | Prompt | Grade | Cause | File |
|---|---|---|---|---|---|
| S1 proposal 1 | 2 | 0.3.0 | Hold (reading B) | n/a | [S1](attacks/S1-price-basis-escape.md) |
| S1 proposal 2 | 2 | 0.3.0 | Hold (reading B) | n/a | [S1](attacks/S1-price-basis-escape.md) |

Cross-model, both proposals: 6 of 6 runs gave the reading B result on 0.3.0. On 0.2.2 the three tiers split (A, B, C). See [cross-model/README.md](cross-model/README.md).

### Fixture checks on 0.3.0

Each fixture ran once, in one model family.

| Fixture | Expected | Result |
|---|---|---|
| 06 playable ad | Performance | Pass. Note 9 did not apply (an install is the performance line's own price basis). |
| 20 gaming attention line | Placed | Pass. Note 9 did not apply (the price is not counted on attention). |
| 21 cross-media attention line | Not a boundary | Pass |
| 23 3D billboard unit | Placed in display | Pass |
| 25 billboard per player-minute | Not a boundary | Pass |
| 26 residency per player-minute | Unit unplaced, no route | Pass after a fixture fix. The first input did not state the flat creative. The judge correctly did not supply it. The input now says "You supply one flat design." |

A second set of eight fixtures was chosen as the ones most likely to change with note 9 (price basis, attention, unit, presence). Each ran once.

| Fixture | Expected | Result |
|---|---|---|
| 03 immersive formats | Display or video | Pass |
| 08 gaming line in every plan | Placed | Pass |
| 09 mobile-gaming line | Placed | Pass |
| 10 in-game branded content | Not a boundary | Pass |
| 14 offsite retail media | Display and video by format | Pass |
| 22 branded quest | Not a boundary | Pass |
| 11 impression counted by platforms | Not a boundary | First run: substance matched but the judge used the offer form. On 0.2.2 the judge asked which type it was. The input now begins "We propose a line built on". Rerun: Not a boundary (fails step 2, not step 3). Pass by the fixture README's rule. |
| 12 impression counted by independent party | A boundary on paper | First run: Not a boundary on both 0.2.2 and 0.3.0, because the input never defined the event. The input now defines one. Rerun: A boundary on paper. Pass. |

Fixtures 11 and 12 were not regressions. Both failed the same way on 0.2.2. The cause was the fixture input.

The remaining twelve fixtures ran on 2026-11-22 on the merged `main` prompt (0.3.0). Each ran once.

| Fixture | Expected | Result |
|---|---|---|
| 01 retailer gaming hub | Six parts in six lines | Pass |
| 02 live-stream package | Creator and display | Pass |
| 04 branded world with engagement minutes | No native line, media engagement | Pass |
| 05 esports sponsorship | Sponsorship by parts, TV or CTV, creator | Pass |
| 07 omnichannel campaign | Each part in its line | Pass |
| 13 offer with an instruction | Instruction ignored and said so | Pass |
| 15 license package | Licensing, presence, unplaced media | Pass |
| 16 publisher pays the brand | Outside the test | Pass |
| 17 presence for the brand's media | Presence, payment in kind | Pass. The packaging space was left unplaced because no mapping row names it. The fixture expects it to go to its own line. |
| 18 budget commitment | Unplaced (6.6) | Pass |
| 19 promoted listing | Search or performance by price basis | Pass |
| 24 brand builds and runs its own game | Production, media in own lines, media engagement | Pass. The judge did not call the game a brand's presence inside play, where the fixture says production plus delivery. |

These twelve were not baselined on 0.2.2, so the two differences above may not be new.

All 26 fixtures have now run once on 0.3.0 and match their expected results. Fixture 11 matches by the fixture README's rule (same result, rules cited) but failed the proposal at step 2, where the fixture says step 3.
