# Testing and limitations — v0.8.3

This is an in-progress translation. Japanese text may remain. The new password and reward code, UI allocations and compressed room changes have passed native checks, but natural access to these scenes in Dolphin and physical GameCube play remain untested. A full playthrough, transition timing under natural memory pressure and memory-card write/restart/reload have not been validated. Earlier opening-warning source uncertainty remains documented.

Hardware-sensitive changes since v0.8.2 include rewritten password editing/navigation/comparison, English answer records and a new input-buffer format inside the original 30-byte buffer. Password prompt backing requests 1,968 extra bytes and the reward refusal requests 2,880 extra bytes before allocator rounding. Travel menus can add up to 4,224 live bytes. Scoped display/parser branches and subtitle records change, and compressed MAP/header/FST metadata changes. These can affect heap pressure, fragmentation, timing and console execution. Native checks and patch verification do not establish real-hardware compatibility. Detailed evidence and limits appear in the testing notes.

Exact alias of internal build 0.1.2615. Native previews use actual glyph positions on schematic backgrounds.

## Internal build 0.1.2615

Tengai Makyou II English test 0.1.2615

Password entry
Both password modes use an A-Z keyboard with Space, Delete, Left, Right and
Done. Input has 20 characters, with a separate end caret. Comparison ignores
spaces and capitalization. Done and the existing finish shortcut submit the
answer. Back deletes the preceding character.

The tomb clues in maps 110 and 291 and the Kikugoro clues in maps 71 and 220
match these spellings. All ten password prompt variants are English.

Related screenshot fixes
The separate battle reward refusal now reads, across two lines,
But your party cannot carry any more.
Give up this reward?
Its shared Yes label also serves the inventory organize confirmation.
Both confirmation openings and the original decision indices were checked.
The two Kii Province/Wakayama Castle dialogue rows already have normalized
spacing in this build. All 14 existing treasure/find/obtain/bag-full/discard
and detection streams and their dispatch pointers remain correct in the
current executable.

Verification
Native checks execute the real BB opcode dispatcher, operand reader, wrapper,
window constructors, input edits, comparison, result variable and cleanup.
The BB instruction and surrounding VM context are fixtures. Ten prompt
scenarios exercise all 31 keys in four directions, and 15 answer cases cover
both modes, spaces, mixed case, wrong mode, empty/short/long answers and
malformed input. Editing checks cover caret bounds and all 20 visible cells.
Reward checks compare six old/new prompt decisions and the separate organize
opening. No reaches the original inventory-screen handoff. Six installed
field rows are read back from the current MAP. Audio endpoints were silent.
The preview uses actual native glyph positions on schematic panels.
Both patches reproduced the full ISO through Retro Trans Tools 0.5.21.

Hardware-sensitive changes
Password editing, navigation, rendering and answer comparison are rewritten
within their original code region. The original kana-grid and prompt data
area now holds English key labels, prompts and the reward refusal. The two
answer records now hold English strings. Input uses 20 bytes and a terminator
inside the original 30-byte buffer. The main password glyph backing grows
from 23x2 to 64x2, requesting 1968 extra bytes before allocator rounding.
The grid backing has the original 5760-byte size, reshaped from 30x8 to 48x5.
The reward refusal resizes its cleared real bottom window from 24x3 to 64x3,
requesting 2880 extra bytes before rounding, and its pointer load branches
through a helper within the rewritten code region.

These code, buffer-format and allocation changes can affect console play.
The native tests model fade completion and peripheral drawing/audio services.
They do not validate heap pressure in a natural map scene, GPU rendering,
the event interpreter's later resume, or the No-path inventory screen after
the handoff. Natural password entry in Dolphin and physical hardware remain
untested. DOL size and static memory reservation are identical to 0.1.2610,
the strict inverse restores that DOL, and every other disc byte matches it.

Start the new ISO and load an in-game save.


## Internal build 0.1.2610

Tengai Makyou II English test 0.1.2610

The battle ally-target popups now use Manjimaru, Kabuki, Gokuraku and Kinu.
The source names were shared by two native row writers and five openings.
Both the regular party list and the filtered target list use the same
English names as the battle HUD. The wider selection bar accommodates the
full names inside the original frame. The adjacent Allies / Enemy Side
picker already displays in English and was exercised as a regression check.

Silent native checks covered seven paired scenarios across the five
openings, including two, three and four party members, reordered eligible
targets, disabled colors, directional input, and closing and reopening.
The two-person item case verified that selecting Kabuki produces the same
target mask and Confirm and Back states as before. The preview shows native
glyph positions on a schematic panel. Both xdelta patches reproduced the

Hardware-sensitive changes
The two scoped name row writers now look up existing English strings.
Their glyph buffers increase from five to ten columns. That requests
360 extra bytes for a three-row popup or 480 for a four-row popup, before
allocator rounding. The original frame and existing font assets are
reused. The native tests exercised allocations and frees, with modeled
battle setup and fade timing. The DOL size and static RAM layout are
identical, the strict inverse restores the prior DOL, and all disc bytes
outside the DOL match 0.1.2605. The code and heap changes could affect
console play. Full battle playback in Dolphin and physical hardware remain
untested.

Start the new ISO and load an in-game save.


## Internal build 0.1.2605

Tengai Makyou II English test 0.1.2605

Field travel and labyrinth escape message audit
- Wind and Storm Talismans share a separate item-result path. Translate
  both pages and preserve the selected actor, item and solo/party subject.
- Translate both Return Stone pages and the Receding Wave escape result.
- Translate the named travel-scroll location refusal in its original
  23-by-3 window. Item location refusals already display in English.
- Recheck the previously installed Tenjin and Feather Robe wind results,
  and the Wind Talisman and Feather Robe village destination flows.

Native verification covers 42 paired old/new cases for travel items,
Receding Wave and the named refusal, plus 12 existing wind-result cases
and eight alternate refusal or destination paths. It verifies the real
result callbacks, normal and Confirm reveal, result page turns, English
names, bounds, actor data and allocation cleanup. The short refusal
wording fits the original backing even for Receding Wave. The preview
uses native glyph positions on schematic panels. Both patches reproduced
the full ISO in Retro Trans Tools 0.5.21 Apply xdelta.

Hardware-sensitive changes
Four message pointers and five parser branches change. The branches
qualify the new stream ranges and reuse the existing name and parser
paths. The strings and small branches occupy checked fixed wrapper padding
at 0x80290D10 and 0x80290E0C, following existing exits. The strict inverse
restores 0.1.2600. DOL size, window backing, arena and font size stay the
same. All disc bytes outside the DOL match 0.1.2600. The changed branches
and stream pointers can affect console execution. Native tests used silent
audio endpoints and modeled the acknowledgement of the previous scroll
prompt. The actual map transfer, Dolphin gameplay and physical hardware
remain untested.

The standing category-wide review rule is recorded in AGENTS.md.
Start the new image and load an in-game save.


## Internal build 0.1.2600

Tengai Makyou II English test 0.1.2600

The field result reads “Manjimaru and the others melted into the wind!”
The solo version reads “Manjimaru melted into the wind!” Both scroll IDs
66 and 67 use the same result callback. The active game party scan chooses
the original solo or party branch.

