# Testing and limitations — v0.8.5

Translation remains in progress; Japanese text and errors may remain. This release is byte-identical to the tested 0.8.5 controls image and retains the preceding newspaper, dialogue-page and handover fixes. Silent native checks passed for the stated message/menu families. No new Dolphin playthrough, natural scene-transition traversal, physical GameCube test or memory-card write/restart/reload test was performed. Patch installation verification is not game or real-hardware validation.

Hardware-sensitive changes since v0.8.4 include newspaper display pointers and a constructor hook, a 4,096-byte larger private reservation, 2,952 extra live bytes per eligible article context, dynamic text lengths/name-return phases, compressed room/header/FST bindings, and event/controller UI hooks and display pointers. Final scene space is 1,040,224 bytes; private slack is 948 bytes. Captured allocation replay for the newspaper change leaves 347,136 bytes at peak with the documented complete-model budget and 256 KiB reserve. Full gameplay peaks, fragmentation and console timing remain unverified. Normal-resolution Balsamiq font, movies, audio and save formats are unchanged. Detailed test notes record the stale Field fixture and modeled graphics/paired-single limits.

## Complete newspapers


Installed changes and complete family audit
All16 newspaper article bodies are translated and installed, including the
reported Manjimaru/Benten story. All3 seller templates are also translated:
introduction with dynamic article insertion and read-another question, farewell,
and insufficient funds. Existing16 complete headlines, prices, money row and
native selection order are retained and rechecked. Body text has54 pages;
the three seller templates add4 pages. No article or paragraph was omitted.

Root cause and durable coverage gate
The earlier catalogue covered headline pointers, not the separate control-bearing
article strings. The earlier native headline test explicitly modeled article
completion. Neither established article-body translation. The new coverage gate
follows every pointer in native table801eff40:16 bodies plus3 seller strings,
checks complete English bytes, and requires actual article reading receipts.
Keep this gate for later builds rather than counting catalogue rows alone.
Coverage: work/analysis/news-coverage-0.8.5.json

Translation review
All19 records were compared with complete source paragraphs in order, then
independently checked for accuracy and editorial voice and finally proofread.
Corrected the island-pulling direction in the Izumo article. Preserved tabloid
innuendo, the princess's age16, thousand-year celibacy, one-month delay, false
claims about Kinu, same-gender romance, sewage and domestic violence. The Ni Hao
article retains China as the paper's allegation; China/Chugoku is ambiguous in
the unannotated source. Purisos Hotel is a source-kana romanization; no independent
approved English form is claimed. Original Japanese scripts stay in the source
DOL; the new review inventory stores English, IDs, source hashes and decisions.

Display and native tests
The actual article/refusal constructor gets durable64x3 backing. The24px normal
Balsamiq font, original600x156 frame, original line pitch and input behavior stay.
English is wrapped by measured widths to528px, reserving the continuation arrow's
third-line area. No HD font or audio/movie asset changes.

24 silent native cases passed: all16 complete slow typed articles, fast
reveal, insufficient funds, Back, both repeat choices and native global completion,
three consecutive paid readings returning to the existing selector, all16
headlines and two menu reopens, scene/general/save heap pressure, actual General
Store transactions/highlights/Buy/Sell/funds/Back/Exit and four store reopens.
The native03/01 article insertion, return stack, page waits/clears and final
question execute; article completion is no longer faked. Initial panel fades and
fade-out completion remain modeled. Native ABI, buffer guards,512-entry queue,
full text order, visible bounds, arrow clearance and balanced cleanup passed.
Three font/geometry proof images were visually inspected. These use native game
glyph positions with schematic backgrounds; they are not emulator screenshots.

Hardware-sensitive changes, evidence and limits
DOL grows5628 bytes. Nineteen display pointers and a source-qualified
constructor branch change; strict inverse restores exact0.8.4 DOL. Original
article strings remain untouched. Native unlock checks, prices90, inventory,
gameplay and save data formats do not change. All non-DOL disc bytes, asset
offsets, MAP/header, normal fonts, movies and audio are byte exact.

