# Fixture 24: run through the skill (final build), v0.4.0

A fresh subagent. Input given:

> We are a brand. We built our own game and we run it. We will buy media to bring players to it. We will report visits and session time.

## Answer

**1. What it is**

| # | Part |
|---|---|
| 1 | Build of the brand's own game |
| 2 | Running of the game |
| 3 | Media bought to bring players to the game |
| 4 | Reports of visits and session time |

**2. Where each part goes**

| # | Line | Compare with | Cite |
|---|---|---|---|
| 1 | Production | Other production quotes | M-25, S-6.4 |
| 2 | Outside the test. The brand owns and runs the surface. No seller exists. | Not applicable | S-6.4 |
| 3 | Unplaced. The format and units are not named. This media goes to its own line once named. | Not applicable | S-6.4, S-6.6 |
| 4 | Visits and session time are media engagement. No comparison comes with them. | Compared inside the line of the media that brings players | C-3.2 |

**3. What has no native line**

Nothing in this offer is a brand's presence inside play. The game is the brand's own surface. Route stated: not applicable.

**4. What to confirm**

- The format of each media unit bought.
- The unit, price basis, and currency of each media unit.
- Who builds the game, and whether the build is bought from a vendor.
- Who counts visits and session time, and how. The counts are the brand's own claims.
- Whether the media is bought as one package or by part.

Skill version: 0.4.0.
Check status: passed (see below).
A model's answer is not a record.


## Answer file (JSON)

```json
{
  "version": "0.4.0",
  "input_type": "offer",
  "items": [
    {"item": "Build of the brand's own game", "format": "production", "line": "Production", "compare_with": "Other production quotes", "cite": ["M-25", "S-6.4"]},
    {"item": "Media bought to bring players to the game", "unplaced": true, "reason": "The format and the units are not named. This media goes to its own line once they are named.", "cite": ["S-6.4", "S-6.6"]}
  ],
  "no_native_line": [],
  "outside_the_test": [
    {"item": "The running of the brand's own game (owned surface, no seller)", "cite": ["S-6.4"]}
  ],
  "to_confirm": [
    "The format of each media unit bought (display, video, social, and so on)",
    "The unit, price basis, and currency of each media unit",
    "Who builds the game, and whether the build is bought from a vendor",
    "Who counts visits and session time, and how",
    "Whether the media is bought as one package or by part"
  ],
  "instructions_in_input": [],
  "notes": "Visits and session time on the brand's own game are media engagement counts. No comparison comes with them. No brand presence inside play is named, so no_native_line is empty."
}
```