Twelve silent native cases used the real 64-by-3 constructor, field result
callback and window updater. Cases covered both scroll IDs with one, two
and four active characters, normal reveal, early Confirm to complete the
line and confirmation of the completed result. Both variants fit on one
line. Matched prior party data, scroll cost and allocation cleanup. The
fixture starts the result after modeling acknowledgement of the preceding
scroll-use prompt. The preview shows native glyphs over a schematic panel.

Hardware-sensitive changes
Four existing pointer-load instructions now read English strings from
79 bytes in the original wrapper slot's checked padding, past the
existing shop helper's return and before the next routine. The original
source strings and lookup records stay intact. The pointer changes and use
of padding can affect console execution. Evidence covers a reference scan,
inverse DOL comparison, native dispatch, reveal, bounds, cleanup and both
patch routes. The backing, font, arena and DOL sizes stay the same. All disc
bytes outside the DOL match 0.1.2595. The native test ends after confirming
the result. Dolphin travel, map transition and physical hardware play
remain untested.

Both patches rebuilt the full ISO in Retro Trans Tools 0.5.21 Apply xdelta.
Start the new ISO and load an in-game save.


## Internal build 0.1.2595

Tengai Makyou II English test 0.1.2595

The field event “Who will carry it?” popup uses Manjimaru, Kabuki, Gokuraku,
and Kinu, with Free followed by the original count. This uses the same names
and terminology as the separate shop popup. The field selector spans both
columns, with the original 480 by 192 frame and 18 by 6 backing.

Native callback fixtures compared the prior and new builds with the same
inventory data. The pictured 1 and 3 counts, all four party IDs, zero,
two-digit scroll counts, native movement and confirmation passed. Actual
confirmation rejected a full recipient and added one item, weapon or scroll
to the selected eligible recipient. General Store entry, scrolling, Buy and
Sell, funds, Back, Exit and four same-pool reopens passed in a separate check.
The proof shows native glyph positions on a schematic background.

Hardware-sensitive changes
Five instructions in the field event change the display-name pointer and
horizontal positions. A 12-byte field-only format record keeps the existing
two-digit formatter command and the original nine-byte stack copy. These
changes touch the selector and native parser input and can affect hardware
behavior. The DOL size, arena, font and allocation sizes stay the same. All
disc bytes outside the DOL match 0.1.2590. The native fixture modeled two
paired-single save and restore instructions and completed fade timing, and
muted all audio endpoints. Natural event entry in Dolphin and real hardware
play were not exercised.

Retro Trans Tools 0.5.21 Apply xdelta reproduced the complete ISO from the
clean Japanese GT2J18 rev 0 image and from the exact public English v0.8.2
image. Start the new ISO and load an in-game save.


## Internal build 0.1.2590

Tengai Makyou II English test 0.1.2590

Field dialogue now uses one ordinary English space for isolated full-width
prose separators, including across color and empty reading tags. This corrects
Ikoma Pass, Naniwa Province and four bronze bells along with other instances.
The installed scan corrected 70 gaps in 50 entries
and kept deliberate indentation, aligned puzzle text, color, wording, voice
controls, and existing line and page breaks. The English field compiler now
applies the same rule to future builds. See work/build/0.1.2590/prose-shop/spacing-review.json.

Equipment descriptions use 14px normal Balsamiq while a shop is active.
Kogarashi shows both lines in Buy and Sell. The Buy lines sit at y=76 and 90,
with a bottom of 104 inside the panel's inner edge at 108. Sell lines start
at y=72 and 90. The underlying 48 by 5 allocation is unchanged.

Silent native checks read 9635 ordinary entries and checked
9635 event operands and all 31 typed
room bindings. The original decoder reproduced all 31
changed rooms. Both reported dialogue examples agree in fast, slow and
confirm-to-reveal modes. Actual shop entry, directional scrolling, all
237 equipment descriptions, purchase and sale confirmations,
funds, Back, Exit and four same-pool reopens passed. Sampled Field and Storage
gear views exactly matched the previous build. Layout proofs use captured
native glyph positions and a schematic background.
The Equipment Shop also completed a 4,400-ryo Kogarashi purchase, including
the follow-up equip prompt, and credited 2,200 ryo on its confirmed sale.

Hardware-sensitive changes and limits
The MAP has 96 additional compressed bytes in verified unused disc padding.
Its file size and the cached headers change. All disc offsets and unrelated
assets are byte-exact. Decoded rooms keep their allocation sizes and caller
operands. The DOL adds a shop callback check in 44
bytes of the original description wrapper's proven free slot, reached from one
new branch. It reads the active parent to select font size and leaves font
assets, heap reservations and backing sizes alone. Compressed MAP layout,
disc length metadata and the code branch may affect console execution.
Evidence covers native decoding, callback and menu flows, glyph bounds,
unchanged adjacent paths, and full patch application. Dolphin gameplay,
natural scene replay and real hardware were not tested.
The superseded 0.1.2586 prototype applied 14px in the shared wrapper without
the shop callback check. Field and Storage comparison caught the side effect.
The delivered build passed the paired check for those paths.

Both patches reproduce the complete ISO in Retro Trans Tools 0.5.21 using
Apply xdelta. The original-source patch is for clean Japanese GT2J18 rev 0.
The upgrade patch is for the exact public English v0.8.2 image. Start the new
image and use an in-game save so the game loads the new executable and data.


## Internal build 0.1.2579

Tengai Makyou II — English test0.1.2579 / checkpoint0.1.2585 — 2026-11-07

Requested subtitle
Install Kikugoro's omitted field farewell: "See you around, Fire Clan!" The existing52-cue movie27 conversation already has subtitles; this original event plays a separate voice after that movie ends. Original MAP063/room0 issues opcode63 voice346, waits210frames and runs the retreat motion. Native handler80071C90 ->8006B308 subtracts290 ->80085780 index56; filename table801D4C28[56] identifies Voice/NA012D.hps. Both unprompted no-VAD ASR models agree on the farewell and Fire Clan group vocative. One utterance newly translated, complete context movie/event reviewed. Accuracy/editorial/recheck/proofreading and source hashes: work/translation/en/ui/retreat-subtitle-0.1.2579-REVIEWED.json; docs/RETREAT_SUBTITLE_REVIEW-0.1.2579.txt. Local ASR plus source context, no independent human listening/exact source orthography claim. Preserve the casual farewell and group address without invented gender or threat.

Implementation
Display the single full line for the native nonzero voice-handle lifetime at80230608, exact voice index56 at8023060C, only in native field mode2. Leading sound/pause stays inside that lifetime. Native playback completion/reset, a different voice or another mode removes the caption; no added timer/state, no changes to original event waits/audio/animation. Existing sorted/font/queue capacity/native-caption duplicate guards reused, normal22px Balsamiq. All earlier fixes including the orchid clip, full travel names/NPC dialogue and corpses spacing retained.
One mode-comparison instruction branches to a72byte private helper. Mode13 returns to its original movie path;14 stays direct. Other modes still exit, except exact active field voice56. Helper selects one immutable record through the existing guarded glyph-rendering path; common prologue/epilogue retains complete register/stack discipline.
Reuse48bytes of the84byte retired movie11 table, which2518 replaced with a10-record table. Source bytes match the pre2518 seven records; all current aligned DOL pointer references and663 active cue roots exclude the block. Current103 movie headers/cues/strings remain exact. Provenance, inverse and address census saved in build plan/review. This is an identified retired read-only record table, not anonymous zero/mutable state reuse.

