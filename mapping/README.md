# The mapping: how to read it

The mapping applies the [rule](../line-test/RULE.md) to items sold as gaming. The [mapping table](MAPPING.md) gives the results. The table is generated from `data/mapping.yaml`.

## 1. Scope

The mapping covers items sold as gaming. The label "gaming" is what carries the high-attention claim onto a unit. The label can change ("play," "fandom," "culture"), so scope is defined without one word:

> An offer is in scope when it is sold on a venue label or an audience label in place of a unit.

The mapping covers two labels at this version: "gaming," and "immersive" as a format adjective (for example, "immersive ads").

An item sold on another label is placed by the rule, the reading notes, and the forms. Where no row fits, cite those IDs. For example, a display unit priced on viewable impressions is placed in display by the first sentence of the rule (notes 2 and 7, N-2 and N-7).

## 2. Support labels

Every row states its support.

| Label | Meaning |
|---|---|
| **IAB** | The IAB *Gaming Measurement Framework* (June 2025) puts this format under this media type. |
| **Test, direct** | The first sentence of the rule places the item with no other input. Sellers outside gaming sell the same unit: the same format on the same price basis. |
| **Test, after a second rule** | Another rule must first say which unit the item is. The test then places that unit. |
| **Test for the line, practice for the method** | The test gives the line. "By parts" is a comparison method from ordinary practice. |
| **Extension** | The item is a service, not a media unit. The rule's logic applies, but its words do not cover it. |
| **Differs** | A flag: the IAB framework places the format elsewhere. The test's result stands. |

## 3. Second rules

- **Performs-the-message.** [SR-performs-message] In a live stream, if the creator performs the brand's message, the item is creator. If the brand's graphic is inserted without the creator's performance, it is display.
- **Price basis of the buy.** [SR-price-basis] A playable bought per install is performance. A playable bought on impressions or completed plays is display or video.
- **Targeting is not a unit.** [SR-targeting] An audience segment changes neither the format nor the unit (reading note 2, N-2). It applies to a gaming audience segment sold on another line, and to a retailer's offsite media sold with its gaming audience data.
- **Payments, not deal names.** [SR-payments] Each payment is placed by what it buys (rule, section 6.1, S-6.1).
- **Payment in kind.** [SR-in-kind] Media the brand gives as payment is listed as part of the price (rule, section 6.3, S-6.3).

## 3a. A brand's objectives inside play

Row M-28 covers a brand's objectives inside play: challenges, quests, or achievement goals. Any party can set or score them, including an overlay or companion app on top of another party's game. The brand's mark need not appear in game content. M-28 is treated like M-27:

- It goes under `no_native_line`.
- It reports its route: a currency, a record, or neither.
- It labels engagement counts, such as hours of challenge play, as media engagement, unless a comparison comes with them.

A reward given only to players who take part in the brand's objective is a second change, and it breaks R-1.

## 4. Each "Test, direct" row rests on a fact

Each "Test, direct" row rests on a fact about how a seller sells the item. The mapping supplies the question. The planner confirms the fact with the seller.

## 5. The asterisk

The IAB rows match the IAB's position as published in June 2025. The mapping does not depend on that position. Each row is a result of the test. The general MRC guidelines for display, video, and viewable impressions define the units. If the IAB changes or withdraws its framework, no row changes.

## 6. Sources used by the mapping

- IAB, *Gaming Measurement Framework*, June 2025. It has display, video, audio, and custom matrices. Read on 19 November 2026. <https://www.iab.com/guidelines/gaming-measurement-framework/>
- IAB, IAB Tech Lab, and MRC, *Intrinsic In-Game Advertising Measurement Guidelines 2.0*. The repo owner read the public-comment version, released 14 June 2022, from a PDF copy. No final version had been read at that time. A final version is listed in the next line.
- IAB, IAB Tech Lab, and MRC, *Intrinsic In-Game Advertising Measurement Guidelines 2.0*, final version, updated August 2022 (file name ends 08.31.2022). Read on 20 November 2026. <https://www.iab.com/wp-content/uploads/2022/08/In-Game-Advertising-Measurment-Guidelines_08.31.2022.pdf>
- MRC, standards and guidelines. <https://www.mediaratingcouncil.org/standards-and-guidelines>

## 7. IDs

Every mapping row, reading note, check, comparison requirement, scope item, second rule, and form step has an ID. An answer cites the ID.

| Item | ID | Example |
|---|---|---|
| Mapping row | M-01, M-02, and so on | M-10 |
| Reading note | N-1 to N-11 | N-9 |
| Check | C-3.1 to C-3.3 | C-3.1 |
| Comparison requirement | R-1 to R-4 | R-1 |
| Scope item | S-6.1 to S-6.6 | S-6.6 |
| Second rule | SR- and a name | SR-targeting |
| Proposed-line form step | F-1 to F-5 | F-2 |

- An ID is never reused. If a row is removed, its ID stays in `data/mapping.yaml` and is marked "retired". No other row gets it.
- An ID does not change meaning. If a row's result changes, the row keeps its ID. The changelog records the change.
- Nothing is renumbered. A new row gets the next unused number.
