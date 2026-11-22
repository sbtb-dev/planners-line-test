# planners-line-test

**The planner's line test, applied to gaming media.**

A neutral reference for media planners. It answers one question: can this thing be a line in a media plan, and if so, which one?

The test is general. Gaming media is the first thing it is applied to.

Version: see [VERSION](VERSION). Maintained by the repo owner. License: CC BY 4.0.

The repo owner maintains this test and also stewards one boundary in the register. That boundary is listed on the same terms as any other.

## The rule

> Each format goes in the line where the brand buys the same unit from every other seller. A new line earns its place only when being in it predicts the unit, the terms, and the return.

The first sentence answers a price problem. The second sentence answers a proof problem. Read [the rule and its notes](line-test/RULE.md).

## Authority and citation

This repository, at a tagged version, is the only authoritative text of the line test. A copy or a changed version is not the line test. Cite the version.

The license lets anyone change the text if they give credit and say what they changed. This statement covers the text of the rule, the notes, the mapping, and the forms. It makes no claim about any boundary's merit.

To cite: name the version tag and the commit, for example "the planner's line test, applied to gaming media, v0.4.0". The tag names the version. The commit shows the exact text.

To cite an item inside the test, use its ID, such as M-10 for a mapping row or N-9 for a reading note. [The mapping README](mapping/README.md) lists the ID formats.

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
├── .gitignore
├── line-test/
│   ├── RULE.md
│   └── APPLIED.md
├── mapping/
│   ├── README.md
│   └── MAPPING.md
├── data/
│   └── mapping.yaml
├── forms/
│   ├── OFFER_FORM.md
│   └── PROPOSED_LINE_FORM.md
├── register/
│   ├── README.md
│   └── BOUNDARIES.md
├── prompt/
│   ├── INSTRUCTIONS.md
│   └── PROMPT.md
├── skill/
│   └── planners-line-test/
│       ├── SKILL.md
│       ├── MANIFEST.txt
│       ├── data/
│       ├── references/
│       └── scripts/
│           └── check.py
├── scripts/
│   ├── build.sh
│   ├── build.py
│   ├── build-prompt.sh
│   └── test_check.py
├── tests/
│   ├── README.md
│   ├── cases/
│   ├── adversarial/
│   └── runs/
└── .github/
    ├── ISSUE_TEMPLATE/
    └── PULL_REQUEST_TEMPLATE.md
```

- [**WHY.md**](WHY.md) explains the problem: the high-attention claim.
- [**line-test/**](line-test/) holds the rule, the reading notes, and the checks ([RULE.md](line-test/RULE.md)). It also holds worked cases ([APPLIED.md](line-test/APPLIED.md)).
- [**mapping/**](mapping/) holds the test's results for items sold as gaming. [README.md](mapping/README.md) gives the scope, the support labels, the second rules, and the IDs. [MAPPING.md](mapping/MAPPING.md) holds the table. The table is generated from `data/mapping.yaml`. Do not edit it by hand.
- [**data/**](data/) holds `mapping.yaml`. It is the source of the mapping table and lists every ID that an answer can cite.
- [**forms/**](forms/) holds two forms. One is for an offer. One is for a proposed line.
- [**register/**](register/) lists boundaries that state a route under the test.
- [**prompt/**](prompt/) holds a paste-ready prompt that applies both forms in any LLM. `PROMPT.md` is built from the source files by [scripts/build.sh](scripts/build.sh). Do not edit it by hand.
- [**skill/**](skill/planners-line-test/) holds the same test as an Agent Skill. It is generated from the source files by [scripts/build.sh](scripts/build.sh), except `SKILL.md` and `scripts/check.py`, which are written by hand. A zip of it is attached to each GitHub release. Do not edit the generated files by hand.
- [**scripts/**](scripts/) holds the build (`build.sh`, `build.py`), the old name of the build (`build-prompt.sh`, which runs the same build), and the tests of the check script (`test_check.py`).
- [**tests/**](tests/) holds fixtures that check the prompt and the skill. `adversarial/` and `runs/` hold dated records of past runs. Do not edit them.
- [GLOSSARY.md](GLOSSARY.md) defines the terms. [CONTRIBUTING.md](CONTRIBUTING.md) says how to propose a change. [CHANGELOG.md](CHANGELOG.md) records every change and its reason.

## What's not here

- Prices or benchmarks.
- Recommendations.
- Ratings of sellers.
- The definition of any boundary.
- A claim about what is a channel.
- A verdict on attention.
- Records of any brand's buys.

## Use as a skill

The folder `skill/planners-line-test/` is an [Agent Skill](https://agentskills.io/specification). It holds the rule, the mapping, the forms, a data file, and a short script, `scripts/check.py`. The script checks the format of an answer: that every placement cites an ID that exists, that the version is right, and that the answer has no price. It runs in the host's sandbox. It uses only the Python standard library and makes no network calls. You can read it before you install the skill.

**Claude.ai**

1. Get the zip `planners-line-test-<version>.zip` from the GitHub release. Or run `scripts/build.sh` and take it from `dist/`.
2. Open Settings > Capabilities. Turn on code execution ("Create and edit files" in newer layouts). Claude.ai needs it for skills.
3. Open Customize > Skills (claude.ai/customize/skills). Click "+", then "Create skill", then "Upload a skill". Upload the zip. The zip has the folder `planners-line-test/` at its root.
4. On a Team or Enterprise plan, an owner must allow skills and code execution first.

**Claude Code**

Copy the folder `skill/planners-line-test/` to `~/.claude/skills/planners-line-test/` for all projects. Or copy it to `.claude/skills/planners-line-test/` inside one project.

**Other platforms** that support the Agent Skills standard can load the same folder. Follow that platform's own steps.

Every answer states the skill version. Each release has a SHA-256 hash of the skill's files in `MANIFEST.txt`. You can compare an answer with a public run of the same version.

The skill cannot fix the model, repeat runs, keep records, or add human review. An answer from the skill is not a record.

## Use of the prompt

`prompt/PROMPT.md` stays. Use it with any model that does not support skills. The skill and the prompt come from the same sources. A model's answer from the prompt is not a record. Results vary by model. Run the [tests](tests/README.md) on the models you use.