Private boot reservation grows4096 bytes to0x8038e000;
remaining private space1676 bytes; scene space becomes
1040224 bytes. Article backing23x3/1656 ->64x3/4608 adds2952 live bytes
per eligible context. Allocation replay includes1151 captured requests,
201376-byte complete-model budget,256KiB reserve and the previously failed1KiB
request; it leaves347136 bytes at peak and releases exactly.
General/save pressure also passes with an extra37248-byte live allocation,
representing32640 newspaper +4608 article backing. These are replayed pressure
scenarios, not full gameplay peaks or fragmentation guarantees. The documented
scene test threshold is300000 bytes, not the older400000 threshold.

Branches, relocated strings, arena changes and larger live backing could affect
console memory/timing. Native fixtures are not physical GameCube validation.
No Dolphin playback, natural NPC traversal, scene-transition playthrough, live
voice synchronization or memory-card write/restart/reload was performed. Tests
intercepted sound endpoints and were silent. Full game translation/validation is
not claimed. Public v0.8.4 stays published; VERSION remains0.8.4 until publication.

Both original Japanese and exact public0.8.4 source patches independently decode
to the same full ISO hash and pass published Retro Trans Tools0.5.23 Apply xdelta.
This is a local test build; Automatic catalog/public GitHub release is unchanged.
Only the new full ISO is retained; prior0.8.4 is restorable from its published
original-source patch. Current +9 historical source patches retained; older test
0.1.2605 patches retired, published assets and historical evidence preserved.

Cold boot the new image and load an in-game save. Emulator save states can
restore old code and old Japanese strings.
ISO: work/output/Tengai-Makyou-II-English-v0.8.5-test.iso
SHA-256: d90c8e7d6964bca4f38d7cf38df12ea70754b9ad83ee5dbb6eee311cbc19faca

## Blank dialogue page correction


Reported issue and reproduction
Confirmed the three screenshots as MAP-028-00-0015bb and the parallel scene
variants MAP-029-00-0015bb / MAP-030-00-0015bb. The previous word stream produces
three acknowledgements: first text, empty box, next text. The new stream produces
exactly the two populated pages, in the same order. Actual native Update/Confirm
reproduced before and after behavior for all three variants.

Cause and category-wide correction
When a source newline follows the third displayed line, the compiler/reflow
inserted F59 automatically. If the authored script next contains F59, the result
is F59(layout), FE(authored), F59(authored): two successive page stops with no text
between them. Remove only the first, explicitly tagged layout F59. All authored
words, newline/page controls, color controls, opaque parameters, waits, voice and
audio commands stay byte-for-word identical and in the same order.

Complete installed inventory:9639 ordinary +87 dynamic-name messages =9726.
Corrected1973 ordinary records plus8 dynamic records, in722 decoded rooms,
removing2711 redundant blank acknowledgements. All remaining installed records
were audited; original intentionally authored page breaks are retained. This is
a fixed message family, not a claim that every game translation is complete.

Future prevention
The shared field compiler and reflow helper apply the same selective repair when
called with release version0.8.5 or later. Historical version behavior remains
reproducible. The gate tests fresh compilation, reflow and intentionally authored
blank pages; metadata and packed words must preserve the complete authored stream.
The installed repair consumes proven layout tags rather than editing translations.
No editorial wording, name, speaker, voice or story changes were made.

Verification
Every affected ordinary row passed the actual native packed parser in modes3/6:
1973 records x2 =3946 complete messages. Complete glyph order, audio/voice calls,
packet bounds/guards and nonempty page stops were checked. Existing hidden source
glyph aliases505/524 ->3753 are included in expected glyphs; they remain unchanged.
All8 changed dynamic messages passed four party names, both modes and four native
loader routes,256 complete messages total, with name insertion, returned byte/
nibble phase, lifetime, source-room immutability and native cleanup checked.
The newspaper introduction/article/return/repeated purchases, actual General Store
entry/highlights/Buy/Sell/funds/Back/Exit and four store reopens also passed.

