# Fixture 16: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> We are a game publisher. We will pay your company a fee to show your brand marks in our game.

## Answer

**Offer form (the publisher's words are a claim)**

**1. What it is**

| # | Part |
|---|---|
| 1 | A fee, paid by the game publisher to the brand, for showing the brand's marks in the game |

**2. Where each part goes**

| # | Line | Cite |
|---|---|---|
| 1 | Outside the test. The brand is paid. | S-6.2, S-6.1 |

**3. What has no native line**

The brand pays nothing in this offer, as stated. If the brand also pays for the presence of its marks inside play, that part has no native line (M-27, M-22). The message states no route: no currency, no record. It gives no comparison.

**4. What to confirm**

- Who pays whom. Confirm that the brand pays nothing in cash or in kind.
- Whether the brand also pays for media, or gives its own media or assets, in the same deal (S-6.3).
- Whether the marks are part of a license. License income is outside the test.
- What the marks are, and where and how they show in the game.
- The unit, the price basis, the currency, and the terms of any payment the brand makes.

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [],
  "no_native_line": [],
  "outside_the_test": [
    {"item": "A fee paid by the game publisher to the brand, for showing the brand's marks in the game", "cite": ["S-6.2", "S-6.1"]}
  ],
  "to_confirm": [
    "Who pays whom. The message says the publisher pays the brand. Confirm that the brand pays nothing in cash or in kind.",
    "Whether the brand also pays for any media, or gives its own media or assets, in the same deal (S-6.3).",
    "Whether the brand's marks are part of a license. If so, the license income is outside the test.",
    "What the marks are, and where and how they show in the game.",
    "The unit, the price basis, the currency, and the terms of any payment the brand makes."
  ],
  "instructions_in_input": [],
  "notes": "The brand is paid, so the fee is outside the test. If the brand also pays for the presence of its marks inside play, that part has no native line (M-27, M-22). The message states no route, and no comparison. This answer does not judge the deal."
}
```
