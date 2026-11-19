# Tests

These fixtures check that the [prompt](../prompt/PROMPT.md) gives the expected result. Each file in [cases/](cases/) has an input and an expected result. The inputs are generic. They name no company.

## How to run

1. Build the prompt: `scripts/build-prompt.sh`.
2. Open two or three different models.
3. Paste the contents of `prompt/PROMPT.md` into each model.
4. For each fixture, paste the "Input" section after the prompt.
5. Compare each model's answer with the "Expected result."

## How to read the results

- An answer matches when it reaches the same lines, or the same one of the three results, and cites a mapping row or a reading note.
- The wording can differ.
- If the models disagree on a case, the mapping may need a row or a second rule. File a correction (see [CONTRIBUTING.md](../CONTRIBUTING.md)).
- A model's answer is not a record. Results vary by model.

## Cases

| File | Type |
|---|---|
| [01](cases/01-retailer-gaming-hub.md) | Offer |
| [02](cases/02-live-stream-package.md) | Offer |
| [03](cases/03-immersive-ad-formats.md) | Offer |
| [04](cases/04-branded-world.md) | Offer |
| [05](cases/05-esports-sponsorship.md) | Offer |
| [06](cases/06-playable-ad.md) | Offer |
| [07](cases/07-omnichannel-gaming-campaign.md) | Offer |
| [08](cases/08-gaming-line-in-every-plan.md) | Proposed line |
| [09](cases/09-mobile-gaming-line.md) | Proposed line |
| [10](cases/10-in-game-branded-content.md) | Proposed line |
| [11](cases/11-in-world-impression-platform-count.md) | Proposed line |
| [12](cases/12-in-world-impression-independent-counter.md) | Proposed line |
| [13](cases/13-instruction-in-offer.md) | Offer |