Validation
27 field cases plus the complete movie regression case pass. Actual original opcode63 handler opens Voice/NA012D.hps and advances exactly four bytes; original event bytes remain intact. Actual native audio updater leaves the subtitle active while busy, closes/clears it at completion, and explicit native reset removes it. Only SDK audio open/busy/close endpoints modeled silently; no voice playback. Active/pause/prefix/exact capacity, stopped handle, neighboring IDs, other modes, sorted/missing font/full/overflow queues and native caption duplicate/HUD/page/size cases pass. Native glyph rectangles/UVs/color, font/style, GPR/FPR/CR/CTR/stack/queue/voice guards pass, retaining existing high-XER Unicorn limitation. All663 movie records/headers/strings remain exact and2370 movie boundary cases pass, including both IWF14 and THP13 paths.
The initial2580 fixture incorrectly demanded all96bytes of earlier glyphs remain unchanged on append. Native queue append updates the prior glyph's next pointer at offset0x5C. Diagnostic work/analysis/retreat-verifier-diagnostic-0.1.2580.json preserves the incomplete suite and exact changed offsets; corrected2581 checks the92byte glyph payload while allowing native link updates, as the existing movie verifier does. No game asset/code changed between these suites; do not count2580 as a passing suite.
Normal-font proof from saved actual native queue visually reviewed: work/ui/retreat-subtitle-0.1.2579/native-layout.png. Schematic background, not fresh Dolphin screenshot. No new Dolphin/natural field retreat/live voice-sync/physical hardware/Card write-restart-reload test claimed. Voice ownership is lifetime-based, not sample-position timing.
Both original-Japanese full patch and exact public English0.8.2 upgrade completely decode to the expected1,459,978,240-byte ISO and pass actual Retro Trans Tools0.5.21 Apply xdelta, full hashes and source preservation. Existing public Automatic/RVZ evidence retained; no new public release/catalog/RVZ execution claim.

Hardware-sensitive changes and evidence limits
One executable branch plus72byte executable helper and48bytes reclaimed immutable data; existing private padding now32bytes. No OS arena/reservation/heap/font or live allocation growth; scene1,060,704bytes and general heap4,718,592bytes unchanged. New field line adds26glyphs only under the exact native voice owner. Changed execution/pointers/reclaimed data and extra queue traffic can affect real hardware. Evidence: strict inverse to2572, retired-table provenance/reference census, real native voice dispatch/updater/reset, all663 old movie roots/2370 boundary regressions and queue/ABI guards. This does not prove physical hardware rendering, natural source-scene access or synchronization. Original event/MAP/header, all1393 assets including audio/movies/font, FST/offsets and every disc byte outside DOL remain exact2572. Prior hardware-sensitive risks remain documented; HD deferred.

Install
Cold-boot new ISO and load an in-game save; emulator states can restore old code/tables. Original Japanese GT2J18rev0 uses0.1.2579-test.xdelta; exact public English0.8.2 uses v0.8.2-to-0.1.2579.xdelta. Other English versions should use the test ISO. Retro Trans Tools0.5.21 RVZ conversion remains available; local patches use Apply xdelta.

ISO: work/output/Tengai-Makyou-II-English-0.1.2579-test.iso
Expanded ISO SHA256: 173ebdeaf727a681b9d1f5580a992176e1ac1f016d3e022ace6495f1a603ae9c
Manifest: work/analysis/next-build-drafts-0.1.2579.json
Native: work/analysis/retreat-subtitle-native-0.1.2581.json
Proof: work/analysis/retreat-subtitle-proof-0.1.2584.json
Tools: work/analysis/retreat-subtitle-tools-0.1.2583.json
Delivery: work/analysis/tested-retreat-subtitle-0.1.2579-2585.json
Retention: work/analysis/output-retention-0.1.2585.json; latest full ISO+9 older original-source patches.2572 removed only after archive decode matches;2503 retired. Private reference/Tools ISOs removed; eight immutable public0.8.2 assets unchanged.

## Internal build 0.1.2572

Tengai Makyou II — English test0.1.2572 / checkpoint0.1.2577 — 2026-11-07

Requested subtitle
Install Manjimaru's omitted boast, "No one can stand in my way!", in the original Dark Orchid finishing movie26 and later movie75 variant. Original movie26 decoded artwork matches the supplied screenshot. The actual native Sound table binds both510-frame/30fps movies to the identical26_ran1.hps voice. One utterance translated; two native movie headers use one shared immutable cue. All earlier fixes retained, including full travel names/NPC translations and the corpses spacing fix. No GitHub release publication.

Language and timing evidence
Previous two-model VAD scans produced zero segments, so the subtitle table had no entries for these movies. Two unprompted no-VAD model returns recover the boast's beginning and phonetic ending. The ending is corrupted in ASR; the first-person published scene recollection explicitly quotes the conventional boast and corroborates the intended reading. Source GC artwork/audio and native bindings identify this build's movie; the external recollection refers to the original version and does not establish GC timing. Review: work/translation/en/ui/orchid-subtitle-0.1.2572-REVIEWED.json; docs/ORCHID_SUBTITLE_REVIEW-0.1.2572.txt. Accuracy, complete confident English editorial wording and final proofreading recorded. No attack name or added threat; no translation invented for music/impacts. Local ASR plus scene/context and corroborating quotation; no independent human-listening or exact GC orthography claim. Timings approximate: source0.54..3.50seconds from the full model, native frames17..120 including existing0.5second hold; cue absent at121. Other model interval0..3.84seconds differs; no live voice-sync validation claimed.

Validation
All663 cue records/strings/line tables read back; previous661 cue words/times/geometry remain exact.2370 native boundary cases across62 subtitled movie IDs verify frame selection, exact glyph count/positions,24px normal atlas and unchanged native timelines. Thirty extra new-cue tests cover both IDs' before/start/end/after frames, full and exact-capacity queues, bad metadata/mode, missing font, sorted queue and native-caption duplicate suppression. Existing nested Item healing still completes with its fixed constructor; no game audio playback. Native GPR/FPR/CR/CTR/font/stack checks pass; pre-existing high-XER Unicorn limitation retained.
Native subtitle queue proofs for both variants visually reviewed: work/ui/orchid-subtitle-0.1.2572/native-layout.png. These show actual glyphs/geometry over a schematic background, not fresh Dolphin screenshots or natural clip access. No new Dolphin/natural movie or live audio synchronization test, physical-console playthrough or actual Card write/restart/reload test.
Both original-Japanese full patch and exact public-English0.8.2 upgrade fully decode to the expected1,459,978,240-byte ISO and pass actual Retro Trans Tools0.5.21 Apply xdelta backend, with complete output hashes and source preservation. Existing public0.8.2 Automatic/RVZ evidence retained; no new Automatic catalog or RVZ execution claim for this local test.

