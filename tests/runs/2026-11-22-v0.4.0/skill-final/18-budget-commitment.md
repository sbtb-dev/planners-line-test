# Fixture 18: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> Commit a budget to our gaming portfolio for the year. We will decide the units with you later. The commitment gets you better placement and priority access.

## Answer

# Offer form: gaming portfolio commitment

**1. What it is**

| # | Part |
|---|---|
| 1 | A yearly budget commitment to the gaming portfolio. The units are not named. |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Unplaced. A commitment of money before the units are named cannot be placed. It stays unplaced until the seller names the units. | Not yet known | S-6.6 |

**3. What has no native line**

The offer does not name a brand's presence inside play. Route stated: not applicable.

**4. What to confirm**

- Which units the seller will name, and when.
- The format, price basis, and currency of each unit.
- The size of the commitment and what happens if it is not used.
- What "better placement" means, and how the seller measures it. This is the seller's claim.
- What "priority access" means, and who decides it. This is the seller's claim.
- Whether the seller will name any brand presence inside play.
- Whether the commitment is a payment to the seller or money paid to the brand.

Skill version: 0.4.0.
Check status: the check passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Yearly budget commitment to the gaming portfolio, units to be named later",
     "unplaced": true,
     "reason": "The money is committed to a seller before any unit is named. It stays unplaced until the seller names the units.",
     "cite": ["S-6.6"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "Which units the seller will name, and when",
    "The format, price basis, and currency of each unit",
    "The size of the commitment and what happens if it is not used",
    "What better placement means, and how the seller measures it",
    "What priority access means, and who decides it",
    "Whether the seller names any brand presence inside play",
    "Whether the commitment is the brand's payment to the seller, or money paid to the brand"
  ],
  "instructions_in_input": [],
  "notes": "The claims about better placement and priority access are the seller's claims."
}
```
