# Testing and limitations — 0.8.1

Public0.8.1 is byte-identical to tested internal 0.1.2518 / checkpoint 0.1.2524. Original-source and exact English 0.8.0 upgrade patches use registered GameCube disc GT2J18. The shared release builder verifies complete outputs and unchanged inputs. No full game image is published. Live Automatic evidence is added after publication.

Tengai Makyou II — English test0.1.2518 / checkpoint 0.1.2524 — 2026-11-07

Opening subtitle repair
Add three missing movie11/11_haha cues before Mother's existing Manjimaru... subtitle:
21.70seconds: Mom! Can I have some more?
24.56seconds: Is Manjimaru here?!
26.36seconds: He won't get away with it this time!
The child asks for another serving, then an unidentified angry caller interrupts from outside. Earlier ASR with voice-activity filtering skipped these lines. Return to original WAV with VAD disabled, both cached models and contextual/stereo crops. Exact Japanese spelling and the final warning ending remain qualified ASR/context decisions; no direct-human-listening claim. Read all seven adjacent mother utterances for accuracy; editorial and final proofreading completed. See docs/OPENING_GAP_REVIEW-0.1.2518.txt.

Installed implementation
Three22px normal-resolution Balsamiq cues use the existing native movie11 ShowFrame timeline. Existing half-second hold is capped at next cue; the final warning's small ASR overlap is trimmed at Mother's unchanged frame 846. Her seven existing cues and the other651 existing cues keep all wording/timing/geometry. Immutable strings/line records and replacement10-cue table add232 DOL bytes; update only movie11 pointer/count and section size. Renderer instructions, fonts, original movies/audio and all 1393 assets/FST/remaining disc bytes remain exact0.1.2509. No movie re-encode. The recent field Item healing fix remains installed.

Validation and limits
- All 661 cue records/strings/line pointers read back. All 658 existing words, times and geometry exact. Strict inverse restores2509 executable.
- 2360 native subtitle boundary cases across60 movies, existing guards plus 45 new cue boundary/full-queue/duplicate/metadata/ABI cases pass with normal24px atlas. Native timeline bytes remain exact; XER high-flag engine limitation retained.
- Actual native menu/effect/nested field healing, exact HP/one-item consumption and cleanup rechecked; earlier72-case/12-repeat healing evidence remains applicable by instruction/data identity outside the small subtitle append.
- Muted isolated Dolphin replay uses unchanged New Game inputs, Null audio backend and Volume0, no game RAM/register writes. Actual screenshot checks show all new captions, Mother cue and cleared overlay after opening. Captured frame-to-native clock mapping varies by a few frames due to read-only sampling; native boundary tests are the exact timing evidence.
- Original-source full xdelta and public 0.8.0 upgrade both fully decode to the expected ISO; Retro Trans Tools0.5.21 Apply xdelta backend verifies both complete images. GUI/Automatic publication is not claimed for this local test.

Hardware-sensitive risk
New immutable DOL data/pointers may affect executable loading/cache/data alignment on a physical console. Append consumes232 bytes of existing private padding; no new reservation, heap or live allocation. Arena low remains0x80389000; scene 1060704 bytes; private padding 1736 bytes. Section bounds, pointer readback, strict inverse, native guards and muted Dolphin opening are evidence, not physical GameCube validation. Previous healing-message backing remains +2952 live bytes; its general-heap fragmentation/timing risk persists. No physical hardware, actual Card write/restart/reload or exact reported healing location validation. HD remains deferred.

Installation
Use the new ISO directly. To patch original Japanese GT2J18rev0, apply0.1.2518-test.xdelta. To upgrade an exact public English v0.8.0 ISO/RVZ, use v0.8.0-to-0.1.2518.xdelta with Retro Trans Tools0.5.21 Apply xdelta; keep RVZ extraction enabled. Do not apply the public upgrade to Japanese or another English build. Cold boot the new image; save states retain old code. New Game is required to replay this opening naturally. Public GitHub assets remain unchanged.

ISO: work/output/Tengai-Makyou-II-English-0.1.2518-test.iso
Expanded ISO SHA256: 9cdaf01108079ae93912220350f4977466f895b49ab26786ffe3c7bf92db7eee
Evidence: work/analysis/opening-gap-native-0.1.2519.json; work/analysis/opening-gap-patches-0.1.2522.json; work/analysis/opening-gap-capture-0.1.2523.json; work/analysis/tested-opening-gap-0.1.2518-2524.json
Retention: latest full ISO and nine prior original-source xdelta versions; work/analysis/output-retention-0.1.2524.json.


## Earlier healing investigation and regression detail

Tengai Makyou II — English test 0.1.2509 / checkpoint 0.1.2514 — 2026-11-07

