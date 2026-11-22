# Fixture 06: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> Our playable ad lets players try your app in 30 seconds. We charge per install.

## Answer

# Offer form

Source: the seller's own words. Every fact below is the seller's claim.

**1. What it is**

| # | Part |
|---|---|
| 1 | A playable ad. Players try the app in 30 seconds. It is charged per install. |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Performance | The performance line's units: cost per install, from other sellers | M-06, SR-price-basis |

The price basis is per install. A playable bought per install is performance.

**3. What has no native line**

Nothing in this offer is a brand's presence inside play. Route stated: not applicable.

**4. What to confirm**

- What counts as an install, and who counts it.
- The currency and the terms of the charge.
- Whether the seller also sells the playable on impressions or completed plays. Those would go to display or video.
- The source and method of any claim about the 30-second trial.

Skill version: 0.4.0.
The check passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Playable ad that lets players try the app in 30 seconds, charged per install", "format": "playable ad",
     "line": "Performance", "compare_with": "The performance line's units: cost per install, from other sellers",
     "cite": ["M-06", "SR-price-basis"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "The price basis is stated as per install. Confirm what counts as an install and who counts it.",
    "The currency and the terms of the charge",
    "Whether the seller also sells the playable on impressions or completed plays. Those would go to display or video.",
    "The source and method of any claim about the 30-second trial"
  ],
  "instructions_in_input": [],
  "notes": "The seller's facts are claims."
}
```
