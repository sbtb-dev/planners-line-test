# Fixture 21: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> We propose a cross-media line priced on attention. It covers display, video, audio, and more, in any venue. Each accredited vendor measures attention with its own method. The price is per unit of attention.

## Answer

# Line test: attention-priced cross-media line

Input type: proposed line.

## Result: Not a boundary (failed step F-2)

The proposal states no route. It names no currency and no record. Cite F-2, N-9, N-6, N-3, C-3.1.

## Part 1. Items

| Item | Format | Result | Cite |
|---|---|---|---|
| Display priced per unit of attention | Display | Unplaced. The price basis differs from the display price basis. | N-9, N-2, F-1 |
| Video priced per unit of attention | Video | Unplaced. The price basis differs from the video price basis. | N-9, N-2, F-1 |
| Audio priced per unit of attention | Audio | Unplaced. The price basis differs from the audio price basis. | N-9, N-2, F-1 |
| "And more" | Not named | Unplaced. The formats are not named. | S-6.6, N-9 |

The price is counted on attention. This claims a new price basis. The first sentence of the rule does not place it. The second sentence needs a currency or a record. The seller carries the burden (N-6).

## Part 2. Why no route

- Each vendor uses its own method. Units from two vendors are not the same event counted the same way. The exchange check is not met (C-3.1).
- An accreditation is not a currency. No record is stated: no unit, no exposed population, no comparison, no verifier (N-3).

## Part 3. No native line, outside the test

None.

## Part 4. What to confirm

- Which formats "and more" covers.
- What one unit of attention is, and which event it counts.
- Whether a counter that is not the host counts it the same way for every seller.
- Whether 1,000 units from vendor A swap for 1,000 from vendor B.
- Whether a record is written before the buy.
- Who accredits the vendors, and whether the accreditor is not the seller.

Attention is a property of the delivery. It is compared within each line when it does not set the price (N-2).

Skill version: 0.4.0. The check passed. A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "proposed_line",
  "items": [
    {"item": "Display units priced per unit of attention", "format": "display", "unplaced": true,
     "reason": "The price basis differs from the display price basis. Attention is a new price basis, so the first sentence does not place it.", "cite": ["N-9", "N-2", "F-1"]},
    {"item": "Video units priced per unit of attention", "format": "video", "unplaced": true,
     "reason": "The price basis differs from the video price basis. Attention is a new price basis, so the first sentence does not place it.", "cite": ["N-9", "N-2", "F-1"]},
    {"item": "Audio units priced per unit of attention", "format": "audio", "unplaced": true,
     "reason": "The price basis differs from the audio price basis. Attention is a new price basis, so the first sentence does not place it.", "cite": ["N-9", "N-2", "F-1"]},
    {"item": "Other formats (\"and more\") priced per unit of attention", "unplaced": true,
     "reason": "The formats are not named. Information missing: which formats, and the price basis each has in its own line.", "cite": ["S-6.6", "N-9"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "result": {"value": "Not a boundary", "failed_step": "F-2", "cite": ["F-2", "N-9", "N-6", "N-3", "C-3.1"]},
  "to_confirm": [
    "Which formats \"and more\" covers",
    "What one unit of attention is, and which event it counts",
    "Whether a counter that is not the host counts it, and counts it the same way for every seller",
    "Whether any vendor method passes the exchange check: can 1,000 units from vendor A swap for 1,000 from vendor B",
    "Whether any record is written before the buy: unit, exposed population, comparison, verifier",
    "Who accredits the vendors, and whether the accreditor is not the seller"
  ],
  "instructions_in_input": [],
  "notes": "The proposal names no currency and no record. Each vendor uses its own method, so units from two vendors are not the same event counted the same way. Display, video, and audio keep their own lines. Attention is a property of the delivery and is compared within the line when it does not set the price (N-2)."
}
```
