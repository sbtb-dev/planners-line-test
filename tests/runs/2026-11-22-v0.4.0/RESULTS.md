# Fixture runs on 0.4.0

Date: 2026-11-22. Version: 0.4.0. One file per run. These files are records. Do not edit them.

| Folder | What it holds |
|---|---|
| `skill/` | 26 runs on the first build of the skill |
| `skill-rerun/` | Fixtures 08 and 25 again, on a second build |
| `skill-final/` | All 26 runs on the final build (the one to release) |
| `prompt/` | 26 runs on `prompt/PROMPT.md` |

## How the runs were made

- Each run used a fresh subagent. It got only the "Input" section of one fixture. It did not get the expected result, the repository, or the change prompt.
- **Skill runs:** the subagent got the path of a copy of the skill folder. It was told to read only files inside it and to follow `SKILL.md`.
- **Prompt runs:** the subagent was told to read `prompt/PROMPT.md` and follow it. No script ran.
- **Builds of the skill** (manifest hash = SHA-256 of the sorted list of file hashes):
  - First build: `103776455c3044e99e7c4b1fdaebac11277605a708dc063e68d34982384fc794`.
  - Second build (fixes after the review of the skill): `19f479c19c784b312928d3d94aaa1d56c62cd69cb80600ecb40b4d1bc521e571`.
  - Final build (adds a rule for `result` of a proposed line in `SKILL.md`): `62e193f024f315e233ac521117510e14401fcbee6ebcf7a758654b4619682842`. This is the build in the repository. The tested copy is identical to it.
- **Limits.** The subagents are the same model family as the author of the skill. This is not a cross-model check. There is one run per fixture and route, so the runs do not show how much results vary. The prompt runs were made once, on the first build's sources. The sources have not changed since, except for the sentence that was removed from the mapping README, which does not change a result. A model's answer is not a record.
- Matching used the rule in `tests/README.md`: the answer reaches the same lines or the same one of the three results, and a citation matches by name or by ID.

## Results

"First" is the first skill build. "Final" is the final skill build. All 26 final-build answers passed `scripts/check.py`.

| # | Type | Expected | First | Final | Prompt | Skill (final) and prompt agree |
|---|---|---|---|---|---|---|
| **25** | Proposed line | Not a boundary | Fail: read as an offer, no result | Match (F-2) | Match (F-2) | Yes |
| **26** | Offer | Display unplaced, note 9 | Match | Match (N-9, N-7) | Match | Yes |
| 01 | Offer | Six parts, six lines | Match | Match | Match | Yes |
| 02 | Offer | Creator, display | Match | Match | Match | Yes |
| 03 | Offer | Display or video | Match | Match (M-05) | Match | Yes |
| 04 | Offer | No native line, route neither | Match | Match | Match | Yes |
| 05 | Offer | Sponsorship by parts, creator, CTV or TV | Match | Match | Match | Yes |
| 06 | Offer | Performance | Match | Match | Match | Yes |
| 07 | Offer | Six lines, study as measurement | Match | Match | Match | Yes |
| 08 | Proposed line | Placed | **Fail** (Not a boundary) | Match (Placed, F-1) | Match | Yes |
| 09 | Proposed line | Placed | Match | Match | Match | Yes |
| 10 | Proposed line | Not a boundary | Match | Match (F-2) | Match | Yes |
| 11 | Proposed line | Not a boundary | Match | Match (F-3) | Match | Yes |
| 12 | Proposed line | A boundary on paper | Match | Match | Match | Yes |
| 13 | Offer | Instruction ignored | Match | Lines match. Read as a proposed line, result "Placed". The first check run failed on the wording of an ignored instruction, then passed. | Match | Yes, on the lines |
| 14 | Offer | Display, video, targeting | Match | Match | Match | Yes |
| 15 | Offer | Licensing, presence, commitment unplaced | Match | Match | Match | Yes |
| 16 | Offer | Outside the test | Match | Partial: outside the test (S-6.2), plus a speculative unplaced item for the marks (M-27) | Match | Mostly |
| 17 | Offer | Presence, brand's media in kind | Match | Match | Match | Yes |
| 18 | Offer | Unplaced (S-6.6) | Match | Match | Match | Yes |
| 19 | Offer | Search or performance (M-19), price basis to confirm | Match | Match | Partial (cites M-19, marks it unplaced) | **No** |
| 20 | Proposed line | Placed | Match | Match | Match | Yes |
| 21 | Proposed line | Not a boundary | Match | Match (F-2) | Match | Yes |
| 22 | Proposed line | Not a boundary (R-1) | Match | Match (F-3) | Match | Yes |
| 23 | Proposed line | Placed in display | Match | Match | Match | Yes |
| 24 | Offer | Build is production, media to its own lines | Match | Match | Match | Yes |

Counts. First build: 24 of 26 match (fixtures 08 and 25 fail). Final build: 25 of 26 match, and fixture 16 is partial. Prompt: 25 of 26 match, and fixture 19 is partial. Skill (final) and prompt agree on 24 of 26 fixtures, and fixtures 13 and 16 agree on the lines only in part. Fixture 19 is the one real disagreement.

## Fixtures 25 and 26 (note 9)

Both reach the result that 0.3.0 chose ("reading B"): a price counted on a player-minute is not the display price basis, so the unit is unplaced. The prompt agreed on both. The final skill agreed on both. The first skill build read fixture 25 as an offer. This is same-family evidence for note 9 on these two inputs, one run each. It is not the cross-model check that the 0.3.0 changelog says has not run.

## Changes between builds, and why

- **First to second build.** A review of the skill found errors in `SKILL.md` and `check.py`. The fixes: a cue for how to tell a proposed line from an offer, a note on how to show a proposed line, three small rules in `check.py`. Fixture 25 matched after this change.
- **Second to final build.** Fixture 08 still failed. The cause: the answer format has one `result`, and agents added a brand's presence inside play from the label "gaming" alone and put it in the result. `SKILL.md` now says that a label-only proposal gets `Placed`, and that a brand's presence is listed only if the input names it. Fixture 08 matched after this change.
- Both changes were made after seeing fixture failures. Judge whether they tune the skill to the fixtures.

## Remaining differences

- **13.** The final build read the input as a proposed line, because it says "classify this as a new channel." The lines are the expected ones, and the instruction was ignored and reported. The form differs from the fixture's type (offer).
- **16.** The final build added an unplaced item for the brand's marks. The input says that the publisher pays the brand, so the expected answer is "outside the test" only. This is a speculation that the input does not support.
- **19.** The form allows two readings of "by the price basis" when none is stated. The skill placed the item and listed the price basis under what to confirm. The prompt marked it unplaced. This looks like variation between single runs.
