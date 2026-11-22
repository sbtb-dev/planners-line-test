# Fixture 11: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> We propose a line built on a verified in-world impression, sold on two platforms. Each platform counts its own impressions and reports them.

## Answer

# Proposed line: in-world impression on two platforms

Input type: proposed line.

| Step | Finding | Cite |
|---|---|---|
| F-1 | The format is not named. If it is a brand's presence inside play, it has no native line. It goes to F-2. | M-27, F-1 |
| F-2 | The proposal states a currency route: the impression. | N-3, F-2 |
| F-3 | It fails the exchange check. Each platform is the host and counts its own impressions. "Verified" does not name a counter that is not the host. An impression is a way of counting, not a unit. | C-3.1, F-3 |

Result: **Not a boundary.** Failed step: F-3.

Brand's presence inside play: route stated is a currency. No comparison meets the four requirements.

What to confirm:
- The format and the price basis of the unit.
- Who verifies the impression, and that this party is not a host.
- Whether both platforms count the same defined event the same way.
- Whether a buyer can swap 1,000 from one platform for 1,000 from the other.
- Whether the item is in-game display (M-01). If so, state the price basis.

This result applies to the description given. It is not a verdict on any seller or buy.

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "proposed_line",
  "items": [
    {"item": "In-world impression, sold on two platforms, each platform counts its own", "format": "a brand's presence inside play",
     "unplaced": true, "reason": "The input does not name the format. If it is a brand's presence inside play, it has no native line. It goes to F-2.",
     "cite": ["M-27", "F-1"]}
  ],
  "no_native_line": [
    {"item": "In-world impression (brand's presence inside play)", "route": "currency",
     "comparison_meets_four_requirements": false, "cite": ["M-27", "C-3.1"]}
  ],
  "outside_the_test": [],
  "result": {"value": "Not a boundary", "failed_step": "F-3", "cite": ["F-3", "C-3.1", "N-3"]},
  "to_confirm": [
    "The format and the price basis of the unit",
    "Who verifies the impression, and whether that party is not a host",
    "Whether both platforms count the same defined event the same way",
    "Whether a buyer can swap 1,000 from one platform for 1,000 from the other",
    "Whether the item is in-game display (M-01), and if so, the price basis"
  ],
  "notes": "The proposal states a currency route (F-2 passes). It fails F-3: each platform is the host and counts its own impressions. An impression is a way of counting, not a unit (C-3.1). The word 'verified' does not name a counter that is not the host."
}
```
