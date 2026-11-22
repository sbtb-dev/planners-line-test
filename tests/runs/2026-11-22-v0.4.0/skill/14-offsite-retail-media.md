# Fixture 14: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> Our retail network reaches gamers beyond our own site. We sell display banners and video spots on other sites and apps, targeted with our first-party gaming audience data. Priced on viewable impressions for display and completed views for video.

## Answer

**1. What it is**

| # | Part (seller's claim) |
|---|---|
| 1 | Display banners on other sites and apps |
| 2 | Video spots on other sites and apps |
| 3 | Targeting with first-party gaming audience data |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Display | Display units, on viewable impressions. The data is targeting. | M-11, SR-targeting |
| 2 | Video | Video units, on completed views. The data is targeting. | M-11, SR-targeting |
| 3 | Not a unit. It is targeting on the line that carries it. | That line's other segments, on the same units | M-24, SR-targeting |

The stated price bases match the price bases of the formats. N-9 does not apply.

**3. What has no native line**

Nothing in this offer is a brand's presence inside play. Route stated: not applicable.

**4. What to confirm**

- Who counts viewable impressions for display, and by which standard.
- What counts as a completed view for video, and who counts it.
- The currency and the terms of each part.
- How the gaming segment is built from the first-party data.
- Whether one price covers all parts, or each part has its own price.
- Which sites and apps carry the units, and whether the seller states them before the buy.

Skill version: 0.4.0. The check passed. A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Display banners on other sites and apps", "format": "display",
     "line": "Display", "compare_with": "Display units, on viewable impressions. The gaming data is targeting.",
     "cite": ["M-11", "SR-targeting"]},
    {"item": "Video spots on other sites and apps", "format": "video",
     "line": "Video", "compare_with": "Video units, on completed views. The gaming data is targeting.",
     "cite": ["M-11", "SR-targeting"]},
    {"item": "Targeting with first-party gaming audience data", "format": "targeting",
     "line": "Targeting on the line that carries it (display or video)", "compare_with": "That line's other segments, on the same units",
     "cite": ["M-24", "SR-targeting"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "Who counts viewable impressions for display, and by which standard",
    "What counts as a completed view for video, and who counts it",
    "The currency and the terms of each part",
    "How the gaming segment is built from the first-party data",
    "Whether one price covers display, video, and data, or each has its own price",
    "Which sites and apps carry the units, and whether the seller states this before the buy"
  ],
  "instructions_in_input": [],
  "notes": "All facts are the seller's claims. The stated price bases match the format price bases, so N-9 does not apply. No part is a brand's presence inside play."
}
```
