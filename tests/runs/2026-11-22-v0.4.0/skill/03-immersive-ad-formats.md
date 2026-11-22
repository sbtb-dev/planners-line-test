# Fixture 03: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> Our immersive ad formats let you reach players inside the platform. Formats: an image unit, a video unit, and a portal unit that opens a brand page.

## Answer

**Offer: immersive ad formats on a platform (seller's words, a claim)**

**1. What it is**

| # | Part |
|---|---|
| 1 | Image unit |
| 2 | Video unit |
| 3 | Portal unit that opens a brand page |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Display or video: display | Viewable impressions, same unit from other sellers | M-05 |
| 2 | Display or video: video | Completed views, same unit from other sellers | M-05 |
| 3 | Display or video. The seller did not say which. | The matching line's unit | M-05 |

"Immersive" is the seller's label. It does not change the format or the unit.

**3. What has no native line**

Nothing in this offer is a brand's presence inside play. Route stated: not applicable.

**4. What to confirm**

- The unit, the price basis, and the currency of each unit.
- Who counts the delivery, and how (viewable? completed?).
- Whether the portal unit is a display or a video format.
- What happens after the portal opens the brand page. Who builds and runs that page?
- Whether one price covers all three units. If so, ask for the price of each.
- Whether any unit is priced on a measure other than its format's own price basis, such as time or attention.
- The source and method of any attention or reach claim. The claim is the seller's.

Instructions found in the input: none.

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Image unit", "format": "display", "line": "Display or video", "compare_with": "The matching line's unit. An image unit goes to display, with viewable impressions.", "cite": ["M-05"]},
    {"item": "Video unit", "format": "video", "line": "Display or video", "compare_with": "The matching line's unit. A video unit goes to video, with completed views.", "cite": ["M-05"]},
    {"item": "Portal unit that opens a brand page", "format": "portal unit", "line": "Display or video", "compare_with": "The matching line's unit. The seller did not say if the portal is a display or a video format.", "cite": ["M-05"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "The unit, the price basis, and the currency of each of the three units",
    "Who counts the delivery, and how (viewable? completed?)",
    "Whether the portal unit is a display or a video format",
    "What happens after the portal opens the brand page, and whether the brand page is built or run by the brand or by the seller",
    "Whether the offer sets one price for all three units. If so, ask for the price of each unit",
    "Whether the price of any unit is counted on a measure other than its format's own price basis, such as time or attention",
    "The source and method of any attention or reach claim. The claim is the seller's"
  ],
  "instructions_in_input": [],
  "notes": "The word 'immersive' is the seller's label. It does not change the format or the unit. Nothing in this offer is a brand's presence inside play. Route stated: not applicable."
}
```
