# The mapping: how to read it

The mapping applies the [rule](../line-test/RULE.md) to items sold as gaming. The table is in [MAPPING.md](MAPPING.md).

## 1. Scope

The mapping covers items sold as gaming. The label "gaming" is what carries the high-attention claim onto a unit. The label can change ("play," "fandom," "culture"), so scope is defined without one word:

> An offer is in scope when it is sold on a venue label or an audience label in place of a unit.

The mapping covers two labels at this version: "gaming," and "immersive" as a format adjective (for example, "immersive ads").

## 2. Support labels

Every row states its support.

| Label | Meaning |
|---|---|
| **IAB** | The IAB *Gaming Measurement Framework* (June 2025) puts this format under this media type. |
| **Test, direct** | The first sentence of the rule places the item with no other input. Sellers outside gaming sell the same unit on the same currency and terms. |
| **Test, after a second rule** | Another rule must first say which unit the item is. The test then places that unit. |
| **Test for the line, practice for the method** | The test gives the line. "By parts" is a comparison method from ordinary practice. |
| **Extension** | The item is a service, not a media unit. The rule's logic applies, but its words do not cover it. |
| **Differs** | A flag: the IAB framework places the format elsewhere. The test's result stands. |

## 3. Second rules

- **Performs-the-message.** In a live stream, if the creator performs the brand's message, the item is creator. If the brand's graphic is inserted without the creator's performance, it is display.
- **Terms of the buy.** A playable bought per install is performance. A playable bought on impressions or completed plays is display or video.
- **Targeting is not a unit.** An audience segment changes neither the format nor the unit (reading note 2).

## 4. Each "Test, direct" row rests on a fact

Each "Test, direct" row rests on a fact about how a seller sells the item. The mapping supplies the question. The planner confirms the fact with the seller.

## 5. The asterisk

The IAB rows match the IAB's position as published in June 2025. The mapping does not depend on that position. Each row is a result of the test. The general MRC guidelines for display, video, and viewable impressions define the units. If the IAB changes or withdraws its framework, no row changes.

## 6. Sources used by the mapping

- IAB, *Gaming Measurement Framework*, June 2025. It has display, video, audio, and custom matrices. Read on 19 November 2026. <https://www.iab.com/guidelines/gaming-measurement-framework/>
- IAB, IAB Tech Lab, and MRC, *Intrinsic In-Game Advertising Measurement Guidelines 2.0*. The repo owner read the public-comment version, released 14 June 2022, from a PDF copy. No final version was read.
- MRC, standards and guidelines. <https://www.mediaratingcouncil.org/standards-and-guidelines>
