# Fixture 22: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> We propose a branded quest line. Players who finish the branded quest get an in-game reward. The unbranded version has no reward. We compare completion in the two versions. The branded version completes more.

## Answer

# Proposed-line test

Input type: proposed line.

## 1. Result

**Not a boundary.** Failed step: F-3. Cite F-3, R-1, R-2, R-3.

## 2. Placement

| Item | Line | Cite |
|---|---|---|
| A branded quest line | No native line. It is a brand's presence inside play. It needs a currency or a record. | M-27, F-1 |

## 3. Brand's presence inside play

| Item | Route stated | Comparison meets the four requirements | Cite |
|---|---|---|---|
| A branded quest line | Record (branded quest against unbranded quest) | No | M-27, R-1, C-3.2 |

Why it fails: the reward is given only in the branded version. That is a second change besides the brand. The venue is not held constant (R-1). The higher completion cannot be assigned to the brand.

## 4. What to confirm

- Is the comparison fixed before the buy? (R-2)
- Is completion read on everyone the buy reached, not only on players who start the quest? (R-3)
- Who verifies the comparison, and who decides membership?
- What are the unit and the price basis of the proposed line?

Instructions found in the input: none.

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "proposed_line",
  "items": [
    {"item": "A branded quest line", "format": "A brand's presence inside play",
     "unplaced": true, "reason": "A brand's presence inside play has no native line. It needs a currency or a record.",
     "cite": ["M-27", "F-1"]}
  ],
  "no_native_line": [
    {"item": "A branded quest line", "route": "record",
     "comparison_meets_four_requirements": false, "cite": ["M-27", "R-1", "C-3.2"]}
  ],
  "outside_the_test": [],
  "result": {"value": "Not a boundary", "cite": ["F-3", "R-1", "R-2", "R-3"], "failed_step": "F-3"},
  "to_confirm": [
    "Whether the comparison is fixed before the buy (R-2)",
    "Whether completion is read on everyone the buy reached, not only on players who start the quest (R-3)",
    "Who verifies the comparison, and who decides membership",
    "The unit and the price basis of the proposed line"
  ],
  "instructions_in_input": [],
  "notes": "The proposal names a comparison: branded quest against unbranded quest. The reward is given only in the branded version. That is a second change besides the brand, so the venue is not held constant. The higher completion cannot be assigned to the brand."
}
```