The static installed-image gate directly checks7343 records in changed rooms;
unchanged rooms retain byte-exact compressed streams. Every related display
reference is preserved. All31 typed-room checksum/descriptors and87 DOL payload
copies/name sites match the final MAP. All19 newspaper body/seller payloads and
their constructor code remain exact. Native-font before/after proof was inspected;
panels are schematic, not emulator screenshots. All tests were silent.

Hardware-sensitive changes and limits
No DOL code branches, text renderer instructions, font cells, save data formats,
buffer sizes, private reservation or decoded room sizes change. DOL file length
is exact. Arena0x8038e000, scene space1040224 bytes and private
slack1676 bytes are inherited unchanged from the news test.
There are42 data rewrites: shorter dynamic payload copies, exact
length/end values, shifted F80 return byte/nibble phases and typed-room integrity/
compressed descriptor bindings. Incorrect values could break name expansion or
room loading on hardware; native name/loader and complete structural gates passed.

Room text is rewritten inside its existing allocation; no decoded-room growth.
The unchanged compressed prefix is reused, and only the English tail is recompressed
with the same native CNS format. All722 streams round-trip and inverse checks
recover the preceding decoded bytes exactly. MAP shrinks150368 bytes; cached
headers and FST MAP size are updated without moving any disc asset. Native CNS
decode is exercised on the two changed dynamic rooms through all four routes.
Other722-room decoding is a format/round-trip check, not full console traversal.
The initial literalized compression prototype exceeded the existing ISO file gap;
it was not packaged. Its evidence is retained under paging-initial. The delivered
tail compression fits, with no file relocation, extra RAM, graphics or audio change.

All unrelated ISO bytes, normal-resolution Balsamiq font, movies and audio remain
exact. Original Japanese, public0.8.4 and the preceding0.8.5 news-test patch routes
independently decode to the same ISO and pass published Retro Trans Tools0.5.23
Apply xdelta. Public GitHub release/catalog remains0.8.4; this is updated unpublished
0.8.5 work, following VERSION. The news-test image is retained as its source patch.

Native harnesses model sound/GPU/DVD endpoints and presentation fades. No Dolphin
playthrough, natural NPC traversal, physical GameCube test, timing/sync validation
or memory-card write/restart/reload occurred. Native passes are not hardware
validation. Cold boot this image and load an in-game save; emulator states can
restore older code, room data and duplicated page breaks.

Image: work/output/Tengai-Makyou-II-English-v0.8.5-paging-test.iso
SHA-256: cf5c3e2adfeba4a7e765aa919df3befb3b245a627319e626eebae196006e5b37
Coverage: work/analysis/paging-coverage-0.8.5.json
Native: work/analysis/paging-native-0.8.5.json
Retro Trans Tools: work/analysis/paging-tools-0.8.5.json

## Event item handover


Reported screen and correction
The event-driven item Give selector still showed a Japanese question, an
interparty divider over its last item row, and a clipped Can use row behind the
list. It is a separate category5 picker from the redesigned Field Give/Exchange.
The heading is now "Which item will you give?" in normal Balsamiq Sans Regular.
Decorative party dividers and the irrelevant eligibility row are suppressed only
for this event picker. Native owner names, slots, rows and selection results stay
unchanged. No item wording, descriptions, inventory data or funds were modified.

Why the text escaped earlier lookup
The catalogue source row DOL-0017ed0f begins one byte before the actual heading
at0x80181d10. Constructor0x80063b88 copies23 bytes into a stack buffer rather than
using a relocated string pointer. The full English question plus NUL needs25
bytes. The draw-call wrapper supplies its full relocated string directly.
Accuracy, editorial and proofreading review are recorded in the UI review JSON.

