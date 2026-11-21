# Changelog

This repository uses semantic versions.

- A change to the rule or a reading note is a minor or a major change.
- A new mapping row is a patch.
- Every change gets a version and a stated reason.

## 0.2.1 — 2026-11-20

Reason: to record the repo owner's decision on reading note 8 for the final intrinsic in-game guidelines. The conditions that the final version adds (screen coverage, angle, occlusion) adapt the display price basis to the venue. They do not define a different event. The mapping text and the intrinsic worked case now say so. No change to the rule, a note, a row, a form, or a fixture's expected result.

## 0.2.0 — 2026-11-20

Reason: to fix cases that the test, as written in 0.1.3, gets wrong or does not cover. The test now reads two things: the format and the price basis. Every other part of a deal is a term, compared within the line. This is a minor change, because it changes how the rule is read. The rule's two sentences do not change. Each change and its reason:

- **Reading note 2.** A unit is now a format plus its price basis. Before, it included terms and currency. That was too strict, and it let a term alone look like a new unit. Deal terms are now compared within the line.
- **Reading note 6.** The burden is now to show a change in the price basis. It follows from note 2.
- **Reading notes 7 and 8 (new).** Note 7 says when two units are the same unit, so a seller cannot claim a new unit from a difference in size, placement, or context. Note 8 says that a measurement standard written for one venue does not create a new price basis unless it defines a different event.
- **Requirement 1 of the comparison check.** A reward given only where the brand appears is a second change. Before, requirement 1 covered this only by implication.
- **Section 5 of the rule.** It now says that the test does not re-examine existing lines that are organized by route or by data, and does not accept a new line on that basis. It also says that law can stop a route in practice.
- **Section 6 of the rule, Scope (new).** The test did not say how to treat money paid to the brand, payment in kind, owned surfaces, collaborations with no media buy, or a commitment made before units are named. It also did not say that each payment is placed by what it buys.
- **Mapping: retail row.** The row is split in two. A retailer's offsite media is display or video bought with the retailer's data. The data is targeting, so the item does not belong in retail media.
- **Mapping: licensing row.** The row is replaced by four rows. One row held several deal structures with different payments. Each now goes to its own line.
- **Mapping: new row for promoted listings in a platform's catalog.** The row had no place before.
- **Mapping: presence row.** Its description now includes a brand's products or marks placed in game content.
- **Mapping: playable ad row and its second rule.** "Terms of the buy" is now "price basis of the buy." Under note 2, the price basis decides this item, and terms do not.
- **Mapping README.** The "Test, direct" label now says the same format on the same price basis. Two second rules are new: payments, not deal names, and payment in kind. The targeting second rule now also covers the offsite retail row.
- **Glossary.** New definition of unit. New entry for price basis. New definition of terms. Currency is unchanged.
- **Other files.** CONTRIBUTING, the mapping-row issue template, the prompt instructions, and the offer form used the old definition of a unit. They now match note 2. The instructions and the offer form also allow a scope item as a citation.
- **Worked cases.** New cases: the performance line, a gaming attention line, a cross-media line priced on attention, and intrinsic in-game display. The CTV case now gives the price basis as the reason the unit changed.
- **Wording of the record route (note 3 and the glossary).** "Terms written in the order" is now "Conditions written in the order". The glossary says terms do not change the unit, and the record states the unit. One word had two meanings. No result changes.
- **Proposed-line form, step 1.** A proposal that counts its price on an attention measure in place of the format's own price basis claims a new price basis (notes 2 and 6). It goes to step 2. Without this, the form placed a cross-media attention line by format, and fixture 21 failed.
- **Mapping README and mapping text: source lines.** A final version of the intrinsic in-game guidelines (August 2022) is public. It adds conditions to the viewable impression. The two files now say so. The two sentences that said no final version was read now say that this was true when they were first written. The mapping's result is unchanged, and the note 8 question is marked open.
- **Fixtures.** Eleven new fixtures (14 to 24) cover the new notes, the scope section, and the new rows. Fixture 06 now names the renamed second rule. Its expected result is unchanged.

## 0.1.3 — 2026-11-20

Reason: to say in the header of `prompt/PROMPT.md` where the offer or the proposed line goes. The header now says to paste it after the prompt, marked with a label. No change to the rule, a note, a row, or a form.

## 0.1.2 — 2026-11-19

Reason: to make `prompt/PROMPT.md` usable on its own. The mapping text no longer points to files that the prompt does not include. The instructions now say that the register is not included. The build script no longer writes repository paths into the prompt. No change to the rule, a note, or a row's result.

## 0.1.1 — 2026-11-19

Reason: to state in the README that this repository, at a tagged version, is the only authoritative text, and to say how to cite a version. No change to the rule, a note, a row, or a form.

## 0.1.0 — 2026-11-19

First version. Reason: to publish the rule, the reading notes, the mapping for items sold as gaming, the two forms, the paste-ready prompt, the test fixtures, and the boundary register.
