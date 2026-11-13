# Tengai Makyou II: Manji Maru — English patch

English translation of the Japanese Nintendo GameCube release, maintained by **binhlt0402 / retro-trans**.

**[Download v0.8.3](https://github.com/retro-trans/Tengai-Makyou-II/releases/tag/v0.8.3)** · [Changes](CHANGELOG.md) · [Testing notes](docs/TESTING.md)

The translation is in progress. This release packages tested internal build **0.1.2615**, including English password entry and the cumulative travel, battle, subtitle, dialogue and layout fixes since v0.8.2.

## Apply

1. Get the current [Retro Trans Tools Windows release](https://github.com/retro-trans/retro-trans-tools/releases/latest).
2. Open **Automatic** and **Refresh catalog**.
3. Select your original Japanese or published English image and choose **0.8.3 / Latest**.
4. Choose a new ISO or RVZ output and patch with verification enabled.
5. Cold boot the new image and load an in-game save.

Compatible RVZ input and output are supported on Windows. Approve extraction when prompted. The bundled converter requires Windows 10 1903 or later, x64, and the [Microsoft Visual C++ v14 x64 runtime](https://aka.ms/vc14/vc_redist.x64.exe).

Manual **Apply xdelta** uses `Tengai-Makyou-II-English-v0.8.3.xdelta` for the Japanese original, or `Tengai-Makyou-II-English-v0.8.2-to-v0.8.3.xdelta` for the exact public English v0.8.2 image.

| Image | Bytes | SHA-256 |
| --- | ---: | --- |
| Japanese GT2J18 revision 0 | 1,459,978,240 | `0f6840aebaa0cc5ed71ffbef6692037f6a3292d88ae8d338626f96b58bafe470` |
| English v0.8.2 upgrade source | 1,459,978,240 | `0e615a1a8b1bd6a4faf3ba5b68e890f15ab06d05049c4d774f712429e280b46d` |
| English v0.8.3 output | 1,459,978,240 | `777e765ac2e424a061896cb9bd757d40416ca41df1256c6ed878c383263a82ac` |

Public Automatic and Windows RVZ installation checks are recorded after publication.

## Included work


- **UI/navigation changes for English text:** roomier labels and descriptions, two-column lists, clearer action buttons, full character names and improved placement. Consistent action → user → item flows; Give / Exchange adds a recipient and destination slot, with clearer Back navigation and a persistent selected-user highlight.
- **Added Random Encounters option:** **Options → Random Encounters → None / Less / Default / More**, adjusting random walking encounters while retaining bosses and scripted battles.
- English dialogue, menus, item/equipment help, Scroll/Arts descriptions, battle messages, subtitles and field-use messages developed so far; further translation/proofreading remains.
- Normal-resolution Balsamiq Sans Regular, consistent **Arts** labels and eight English castle banners preserving the original frames/colors.
- **Direct Control / AI Control** clarifies the original game's existing Strategy control setting; we did not add party-control functionality.

## Testing and feedback

This is an in-progress translation. Japanese text may remain. The new password and reward code, UI allocations and compressed room changes have passed native checks, but natural access to these scenes in Dolphin and physical GameCube play remain untested. A full playthrough, transition timing under natural memory pressure and memory-card write/restart/reload have not been validated. Earlier opening-warning source uncertainty remains documented.

Hardware-sensitive changes since v0.8.2 include rewritten password editing/navigation/comparison, English answer records and a new input-buffer format inside the original 30-byte buffer. Password prompt backing requests 1,968 extra bytes and the reward refusal requests 2,880 extra bytes before allocator rounding. Travel menus can add up to 4,224 live bytes. Scoped display/parser branches and subtitle records change, and compressed MAP/header/FST metadata changes. These can affect heap pressure, fragmentation, timing and console execution. Native checks and patch verification do not establish real-hardware compatibility. Detailed evidence and limits appear in the testing notes.

Report issues with the patch version, location, steps and a screenshot through [Issues](https://github.com/retro-trans/Tengai-Makyou-II/issues). Read the [release notes](docs/releases/v0.8.3.md) and [testing details](docs/TESTING.md).

## Repository and credits

The repository provides release documentation, a packaging recipe and provenance. Building the package requires local original and translated ISO inputs.

Translation maintenance by **binhlt0402 / retro-trans**. English font is **Balsamiq Sans Regular**, under the included [SIL Open Font License](docs/BalsamiqSans-OFL.txt). Translation is LLM-assisted with accuracy, editorial and proofreading review. Patching uses [Retro Trans Tools](https://github.com/retro-trans/retro-trans-tools). Original assets belong to their respective rights holders. This is an unofficial fan translation.
