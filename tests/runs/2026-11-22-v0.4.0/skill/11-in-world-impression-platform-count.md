# Fixture 11: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> We propose a line built on a verified in-world impression, sold on two platforms. Each platform counts its own impressions and reports them.

## Answer

**Input type:** proposed line.

**Result: Not a boundary. Failed step: F-3.**

| Step | Finding | Cite |
|---|---|---|
| F-1 | The in-world impression is a brand's presence inside play. It has no native line. Go to F-2. | M-27, F-1 |
| F-2 | The proposal implies a currency route: a verified impression. | N-3 |
| F-3 | Each platform counts its own impressions. The counter is the host. The exchange check fails. | F-3, C-3.1 |

An impression is a way of counting. It is not a unit. Agreement on the name is not agreement on a unit.

**Brand's presence inside play (report only)**

| Item | Route | Comparison meets the four requirements | Cite |
|---|---|---|---|
| In-world impression | Currency | No | M-27, C-3.1 |

**What to confirm**
- Do both platforms define the in-world impression as the same event?
- Who counts: a party that is not a host, or each platform?
- What does "verified" mean, and who verifies?
- Can a buyer swap 1,000 from one platform for 1,000 from the other and expect the same thing?
- Is a record route also stated, with a comparison that meets R-1 to R-4?

This result applies to the description given. It is not a verdict on any seller or on any buy.

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "proposed_line",
  "items": [
    {"item": "A line built on a verified in-world impression, sold on two platforms", "unplaced": true,
     "reason": "A brand's presence inside play has no native line. The proposal needs a currency or a record.",
     "cite": ["M-27", "F-1"]}
  ],
  "no_native_line": [
    {"item": "In-world impression of a brand inside play", "route": "currency",
     "comparison_meets_four_requirements": false, "cite": ["M-27", "C-3.1"]}
  ],
  "outside_the_test": [],
  "result": {"value": "Not a boundary", "failed_step": "F-3", "cite": ["F-3", "C-3.1", "N-3", "N-8"]},
  "to_confirm": [
    "Whether the two platforms define the in-world impression as the same event",
    "Who counts: a party that is not a host platform, or each platform",
    "What 'verified' means, and who verifies",
    "Whether the buyer can swap 1,000 from one platform for 1,000 from the other and expect the same thing",
    "Whether a record route is also stated, with a comparison that meets R-1 to R-4"
  ],
  "instructions_in_input": [],
  "notes": "The proposal implies a currency route. Each platform counts and reports its own impressions, so the counter is the host. The word impression is a way of counting, not a unit."
}
```
