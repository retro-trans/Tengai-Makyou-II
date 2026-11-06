# Testing and limitations — 0.8.0

## Release identity

Public 0.8.0 is byte-identical to internal 0.1.2503, verified at delivery checkpoint 0.1.2506. The original and output SHA-256 identities are pinned in `release/provenance.json`. No ISO is published. The shared Retro Trans Tools release builder encodes and decodes the full patch, checks every byte of the result, rehashes both inputs, and produces the canonical manifest, validation report and checksums. Live Automatic recognition, routing, download and application results are recorded separately after publication.

## Existing native evidence

- 101 named Scroll/Art refusal constructors, full runtime names, asynchronous reveals, text bounds, source controls, ABI/stack/heap guards and native cleanup passed. The actual invalid-use callbacks for Ice Blade, Blossom Storm and Benimaru Slash produced English without changing inventory, HP or MP. Three concurrent contexts retained independent strings after stack overwrite. 1,500 retained Item/owner/gear/Scroll expansion cases passed. Natural controller dismissal of these refusal bubbles was not tested.
- Legal Young Grass field use still opens the original target chooser; Back preserves inventory, HP and MP. This does not verify every allowed effect.
- Earlier checks covered 528 Battle Item hover cases; all 104 reviewed descriptions; Arts command matrices; Strategy native policy gates/import/export; Back/re-entry and same/cross-character empty/occupied transfers; persistent selected-user highlights; and actual General Store construction, long highlights/scrolling, Buy/Sell confirmations, funds updates, Back/Exit and reopening.
- Eight castle titles passed native decode/copy/free and image checks, preserving original packed lengths, palette/alpha, texture dimensions and animation. Movie subtitle timing changes do not reencode the movies. Every THP opening movie remained identical to the original disc.
- Latest native six-partition/graphics/HSD initialization and 1,151 captured scene allocation sizes plus a 201,376-byte model budget, 262,144-byte reserve and the former 1,024-byte failed allocation passed. Scene peak free space was 367,616 bytes. Captured general/save allocation replays, including an extra 9,216-byte message allocation and a 57,600-byte save-window request, passed with 689,984 bytes free.
- Latest delivery verified all 1,393 assets, FST and bytes outside the changed executable against the preceding checkpoint. Public packaging does not modify those verified bytes.

These checks execute native routines offline with GPU, audio and services modeled. They are not emulator playthroughs or real-hardware validation. No audio or desktop testing is needed for patch packaging.

## Hardware-sensitive changes and risks

The translation inherits executable hooks, relocated English text, proportional text rendering, larger native glyph backing, menu state/control changes, subtitles, and castle-title image payload changes. Risks include caller/source assumptions, dynamic name state, per-context buffer indexing and lifetime, native allocation ownership, loader/cache behavior, scene pressure, image codec behavior, and real rendering/controller timing.

The final internal change adds 652 private executable bytes. Static reservation ends at `0x80389000`, up 2,560 bytes from the preceding checkpoint; scene capacity is 1,060,704 bytes, private spare capacity 1,968 bytes, and the fixed general heap remains 4,718,592 bytes. Captured pressure checks pass; these are size-pressure models, not actual transitions or card operations.

HD fonts are deferred. Historical overworld-transition scene-heap failures, a separate save-window general-heap failure, and a shop constructor capacity failure were diagnosed earlier. Relevant regression evidence remains in the development workspace; native replay successes do not prove all natural gameplay paths safe. Cold boot and load an in-game save rather than using an old save state.

## Remaining validation

Full-game translation and a complete playthrough are not finished. Physical-console operation, real GPU/cache behavior, natural full-game transitions, actual save/write/restart/reload and long-session stability remain unverified. Public version 0.8.0 does not mean measured 80% coverage.
