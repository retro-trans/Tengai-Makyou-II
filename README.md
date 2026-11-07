# Tengai Makyou II: Manji Maru — English patch

An English translation patch for the Japanese Nintendo GameCube release of **Tengai Makyou II: Manji Maru**. Maintained by [binhlt0402](https://github.com/binhlt0402) at [retro-trans](https://github.com/retro-trans).

**[Download version 0.8.2](https://github.com/retro-trans/Tengai-Makyou-II/releases/tag/v0.8.2)** · [Changes](CHANGELOG.md) · [Testing and known limits](docs/TESTING.md)

This is an in-progress translation. Japanese text may remain, and a complete playthrough has not been verified. The version number is a release identifier, not a measured translation percentage.

## Apply with Retro Trans Tools

1. Get the current [Retro Trans Tools Windows release](https://github.com/retro-trans/retro-trans-tools/releases/latest).
2. Open **Automatic**, then **Refresh catalog**.
3. Browse to your original Japanese GameCube ISO or exact English v0.8.1 image. Select **0.8.2** or **Latest**.
4. Choose a new output ISO filename and click **Patch**. The app downloads the patch and verifies both the original and the completed ISO.
5. Cold boot the patched image and load an in-game save. Older save states can retain old code or text.

Use an image extracted from your own original disc. The patch applies to the exact original below, regardless of filename. Other editions and modified images are unsupported, except the exact English v0.8.1 image supported by the upgrade patch.

**RVZ:** [Retro Trans Tools 0.5.21 for Windows](https://github.com/retro-trans/retro-trans-tools/releases/tag/v0.5.21) supports RVZ directly in Automatic: approve ISO extraction, select the release, choose **RVZ** output or **Original format** for ISO, then patch. Your original RVZ and extracted ISO are retained. RVZ output is verified against the complete patched ISO. The converter is bundled. Requires Windows 10 1903 or later, x64, and the current [Microsoft Visual C++ v14 x64 runtime](https://aka.ms/vc14/vc_redist.x64.exe).

With older **0.5.20** installations, update or convert RVZ to ISO in Dolphin before patching; optionally convert the patched ISO back to RVZ afterward. Mac and Android downloads are unchanged; direct RVZ conversion is Windows-only. Renaming does not convert formats. The same patch and ISO hashes apply to both workflows; RVZ compression hashes are not disc identities. [RVZ test evidence](docs/RVZ-0.8.1.json).

| Image | Bytes | SHA-256 |
| --- | ---: | --- |
| Original Japanese ISO | 1,459,978,240 | `0f6840aebaa0cc5ed71ffbef6692037f6a3292d88ae8d338626f96b58bafe470` |
| English 0.8.2 ISO | 1,459,978,240 | `0e615a1a8b1bd6a4faf3ba5b68e890f15ab06d05049c4d774f712429e280b46d` |

For manual installation, download the `.xdelta` asset and use **Apply xdelta** with a matching input and a new output filename. Use `Tengai-Makyou-II-English-v0.8.2.xdelta` for the Japanese original, or `Tengai-Makyou-II-English-v0.8.1-to-v0.8.2.xdelta` for exact English v0.8.1 (SHA-256 `9cdaf01108079ae93912220350f4977466f895b49ab26786ffe3c7bf92db7eee`). `BUILD-MANIFEST.json`, `VALIDATION.json`, and `SHA256SUMS.txt` provide the exact identities and patch verification. No complete game image is distributed.

Automatic from the Japanese original and public English v0.8.0/v0.8.1, plus real RVZ input/output in the published Windows 0.5.21 app, passed complete output verification. [Automatic evidence](docs/AUTOMATIC-0.8.2.json) · [RVZ evidence](docs/RVZ-0.8.2.json).

## Included work

- UI and navigation improvements for English text: roomier labels and descriptions, two-column lists, clearer actions, and more consistent navigation than the original menus.
- New **Options → Random Encounters** setting: **None / Less / Default / More**. Adjust random walking encounters while retaining bosses and scripted battles.
- English dialogue, menus, item and equipment descriptions, scrolls, Arts, battle messages, and movie subtitles developed during the project; translation remains incomplete.
- Normal-resolution **Balsamiq Sans Regular** lettering and clearer menu labels. All Arts command categories use **Arts**.
- Item, scroll, and equipment flows select an action, a user, and an item. Give / Exchange then selects a recipient, including the giver, and a destination slot. The selected user's highlight remains visible while choosing an item.
- Clearer **Direct Control / AI Control** labels for the original game's existing manual/automatic Strategy setting; no new party-control functionality.
- Eight English castle title banners, preserving the original decorative frames and colors. Opening movie files remain original; movies have not been reencoded.
- Complete English field-use refusal messages such as “Ice Blade cannot be used outside battle.”

## Status and feedback

0.8.2 packages the verified internal checkpoint **0.1.2552**, without changing its game bytes. This release repairs dialogue spacing/wrapping and translates more item actions, no-effect results and postbattle rewards. Previous healing/opening fixes remain installed. Native checks and patch round trips pass; no new natural-scene Dolphin replay is claimed. **Physical GameCube operation, a full playthrough, natural transition timing, and actual memory-card write/restart/reload are unverified.** Read [testing notes](docs/TESTING.md) for memory and runtime risks.

Report problems through [Issues](https://github.com/retro-trans/Tengai-Makyou-II/issues). Include the patch version, location, steps, and a screenshot where possible. Do not upload game images or original game files.

## Repository and credits

This repository contains release documentation, the public packaging recipe, and binary provenance. It is not a complete clean-room rebuild of the translation from source. The release recipe requires a local original ISO and the verified translated checkpoint; neither is included.

Translation maintenance and release: **binhlt0402 / retro-trans**. English font: **Balsamiq Sans Regular**, used under the [SIL Open Font License](docs/BalsamiqSans-OFL.txt). Automatic patching and verified release packaging: [Retro Trans Tools](https://github.com/retro-trans/retro-trans-tools). Original game, characters, artwork, and media belong to their respective rights holders. This is an unofficial fan translation.
