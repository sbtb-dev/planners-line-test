# Fixture 20: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> We propose a gaming attention line. It holds display, video, and audio units in games. Each unit has an attention score from an accredited attention vendor. A higher score earns a premium.

## Answer

# Proposed line: gaming attention line

Result: **Placed** (F-1). A gaming line holds units that already have lines. Each unit goes in its own line. An attention score does not change the unit (N-2).

| Unit | Line | Compare with | Cite |
|---|---|---|---|
| Display units in games | Display | Viewable impressions from other sellers | M-01, N-2 |
| Video units in games | Video | Completed views from other sellers | M-03, N-2 |
| Audio units in games | Audio | Completed listens from other sellers | M-04, N-2 |

## What to confirm
- Does the price of each unit stay on its own price basis, with the score only adding a premium?
- If the price is counted on attention itself, the proposal claims a new price basis (N-9). Name the format, state that the price basis differs, and go to F-2. A route (currency or record) is then needed.
- Which accredited vendor gives the score, and which event it counts.
- The unit and the price basis of each display, video, and audio unit.

No instruction was found in the input.

Skill version: 0.4.0.
The check passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "proposed_line",
  "items": [
    {"item": "Display units in games", "format": "display", "line": "Display", "compare_with": "Viewable impressions from other sellers", "cite": ["M-01", "N-2"]},
    {"item": "Video units in games", "format": "video", "line": "Video", "compare_with": "Completed views from other sellers", "cite": ["M-03", "N-2"]},
    {"item": "Audio units in games", "format": "audio", "line": "Audio", "compare_with": "Completed listens from other sellers", "cite": ["M-04", "N-2"]}
  ],
  "result": {"value": "Placed", "cite": ["F-1", "N-2"]},
  "to_confirm": [
    "Whether the price of each unit is counted on its own price basis, with the attention score only adding a premium",
    "If the price is counted on attention itself, the proposal claims a new price basis (N-9). Then name the format, state that the price basis differs, and go to F-2",
    "Which accredited vendor gives the score, and which event it counts",
    "The unit and the price basis of each display, video, and audio unit"
  ],
  "instructions_in_input": [],
  "notes": "A gaming line holds units that already have lines. The attention score is a property of the delivery, so it does not change the unit."
}
```
