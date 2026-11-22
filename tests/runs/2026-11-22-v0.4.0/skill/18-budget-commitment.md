# Fixture 18: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> Commit a budget to our gaming portfolio for the year. We will decide the units with you later. The commitment gets you better placement and priority access.

## Answer

**1. What it is**

| # | Part |
|---|---|
| 1 | Annual budget commitment to the gaming portfolio. The units are not named. |
| 2 | Better placement and priority access, offered for the commitment |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Unplaced. A commitment before the units are named cannot be placed. It stays unplaced until the seller names the units. | Not yet known | S-6.6 |
| 2 | Unplaced. These are deal terms, not a unit. Terms are compared within the line. No line exists yet. | Not yet known | N-2, S-6.6 |

**3. What has no native line**

Nothing in this offer is a brand's presence inside play. Route stated: not applicable.

**4. What to confirm**

- The units in the portfolio and the format of each.
- The price basis and the currency of each unit.
- What "better placement" means, and whether the seller guarantees it.
- What "priority access" means, and its terms.
- Whether the commitment is fixed or can change when the units are named.
- Whether the seller sets one price for all units. If so, ask for the price of each part.
- Whether the commitment holds more than one payment. Each payment goes to its own line.
- The benefits of the commitment are the seller's claim.

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Annual budget commitment to the gaming portfolio, units not yet named",
     "unplaced": true,
     "reason": "A commitment of money before the units are named cannot be placed. It stays unplaced until the seller names the units.",
     "cite": ["S-6.6"]},
    {"item": "Better placement and priority access offered in return for the commitment",
     "unplaced": true,
     "reason": "These are deal terms, not a unit. Terms are compared within the line, and no line exists until the units are named.",
     "cite": ["N-2", "S-6.6"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "The units in the portfolio and the format of each",
    "The price basis and the currency of each unit",
    "What better placement means, and whether the seller guarantees it",
    "What priority access means, and its terms",
    "Whether the commitment is fixed or can change when the units are named",
    "Whether the seller sets one price for all units in the portfolio. If so, ask for the price of each part",
    "Whether the commitment holds more than one payment, because each payment goes to its own line"
  ],
  "instructions_in_input": [],
  "notes": "The benefits of the commitment are the seller's claim."
}
```