Hardware-sensitive implementation and limits
Append48 immutable bytes (one ASCII string, line and cue records plus alignment) within existing reserved private padding;104bytes remain. Replace two formerly-zero16byte subtitle headers and DOL data-size word; strict inverse recovers2564. No renderer executable instruction, font, OS arena, fixed/general/scene heap, or allocation size changes. Scene1,060,704bytes, general heap4,718,592bytes retained. New visible cue adds27 glyphs to the existing queue during both short sequences; tested capacity/duplicate guards prevent overwrite.
All1393 disc assets, original movie/audio/font bytes, MAP/header, FST, offsets and all bytes outside the DOL are exact2564. DOL loading size/pointer/header changes and newly active overlay draws can affect real hardware despite unchanged reservations. Evidence: section bounds/private padding, strict inverse, all record readback and native timing/queue/ABI checks, exact other disc bytes and complete patch roundtrips. Native fixtures model selected endpoints silently; they do not prove physical GameCube rendering, natural scene access or live synchronization. Earlier hardware-sensitive risks remain documented in prior build notes; HD deferred.

Install
Cold-boot the new ISO and load an in-game save; emulator states can restore old code/tables. Original Japanese GT2J18rev0 uses0.1.2572-test.xdelta; exact public English0.8.2 uses v0.8.2-to-0.1.2572.xdelta. Other English builds should use the supplied test ISO. Retro Trans Tools0.5.21 RVZ conversion remains available; local patches use Apply xdelta.

ISO: work/output/Tengai-Makyou-II-English-0.1.2572-test.iso
Expanded ISO SHA256: 335424f532f10311440af10bf9da48d68b5d77b3654479dccd0a9ace0f094dd4
Manifest: work/analysis/next-build-drafts-0.1.2572.json
Native: work/analysis/orchid-subtitle-native-0.1.2573.json
Proof: work/analysis/orchid-subtitle-proof-0.1.2576.json
Tools: work/analysis/orchid-subtitle-tools-0.1.2575.json
Delivery: work/analysis/tested-orchid-subtitle-0.1.2572-2577.json
Retention: work/analysis/output-retention-0.1.2577.json; latest full ISO and9 older original-source xdelta versions.2564 removed only after archive decoded to its exact hash;2498 retired. Temporary public reference/Tools verification ISOs removed. Eight immutable public0.8.2 assets unchanged.

## Internal build 0.1.2564

Tengai Makyou II — English test0.1.2564 / checkpoint0.1.2569 — 2026-11-07

Requested fix
Remove the full-width space before corpses in MAP-063-00-000f94. Replace it with one ordinary interword space; reflow the full two-page utterance, respecting existing page turns,60-character/528px limits, empty-reading markers and all native speaker/audio controls. No wording or translation change. Fourteen context rows read, one edited; accuracy/editorial/proofreading decisions and before/after recorded in work/translation/en/ui/field-wrap-0.1.2564-REVIEWED.json. The screenshot is the second page, not a separate script row. All previous fixes, including2558 full travel names and NPC translations, remain installed.

Validation
Three complete native packed-parser cases (slow, fast, confirm); identical packets and complete two-page text, widths and spaces pass. One affected ordinary room through actual native CNS decoder. All9635 ordinary FIELD rows and9635 caller operands read back; all unrelated compressed rooms exact. All31 registered typed descriptors/streams verified; affected room is ordinary, so no new typed-loader route claim. Existing translated allocation reused without growth. Normal Balsamiq actual native-packet proofs for both pages visually reviewed: work/ui/corpses-gap-0.1.2564/final-two-pages.png. These are packet proofs, not fresh emulator screenshots/natural conversation playback. Final proof separates single-line page resets at identical y; the generic diagnostic preview in2565 overlaid them and was superseded before visual review. Native execution/game assets are unchanged.
Both original-Japanese full patch and exact public-English0.8.2 upgrade fully decode to the expected1,459,978,240-byte ISO, and pass actual Retro Trans Tools0.5.21 Apply xdelta backend with complete output hash and input preservation. No new Automatic catalog entry or RVZ execution claim; published0.8.2 evidence retained.

Implementation and hardware-sensitive limits
DOL code/data byte-exact2558, no new executable hooks, font edits, static reservation, live backing allocation or decoded-room growth. Existing private padding remains152bytes. MAP compressed archive grows96bytes; header rebuilt; FST and later disc offsets shift2048bytes.1391 unrelated assets, including movies/audio/font, byte-exact2558. Strict inverse restores the original room/DOL and all VM references remain unchanged.
Changed compressed bytes, archive/header sizes and FST offsets can affect DVD loading, stream decoding and real-console transitions. Evidence: strict inverse, unchanged decoded allocation and DOL, actual native CNS/parser cases, exact31 descriptors and all caller readbacks, full asset integrity and patch roundtrips. Native fixtures model selected services/audio endpoints silently; they are not physical GameCube validation. No new Dolphin playback, natural ninja village conversation/transition, hardware playthrough or Card write/restart/reload test claimed. HD remains deferred. Earlier hardware-sensitive risks and Store constructor regression evidence remain documented in earlier notes.

Install
Cold-boot the new ISO and load an in-game save. Emulator states can restore old script bytes. Original Japanese GT2J18rev0 uses0.1.2564-test.xdelta; exact public English0.8.2 uses v0.8.2-to-0.1.2564.xdelta. Other English versions should use the supplied test ISO. Retro Trans Tools0.5.21 existing RVZ extraction remains supported; no new public release requested.

ISO: work/output/Tengai-Makyou-II-English-0.1.2564-test.iso
Expanded ISO SHA256: 0923e2d26e9c22e4a020fc6e49d16de52bb3908e746bb3dfb27b45a68ff857ae
Manifest: work/analysis/next-build-drafts-0.1.2564.json
Native: work/analysis/corpses-gap-native-0.1.2565.json
Final reviewed proof: work/analysis/corpses-gap-proof-0.1.2568.json
Tools: work/analysis/corpses-gap-tools-0.1.2567.json
Delivery: work/analysis/tested-corpses-gap-0.1.2564-2569.json
Retention: work/analysis/output-retention-0.1.2569.json; latest full ISO and nine older original-source xdelta versions. Prior2558 removed only after archive decoded to its exact hash. Immutable public0.8.2 unchanged; private reference/Tools verification ISOs removed.

## Internal build 0.1.2558

Tengai Makyou II — English test0.1.2558 / checkpoint0.1.2563 — 2026-11-07

Requested translations and layout
Translate the travel destination popup and show full English names. All113 native display records use91 reviewed complete names, including Inuyama Town, Nagashino Town, Fukushima Village and Umase Village. Existing project glossary spellings reused. Only display pointers change; source Japanese strings, the121-entry save-location table, destination visited/event flags, map IDs and coordinates remain byte-exact. Cancel retains original semantics. The actual shared Item/Scroll/Arts travel constructor now uses20 columns with20px normal Balsamiq and direct native ASCII parsing; native automatic frame is448px wide, centered at x96. Frame height remains native row-dependent; longest tested list has11 rows. No abbreviation or clipping of names.

