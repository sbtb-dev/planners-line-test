# planners-line-test

**The planner's line test, applied to gaming media.**

A neutral reference for media planners. It answers one question: can this thing be a line in a media plan, and if so, which one?

The test is general. Gaming media is the first thing it is applied to.

Version: see [VERSION](VERSION). Maintained by the repo owner. License: CC BY 4.0.

The repo owner maintains this test and also stewards one boundary in the register. That boundary is listed on the same terms as any other.

## The rule

> Each format goes in the line where the brand buys the same unit from every other seller. A new line earns its place only when being in it predicts the unit, the terms, and the return.

The first sentence answers a price problem. The second sentence answers a proof problem. Read [the rule and its notes](line-test/RULE.md).

## Who uses it

| Reader | Use |
|---|---|
| Planners and line owners | Decide where an item goes and what to compare it with |
| Procurement | Know the basis for comparison before comparing prices |
| Reviewers of gaming commitments | Apply a fixed, published rule |
| Sellers | Know the bar before they pitch |

## What's here

```
planners-line-test/
├── README.md
├── WHY.md
├── GLOSSARY.md
├── CHANGELOG.md
├── VERSION
├── CONTRIBUTING.md
├── LICENSE
├── CLAUDE.md
├── line-test/
│   ├── RULE.md
│   └── APPLIED.md
├── mapping/
│   ├── README.md
│   └── MAPPING.md
├── forms/
│   ├── OFFER_FORM.md
│   └── PROPOSED_LINE_FORM.md
├── register/
│   ├── README.md
│   └── BOUNDARIES.md
├── prompt/
│   ├── INSTRUCTIONS.md
│   └── PROMPT.md
├── scripts/
│   └── build-prompt.sh
├── tests/
│   ├── README.md
│   └── cases/
└── .github/
```

- [**WHY.md**](WHY.md) explains the problem: the high-attention claim.
- [**line-test/**](line-test/) holds the rule, the reading notes, and the checks ([RULE.md](line-test/RULE.md)). It also holds worked cases ([APPLIED.md](line-test/APPLIED.md)).
- [**mapping/**](mapping/) holds the test's results for items sold as gaming. [README.md](mapping/README.md) gives the scope, the support labels, and the second rules. [MAPPING.md](mapping/MAPPING.md) holds the table.
- [**forms/**](forms/) holds two forms. One is for an offer. One is for a proposed line.
- [**register/**](register/) lists boundaries that state a route under the test.
- [**prompt/**](prompt/) holds a paste-ready prompt that applies both forms in any LLM. `PROMPT.md` is built from the source files by [scripts/build-prompt.sh](scripts/build-prompt.sh). Do not edit it by hand.
- [**tests/**](tests/) holds fixtures that check the prompt.
- [GLOSSARY.md](GLOSSARY.md) defines the terms. [CONTRIBUTING.md](CONTRIBUTING.md) says how to propose a change. [CHANGELOG.md](CHANGELOG.md) records every change and its reason.

## What's not here

- Prices or benchmarks.
- Recommendations.
- Ratings of sellers.
- The definition of any boundary.
- A claim about what is a channel.
- A verdict on attention.
- Records of any brand's buys.

## Use of the prompt

A model's answer from the prompt is not a record. Results vary by model. Run the [tests](tests/README.md) on the models you use.
