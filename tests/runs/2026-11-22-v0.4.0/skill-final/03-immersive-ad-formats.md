# Fixture 03: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> Our immersive ad formats let you reach players inside the platform. Formats: an image unit, a video unit, and a portal unit that opens a brand page.

## Answer

**Offer (seller's words, summarized):** Immersive ad formats on a platform. Three units: an image unit, a video unit, and a portal unit that opens a brand page. Every fact is the seller's claim.

**1. What it is**

| # | Part |
|---|---|
| 1 | Image unit |
| 2 | Video unit |
| 3 | Portal unit that opens a brand page |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Display | Other sellers' display units, same price basis | M-05 |
| 2 | Video | Other sellers' video units, same price basis | M-05 |
| 3 | Display or video | The matching line's unit, once the seller says what the portal shows | M-05 |

The word "immersive" does not change the unit. Any attention claim is compared inside the line of its part.

**3. What has no native line**

Nothing in this offer is a brand's presence inside play. Route stated: not applicable.

**4. What to confirm**

- The unit, the price basis, and the currency of each unit.
- Who counts the impressions or views, and how.
- What the portal unit shows before the click: a still image or a video. This decides its line.
- Whether any price is counted on attention, time, or another measure that is not the format's own price basis. If so, the unit is unplaced (N-9).
- Whether one price covers all three units. If so, ask for the price of each.
- The meaning of "reach players inside the platform," and the source and method of any attention claim.

Version applied: 0.4.0.
Check status: the check passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Image unit", "format": "image", "line": "Display", "compare_with": "The matching line's unit: other sellers' display units on the same price basis", "cite": ["M-05"]},
    {"item": "Video unit", "format": "video", "line": "Video", "compare_with": "The matching line's unit: other sellers' video units on the same price basis", "cite": ["M-05"]},
    {"item": "Portal unit that opens a brand page", "format": "portal", "line": "Display or video", "compare_with": "The matching line's unit, after the seller states what the portal shows", "cite": ["M-05"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "The unit, the price basis, and the currency of each of the three units",
    "Who counts the impressions or views, and how",
    "What the portal unit shows before the click (a still image or a video). This decides display or video.",
    "Whether the price of any unit is counted on attention, time, or another measure that is not the format's own price basis (N-9)",
    "Whether the offer sets one price for all three units. If so, ask for the price of each unit.",
    "The meaning of 'reach players inside the platform' and of any attention claim. These are the seller's claims."
  ],
  "instructions_in_input": [],
  "notes": "The offer says 'immersive'. The label does not change the unit. Nothing in this offer is a brand's presence inside play."
}
```