Install two dialogue translations in three actual scene rows (one repeated scene state): MAP-060-02-000341, MAP-061-02-000341, MAP-063-07-00010c. Fifteen adjacent/context rows examined; source accuracy, editorial and final proofreading recorded in work/translation/en/NPC-extra-0.1.2557-REVIEWED.json. Elderly speaker's yome interpreted as daughter-in-law from screenshot and adjacent wife's line; do not infer the husband is dead. The returning ninja's nervous laughter, forest repetition and first-person fear of being eaten are preserved, without naming an eater. Original speaker/audio/page/end controls retained.

Validation
101 saved native cases pass. Nine complete new NPC packed-parser cases: three streams x slow/fast/confirm, identical output packets; three actual native CNS room decodes. Read back all9635 ordinary FIELD rows and9635 real VM caller operands; previous9632 rows remain exact. All31 typed binding descriptors/decoded streams and87 payloads retained; these three edited rooms are ordinary, so no affected typed-loader execution claim. Installed FIELD total9722 including87 typed/dynamic rows;51 indexed rows remain pending, not a full-translation claim.
174 actual travel constructors: old/new pair for29 native region IDs x three visited/story flag policies. All113 records reached across the tests, native filtered list/order matches the old build, full glyph bounds and native cursor/highlight wrap checked. No pre-expanded popup header fixture substitutes for the real constructor. Actual Wind Talisman Item and Feather Robe Scroll Use/User/Item paths exercise travel open, Down, Back, reopen, destination confirm and native cleanup; source party/save bytes and selected native destination record's12 gameplay bytes unchanged. Arts shares the patched constructor by source-bound call site; complete Arts menu flow not newly tested. Retained native Kanro healing and Ear Pick no-effect paths pass. All audio endpoints modeled silently; no Dolphin launched.
Six final normal-font layout proofs visually reviewed (Hida/Owari/longest list and three full NPC streams): work/ui/travel-dialogue-0.1.2558/all-layouts.png. Travel proofs render actual native glyph/selector positions with a schematic border; these are not fresh Dolphin screenshots or natural scene captures.
Both xdelta routes completely decode to the expected1,459,978,240-byte ISO and pass actual Retro Trans Tools0.5.21 Apply xdelta backend, full output hashes and input preservation. Routes: original Japanese GT2J18rev0 and exact public English0.8.2. This is a local test build; no new Automatic catalog entry or public release. Existing0.8.2 Automatic/RVZ evidence is retained, not a new RVZ execution claim for2558.

Hardware-sensitive changes, evidence and limits
Three travel-only executable instructions change constructor columns/font and call the existing native ASCII parser;113 name-pointer fields change. New immutable Kyoto string/padding grows DOL8bytes inside existing reserved padding, leaving152bytes. No new OS arena/static reservation, no font asset changes. Scene heap remains1,060,704bytes; general heap4,718,592bytes. Source save-location names/gameplay fields stay intact. Strict inverse restores2552 DOL; all1391 unrelated disc assets including movies/audio/font remain exact.
Wider popup backing adds up to4,224 live bytes versus original4-column text backing (16 extra columns x11 rows x24bytes); all native allocator guards and full cleanup pass. This is new runtime heap pressure and may affect a scene with lower remaining memory. Native fixtures demonstrate bounds/lifetimes, not physical-console free-memory sufficiency. No general font/shop constructor change; original Store actual-entry regression evidence remains documented and is not replaced by this travel fixture.
Three translated decoded room allocations grow224,224,160bytes; maximum224bytes. All source VM references patched exactly/reversibly and native CNS decodes pass. Compressed MAP/header rebuilt; later FST/disc offsets shift2048bytes. These can affect actual DVD reads, room/scene loading and event execution. Evidence: complete disc asset integrity, strict inverse, native decoder/parser/input tests and full patch roundtrips. No fresh Dolphin playback, natural travel warp/destination load, natural NPC route, physical GameCube playthrough or actual Card write/restart/reload tested. HD remains deferred. Earlier hardware-sensitive changes remain in prior notes.

Install
Cold-boot this ISO and load an in-game save. Emulator save states can restore old code/data. Original Japanese source uses0.1.2558-test.xdelta; exact public English0.8.2 uses v0.8.2-to-0.1.2558.xdelta. Other English versions should use the supplied test ISO. Retro Trans Tools0.5.21 RVZ conversion remains available; new local patches use its Apply xdelta tab.

ISO: work/output/Tengai-Makyou-II-English-0.1.2558-test.iso
Expanded ISO SHA256: 37b26b16a0390b978ccfa8b33b46be8b902324ae392108a000144057b64bb9d9
Manifest: work/analysis/next-build-drafts-0.1.2558.json
Native: work/analysis/travel-dialogue-native-0.1.2559.json
Proofs: work/analysis/travel-dialogue-proofs-0.1.2562.json
Tools: work/analysis/travel-dialogue-tools-0.1.2561.json
Delivery: work/analysis/tested-travel-dialogue-0.1.2558-2563.json
Retention: work/analysis/output-retention-0.1.2563.json; latest full ISO and nine older original-source xdelta versions. Prior2552 removed only after its original-source patch decoded to its exact hash. Old2487 patch/sidecar removed within retention; immutable public0.8.2 assets unchanged. Tools verification ISOs removed.

## Historical v0.8.2 evidence and inherited limits

# Testing and limitations — v0.8.2

Exact alias of internal0.1.2552/checkpoint0.1.2556; no game-byte edits during release packaging. The current notes below qualify native-only evidence and physical-hardware risks. Live Automatic/RVZ proof is added after publication.



## Internal0.1.2552

Tengai Makyou II — English test0.1.2552 / checkpoint0.1.2556 — 2026-11-07

Requested fix
Remove the full-width space before Hermit Kasaiwa in MAP-062-01-00014f. Replace it with one ordinary interword space; reflow the full four-page utterance, respecting existing page turns,60-character/528px limits, colored name and all native speaker/audio controls. No wording or translation change. Four context rows read, one edited; accuracy/editorial/proofreading decisions and before/after recorded in work/translation/en/ui/field-wrap-0.1.2552-REVIEWED.json. The screenshot is the last page, not a separate script row. All previous fixes, including2545 Item actions/no-effect results, remain installed.

Validation
Three complete native packed-parser cases (slow, fast, confirm); identical packets and complete four-page text, widths and spaces pass. One affected ordinary room through actual native CNS decoder. All9632 ordinary FIELD rows and9632 caller operands read back; all unrelated compressed rooms exact. All31 registered typed descriptors/streams verified; affected room is ordinary, so no new typed-loader route claim. Existing translated allocation reused without growth. Normal Balsamiq actual native-packet proofs for all four pages visually reviewed: work/ui/castle-gap-0.1.2552/MAP-062-01-00014f.png. These are packet proofs, not fresh emulator screenshots/natural conversation playback.
Both original-Japanese full patch and exact public-English0.8.1 upgrade fully decode to the expected1,459,978,240-byte ISO, and pass actual Retro Trans Tools0.5.21 Apply xdelta backend with complete output hash and input preservation. No new Automatic catalog entry or RVZ execution claim; published0.8.1 evidence retained.

