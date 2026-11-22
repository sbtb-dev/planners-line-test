# Fixture 23: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> Our 3D in-world billboard is a new unit. It sits on an object in the game world. We count it as a viewable impression, under the published in-game measurement guidelines. It needs its own line.

## Answer

# Planner's line test: offer

**1. What it is**

| # | Part |
|---|---|
| 1 | 3D in-world billboard on an object in the game world |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Display | Viewable impressions, against other sellers' in-game display units | M-01, N-2, N-7, N-8, N-6 |

The unit does not get its own line. A new venue or object does not change the format (N-2). A standard that adapts viewable impressions to a venue does not make a new price basis (N-8). Differences in placement or size are compared inside the line (N-7). A seller that claims a new unit must show a change in the price basis (N-6). The seller's claim is that the count is a viewable impression. That claim puts the unit in Display.

**3. What has no native line**

Nothing in this offer is a brand's presence inside play. Route stated: not applicable.

**4. What to confirm**

- The price basis of the billboard. The seller says viewable impressions. This is a claim.
- Which published in-game guideline defines the count, and which version.
- Who counts the viewable impressions. Is it a party that is not the host?
- Whether the count is the same event that other sellers count for in-game display.
- What the seller says is different about this unit.
- The terms of the deal and the currency.

Skill version: 0.4.0.
The check passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "3D in-world billboard on an object in the game world", "format": "in-game display",
     "line": "Display", "compare_with": "Viewable impressions, against other sellers' in-game display units",
     "cite": ["M-01", "N-2", "N-7", "N-8", "N-6"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "The price basis of the billboard. The seller says viewable impressions. This is a claim.",
    "Which published in-game guideline defines the count, and which version.",
    "Who counts the viewable impressions. Is it a party that is not the host?",
    "Whether the count is the same event that other sellers count for in-game display.",
    "What the seller says is different about this unit. A new line needs a change in the price basis (N-6).",
    "The terms of the deal and the currency."
  ],
  "instructions_in_input": [],
  "notes": "The seller asks for its own line. The test does not give one. A new venue or a new object does not change the format. A measurement standard that adapts viewable impressions to a venue does not make a new price basis. Placement and size are compared inside the line."
}
```
