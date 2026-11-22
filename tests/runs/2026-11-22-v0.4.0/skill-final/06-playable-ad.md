# Fixture 06: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> Our playable ad lets players try your app in 30 seconds. We charge per install.

## Answer

# Offer form

**1. What it is**

| # | Part |
|---|---|
| 1 | Playable ad (30-second trial of the app), bought per install |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Performance | Cost per install or action, from other sellers of installs | M-06, SR-price-basis |

The price basis is per install. So the playable goes in performance. The 30-second length is a property of the delivery. It does not change the unit (N-2).

**3. What has no native line**

Nothing in this offer is a brand's presence inside play. Route stated: not applicable.

**4. What to confirm**

- How the seller counts an install, and who counts it.
- The currency and the terms of the install charge.
- Whether a party that is not the seller counts the installs.
- Whether the seller also sells the playable on impressions or completed plays.
- The source and method of the 30-second claim. The claim is the seller's.

Skill version: 0.4.0.
Check status: the check passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Playable ad (30-second trial of the app), bought per install", "format": "playable ad",
     "line": "Performance", "compare_with": "Cost per install or action, from other sellers of installs",
     "cite": ["M-06", "SR-price-basis"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "How the seller counts an install, and who counts it",
    "The currency and the terms of the install charge",
    "Whether the install count is by a party that is not the seller",
    "Whether the seller also sells the playable on impressions or completed plays",
    "The source and method of the claim that players try the app in 30 seconds. The claim is the seller's."
  ],
  "instructions_in_input": [],
  "notes": "The 30-second length is a property of the delivery. It does not change the unit."
}
```