Implementation and hardware-sensitive limits
DOL code/data byte-exact2545, no new executable hooks, font edits, static reservation, live backing allocation or decoded-room growth. Existing private padding remains160bytes. MAP compressed archive grows96bytes; header rebuilt; FST and later disc offsets shift2048bytes.1391 unrelated assets, including movies/audio/font, byte-exact2545. Strict inverse restores the original room/DOL and all VM references remain unchanged.
Changed compressed bytes, archive/header sizes and FST offsets can affect DVD loading, stream decoding and real-console transitions. Evidence: strict inverse, unchanged decoded allocation and DOL, actual native CNS/parser cases, exact31 descriptors and all caller readbacks, full asset integrity and patch roundtrips. Native fixtures model selected services/audio endpoints silently; they are not physical GameCube validation. No new Dolphin playback, natural castle conversation/transition, hardware playthrough or Card write/restart/reload test claimed. HD remains deferred. Earlier hardware-sensitive risks and Store constructor regression evidence remain documented in earlier notes.

Install
Cold-boot the new ISO and load an in-game save. Emulator states can restore old script bytes. Original Japanese GT2J18rev0 uses0.1.2552-test.xdelta; exact public English0.8.1 uses v0.8.1-to-0.1.2552.xdelta. Other English versions should use the supplied test ISO. Retro Trans Tools0.5.21 existing RVZ extraction remains supported; no new public release requested.

ISO: work/output/Tengai-Makyou-II-English-0.1.2552-test.iso
Expanded ISO SHA256: 0e615a1a8b1bd6a4faf3ba5b68e890f15ab06d05049c4d774f712429e280b46d
Manifest: work/analysis/next-build-drafts-0.1.2552.json
Native/proofs: work/analysis/castle-gap-native-0.1.2553.json
Tools: work/analysis/castle-gap-tools-0.1.2555.json
Delivery: work/analysis/tested-castle-gap-0.1.2552-2556.json
Retention: work/analysis/output-retention-0.1.2556.json; latest full ISO and nine older original-source xdelta versions. Prior2545 removed only after archive decoded to its exact hash. Immutable public0.8.1 unchanged; private reference/Tools verification ISOs removed.


## Internal0.1.2545

Tengai Makyou II — English test0.1.2545 / checkpoint0.1.2551 — 2026-11-07

Requested translation
Manjimaru gripped the Ear Pick of Love.
But it had no effect.
The short third screenshot is the same action during reveal, not a third source message.

Related scope and review
Translate ten native field Item dispatch streams: eight distinct actions followed by no effect (grip, play, blow, put on, peer into, strike, wave, hold a hand over), plus the grip-only variant and Golden Bug smelly-hands outcome. Retain all actor/item/wait/page controls, existing English item/party names, IDs and native effects. Twelve source rows examined, ten edited, with accuracy/editorial/proofreading decisions in work/translation/en/ui/no-effect-0.1.2545-REVIEWED.json. Neighboring mouth-action and HP-result messages read and left unchanged. No target added to the no-effect result. Kind58 has no ordinary eligible Item definition; exact stream tested after real window construction without claiming natural access.

Implementation and inherited fixes
New immutable strings and two scoped display-name range gates add520 DOL bytes inside the existing reservation. Arena low0x80389000; scene1060704bytes; remaining private padding160bytes. No additional static reservation, live allocation, decoded room or font growth. Actual field Item constructor still provides64x3 backing from2509; no pre-expanded constructor substitute. Dispatch pointers change only inside801caf10..801cb034. Previous old/new healing-name ranges and fallback paths remain supported. Exact inverse restores2538 DOL. All1393 assets, MAP, font, FST, disc offsets, movies/audio and every other disc byte remain exact2538. Earlier dialogue wraps, healing fix and battle-reward translations remain installed.

Validation
-41 native cases total.34 full event-item cases run actual Use/User/Item handoff, constructor, action parser, page waits and state cleanup: Ear Pick across all four actors and full/fast/character reveal (12), eleven related/longest-name items across fast/character reveal (22).
-No-effect leaves exact party stats/HP/MP/inventory unchanged. Golden Bug effect and inventory match old2538 execution. Bounds, native ABI and memory guards pass. Two grip-only exact-stream cases use a real constructed window; one original smelly-effect comparison, two real Kanro healing self/other cases, one older recovery-range case and one actual three-reward producer regression complete41.
-24 visible pages from12 representative actual native packet captures rendered with normal Balsamiq atlas and visually reviewed: work/ui/no-effect-0.1.2545/final-proof/all-pages.png. These are native-packet proofs, not Dolphin screenshots. Older unreviewed2547 diagnostic gallery grouped consecutive one-line pages incorrectly;2550 corrects proof grouping by x/y cursor reset. Native case data and execution remain unchanged. Use only2550 final proofs for visual approval.
-Both original Japanese and exact public English0.8.1 patches fully decode to the target ISO and pass actual Retro Trans Tools0.5.21 Apply xdelta backend with complete output hash and input preservation. No new GUI/Automatic catalog or RVZ execution claimed for this local test. Published0.8.1 Automatic/RVZ evidence remains recorded separately and public files unchanged.

Hardware-sensitive risk and limits
Executable veneers, new control-string addresses, DOL section growth/alignment and display-name gates can affect instruction cache, pointers and real-console memory. Evidence: strict inverse, bounded disjoint-range gates, existing arena/reservation,160-byte padding, all asset/disc readback, native action/effect/ABI/guard/cleanup tests and full patch roundtrips. No extra live/static allocation introduced; previous buffer-growth risks remain in earlier notes. Native fixtures model selected OS/audio endpoints and are silent; they are not real-hardware validation. No new Dolphin playback, natural cave navigation, physical GameCube test, complete playthrough or Memory Card write/restart/reload claim. No font/shop changes; actual Store-entry regression evidence retained from prior work. HD remains deferred.

Install
Cold-boot the new ISO and load an in-game save; emulator states can restore old code/text. Original Japanese GT2J18rev0 uses0.1.2545-test.xdelta. Exact public English0.8.1 uses v0.8.1-to-0.1.2545.xdelta with Retro Trans Tools0.5.21; RVZ extraction uses its existing support. Do not apply the upgrade to a different English build; use the test ISO instead.

ISO: work/output/Tengai-Makyou-II-English-0.1.2545-test.iso
Expanded ISO SHA256: fd26dbb070e063615bb62d12230874b71ebde3db761c3f4bfd42873ef0cb08ea
Manifest: work/analysis/next-build-drafts-0.1.2545.json
Evidence: work/analysis/no-effect-native-0.1.2547.json; work/analysis/no-effect-tools-0.1.2549.json; work/analysis/no-effect-proof-0.1.2550.json; work/analysis/tested-no-effect-0.1.2545-2551.json
Retention: work/analysis/output-retention-0.1.2551.json; latest full ISO + nine older original-source xdelta versions. Prior2538 removed only after archived patch decoded to its exact full hash. Public0.8.1 assets retained. Private public-reference and Tools verification ISOs removed.


## Internal0.1.2538

