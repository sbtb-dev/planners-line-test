# Changelog

This repository uses semantic versions.

- A change to the rule or a reading note is a minor or a major change.
- A new mapping row is a patch.
- Every change gets a version and a stated reason.

## 0.4.0 — 2026-11-22

Reason: to package the line test as an Agent Skill that runs on hosted platforms with no backend, and to let an answer cite a stable ID. The rule, the reading notes, the checks, the scope section, the forms, and every mapping result do not change. The way answers cite changes, and contributors now edit a data file. So this is a minor change. Each change and its reason:

- **IDs (new).** Every mapping row (M-01 to M-27), reading note (N-1 to N-9), check (C-3.1 to C-3.3), comparison requirement (R-1 to R-4), scope item (S-6.1 to S-6.6), second rule (SR-...), and proposed-line form step (F-1 to F-5) has an ID. A free-text citation can be read two ways. An ID cannot. IDs are never reused and never renumbered. The mapping README (section 7) and CONTRIBUTING say so.
- **`data/mapping.yaml` (new).** It is the source of the mapping table and lists every ID. `mapping/MAPPING.md` renders the table from it, with a new first column, "ID." The rows are the same as in 0.3.0. The build checks that the IDs in the data file match the IDs in the source text.
- **Skill (new): `skill/planners-line-test/`.** It holds `SKILL.md`, generated copies of the source files, the data file, a manifest with a SHA-256 hash of each file, and `scripts/check.py`. The script checks the format of an answer and finds no error of fact. A zip of the folder is attached to each release, so an answer can be compared with a public run of the same version.
- **Build.** `scripts/build.sh` builds the table, the prompt, the skill folder, the manifest, and the zip, and runs the tests of the check script. `scripts/build-prompt.sh` stays and runs the same build, so older instructions still work. `scripts/test_check.py` is new.
- **Citation instructions.** The prompt instructions, the offer form, and the proposed-line form now say to cite by ID. The filled example in the offer form cites IDs. The text of every result is unchanged.
- **Fixtures.** The fixtures and their expected results do not change. A citation now matches by name or by ID (tests/README.md).
- **Glossary.** New terms: skill and ID.
- **Mapping README.** The sections are not renumbered. The new section on IDs is section 7.

## 0.3.0 — 2026-11-21

Reason: to close a gap that the seeded pressure test of 2026-11-21 found. A seller can sell a standard display unit and count the price on a time measure, such as a player-minute. The step 1 exception named only "an attention measure." The exception was in the proposed-line form only. Two fresh judges gave two different results for the same facts: one placed the unit in display, and one placed it as a brand's presence inside play. This is a change to the reading notes, so it is a minor change. Each change and its reason:

- **Reading note 9 (new).** A price counted on a measure other than the format's own price basis claims a new price basis, whatever the measure is. The unit is then not placed by the first sentence. The second sentence applies. A score that only adds to a unit stays a property of the delivery (note 2). Note 7 already said that the same unit needs the same price basis. Note 6 did not say whether a plain statement of a different price basis meets the burden. Note 9 says it does not.
- **Proposed-line form, step 1.** The exception now says "a measure ... such as attention or time" and cites note 9. It also says to name the format and say that the price basis differs.
- **Offer form.** A new rule says the same for an offer. It also says not to move a standard creative in a slot to "a brand's presence inside play" because of its price basis.
- **Mapping, section "Three places for a brand's presence inside play."** One paragraph says that a standard creative in a slot is not a brand's presence, even if the seller leaves out the format or prices it on another measure.
- **Worked cases.** New hypothetical case: a display unit priced on time.
- **Fixtures.** Two new fixtures (25 and 26) cover a proposed line and an offer. No existing expected result changes.
- **Fixture inputs 11 and 12.** The input of fixture 11 did not say that it is a proposed line, so a judge could take it for an offer. It now begins "We propose a line built on". The input of fixture 12 said that an event is "defined in the proposal" but did not define it, so a judge could not pass it. It now defines one event that differs from the published viewable impression: a branded object is rendered on a player's screen at ten metres or less, with no minimum pixel share and no minimum time. Both gave the same result on 0.2.2 and 0.3.0 before the change, so 0.3.0 did not cause either problem. The expected results do not change.

This change follows "reading B": a different price basis means a different unit. The repo owner confirmed this choice on 2026-11-21. The other choice, "reading A", keeps display as the default and puts the price basis under "what to confirm." The cross-model check of the two S1 proposals has not run. If other models split, review this change.

## 0.2.2 — 2026-11-21

Reason: to fix two fixtures (08 and 09) that failed on the prompt in 0.1.3 and in 0.2.1. A proposal for a line named for a venue or an audience, such as "a gaming line" or "a mobile-gaming line", names no unit. The form stopped at step 2 and returned Not a boundary. The form now says that such a line holds units that already have lines, and each unit is Placed in its own line. A brand's presence inside play is the exception, and it goes to step 2. No change to the rule, a note, a mapping row, or a fixture's expected result.

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
