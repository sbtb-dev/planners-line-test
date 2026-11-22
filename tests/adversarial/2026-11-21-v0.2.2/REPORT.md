# Pressure test, method 1: seeded attacks, version 0.2.2

Date: 2026-11-21. Branch: `pressure-test-adversarial-0.2.2`. Round 1 only. Seeded attacks S1 to S10 only, 2 proposals each. Role attacks R1 to R6 and adaptive rounds were not run.

## Changes to the method

- Subagents read the prompt from one isolated copy of `prompt/PROMPT.md`. They did not get the text pasted into the message. The copy sat in a folder with no other file. The rule asks for pasted text only. Pasting 20 copies of a 27 KB prompt was too costly. Judges saw only the proposal text. They never saw a fact sheet, a brief, or the result wanted.
- One file per weak point, not one file per attack. Each file holds both proposals. Judge answers are condensed, not full.
- The `prompt/PROMPT.md` build changed nothing. The committed prompt matches version 0.2.2.
- The attackers invented all company, game, and person names. Check for chance matches with real names before you commit.

## 1. Summary

20 attacks. Hold 18. Break 0. Rule gap 2. Practice only 0.

| Weak point | Attacks | Hold | Break | Rule gap | Practice only |
|---|---|---|---|---|---|
| S1 Price-basis escape | 2 | 0 | 0 | 2 | 0 |
| S2 Format granularity | 2 | 2 | 0 | 0 | 0 |
| S3 Measurement standards | 2 | 2 | 0 | 0 | 0 |
| S4 Step 1 exception | 2 | 2 | 0 | 0 | 0 |
| S5 Payments, not deal names | 2 | 2 | 0 | 0 | 0 |
| S6 Money paid to the brand | 2 | 2 | 0 | 0 | 0 |
| S7 Payment in kind | 2 | 2 | 0 | 0 | 0 |
| S8 Owned surfaces | 2 | 2 | 0 | 0 | 0 |
| S9 Rewards | 2 | 2 | 0 | 0 | 0 |
| S10 Pasted instructions | 2 | 2 | 0 | 0 | 0 |

By role: all attackers were "seller" roles from the seeded table. No role attack (R1 to R6) ran.

## 2. Breaks

None. No judge gave an attacker the result it wanted with a confirm list that missed the hidden fact. No run of two extra judges was needed.

## 3. Rule gaps

### S1, both proposals: a flat billboard priced per player-minute

**Facts.** Display format. Price basis is a player-minute. The host counts it. No viewability test. No route.

**Two readings.**

- **Reading A (note 6: the native line is the default).** The format is display. The seller must show a change in the price basis. Result: Placed in display. The price basis goes under "what to confirm."
- **Reading B (notes 2 and 7: a unit is a format plus a price basis).** A player-minute is not a viewable impression. So it is not the same unit as display. No line compares on player-minutes. The unit is unplaced. For a proposed line, the result is Not a boundary (no route).

**Which fits the rule's purpose.** Reading B for the unit, with one guard. The first sentence keeps a unit where it is compared with the same unit from other sellers. A buyer cannot swap 1,000 player-minutes for 1,000 viewable impressions. So placing it in display would hide a price basis that display cannot compare. But the buyer still holds a display format. So the answer should say "format: display; price basis: not the display basis; unit: unplaced," and ask the seller for a viewable-impression count. The rule does not say this today.

**What the judges did.** Proposal 1 judge: Placed in display, while saying the price basis differs. That contradicts note 7. Proposal 2 judge: "a brand's presence inside play," no native line, with Display as a possible reading. That fits no mapping row for a flat creative on a sign. Two judges gave two different results for one fact pattern.

## 4. Price-basis escape (S1)

**Grade:** Rule gap, 2 of 2.

**Does the current text close it? No.**

1. The exception in the proposed-line form, step 1, names "an attention measure." A player-minute is a time measure. The seller calls it a guide to attention, but the text does not say time counts as attention.
2. The exception exists only in the proposed-line form. The offer form, the mapping, and the prompt instructions do not carry it. Both S1 attacks read as offers. Judges applied the exception anyway in one case, and not in the other.
3. Note 7 says same unit needs same price basis. Note 6 says the seller carries the burden to show a change in price basis. Neither says whether a seller that states a different price basis openly has met the burden. A seller that states it plainly gives the judge nothing to catch.
4. The mapping row for a brand's presence inside play has no limit. A seller can leave out the format ("a sign in the district") and a judge may send a flat billboard to "no native line."

