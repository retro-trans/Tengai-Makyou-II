# Testing and limitations — v0.8.6

Translation remains in progress; Japanese text and errors may remain. This release promotes the exact tested 0.8.6 gallery image and retains the preceding six-screen fixes. Silent native checks cover real constructors, selectors, native input, text queues, allocation/free guards and actual General Store entry/scrolling/Buy/Sell/funds/Exit/reopen. Earlier six-screen native evidence is retained; the final gallery increment was strictly reversed to its exact tested predecessor rather than rerunning every earlier suite. Gallery proofs use native glyph/highlight bounds and original thumbnail pixels with schematic panels; they are not Dolphin screenshots. Movie dispatch IDs were checked with a modeled player endpoint, not video playback.

Hardware-sensitive changes since public v0.8.5 include PPC branches/call redirects, display pointers and private line records, selector geometry, native battle clear, proportional heading placement and arena loads. Incorrect pointers, ownership, bounds or register/font-state restoration could crash a real GameCube. The DOL grows 6,108 bytes into verified zero disc padding; private reservation grows 8,192 bytes to 0x80390000, leaving 3,032 bytes unused and 1,032,032 scene bytes. The alternate Scroll constructor changes allocation demand; gallery backing remains 223,488 bytes. Strict inverse/native ABI/heap/free/fallback tests pass, but complete concurrent scene heaps, fragmentation, timing and natural transitions remain unverified. Font, MAP, movies, audio, save formats and unrelated disc bytes/offsets are unchanged.

No new Dolphin playthrough, natural NPC/gallery access, actual video playback, physical GameCube test or memory-card write/restart/reload test was performed. Native and patch-installation passes do not constitute real-hardware validation. Normal-resolution Balsamiq Sans is retained; HD testing remains deferred.

## Historical local test evidence

The following 2026-11-21 snapshots describe the exact tested game bytes. Their local-test packaging/version status is historical; current release installation results are recorded separately below.

## Six-screen message and menu fixes


Base: exact public0.8.5, SHA-256 eea819dee7e887c78e44eb2439d903b79f1764c5cdc93efce2ed2c9b7cbec3eb.
VERSION/GitHub remain public0.8.5. This is unpublished0.8.6 work.

Installed fixes and category coverage
1. Translate the other copied handover heading and suppress the divider that
   crosses item rows. The old fix covered constructor0x80063b88/category5;
   the reported constructor0x80060b90/category4 used a second copied literal.
   Check both categories, all125 item highlights each, all four actor IDs,
   full/sparse parties, native scrolling, Confirm/Back and cleanup. Inventory,
   funds and chosen item/slot results compare exactly with public0.8.5.
2. Translate the main Settings Default question: Restore the default controls?
   This is separate from the Custom controller diagrams. All four initial
   presets pass native Yes/No/Back comparisons; Custom Back paths also pass.
3. Face choices: Front / Profile. Execute MAP049 room03's actual packed
   opcode1D constructor and both original row branches plus Back.
4. Rude-shop choices: Endure / Run Away / Attack. Audit all six identical
   source lists and execute every row/Back through the actual constructor.
   Include both bare Attack and the hidden524 glyph variant. Original source
   scripts, row IDs, branch targets and VM results remain exact.
5. Translate the separate direct remaining-enemies sprintf producer and clear
   the previous battle packets through native cleanup before drawing it.
   The existing translated formatter739 remains covered. Counts0/1 retain
   native behavior;2,9,10,99,100,999,65535 retain count/timer/state bytes and
   display only Remaining: integer, with no prior-line or second-line residue.
6. Extend canonical full English Scroll names/two-column geometry to the
   event redraw and alternate initializer omitted from the earlier range.
   Check all69 names/descriptions, capacities14/14/7/21, odd padding cells,
   native navigation, Confirm/Back, all seven NPC heading variants and cleanup.
   Suppress irrelevant event MP cost/eligibility/ownership overlays. Position
   complete headings explicitly using actual proportional24px glyph advances.

Why previous scans/checks missed these
Copied stack literals, packed scene choice lists, a direct sprintf battle
producer, the main Settings confirmation and alternate Scroll constructors
fall outside the ordinary dialogue pointer path. Previous handover checks
covered only category5. This build records producer/constructor coverage, not
only catalogue presence. Accuracy, editorial and final proofreading reviews
are retained with category coverage. Existing approved69 Scroll names reused.

Verification
Eight native case families pass under the exact final DOL hash. They use real
constructors/allocations and native callbacks with seeded state, not prebuilt
larger headers. General Store actual entry, highlights/scrolling, Buy/Sell,
funds, Back/Exit and reopen pass. Complete-row negative/prefix/other-header
guards and native Yes/No input pass. Six normal-font native glyph-queue proofs
were inspected. They use schematic panels and omit backgrounds/highlights;
they are not Dolphin screenshots. Sound/GPU services and fades are modeled.
All tests are silent. No actual emulator test was run, so no audio played.

