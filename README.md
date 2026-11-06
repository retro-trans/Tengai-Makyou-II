# Tengai Makyou II: Manji Maru — English patch

An English translation patch for the Japanese Nintendo GameCube release of **Tengai Makyou II: Manji Maru**. Maintained by [binhlt0402](https://github.com/binhlt0402) at [retro-trans](https://github.com/retro-trans).

**[Download version 0.8.0](https://github.com/retro-trans/Tengai-Makyou-II/releases/tag/v0.8.0)** · [Changes](CHANGELOG.md) · [Testing and known limits](docs/TESTING.md)

This is an in-progress translation. Japanese text may remain, and a complete playthrough has not been verified. The version number is a release identifier, not a measured translation percentage.

## Apply with Retro Trans Tools

1. Get the current [Retro Trans Tools Windows release](https://github.com/retro-trans/retro-trans-tools/releases/latest).
2. Open **Automatic**, then **Refresh catalog**.
3. Browse to your original Japanese GameCube ISO. Select **0.8.0** or **Latest**.
4. Choose a new output ISO filename and click **Patch**. The app downloads the patch and verifies both the original and the completed ISO.
5. Cold boot the patched image and load an in-game save. Older save states can retain old code or text.

Use an ISO extracted from your own original disc. RVZ files must first be converted back to an unmodified ISO; renaming an RVZ does not convert it. The patch applies to the exact original below, regardless of filename. Other editions and already modified images are unsupported.

| Image | Bytes | SHA-256 |
| --- | ---: | --- |
| Original Japanese ISO | 1,459,978,240 | `0f6840aebaa0cc5ed71ffbef6692037f6a3292d88ae8d338626f96b58bafe470` |
| English 0.8.0 ISO | 1,459,978,240 | `39a881525956fbf977b25c691c7e94cef57573bb1f927d5628c37295f898891e` |

For manual installation, download the `.xdelta` asset and use **Apply xdelta** with the same original ISO and a new output filename. `BUILD-MANIFEST.json`, `VALIDATION.json`, and `SHA256SUMS.txt` provide the exact identities and patch verification. No complete game image is distributed.

## Included work

- UI and navigation improvements for English text: roomier labels and descriptions, two-column lists, clearer actions, and more consistent navigation than the original menus.
- New **Options → Random Encounters** setting: **None / Less / Default / More**. Adjust random walking encounters while retaining bosses and scripted battles.
- English dialogue, menus, item and equipment descriptions, scrolls, Arts, battle messages, and movie subtitles developed during the project; translation remains incomplete.
- Normal-resolution **Balsamiq Sans Regular** lettering and clearer menu labels. All Arts command categories use **Arts**.
- Item, scroll, and equipment flows select an action, a user, and an item. Give / Exchange then selects a recipient, including the giver, and a destination slot. The selected user's highlight remains visible while choosing an item.
- **Direct Control / AI Control** in Strategy uses the game's existing control policy.
- Eight English castle title banners, preserving the original decorative frames and colors. Opening movie files remain original; movies have not been reencoded.
- Complete English field-use refusal messages such as “Ice Blade cannot be used outside battle.”

## Status and feedback

0.8.0 packages the verified internal checkpoint **0.1.2503**, without changing its game bytes. Automated native checks and patch round trips have passed. **Physical GameCube operation, a full playthrough, natural transition timing, and actual memory-card write/restart/reload are unverified.** Read [testing notes](docs/TESTING.md) for memory and runtime risks.

Report problems through [Issues](https://github.com/retro-trans/Tengai-Makyou-II/issues). Include the patch version, location, steps, and a screenshot where possible. Do not upload game images or original game files.

## Repository and credits

This repository contains release documentation, the public packaging recipe, and binary provenance. It is not a complete clean-room rebuild of the translation from source. The release recipe requires a local original ISO and the verified translated checkpoint; neither is included.

Translation maintenance and release: **binhlt0402 / retro-trans**. English font: **Balsamiq Sans Regular**, used under the [SIL Open Font License](docs/BalsamiqSans-OFL.txt). Automatic patching and verified release packaging: [Retro Trans Tools](https://github.com/retro-trans/retro-trans-tools). Original game, characters, artwork, and media belong to their respective rights holders. This is an unofficial fan translation.
