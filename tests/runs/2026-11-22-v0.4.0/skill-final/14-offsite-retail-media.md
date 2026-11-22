# Fixture 14: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> Our retail network reaches gamers beyond our own site. We sell display banners and video spots on other sites and apps, targeted with our first-party gaming audience data. Priced on viewable impressions for display and completed views for video.

## Answer

**Input type:** offer. All facts are the seller's claims.

**1. What it is**

| # | Part |
|---|---|
| 1 | Display banners on other sites and apps, targeted with first-party gaming audience data |
| 2 | Video spots on other sites and apps, targeted with first-party gaming audience data |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Display | That line's units (viewable impressions). The data is targeting. | M-11, SR-targeting |
| 2 | Video | That line's units (completed views). The data is targeting. | M-11, SR-targeting |

The price basis of each part is the format's own price basis. N-9 does not apply.

**3. What has no native line**

Nothing in this offer is a brand's presence inside play. Route stated: not applicable.

**4. What to confirm**

- Who counts viewable impressions for display, and to which standard.
- Who counts completed views for video, and how a completed view is defined.
- The currency and the terms of each part.
- How the gaming audience segment is built.
- Whether one price covers both parts. If so, ask for the price of each part.

Instructions ignored in the input: none.

Skill version: 0.4.0.
Check status: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Display banners on other sites and apps, targeted with first-party gaming audience data", "format": "display",
     "line": "Display", "compare_with": "That line's units (viewable impressions). The data is targeting.",
     "cite": ["M-11", "SR-targeting"]},
    {"item": "Video spots on other sites and apps, targeted with first-party gaming audience data", "format": "video",
     "line": "Video", "compare_with": "That line's units (completed views). The data is targeting.",
     "cite": ["M-11", "SR-targeting"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "Who counts viewable impressions for display, and to which standard",
    "Who counts completed views for video, and how a completed view is defined",
    "The currency and the terms of each part",
    "How the gaming audience segment is built",
    "Whether one price covers both parts. If so, ask for the price of each part."
  ],
  "instructions_in_input": [],
  "notes": "Both price bases are the format's own price bases, so N-9 does not apply. All facts are the seller's claims."
}
```