Category-wide native checks
Actual seeded constructor/callback, not a precreated larger header, passed14
paired baseline/new cases: Confirm/Back for each actor0/1/2/3 alone, pair0+1,
sparse1+3 and full0+1+2+3. Navigation crosses owner columns and last rows. Native
owner/item/slot and complete selector state match the baseline, inventories and
funds stay exact during picking, native cleanup/heap guards pass. All125 item IDs
pass full English title/description, top-panel bounds and no eligibility row.
Shared divider categories0..6 were compared before/after; only category5 changes.
The exact inverse of the three hooks and appended section returns the paging DOL.
The actual General Store workflow and reopens pass. No extra backing is allocated.

Older Field fixture limitation
The old synthetic Give/Exchange focus fixture fails before and after this change
with identical selector state. The real-entry fixture kinds1..3 also hits the
same assertion on baseline/new; kind4 actual entry/Back passes both. These are
reported as baseline-equivalent fixture outcomes, not successful Give/Exchange
transaction coverage. The category guards and strict inverse preserve unrelated
menu instructions, but full transfer transaction matrices were not replayed.

Visual proof
Native normal-font glyph quads were rendered and inspected. The English heading,
description and item rows fit. Panels are schematic, not emulator screenshots;
selection highlight and owner post-draw labels are not rendered in this proof.

Hardware-sensitive changes, evidence and limits
Three branches/calls are redirected: actual heading draw0x80063c54, shared divider
call0x800bbb64, and eligibility entry0x80379824. The wrappers use volatile r7/r12;
non-event eligibility executes its original stack prologue/body, and non-event
dividers tail-call their original routine. Wrong branch, ABI or category checks
could break native menus on hardware. Actual event constructor/callback, guards,
scope comparison and strict inverse checks pass. These are native-harness checks,
not real-hardware validation.

The DOL grows76 bytes inside the existing private reservation.
Arena0x8038e000, scene space1040224 bytes, no additional RAM
reservation, backing resize or decoded-room growth; private slack is now
1600 bytes. The appended DOL bytes fit verified zero
padding at the same disc offset. All other ISO bytes, MAP, Map_Header, normal
font, movies and audio remain exact relative to the paging test. All earlier news
translations and the1981-record blank-page correction are retained.

All tests were silent; sound/GPU services and fades are modeled. No Dolphin
playthrough, natural NPC access/item deduction, timing/sync, physical GameCube or
memory-card write/restart/reload was tested. Cold boot this ISO and load an
in-game save; emulator states can restore old code and text.

Original Japanese, public0.8.4 and exact preceding0.8.5 paging-test patch routes
independently decode to the same complete ISO. Published Retro Trans Tools0.5.23
Apply xdelta passes all three routes and preserves source images. Public VERSION
and GitHub release remain0.8.4; this is unpublished0.8.5 work. The preceding
paging image is retained as its original-source patch with its exact hash.

Image: work/output/Tengai-Makyou-II-English-v0.8.5-handover-test.iso
SHA-256: 42455907559f688cccd159f49d81f01521773f22d7b86e4fcfd27bb3da88b68f
Coverage: work/analysis/handover-coverage-0.8.5.json
Native: work/analysis/handover-native-0.8.5.json
Proof: work/analysis/handover-proofs-0.8.5.json
Patch application: work/analysis/handover-tools-0.8.5.json

## Complete controller layouts


Installed translation and family audit
Translate the reported Control Settings screen and all four control presets,
including Type1..4, Back, the choose/apply instructions, unchanged-Back help and
application question. Translate all12 unique Y/X/A/B/LR binding strings, Type3's
X continuation, Type4's combined Talk/Confirm + Fast-Forward action, movement,
camera and Z reset legends.20 unique English payloads; repeated table aliases
share the appropriate target. Preserve native row gaps, null continuations,
button identities and all actual input-mapping data. Accuracy, editorial and
proofreading stages are recorded in the reviewed UI JSON.

