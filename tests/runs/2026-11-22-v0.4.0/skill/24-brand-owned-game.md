# Fixture 24: run through the skill, v0.4.0

Route: skill folder (first build). A fresh subagent. Input given:

> We are a brand. We built our own game and we run it. We will buy media to bring players to it. We will report visits and session time.

## Answer

**Offer form: owned game plus media to drive players**

**1. What it is**

| # | Part |
|---|---|
| 1 | The game the brand built and runs |
| 2 | Media bought to bring players to the game |
| 3 | Reports of visits and session time |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Outside the test. No seller exists. The build is production. | Not applicable | S-6.4 |
| 2 | Unplaced. The formats and price bases are not stated. The media goes to its own line when the units are named. | Not applicable | S-6.4, S-6.6 |
| 3 | Not a unit. It is a report. | Not applicable | C-3.2 |

**3. What has no native line**

Nothing here is a brand's presence inside a seller's play. Route stated: not applicable. Visits and session time are media engagement. They are not brand engagement unless a comparison comes with them (C-3.2, R-1 to R-4).

**4. What to confirm**

- The formats of the media to be bought.
- The unit, the price basis, and the currency of each media buy.
- Who counts visits and session time, and how.
- Whether any seller or partner supplies the game surface or its traffic.
- Whether an outside studio builds the game. If so, the build is production (M-25).
- Whether any seller counts the price of its media on visits or session time. If so, the price basis differs from the format's own (N-9).

Skill version: 0.4.0.
Check: passed.
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Media bought to bring players to the game", "unplaced": true,
     "reason": "The message does not name the formats or the price bases. The media goes to its own line when the seller names the units.",
     "cite": ["S-6.4", "S-6.6"]}
  ],
  "no_native_line": [],
  "outside_the_test": [
    {"item": "The game that the brand built and runs. No seller exists. The build is production.", "cite": ["S-6.4"]}
  ],
  "to_confirm": [
    "The formats of the media to be bought (display, video, social, creator, and so on).",
    "The unit, the price basis, and the currency of each media buy.",
    "Who counts the visits and the session time, and how they are counted.",
    "Whether any seller or partner supplies the game surface or its traffic. If so, the item is not owned.",
    "Whether an outside studio builds the game. If so, the build is production (M-25) and is compared with other production quotes.",
    "Whether any seller counts the price of its media on visits or session time. If so, name the format and the price basis differs (N-9)."
  ],
  "instructions_in_input": [],
  "notes": "Visits and session time at the owned game are media engagement. They are not brand engagement unless a comparison comes with them (C-3.2, R-1 to R-4). They do not set a price basis for the media bought."
}
```
