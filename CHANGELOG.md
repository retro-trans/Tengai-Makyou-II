# Changelog

## 0.8.2 — 2026-11-07

- Live Automatic from original/English0.8.0/English0.8.1 and unchanged published Windows0.5.21 actual RVZ input/output pass complete hashes and source preservation. Scoped catalog refresh succeeds; old assets/identities retained.

- Remove wide spaces around colored names and rewrap the reported festival, inn, castle and village conversations, including Hermit Kasaiwa's castle explanation. Preserve wording, names, colors and original page turns.
- Translate the shared field item-use action and actor/recipient names, including the Kanro Pill mouth action and nested healing result. Translate related no-effect actions, the Ear Pick of Love action, grip-only and smelly-hands outcomes.
- Translate one-, two- and three-item postbattle reward messages with English item/equipment names. Resize a smaller reused battle result window before parsing the longer English text.
- Package exact tested internal0.1.2552; retain the healing freeze fix, opening subtitles and earlier improvements. Original movies/audio/font are unchanged. Provide original-source and exact English0.8.1 upgrade patches for Automatic and Apply xdelta.
- Hardware-sensitive: +1576 immutable executable bytes within the existing reservation (160 spare); reused battle-result backing can add2952 live bytes. MAP compression/FST offsets changed without decoded-room growth. Native tests are not physical-hardware validation; no new Dolphin/natural-scene/Card/full-playthrough claim. Detailed evidence and limits in docs/TESTING.md.

## 0.8.1 — 2026-11-07

- Live Automatic original/English 0.8.0 routes and the unchanged public Windows 0.5.21 EXE with actual RVZ input/output pass complete hashes; historical catalog identities and old release assets retained.

- Fix the native field Item nested-English healing-message freeze reported with Buckwheat Dumpling. Reserve 64x3 in the real producer; HP/RNG/item consumption and visual frame unchanged.72 native cases/12 repeated cycles, Store/reopen and captured pressure checks pass; exact reported lakeside save not replayed.
- Add three missing opening cues before Mother's Manjimaru line. Keep all 658 existing cues and original movie/audio bytes.661 records/2360 native boundary checks/45 additional cases and muted actual opening/return pass.
- Package exact internal 0.1.2518 without further game-byte changes, with original-source and English 0.8.0 upgrade patches for Retro Trans Tools Automatic/Apply xdelta, including Windows 0.5.21 RVZ conversion.
- Hardware-sensitive: +2952 live Item-message bytes; +232 immutable DOL bytes within existing reservation. Scene 1060704, general heap 4718592, private padding 1736; no physical-hardware/Card validation. Warning-ending source uncertainty and inherited risks are explicit in testing notes.

## 0.8.0 published RVZ tools link — 2026-11-06

- Link the published Retro Trans Tools 0.5.21 Windows release and update RVZ installation instructions, requirements and older-client guidance. Retain ISO-based patch identities and verification.
- Documentation only; no game or release-asset bytes changed. Conversion checks do not establish gameplay or physical-console compatibility.

## 0.8.0 RVZ installation notes — 2026-11-06

- Document direct RVZ input and verified RVZ/ISO output in the local Retro Trans Tools 0.5.21 Windows test build. Explain extraction consent, retained original/extracted ISO, and complete ISO verification; publish the existing conversion-test evidence.
- Distinguish the unpublished test build from public 0.5.20, which still needs RVZ-to-ISO conversion in Dolphin before patching. ISO hashes identify the disc independently of RVZ compression settings.
- Documentation only; release assets, catalog identities and game bytes are unchanged. Conversion verification does not establish gameplay or physical GameCube compatibility.

## 0.8.0 party-control wording correction — 2026-11-06

- Clarify that manual/automatic party control already exists in the original game. Our change only improves the English Direct Control / AI Control labels and text layout; no party-control logic was added. Correct the release introduction, feature list and README.
- Documentation only; published patch and catalog identities remain unchanged.

## 0.8.0 release-note revision — 2026-11-06

- Reorganize the public release notes using SRW-Z's release-note structure: Apply, What's Included, validation, downloads/source, and acknowledgements.
- Highlight the added English-focused UI/navigation improvements and Options → Random Encounters (None / Less / Default / More), alongside clearer labels for existing manual/automatic party control. Add the same two features to the repository README.
- Documentation only. Published patch bytes, manifests, checksums, catalog identities and game behavior remain unchanged.

## 0.8.0 — 2026-11-06

First public release in this repository, packaging internal test build 0.1.2503 (delivery checkpoint 0.1.2506). Game bytes are unchanged from that checkpoint.

- Publish a full patch from the exact original Japanese GameCube ISO, with a Retro Trans Tools Automatic manifest, central game registration, checksums, and verified round-trip report.
- Retain the English translation, normal Balsamiq font, eight English castle banners, and original opening movies.
- Retain unified Arts labels, Direct Control / AI Control, clearer Scroll action labels, selected-user highlighting, corrected Back / Give / Exchange navigation, raised shop metadata, and full shop character names.
- Battle Item help uses the reviewed English description bank. Field-use refusal messages resolve the full English Scroll or Art name; all 69 Scroll and 32 named Art variants passed native checks.
- Live published 0.5.20 Automatic backend passed catalog refresh, all three routes, empty-cache download, exact full-ISO output, already-current recognition and overwrite refusal. Existing catalog identities stayed unchanged; no GUI or gameplay validation claimed.
- This public packaging step changes no runtime code, asset, memory reservation, or game behavior.

Hardware-sensitive changes inherited from the internal builds include executable hooks and expansion, proportional font rendering, dynamic text buffers, menu state changes, subtitle timing, and compressed castle-title image replacements. The latest internal change appended 652 executable bytes and reserved 2,560 more bytes, reducing scene capacity to 1,060,704 bytes. Native ownership/ABI/guard checks and captured allocation-pressure models passed; real GPU/cache behavior, controller timing, physical-console execution, natural scene transitions and actual memory-card write/restart/reload remain unverified. See [test notes](docs/TESTING.md).