Why prior plain-string scans missed it
The child has its own title/list producer and three help pointers. The controller
diagram uses a direct renderer rather than the plain window parser, so existing
English pointer annotations did not apply. Draw18px normal Balsamiq labels through
scoped call wrappers and restore the caller font after each label. The existing
24px menu/help renderer and original headers/backing sizes remain unchanged.
The native post-draw heading reposition operation also needs the full English
glyph count16 instead of the original9. An initial prototype exposed a scrambled
heading in visual QA; that rejected prototype is retained under controls-initial.
The delivered heading has ordered, nonoverlapping, centered glyphs on one row.

Native verification
Seed the existing main Settings Custom selection, then execute its actual native
decision, both real child constructors/allocations and callback. No enlarged
fixture headers stand in for constructor coverage. For all four initial presets,
exercise native Up/Down, wrap across Back, Confirm Yes/No, cancellation of the
question and direct Back.16 scenarios compare baseline/new navigation, settings,
confirmation/cancel masks and cleanup exactly. Applying a preset changes only
the original control setting. Four additional apply/exit/reopen flows preserve
that setting and select the correct preset. Native guards and nonvolatile ABI
pass; complete labels and normal font bounds pass for each diagram. All three
help states are English. The real General Store Buy/Sell/funds/highlight/Back/
Exit workflow and reopens also pass.

Four native-glyph layout proofs were inspected, including both combined-action
variants. Panels are schematic; connector lines and selection highlight are
omitted. Diagram text/graphics use the actual native callback and rendering queue.
The harness models SDK rotation math because Unicorn lacks Gekko paired-single
matrix instructions. The two redundant paired f31 spills are modeled; native
stfd/lfd save/restore, ordinary arithmetic, string rendering and ABI execute.
Sound/GPU services and presentation fades are modeled. All tests were silent.

Hardware-sensitive changes and limits
36 scoped display rewrites:24 English display-table pointers,
11 title/list/direct-render call redirects, and the title glyph-count immediate.
The shared input mapping/application routines, button tables, native save format
and selector IDs remain exact. An incorrect pointer, branch, font restoration or
count could break menus on a physical GameCube. Native decisions, pointer/target
checks, restored fonts/ABI, guards, complete diagram labels and strict inverse
checks pass. Native passes do not constitute real-hardware validation.

DOL growth652 bytes fits verified zero disc padding and the existing
private reservation. Arena0x8038e000, scene space1040224 bytes,
private slack948 bytes. No backing resize, extra RAM,
decoded-room growth, font rebuild, movie or audio change. Undoing the36 scoped
rewrites and appended section recovers the preceding handover DOL exactly.
All non-DOL ISO bytes, MAP, Map_Header and font remain byte-exact. The previous
event handover, all16 newspaper articles and1981-message paging fixes are retained.

Original Japanese, public0.8.4 and preceding0.8.5 handover-test routes decode to
the same complete ISO. Published Retro Trans Tools0.5.23 Apply xdelta passes all
three, with source images preserved. VERSION/GitHub remain public0.8.4; this is
updated unpublished0.8.5. The previous full test image is retained as a source
patch with its exact revision hash, within the ten-revision retention limit.

No natural controller/GPU playthrough, Dolphin playback, physical GameCube,
timing/sync or memory-card write/restart/reload validation occurred. Settings
persist across menu reopen in the native fixture; disk save/reload is untested.
Cold boot this image and load an in-game save; emulator states can restore old
menu code, strings and fonts.

Image: work/output/Tengai-Makyou-II-English-v0.8.5-controls-test.iso
SHA-256: eea819dee7e887c78e44eb2439d903b79f1764c5cdc93efce2ed2c9b7cbec3eb
Coverage: work/analysis/controls-coverage-0.8.5.json
Native: work/analysis/controls-native-complete-0.8.5.json
Proofs: work/analysis/controls-proofs-0.8.5.json
Patch application: work/analysis/controls-tools-0.8.5.json

## Inherited release evidence

Earlier tests and remaining limitations are retained in [v0.8.4 testing notes](https://github.com/retro-trans/Tengai-Makyou-II/blob/v0.8.4/docs/TESTING.md). Historical evidence is not a new playthrough or hardware validation.
