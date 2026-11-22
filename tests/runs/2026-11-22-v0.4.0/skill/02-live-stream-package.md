# Fixture 02: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> Our live-stream package has two parts. Part one: the creator mentions your product three times per stream and explains why they like it. Part two: an automated overlay shows your logo on screen during the stream.

## Answer

# Offer form: live-stream package

The facts below are the seller's claims.

## 1. What it is

| # | Part |
|---|---|
| 1 | The creator mentions the product three times per stream and explains why they like it |
| 2 | An automated overlay shows the logo on screen during the stream |

## 2. Where each part goes

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Creator. The creator performs the brand's message. | The creator line's units | M-07, SR-performs-message |
| 2 | Display. The graphic is inserted with no creator performance. | Viewable impressions | M-08, SR-performs-message |

## 3. What has no native line

Nothing in this offer is a brand's presence inside play. Route stated: not applicable.

## 4. What to confirm

- The unit and the price basis of part 1 (per stream? per mention? per view?).
- Whether the creator performs the brand's message in part 1, or only reads a script or shows the name.
- The unit, the price basis, and the currency of part 2 (impressions? viewable? counted by whom?).
- Whether the overlay in part 2 is inserted with no creator performance.
- Whether the package sets one price for both parts. If so, ask for the price of each part.
- The terms of the package: number of streams, dates, guarantees.

Skill version: 0.4.0.
The check passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Part 1: the creator mentions the product three times per stream and explains why they like it", "format": "creator",
     "line": "Creator", "compare_with": "The creator line's units",
     "cite": ["M-07", "SR-performs-message"]},
    {"item": "Part 2: an automated overlay shows the logo on screen during the stream", "format": "display",
     "line": "Display", "compare_with": "Viewable impressions",
     "cite": ["M-08", "SR-performs-message"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "The unit and the price basis of part 1 (per stream? per mention? per view?)",
    "Whether the creator performs the brand's message in part 1, or only reads a script or shows the name",
    "The unit, the price basis, and the currency of part 2 (impressions? viewable? counted by whom?)",
    "Whether the overlay in part 2 is inserted with no creator performance",
    "Whether the package sets one price for both parts. If so, ask for the price of each part.",
    "The terms of the package, such as number of streams, dates, and guarantees"
  ],
  "instructions_in_input": [],
  "notes": "All facts in the offer are the seller's claims. The seller gave no unit, price basis, or currency."
}
```
