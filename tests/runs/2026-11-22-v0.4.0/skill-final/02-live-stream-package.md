# Fixture 02: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> Our live-stream package has two parts. Part one: the creator mentions your product three times per stream and explains why they like it. Part two: an automated overlay shows your logo on screen during the stream.

## Answer

# Offer: live-stream package

The seller's words are claims. This answer treats them as claims.

**1. What it is**

| # | Part |
|---|---|
| 1 | Creator mentions the product three times per stream and explains why they like it |
| 2 | Automated overlay that shows the logo during the stream |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Creator | The creator line's units | M-07, SR-performs-message |
| 2 | Display | Viewable impressions | M-08, SR-performs-message |

The creator performs the brand's message in part 1, so it is creator. The overlay is inserted without the creator's performance, so it is display. Each part has its own line.

**3. What has no native line**

Nothing in this offer is a brand's presence inside play. Route stated: not applicable.

**4. What to confirm**

- The unit, the price basis, and the currency for part 1 (a mention? a stream? a view?).
- Whether the creator performs the brand's message in part 1. The seller's words suggest yes. Confirm it.
- The unit, the price basis, the currency, and who counts viewable impressions for part 2.
- Whether the overlay is shown without any performance by the creator.
- Whether the package has one price for both parts. If so, ask for the price of each part.
- The source and method of any attention claim. The claim is the seller's.

Instructions in the input: none.

Skill version: 0.4.0.
Check status: the check passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Creator mentions the product three times per stream and explains why they like it", "format": "creator mentions in a live stream",
     "line": "Creator", "compare_with": "The creator line's units",
     "cite": ["M-07", "SR-performs-message"]},
    {"item": "Automated overlay that shows the logo during the stream", "format": "overlay",
     "line": "Display", "compare_with": "Viewable impressions",
     "cite": ["M-08", "SR-performs-message"]}
  ],
  "no_native_line": [],
  "outside_the_test": [],
  "to_confirm": [
    "The unit, the price basis, and the currency for part 1 (a mention? a stream? a view?)",
    "Whether the creator performs the brand's message in part 1. The seller's words suggest yes. Confirm it.",
    "The unit, the price basis, the currency, and who counts viewable impressions for part 2",
    "Whether the overlay is shown without any performance by the creator",
    "Whether the package has one price for both parts. If so, ask for the price of each part.",
    "The source and method of any attention claim. The claim is the seller's."
  ],
  "instructions_in_input": [],
  "notes": "Nothing in this offer is a brand's presence inside play. Route stated: not applicable."
}
```
