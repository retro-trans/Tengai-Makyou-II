# Changelog

## 0.8.0 release-note revision — 2026-11-06

- Reorganize the public release notes using SRW-Z's release-note structure: Apply, What's Included, validation, downloads/source, and acknowledgements.
- Highlight the added English-focused UI/navigation improvements and Options → Random Encounters (None / Less / Default / More), alongside Direct Control. Add the same two features to the repository README.
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
