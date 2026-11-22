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

The other 20 fixtures were not run on 0.3.0.