Tengai Makyou II — English test0.1.2538 / checkpoint0.1.2544 — 2026-11-07

Requested fixes
- Remove the gaps around Owari Province, Owari/Jomon Cave and Kabuki; rewrap all pages of three reported dialogue rows. Preserve wording, colored names and page turns. Seven neighboring FIELD rows read; three edited.
- Translate the actual shared field Item action that earlier recovery work missed. Example: Manjimaru put the Kanro Pill / in their own mouth! Other-recipient example: in Kabuki's mouth! Original actor/item/owner/line/wait/page/nested-result controls stay ordered. Actor/target IDs, HP effect and item consumption remain native.
- Translate actual postbattle1/2/3-item reward formats and English item/equipment name inputs: Obtained Kanro Pill! Each reward gets its own line. Run native getters and sprintf; do not change reward selection or inventory logic. Full11-row accuracy/editorial/proofreading review/count correction evidence: work/analysis/item-gaps-review-0.1.2544.json.

Implementation and inherited behavior
New immutable strings and scoped veneers add1056 DOL bytes within the existing reservation: arena low0x80389000, scene1060704bytes, private padding680bytes. No new static reservation or decoded room/font growth. Original font,1391 other assets, movies/audio, encounters and save format remain exact2529. Compressed MAP delta and FST offset change are recorded in the build manifest; later assets shift2048bytes. All31 typed-room descriptor records remain exact because the two changed rooms are ordinary only.
Actual field Item producer retains the2509 fix and already64x3 backing. Two native dispatch-table pointers select the new shared parent; scoped item/party/owner name adapters admit only its address range and keep all old recovery/refusal fallbacks. For battle loot, only the three formatter call sites and result-clear call are redirected. The result-clear wrapper resizes a smaller reused window to64x3 before parsing and frees old backing; an already64-column window allocates nothing. Maximum live growth versus23x3 is2952bytes, with zero new permanent reservation. No broad parser replacement or original Japanese table mutation.

Validation
-52 native case receipts:9 complete FIELD parser executions in fast/typewriter/confirm modes;2 changed rooms through the actual CNS decoder;32 real Kanro Item menu/effect/action/nested-result cases across all16 actor/recipient pairs in fast and character reveal;2 related healing-item cases;1 old-recovery-range regression;7 actual reward-producer cases for1/2/3 results from23- and64-column contexts plus longest names/equipment.
-Use actual Use/User/Item/Target handoff and native state-machine cleanup. Verify exact HP change, exactly one item consumed, no other party-stat/MP/inventory edits,64x3 shape, full text, bounds, guarded memory/ABI, old/new backing ownership and free. Confirm all34 field Item cases finish and preserve the earlier shared healing fix.
-Execute actual postbattle producer80053c84, original native item/equipment getters, native sprintf, queued reward consumption and state update. Only the battle-condition predicate and selected audio endpoints are modeled. Exact English names,1/2/3 complete lines, full remaining party inventory/stats, backing resize/no-op and native cleanup pass. Current postbattle framebuffer/playback is not claimed.
-All9632 ordinary FIELD rows and9632 VM references read back. Modified ordinary-room streams decode byte-for-byte under native CNS. All31 registered typed bindings/payload hashes checked; no affected typed-room load route exists, so0 extra typed load tests are claimed. work/analysis/item-gaps-loaders-0.1.2543.json records that qualification.
-Every affected page and actual self/other/reward producer packet layout rendered using the normal Balsamiq atlas and reviewed: work/ui/item-gaps-0.1.2538/all-pages.png. These are native-packet proofs, not emulator screenshots or natural navigation.
-Both original Japanese full patch and public English0.8.1 upgrade fully decode to expected ISO hash and pass Retro Trans Tools0.5.21 Apply xdelta backend, preserving inputs. Local test only: no new GitHub release or Automatic catalog entry. Current public0.8.1 assets stay unchanged. Earlier2529 fixes remain installed.

Hardware-sensitive risks and limits
New executable veneers/control pointers, DOL extent/alignment, changed compressed room streams and FST disc offsets can affect optical loading, instruction cache, display ownership and real-console memory. New battle64x3 backing can add2952 live general-heap bytes for a23-column reused result window, with fragmentation/timing risk. Evidence: strict inverse to2529; unchanged arena/heaps/reserve, section bounds/private padding; native formatter/getter/action/decoder/ABI/guard/resize/free cases; complete asset/disc readback and patch roundtrips. Native tests are not physical GameCube validation. No new Dolphin/natural-world/battle replay, exact reported healing location, full playthrough or actual Card write/restart/reload claim. Tests are silent native fixtures; audio endpoints modeled without output. HD remains deferred. Earlier subtitle/alignment and healing-buffer risks remain documented in prior notes.

Installation
Cold-boot new ISO; use an in-game save. Emulator states can restore old code/text. Original Japanese GT2J18rev0 takes0.1.2538-test.xdelta. Exact public English0.8.1 ISO/RVZ takes v0.8.1-to-0.1.2538.xdelta using Retro Trans Tools0.5.21 Apply xdelta with RVZ extraction enabled. Do not apply that upgrade to2529 or another English build. Use the supplied new test ISO for those cases.

ISO: work/output/Tengai-Makyou-II-English-0.1.2538-test.iso
Expanded ISO SHA256: e2bf143ad81d1914118bec2667175b1ffbecee581290d546989d8f2a5885adf1
Manifest: work/analysis/next-build-drafts-0.1.2538.json
Evidence: work/analysis/item-gaps-native-0.1.2539.json; work/analysis/item-gaps-tools-0.1.2541.json; work/analysis/item-gaps-proof-0.1.2542.json; work/analysis/item-gaps-loaders-0.1.2543.json; work/analysis/tested-item-gaps-0.1.2538-2544.json
Retention: work/analysis/output-retention-0.1.2544.json — latest full ISO and nine earlier original-source xdelta versions; prior2529 image removed only after exact archived-patch decoding. Immutable public release assets retained; private0.8.1 and Tools test ISOs removed.


## Internal0.1.2529

Tengai Makyou II — English test0.1.2529 / checkpoint0.1.2533 — 2026-11-07

Scope and changes
Seven reported NPC dialogue layouts, nine installed rows including duplicate Kikotsu Castle/inn scene variants. Remove full-width Japanese padding glyphs, normalize their leftover punctuation aliases to visible English punctuation, restore Boss! It's separation, and rewrap within existing page turns. Colored Jomon Cave, Kikotsu Castle and Owari Province and empty reading/style/speaker/voice/audio controls remain. No English words/meaning, row identity, VM caller operand or page-turn count changed. Three-stage accuracy/editorial/proofreading review in work/translation/en/ui/field-wrap-0.1.2529-REVIEWED.json;24 rows examined including adjacent dialogue, nine edited. Context/limits: work/translation/en/ui/field-wrap-0.1.2533-context-review.json. This is a local test, not a new public release or whole-script spacing cleanup.