Reported problem and reproduced cause
The player reports that Buckwheat Dumpling healing freezes near the lakes on public v0.8.0, stopping partway through Manjimaru's name. Public v0.8.0 aliases internal 0.1.2503. The reported location itself has not been replayed; emulator and fresh-boot/save-state details were not supplied.
Native tests reproduce a shared field Item message-parser loop on the exact public executable with valid HP 10/100. Actual Use -> User -> Item -> Target hands off to field Item producer 8005805c. Its 23x3 parent stream 8017e910 inserts the translated HP result via control 0301. That nested stream can bypass the older direct-entry recovery resize guard. In animated mode 3 the parser stalls at 800a0ac4; the partial string in the verified case is Manjimaru's HP recovered. The screenshot stops earlier; exact on-screen prefix/location timing is not claimed. Direct English-stream tests alone (2507) pass and therefore miss this parent/nested path.
The initial exploratory 2508 diagnostic lowered max HP rather than current HP and reached the full-recovery variant. It is retained as exploratory evidence, not a valid damaged-HP reproduction. Final 2510 repeats the failure with valid current/max HP, actual native producer and partial-healing result.

Installed fix
Change only the field Item producer's native resize argument at 800580d8, li r4,23 -> li r4,64. The existing resize call at 800580e0 now reserves 64x3 before any parent or nested result is parsed. The visual frame, font, text, IDs, RNG, healing formula, item consumption and original state-machine decisions remain unchanged. This is one instruction / one changed disc byte. Strict inverse restores the exact public executable. No translation or game asset is rewritten.

Validation
- 72 actual native menu/field-effect/nested-result cases: all 16 giver/recipient pairs in modes0/3/6; Miso Dumpling16 and Kanro Pill86 with all four actors in modes3/6; HP cap/full/zero-at-effect-boundary/low-HP cases. HP change and exactly one item consumed are verified; all other party/inventory/MP bytes remain exact. The zero-HP effect-boundary check is not natural defeated-target menu-eligibility coverage.
- Complete expected English HP result, actual 64x3 allocation, nonvolatile ABI/stack guards and glyph bounds pass. The original Item state machine and destructor release every allocation. Dismissal/message-complete and finished-fade flags are modeled; natural controller/animation timing is not tested.
- Twelve consecutive actual field Item produce/reveal/free cycles in the same native fixture pass with advancing native RNG and no outstanding allocation.
- Existing direct recovery and unrelated parser fallback remain intact. Native actual Store construction, highlight/scroll, Buy/Sell funds, Back and same-machine reopening pass.
- Both captured Save/overworld general-heap pressure replays pass with an extra 4608-byte message and a simultaneous 57600-byte save-window request. These replay captured allocation sizes, not physical Card writes or exact live fragmentation/history.
- All 1393 assets, FST and every other disc byte match public 0.8.0. Both deltas fully decode to the target hash. Retro Trans Tools0.5.21 Apply xdelta backend also applies both to the exact expected full ISO; original inputs remain unchanged and private verification ISOs are removed.

Hardware-sensitive risk and limits
The Item message allocation rises from1656 to4608 bytes (+2952 live bytes), using the existing native allocator and destructor. This can affect general-heap headroom, fragmentation and allocation timing on a physical console. DOL size/static reservation/six fixed heaps are unchanged; scene arena remains 1060704 bytes and private free space 1968 bytes. Native guards/cleanup/pressure checks are evidence, not real-hardware validation. No actual emulator gameplay, exact lakeside save, natural scene transition, physical GameCube or actual memory-card write/restart/reload was tested. Audio/GPU endpoints are modeled/muted; no user emulator, audio, settings or save was touched. Normal-resolution Balsamiq remains; HD is deferred.

Install/test
For an existing exact English v0.8.0 ISO/RVZ, use Retro Trans Tools0.5.21 Apply xdelta with the v0.8.0-to-0.1.2509 upgrade patch. Keep Unpack CHD/RVZ input before patching enabled; save a new ISO or RVZ. This local test build is not listed in Automatic. For the exact original Japanese image, use the full 0.1.2509-test.xdelta instead. Do not apply the upgrade patch to an original Japanese or a different translated build.
Cold boot the new image and load an in-game memory-card save; emulator save states retain old code/window state. Retest the reported location. Public GitHub release and its downloads are unchanged.
ISO: work/output/Tengai-Makyou-II-English-0.1.2509-test.iso
Expanded ISO SHA256: aff8c037c31d314babf0fa364869a65b8cadf3a1aea23e166445ae80cb798574
Retention: newest ISO plus nine previous exact xdelta versions; work/analysis/output-retention-0.1.2514.json. Latest original and upgrade patches are alternate outputs of the same version.
Evidence: work/analysis/item-healing-native-0.1.2510.json; work/analysis/item-healing-regression-0.1.2511.json; work/analysis/item-healing-patches-0.1.2513.json; work/analysis/tested-item-healing-0.1.2509-2514.json.


## Historical0.8.0 validation

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

## Live Automatic verification — 2026-11-06

The published Retro Trans Tools 0.5.20 backend refreshed the public catalog, recognized the actual original ISO, selected 0.8.0 through Latest, Next version only and the explicit version, downloaded the live release patch into an empty cache, applied it, and verified the complete target hash. The output was recognized as already current; the source remained unchanged and attempts to overwrite the source or an existing output were refused. All earlier catalog release, DCP and withdrawn records remained unchanged. This tested the actual Automatic backend, not GUI automation or gameplay. [Machine-readable verification](AUTOMATIC-0.8.0.json).

Hosted registration/catalog validation: [successful workflow](https://github.com/retro-trans/retro-trans-tools/actions/runs/42171219265).
