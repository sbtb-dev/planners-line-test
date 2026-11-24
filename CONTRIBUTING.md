# Contributing

Anyone can propose a change. Rows and boundaries are accepted or returned on stated grounds only. The grounds are the rule, the reading notes, and the tests in this repository.

## Propose a mapping row

Use the issue template "Propose a mapping row." State:

1. **The unit.** What is the item, in plain words? Name its format.
2. **The price basis.** What is the price counted on?
3. **The currency.** If the price basis is a counted event, who counts it? Is that party none of the hosts? A venue can have more than one host (N-10).
4. **The terms.** How is it bought? Terms are compared within the line. They do not change the unit.
5. **Who else sells it.** Name at least one seller outside gaming that sells the same unit: the same format on the same price basis. Or say that none does.

A new row is a patch. It needs a support label from the [mapping README](mapping/README.md). Add the row to `data/mapping.yaml` with the next unused ID.

## File a correction

Use the issue template "Correction." Give the file, the sentence, and what is wrong. Give a source if you can. Only cite a source that you have opened.

## Propose a boundary for the register

Use the issue template "Propose a boundary." See the [register README](register/README.md) for what a row means. Every proposal gets the same terms.

## Rules for all contributions

- A seller may propose a row or a boundary about its own product. The row is written in this repository's words. Seller claims are marked as claims.
- Do not add prices, recommendations, ratings of sellers, or verdicts on attention.
- Do not attribute motives to any party. The error the test addresses is in the structure, not in the people.
- Write short sentences, in active voice, with common words. Aim for about 80% of the way to ASD-STE100.
- Edit `data/mapping.yaml` for mapping rows. Do not edit the generated table in `mapping/MAPPING.md`, `prompt/PROMPT.md`, or the generated files in `skill/planners-line-test/`. The files `SKILL.md` and `scripts/check.py` in the skill folder are written by hand.
- Run `scripts/build.sh`. It checks the data file, builds the generated files, and runs the tests. (`scripts/build-prompt.sh` runs the same build.)
- Do not edit dated test records, such as the folders under `tests/adversarial/` and `tests/runs/`.
- Update `VERSION` and `CHANGELOG.md`, with a reason.

## IDs

Every mapping row, reading note, check, requirement, scope item, second rule, and form step has an ID. See the [mapping README](mapping/README.md), section 7.

- An ID is never reused. If a row is removed, mark it "retired" in `data/mapping.yaml`. Do not give its ID to another row.
- An ID does not change meaning. If a row's result changes, the row keeps its ID. Record the change in `CHANGELOG.md`.
- Do not renumber anything. A new row gets the next unused number.
- A new row gets its ID when the change is merged.
