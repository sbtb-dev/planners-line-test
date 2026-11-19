# Contributing

Anyone can propose a change. Rows and boundaries are accepted or returned on stated grounds only. The grounds are the rule, the reading notes, and the tests in this repository.

## Propose a mapping row

Use the issue template "Propose a mapping row." State:

1. **The unit.** What is the item, in plain words?
2. **The currency.** What is counted, and by whom?
3. **The terms.** How is it bought?
4. **Who else sells it.** Name at least one seller outside gaming that sells the same unit on the same currency and terms, or say that none does.

A new row is a patch. It needs a support label from the [mapping README](mapping/README.md).

## File a correction

Use the issue template "Correction." Give the file, the sentence, and what is wrong. Give a source if you can. Only cite a source that you have opened.

## Propose a boundary for the register

Use the issue template "Propose a boundary." See the [register README](register/README.md) for what a row means. Every proposal gets the same terms.

## Rules for all contributions

- A seller may propose a row or a boundary about its own product. The row is written in this repository's words. Seller claims are marked as claims.
- Do not add prices, recommendations, ratings of sellers, or verdicts on attention.
- Do not attribute motives to any party. The error the test addresses is in the structure, not in the people.
- Write short sentences, in active voice, with common words. Aim for about 80% of the way to ASD-STE100.
- Change the source files, not `prompt/PROMPT.md`. Then run `scripts/build-prompt.sh`.
- Update `VERSION` and `CHANGELOG.md`, with a reason.