Rejected development candidates are preserved in work/build/0.8.6/screens,
screens-final and screens-checked with their native evidence. The source-alias
audit exposed Attack's extra glyph. Scope guards reject wrapped prefixes and
unrelated calls. Visual QA exposed an off-screen39-character Scroll heading;
the final screens-ready candidate positions all seven complete headings inside
the original frame. Do not use earlier0.8.6 candidate DOLs or proofs for builds.

Hardware-sensitive changes and limits
52 display/geometry rewrites include PPC branches/call redirects,
seven heading display pointers, row-table/selector adapters, native battle clear,
proportional heading placement, private marker tables and two arena loads.
Incorrect pointers, branches, ownership cleanup, row counts, bounds or register
restoration could crash a real GameCube. Strict inverse, full native ABI,
allocation guards/cleanup, semantic result comparisons and scoped fallback
checks pass. Native/harness passes do not constitute real-hardware validation.

The final DOL grows3520 bytes into verified zero disc padding.
Private reservation grows4096 bytes to
0x8038f000; remaining private slack1524.
Scene space falls from1040224 to1036128 bytes. The alternate Scroll
initializer now allocates established28-column backing with two-column row
counts. This changes its real allocation demand; actual constructor/guard/free
checks pass, but complete scene heaps/timing on hardware remain unvalidated.
No MAP/decoded-room growth, font rebuild, HD font, movie or audio-asset change.
Every unrelated disc byte and all offsets remain exact. Undoing52 rewrites and
the append reproduces the exact public0.8.5 DOL.

No natural NPC access/playthrough, Dolphin playback, physical GameCube, timing,
card write/restart/reload or full-game memory validation occurred. Retain the
historical HD/store regressions and physical-hardware caveat. Cold boot this
image and load an in-game save; emulator states can restore old code/text.

Packaging
Original Japanese and exact public0.8.5 upgrade patches independently decode to
the same complete1,459,978,240-byte ISO. Published Retro Trans Tools0.5.23's real
Apply xdelta path passes both, preserves source images and hashes final output.
Automatic catalog/RVZ/live Windows GUI were not retested for this local build.
The public0.8.5 release assets stay immutable. Keep only this latest full test
ISO; public0.8.5 remains restorable from its verified original-source patch.

ISO: work/output/Tengai-Makyou-II-English-v0.8.6-test.iso
SHA-256: 845f436f1c27c9d454d1cedb968dc66f1e1061edffca700a81b3c41b4e52a51f
Build plan: work/build/0.8.6/screens-ready/plan.json
Native: work/analysis/screens-native-0.8.6.json
Category audit: work/analysis/screens-ready-coverage-0.8.6.json
Proofs: work/analysis/screens-ready-proofs-0.8.6.json
Patch application: work/analysis/screens-tools-0.8.6.json

## Movie gallery translation and selector


Installed changes
Translate the Japanese gallery heading as Tengai Movie Gallery. The original page13
logo is an image in font bank entry2, outside the plain-text catalogue. Replace
its dedicated draw call with English text from the existing normal Balsamiq
atlas at30px. Keep the original logo source texture, font assets, palettes,
all other bank pages, fade alpha, depth and restored global font dimensions.
No bitmap/HD font rebuild or texture allocation is introduced.

Fix the real gallery selector factory: the vertical movement pitch was22px,
while each logical title used three22px rows and the highlight height was66px.
Row1 highlight started at166px but its text started at210px. Set the scoped
gallery pitch to66px, matching the native block/scroll pitch and highlight.
Other native selectors retain their original fallback. Reflow all97 complete
English titles against current Balsamiq advances, inside264px and31 characters
per line. Preserve full words and source spacing; normalize fullwidth digits,
spaces and Japanese quotation brackets to standard English forms. Retain the
source female-symbol ornament.54 complete title strings normalize;11 titles
occupy two lines and none need more than two, within three-row logical cells.
Movie IDs, unlock keys, opaque halfwords, order and original thumbnail pixels
remain exact. This is a layout/punctuation audit of existing approved movie
titles, not a new scene-meaning retranslation. Accuracy/editorial/proofreading
stages are recorded with the98-row UI review.

Verification
Run actual native gallery constructors and allocations, then original selector
input, GPU highlight, text queues, paging, thumbnail getter and movie-dispatch
decisions. Test all97 rows with all unlocked, all locked and a nonuniform real
native bitfield. Per mode:192 top/row highlight positions,194 Up/Down positions,
384 Left/Right page decisions and97 thumbnail/Confirm cases. Totals:576 highlight
positions,582 Up/Down positions,1152 pages and291 dispatch cases. Each selected
title lies completely inside its highlight after scrolling. Check both ends,
the last row, locked refusal, original IDs and native Cancel/Start recheck.
Native allocate/free balances, restored heap headers and outer guards pass.
The native archive fixture has103 entries, derived from the true maximum ID102;
an initial100-entry diagnostic failed at row32/ID102 and was corrected. No game
binding was changed to accommodate the fixture.

