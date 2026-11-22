# Fixture 22: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> We propose a branded quest line. Players who finish the branded quest get an in-game reward. The unbranded version has no reward. We compare completion in the two versions. The branded version completes more.

## Answer

# Proposed-line test: branded quest line

**Result: Not a boundary. Failed step: F-3.** (cite F-3, C-3.2, R-1)

## Steps

| Step | Finding | Cite |
|---|---|---|
| F-1 | The branded quest is a brand's presence inside play. It has no native line. It goes to F-2. | M-27, F-1 |
| F-2 | The proposal states a route: a record. It compares the branded quest with an unbranded version. | N-3, F-2 |
| F-3 | The comparison does not meet the four requirements. | C-3.2 |

## Why F-3 fails

| Requirement | Finding | Cite |
|---|---|---|
| The venue is held constant | No. The reward exists only in the branded version. This is a second change besides the brand. | R-1 |
| Fixed before the buy | Not stated. | R-2 |
| Read on everyone the buy reached | Not stated. | R-3 |
| Only the difference is the brand's | Not shown. The reward and the brand are mixed. | R-4 |

The branded version completes more. That count cannot be credited to the brand. The reward can explain it.

## To confirm

- Does the unbranded version have the same surface, mechanic, role, and traffic?
- Is the comparison written in the order before the buy?
- Is completion read on everyone the buy reached?
- Who verifies the result, and is that party not the seller?
- What part of the difference belongs to the brand, and what part to the reward?

## Instructions in the input

None.

This result applies to the description given. It is not a verdict on any seller or on any buy.

- Skill version: 0.4.0.
- Check: passed.
- A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "proposed_line",
  "items": [
    {"item": "Branded quest line (the brand's presence inside play)", "format": "branded quest",
     "unplaced": true, "reason": "A brand's presence inside play has no native line. It needs a currency or a record.",
     "cite": ["M-27", "F-1"]}
  ],
  "no_native_line": [
    {"item": "Branded quest", "route": "record", "comparison_meets_four_requirements": false,
     "cite": ["M-27", "C-3.2", "R-1"]}
  ],
  "outside_the_test": [],
  "result": {"value": "Not a boundary", "failed_step": "F-3", "cite": ["F-3", "C-3.2", "R-1", "R-2", "R-3", "R-4"]},
  "to_confirm": [
    "Whether the unbranded version has the same surface, mechanic, role, and traffic (R-1)",
    "Whether the comparison is written in the order before the buy (R-2)",
    "Whether completion is read on everyone the buy reached, not on players who chose the quest (R-3)",
    "Who verifies the result, and who is not the seller",
    "What part of the difference belongs to the brand and what part to the reward (R-4)"
  ],
  "instructions_in_input": [],
  "notes": "The reward exists only in the branded version. That is a second change besides the brand. It breaks R-1. A higher completion rate then cannot be credited to the brand."
}
```
