# Fixture 20: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> We propose a gaming attention line. It holds display, video, and audio units in games. Each unit has an attention score from an accredited attention vendor. A higher score earns a premium.

## Answer

**Result: Placed (F-1).** The gaming attention line is not one line. Each unit goes in its own line.

| Unit | Line | Compare with | Cite |
|---|---|---|---|
| Display units in games | Display | Viewable impressions from other sellers of display | F-1, M-01, N-2 |
| Video units in games | Video | Completed views from other sellers of video | F-1, M-03, N-2 |
| Audio units in games | Audio | Completed listens from other sellers of audio | F-1, M-04, N-2 |

A venue label does not change the format (N-2). An attention score is a property of the delivery. Compare it within the line. A premium for a higher score is a deal term in that line.

**What to confirm**
- The price basis of each unit. Is it the price basis of its own line?
- Whether the premium is added to the format's own price basis. Or whether the price itself is counted on the attention score. If the price is counted on the score, N-9 applies. The units are then not the same units. The proposal goes to F-2, and it needs a currency or a record.
- Who accredits the attention vendor.
- Whether any unit is a brand's presence inside play (M-27).

This result applies to the description given. It is not a verdict on any seller or buy.

Skill version: 0.4.0.
The check passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "proposed_line",
  "items": [
    {"item": "Display units in games", "format": "display", "line": "Display",
     "compare_with": "Viewable impressions, from other sellers of display", "cite": ["F-1", "M-01", "N-2"]},
    {"item": "Video units in games", "format": "video", "line": "Video",
     "compare_with": "Completed views, from other sellers of video", "cite": ["F-1", "M-03", "N-2"]},
    {"item": "Audio units in games", "format": "audio", "line": "Audio",
     "compare_with": "Completed listens, from other sellers of audio", "cite": ["F-1", "M-04", "N-2"]}
  ],
  "result": {"value": "Placed", "cite": ["F-1", "N-2", "N-7"]},
  "to_confirm": [
    "The price basis of each unit: is it the price basis of its own line?",
    "Whether the premium is added to the format's own price basis, or the price itself is counted on the attention score (N-9)",
    "Who accredits the attention vendor, and whether the score is a property of the delivery",
    "Whether any unit is a brand's presence inside play (M-27)"
  ],
  "notes": "A line named for a venue holds units that already have lines. A higher attention score is a property of the delivery. It is compared within the line (N-2). If the price is counted on attention, N-9 applies. Then the units are not the same units, and the proposal goes to F-2."
}
```