Execute the actual shared background/heading callback at alpha0,64,255. All
complete English glyphs fit the original288x48 title region; font dimensions,
native alpha/depth and nonvolatile ABI are preserved. Unknown page/bank calls
take the original textured renderer. General Store actual entry/highlights/
scrolling/Buy/Sell/funds/Exit and reopen pass. All testing was silent.

Three layouts were inspected: the reported Takayama title, the longest title
and the final ending. Proofs show native glyphs/highlight bounds and unchanged
actual source thumbnails. Panels/footer and decorative highlight corners are
schematic, not Dolphin screenshots. The movie player and image decoder/final
GPU services are modeled; actual IDs and source pixels are checked. Full video
playback, natural memory-card access and natural gallery access remain untested.

Hardware-sensitive risk and limits
198 rewrites:97 native title pointers,97 private line records,
one selector-pitch immediate, one gallery-logo call and two arena loads.
Bad pointers/branches, selector geometry or font-state restoration could break
menus on hardware. Strict inverse, original non-title record-word comparisons,
real constructors, native input/queue/ABI/heap/free guards and unknown-bank/page
fallbacks pass. Native passes do not constitute physical GameCube validation.

The DOL grows2588 bytes into verified zero disc padding. Private
reservation grows4096 bytes to0x80390000,
with3032 bytes unused. Scene space falls from1036128
to1032032 bytes. This gallery update adds4096 reserved bytes relative
to the preceding0.8.6 test,8192 cumulatively relative to public0.8.5. Existing
32x291 gallery backing remains223488 bytes; no constructor backing growth.
The native OS-heap fixture uses the new scene-byte limit, but does not model
every concurrently loaded game resource. No natural heap timing/whole-scene
or console validation is claimed. Original font/MAP/movie/audio assets and
every unrelated disc byte/offset remain exact.

Existing six-screen fixes are retained. Reversing these198 gallery rewrites
and the appended section returns the exact prior tested DOL; complete earlier
six-screen test suites were not rerun. Keep their evidence and all historical
HD/store regressions. No Dolphin, physical hardware, card write/restart/reload
or full-game validation occurred. Cold boot the updated ISO and load an in-game
save; emulator states may restore old strings/code.

Packaging and version
Original Japanese, exact public0.8.5 and previous six-screen0.8.6 test patches
independently decode to the same complete ISO. Published Retro Trans Tools
0.5.23 Apply xdelta passes all three and preserves input images. Automatic/RVZ
were not retested for this local update. VERSION/GitHub remain public0.8.5;
this remains unpublished0.8.6. The previous full test is archived as its exact
original-source patch, within the ten-revision policy; public assets immutable.

ISO: work/output/Tengai-Makyou-II-English-v0.8.6-gallery-test.iso
SHA-256: 05478cccc8a09ec692778a54167d42efe69c8d764066dd88dc2ee6ce9aa4c7a6
Native: work/analysis/gallery-native-0.8.6.json
Coverage: work/analysis/gallery-coverage-0.8.6.json
Proof: work/analysis/gallery-proofs-0.8.6.json
Patch verification: work/analysis/gallery-tools-0.8.6.json

## Inherited release evidence

Earlier tests and remaining limitations are retained in [v0.8.5 testing notes](https://github.com/retro-trans/Tengai-Makyou-II/blob/v0.8.5/docs/TESTING.md). Historical evidence is not a new playthrough or hardware validation.

## Live public installation verification — 2026-11-27

Live **Retro Trans Tools 0.5.24 Automatic** passed from the Japanese original and all six earlier public English versions, **v0.8.0 through v0.8.5**. Fresh catalog and patch downloads produced the exact v0.8.6 ISO, recognized it as current, preserved inputs and rejected overwriting existing files. Latest, explicit version and Next version only routes were checked. [Automatic evidence](https://github.com/retro-trans/Tengai-Makyou-II/blob/main/docs/AUTOMATIC-0.8.6.json).

The published **Windows v0.5.24 app** passed original **RVZ → Automatic → RVZ** with a fresh patch cache and live downloads. Independent extraction reproduced the complete v0.8.6 ISO hash. Installation was verified; game playback and physical hardware were not exercised. [RVZ evidence](https://github.com/retro-trans/Tengai-Makyou-II/blob/main/docs/RVZ-0.8.6.json) · [Catalog refresh](https://github.com/retro-trans/retro-trans-tools/actions/runs/45932752255).
