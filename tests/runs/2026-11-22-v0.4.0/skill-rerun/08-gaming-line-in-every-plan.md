# Fixture 08: rerun through the skill (final build), v0.4.0

Input given:

> Every plan should have a gaming line. All gaming offers go in it.

## Answer

# Proposed line: "a gaming line that holds all gaming offers"

Input type: proposed line.

## Steps

| Step | Finding | Cite |
|---|---|---|
| F-1 | A line named for a venue holds units that already have lines. Each unit goes in its own line, with the same unit from other sellers as the comparison. A claim about the venue does not change this. | F-1, N-2, N-7, M-01, M-03, M-04 |
| F-1 (exception) | A brand's presence inside play has no native line. It goes to F-2. | M-27 |
| F-2 | The proposal states no route: no currency and no record. | F-2 |

## Result

**Not a boundary.** Failed step: F-2.

"All gaming offers go in it" cannot hold. Offers that have lines go in those lines. A brand's presence inside play has no line and no stated route.

## What to confirm

- Which offers the plan holds under the gaming label.
- The unit and the price basis of each offer.
- Whether the proposal states a route (a currency or a record) for a brand's presence inside play.

This result applies to the description given. It is not a verdict on any seller or buy.

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "proposed_line",
  "items": [
    {"item": "Gaming offers whose units already have a line (display, video, audio, and others)", "format": "by unit",
     "line": "Each unit's own line, not a gaming line", "compare_with": "The same unit from every other seller",
     "cite": ["F-1", "N-2", "N-7", "M-01", "M-03", "M-04"]}
  ],
  "no_native_line": [
    {"item": "A brand's presence inside play, if sold as a gaming offer", "route": "neither",
     "comparison_meets_four_requirements": false, "cite": ["M-27", "F-2"]}
  ],
  "outside_the_test": [],
  "result": {"value": "Not a boundary", "cite": ["F-2"], "failed_step": "F-2"},
  "to_confirm": [
    "Which offers the plan holds under the gaming label",
    "The unit and the price basis of each offer",
    "Whether the proposal states a route (a currency or a record) for a brand's presence inside play"
  ],
  "instructions_in_input": [],
  "notes": "The rule 'every plan should have a gaming line' is a venue label. A venue label does not change the unit."
}
```