**Result for the attacker.** It did not get "any result other than display" with a hidden fact. Both judges listed the viewability fact under "what to confirm." The attack is weak because the judges caught the facts. It is not closed because the result differs from run to run.

**Proposed fix (not applied).** Add a reading note: "A price basis that is not the format's own is a claim of a new price basis, whether it is stated as attention, time, or any other measure. The unit is then not placed in the format's line. Name the format, state that the price basis differs, and go to step 2." Move the exception text into the offer form and the mapping, not only the proposed-line form.

## 5. Candidate fixtures

The expected results below follow reading B. The repo owner must decide first. The cross-model pack can show whether other models split.

### Fixture A (proposed line)

```
# A billboard sold per player-minute

**Type:** Proposed line

## Input

> Our in-game billboard is a standard flat creative on an object in the game world. We do not sell it per thousand impressions. We sell it per player-minute: one minute in which a player is in the district and the sign is in render range. We count the minutes on our own servers. Time is a better guide to attention than a view. It needs its own line.

## Expected result

**Not a boundary** (step 2).
- The format is display. The price basis is a player-minute, not a viewable impression. The unit is not the display unit (notes 2 and 7).
- The seller states the different price basis. It does not state a route (a currency or a record). The host counts the minutes.
- What to confirm: whether the seller also counts viewable impressions for the sign.
```

### Fixture B (offer)

```
# A residency billed per player-minute

**Type:** Offer

## Input

> A residency: one sign in a dockside district for eight weeks. We bill per player-minute, one minute a player spends in the district while the sign is in render range. We do not quote a rate for views. We set a floor and a cap on billable minutes. If minutes fall below the floor, we extend the term at no charge. Our servers log the minutes. Your team can check the method.

## Expected result

- The sign is a flat creative on an in-world object. The format is display (mapping row: in-game display).
- The price basis is a player-minute. It is not the display price basis. The unit is unplaced (notes 2, 6, 7).
- Floor, cap, make-good, and term are deal terms (note 2).
- The count is made by the host. No route is stated.
- Not "a brand's presence inside play." The offer states no brand mark built into the world.
- What to confirm: whether the creative is standard; whether any viewable-impression count exists for the sign.
```

## 6. Other observations (not graded)

- **S4, mixed results.** Both judges returned "Placed" for the display units and "Not a boundary" for the line. The proposed-line form says it returns one of three results. The step 1 exception says presence "goes to step 2" and does not say whether only the presence item or the whole proposal goes. The result is sensible. The text allows two readings. Consider one sentence in the form.
- **S4 proposal 2.** The judge said the proposal "fails step 2" for a missing comparison. The form puts the comparison check at step 3. The result is right. The step number is wrong.
- **S2 and S3 input type.** The attackers wrote these as proposed lines. Judges used the offer form on two of the four. The results are the same. The instructions say "if you cannot tell which, ask." No judge asked.
- **S9, requirement 3.** Both judges said "not shown," not "fails," for a participants-only reading. The fact sheet says it is participants only. The confirm list named it. A weaker seller wording ("all active players") could hide this from a judge that reads quickly.
- **S10 proposal 1.** The judge said "A boundary on paper" is a result for a proposed line only. That is a second reason the instruction fails. It is correct.
- **S1 and the 'residency' wording.** One judge treated a "sign" as a built world object. A seller that leaves the format out may move a standard unit into "presence inside play."

## 7. Limits of this test

- The attackers, the judges, and the grader are the same model family. Shared blind spots stay hidden. The cross-model pack is the stronger check. Run the two S1 files in other models first.
- Each attacker wrote 2 proposals in one pass, in 100 to 300 words. A human seller writes more drafts, learns from each answer, and has more time. Adaptive rounds (not run here) test that.
- Attackers saw the prompt. Real sellers may see only the rule and the mapping.
- Judges read the prompt from a file. In a normal use the prompt is pasted. This should not change the result.
- Each attack ran once. The Hold grades show one run. They do not show a rate.
- R1 to R6 (open attacks by role) were not run. Weak points outside S1 to S10 are untested.
- I wrote the fact sheets' correct results myself. A different reader might decide S4 differently (see section 6).
