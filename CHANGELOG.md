# Changelog

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