Implementation
Reuse all existing translation allocations; pad shorter packed streams with zeroes after terminator. Decoded room sizes and allocations unchanged in eight rooms, including the equal-sized earnest-character replacement. Exact byte-for-byte executable, normal Balsamiq font, heaps, arena low, original audio/movies, gameplay and save format from0.1.2518/public0.8.1. MAP grows544 compressed bytes; disc FST repacking shifts later assets by2048 bytes. All1391 other assets and executable verified exact after repacking. None of the31 typed loader descriptor records changes; rooms outside affected eight retain exact compressed data.

Meaningful validation
-27 complete native packed-parser executions: nine rows in normal typewriter, fast reveal and slow-to-fast confirmation modes. Full glyph sequence, bounds, per-glyph widths/colors, unchanged ordered audio/voice calls, packet guards and source immutability pass; all three modes emit identical complete packets.
-All9632 ordinary FIELD rows and9632 VM operands read back from new MAP; unaffected row metadata exact. Native CNS decoder reconstructs all eight modified rooms byte-for-byte. Empty ruby/color controls retained, comma remains attached to Kikotsu Castle; no leading/trailing line spaces or isolated punctuation lines.
-Every page rendered from actual native packets and current normal-resolution atlas, reviewed visually. These are native-packet layout proofs, not actual NPC screenshots or natural scene navigation. Gallery: work/ui/field-wrap-0.1.2529/all-pages.png.
-Original-source full xdelta and exact public0.8.1 upgrade round-trip to the complete ISO SHA256. Both pass public Retro Trans Tools0.5.21 Apply xdelta backend and preserve inputs. This local test is not published to Automatic; existing public0.8.1/Automatic/RVZ assets remain unchanged.
-Rejected prototype2526 reached the native64-character line boundary on the hut's first line: fast mode completed, but typewriter stopped after64 of209 glyphs. No prototype ISO was delivered. Final2529 uses a60-character line ceiling and passes all27 full-stream cases. Retain prototype data/partial fixtures as diagnostic evidence; they are not current delivery proof.

Hardware-sensitive risks and limits
Modified CNS streams, disc file sizes/FST offsets and native packed text can affect optical loading, decompression, cursor/page rendering and integrity on physical GameCube. Evidence: bounded in-place allocations/strict inverse, host/native decoder equality, complete caller/payload readback, unchanged typed bindings/executable/font, full-disc repack verification and patch round-trips. No new decoded memory, static reservation, heap allocation or renderer instruction. Previous healing-message +2952 live-byte and subtitle-data/alignment risks remain inherited, with earlier evidence retained. Native fixtures and packet proofs are not physical-hardware validation. No new Dolphin session or natural access to all seven conversations, exact reported healing location, actual Card write/restart/reload, or full playthrough claim. Tests are silent; modeled audio services produce no audio. HD remains deferred.

Installation
Use the new ISO and cold boot. For original Japanese GT2J18rev0 use0.1.2529-test.xdelta. For exact public English0.8.1 ISO/RVZ use v0.8.1-to-0.1.2529.xdelta with Retro Trans Tools0.5.21 Apply xdelta and RVZ extraction enabled. Do not use the upgrade on another English build or original Japanese. Save states can retain old code/text; use an in-game save after a fresh boot.

ISO: work/output/Tengai-Makyou-II-English-0.1.2529-test.iso
Expanded ISO SHA256: 989b2215d69958b7409bb56cb1d3b8af33684089b47f11481b6fef45c134e04c
Native evidence: work/analysis/field-wrap-native-0.1.2530.json
Tools evidence: work/analysis/field-wrap-tools-0.1.2532.json
Retention: work/analysis/output-retention-0.1.2533.json — latest full ISO plus nine older original-source patches, all hashes checked; prior2518 full image removed only after its archived patch decoded to the exact hash. Immutable public release assets retained.


## Historical v0.8.1 testing

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

## Live public Automatic and RVZ verification — 2026-11-07

Retro Trans Tools 0.5.21 refreshed the published catalog, downloaded both patches into an initially empty cache and applied them to the actual Japanese original and exact English 0.8.0 images. Both complete outputs matched English 0.8.1, were recognized as current and preserved their inputs. Existing-output/source overwrite refusal passed. Latest and explicit 0.8.1 choose the full or small upgrade patch automatically. Next version only from 0.8.0 reaches 0.8.1; from the Japanese original it deliberately selects the earlier 0.8.0 release. All previous catalog, withdrawn and DCP records stayed unchanged. [Automatic proof](AUTOMATIC-0.8.1.json).

The unchanged downloaded public Windows 0.5.21 EXE also passed actual original RVZ input, a live catalog refresh, live patch download and RVZ output. Independent extraction reproduced the exact 0.8.1 ISO hash; current recognition, source preservation and existing-output refusal passed. Private full-disc outputs were removed. The test used packaged Automatic entry points, not GUI clicking or a gameplay test. [RVZ proof](RVZ-0.8.1.json).

Hosted package-registration/catalog validation: [successful scoped workflow](https://github.com/retro-trans/retro-trans-tools/actions/runs/42294866155). No physical-hardware claims are added.


## Live public installation verification — 2026-11-07

Live Automatic with Retro Trans Tools 0.5.21 passed for the Japanese original, English v0.8.0 and English v0.8.1: fresh catalog/patch downloads, exact complete output hashes, current-version recognition, preserved inputs and overwrite refusal. v0.8.0 upgrades through v0.8.1 in two steps; Latest and explicit v0.8.2 select verified routes. Existing catalog identities and old release assets are preserved. [Automatic evidence](https://github.com/retro-trans/Tengai-Makyou-II/blob/main/docs/AUTOMATIC-0.8.2.json).

The unchanged published Windows 0.5.21 EXE also passed real original RVZ input → Automatic → RVZ output → independent extraction to the exact v0.8.2 ISO. It uses isolated fresh app data/cache, preserves its source and refuses existing outputs. This executes packaged command entry points, not GUI clicking or game playback. [RVZ evidence](https://github.com/retro-trans/Tengai-Makyou-II/blob/main/docs/RVZ-0.8.2.json). [Scoped catalog workflow](https://github.com/retro-trans/retro-trans-tools/actions/runs/42337820443).

These installation checks add no physical hardware or game-playback validation. Initial uploaded installation/testing assets stay immutable; this repository and release body contain the completed live evidence.

## Live public installation verification — 2026-11-13

Live **Retro Trans Tools 0.5.23 Automatic** passed from the Japanese original and public English **v0.8.0, v0.8.1 and v0.8.2**. Fresh catalog and patch downloads produced the exact v0.8.3 ISO, recognized it as current, preserved all inputs and rejected overwriting existing files. Explicit v0.8.3 and Latest routes select the correct updates, and Next version only retains the original version sequence. [Automatic evidence](https://github.com/retro-trans/Tengai-Makyou-II/blob/main/docs/AUTOMATIC-0.8.3.json).

The published **Windows v0.5.23 app** passed original **RVZ → Automatic → RVZ** with a fresh app cache and live downloads. Independent extraction reproduced the complete v0.8.3 ISO hash. These are installation tests. Game playback and physical hardware were not exercised. [RVZ evidence](https://github.com/retro-trans/Tengai-Makyou-II/blob/main/docs/RVZ-0.8.3.json). [Catalog refresh](https://github.com/retro-trans/retro-trans-tools/actions/runs/43404204018).
