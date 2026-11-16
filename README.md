# Tengai Makyou II: Manji Maru — English patch

Maintained by **binhlt0402 / retro-trans**.

**[Download v0.8.4](https://github.com/retro-trans/Tengai-Makyou-II/releases/tag/v0.8.4)** · [Changes](CHANGELOG.md) · [Testing notes](docs/TESTING.md)

English translation for the Japanese Nintendo GameCube release. Translation remains in progress.

## Apply

Use the current [Retro Trans Tools Windows release](https://github.com/retro-trans/retro-trans-tools/releases/latest). Open **Automatic → Refresh catalog**, select your original Japanese or published English image, choose **0.8.4 / Latest**, choose a new output and patch. Automatic chooses the matching verified full or upgrade route.

| Your source image | Manual Apply xdelta patch |
| --- | --- |
| Original Japanese GameCube ISO, GT2J18 revision 0 | `Tengai-Makyou-II-English-v0.8.4.xdelta` |
| Exact published English v0.8.3 ISO | `Tengai-Makyou-II-English-v0.8.3-to-v0.8.4.xdelta` |

Compatible **RVZ input and output** are supported on Windows. Approve ISO extraction, then choose RVZ output or Original format for ISO output. Recognition uses the expanded ISO identity. The converter is bundled. Windows 10 1903 or later, x64, and the [Microsoft Visual C++ v14 x64 runtime](https://aka.ms/vc14/vc_redist.x64.exe) are required.

Keep verification enabled. The upgrade requires the exact public v0.8.3 image. **Cold boot the new image and load an in-game save.** Emulator states can restore old code and text.

Live **Retro Trans Tools 0.5.23 Automatic** passed from the Japanese original and public English **v0.8.0, v0.8.1, v0.8.2 and v0.8.3**. Fresh catalog and patch downloads produced the exact v0.8.4 ISO, recognized it as current, preserved all inputs and rejected overwriting existing files. Latest, explicit version and Next version only routes were checked. [Automatic evidence](https://github.com/retro-trans/Tengai-Makyou-II/blob/main/docs/AUTOMATIC-0.8.4.json).

The published **Windows v0.5.23 app** passed original **RVZ → Automatic → RVZ** with a fresh patch cache and live downloads. Independent extraction reproduced the complete v0.8.4 ISO hash. Installation was verified; game playback and physical hardware were not exercised. [RVZ evidence](https://github.com/retro-trans/Tengai-Makyou-II/blob/main/docs/RVZ-0.8.4.json) · [Catalog refresh](https://github.com/retro-trans/retro-trans-tools/actions/runs/43857563169).

## What's included


- **UI/navigation changes for English text:** roomier labels and descriptions, two-column lists, clearer action buttons, full character names and improved placement. Consistent action → user → item flows; Give / Exchange adds a recipient and destination slot, with clearer Back navigation and a persistent selected-user highlight.
- **Added Random Encounters option:** **Options → Random Encounters → None / Less / Default / More**, adjusting random walking encounters while retaining bosses and scripted battles.
- English dialogue, menus, item/equipment help, Scroll/Arts descriptions, battle messages, subtitles and field-use messages developed so far; further translation/proofreading remains.
- Normal-resolution Balsamiq Sans Regular, consistent **Arts** labels and eight English castle banners preserving the original frames/colors.
- **Direct Control / AI Control** clarifies the original game's existing Strategy control setting; we did not add party-control functionality.

## Changes in v0.8.4

- Fix Yamainu Helmet and all 13 equipment names in the later name bank, including treasure notices, battle rewards and equipped labels.
- Translate all 17 province destinations in both display tables and widen all three province-picker paths. Correct related item-use and self/recipient messages.
- Translate equipment curse discovery/removal notices and the missing titles across all 14 shop entries.
- Complete the field-item message audit: translate the missed use, reaction, novelty and fallback messages, preserving original item effects and full approved names.
- Translate the remaining Scroll restriction/status warnings, Lottery actions and prizes, merchant apology, Kyoto and province-qualified Ninja Village save labels.
- Separate all 16 complete newspaper headlines and prices, improve selection geometry and translate its money display.
- Translate both engraved-ticket messages and all three information-broker offers; check the related buy/sell tips and payment/refusal variants.
- Fix scrambled Commodity Exchange names and headings, all current/high/low price cells, skipped prompts, recipient names/free-slot counts and overlapping Japanese/English money displays. Preserve native prices, capacities and transactions.
- Use public release versions for new builds and current documentation. Existing evidence retains its historical filenames for traceability.

## Testing and feedback

Translation is still in progress; Japanese text and errors may remain. The updated game code and larger UI buffers passed silent native checks, but no new Dolphin playthrough, natural scene-transition test, physical GameCube test or real memory-card write/restart/reload test occurred. Installation verification does not establish game or real-hardware compatibility.

Hardware-sensitive changes since v0.8.3 include equipment/name lookup branches, item-message expansion and constructor hooks, wider province/Lottery/newspaper/Commodity buffers, new display pointers and compressed room/header/FST updates. The new newspaper backing alone adds 27,672 live bytes; Commodity table backing adds 8,208 bytes, parent prompt backing can add 5,760 bytes, and each updated Sell child adds 2,688 bytes. The final scene space is 1,044,320 bytes. Captured allocation replay with the complete-model budget and 256 KiB reserve leaves 351,232 bytes at peak, above the documented 300,000 test margin but below the older 400,000 margin. Full gameplay peaks, fragmentation, timing and console execution remain unverified. Detailed evidence and limits are in the testing notes.

Read the [release notes](docs/releases/v0.8.4.md) and [testing details](docs/TESTING.md). Report problems with the version, location, steps and a screenshot through [Issues](https://github.com/retro-trans/Tengai-Makyou-II/issues).

## Disc identities

All expanded disc images have **1,459,978,240 bytes**.

| Image | SHA-256 |
| --- | --- |
| Original Japanese ISO | `0f6840aebaa0cc5ed71ffbef6692037f6a3292d88ae8d338626f96b58bafe470` |
| English v0.8.3 upgrade source | `777e765ac2e424a061896cb9bd757d40416ca41df1256c6ed878c383263a82ac` |
| English v0.8.4 ISO | `24631312ba51f4e901b527e2dc83821d11a24d6744c3e3ad9e508ffefe23d2f7` |

## Repository and credits

Translation maintenance by **binhlt0402 / retro-trans**. Translation is LLM-assisted with a shared glossary, accuracy review, editorial review and proofreading. English font is **Balsamiq Sans Regular**, under the included SIL Open Font License. Patching uses **Retro Trans Tools**. Original game, characters, artwork and media belong to their respective rights holders. This is an unofficial fan translation.

Report remaining Japanese, errors or freezes through [Issues](https://github.com/retro-trans/Tengai-Makyou-II/issues), including version, location, steps and a screenshot.
