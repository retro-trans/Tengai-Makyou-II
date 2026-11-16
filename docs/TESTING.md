# Testing and limitations — v0.8.4

Translation is still in progress; Japanese text and errors may remain. The updated game code and larger UI buffers passed silent native checks, but no new Dolphin playthrough, natural scene-transition test, physical GameCube test or real memory-card write/restart/reload test occurred. Installation verification does not establish game or real-hardware compatibility.

Hardware-sensitive changes since v0.8.3 include equipment/name lookup branches, item-message expansion and constructor hooks, wider province/Lottery/newspaper/Commodity buffers, new display pointers and compressed room/header/FST updates. The new newspaper backing alone adds 27,672 live bytes; Commodity table backing adds 8,208 bytes, parent prompt backing can add 5,760 bytes, and each updated Sell child adds 2,688 bytes. The final scene space is 1,044,320 bytes. Captured allocation replay with the complete-model budget and 256 KiB reserve leaves 351,232 bytes at peak, above the documented 300,000 test margin but below the older 400,000 margin. Full gameplay peaks, fragmentation, timing and console execution remain unverified. Detailed evidence and limits are in the testing notes.

The following retained category notes describe evidence inherited by this exact release. Historical filenames and source evidence are unchanged.

## Equipment names


Yamainu Helmet and related equipment names
Treasure acquisition now reads Found Yamainu Helmet! The English name remains
visible after Equip, with the original DEF12. The same correction covers all
13 names in the later equipment-name bank. Eight older direct lookups now use
the complete357-name equipment/item bank: the legacy found notice, scoped
treasure insert, and all six inserts in one/two/three battle reward formats.
The69-scroll name map remains separate and unchanged.

The field list/equipped name wrapper now distinguishes the original label bank
from extension markers20000..20012. Previously the extension marker indexed
past the original bank, explaining the blank label and a native unmapped read
in the reproduction. The name, source strings, game IDs, eligibility, stats,
equipment records, inventory logic and translations are unchanged.

Category audit and verification
All237 native gear IDs were displayed through actual equipment-choice
constructors and the native equipped-row producer, including complete glyph
and bounds checks. Display fixtures deliberately seed IDs regardless of the
chosen actor's eligibility. Separately, all13 extension items were equipped
through real native menu confirmation/eligibility and their names checked on
reopening. Ordinary items were also removed through native entry0. Cursed
items preserve their original flag and native removal refusal; the fixture
models announcement dismissal for teardown, rather than executing its later
game-loop resume.
Equipment IDs, flags and derived-stat updates exactly matched public0.8.3
under the same native confirmation inputs and party records.
Both legacy357 and scoped426 equipment/item/scroll substitutions passed.
All13 names passed the related treasure/find/obtain/give-up/discard variants
in full, line and character reveal modes, and real battle result production
with one/two/three rewards. Alternate ordinary/storage/overview label markers
and three native colors were checked for all13 names. The451 older wrapped
labels and the Yamainu shop highlight/quote/No path also passed.
Native audio endpoints were intercepted and silent. The preview composites
the captured native glyphs/coordinates onto schematic panels; it is not a
Dolphin screenshot. Both original-source and publicv0.8.3 upgrade patches
reproduced the complete ISO through Retro Trans Tools0.5.23 Apply xdelta.

Hardware-sensitive changes and limits
Eight pointer/count instruction groups change from344 to357-name lookup.
The wrapped-name code calls a bounded two-bank resolver placed in140 bytes
of an already bypassed secondary bitmap scan. The unconditional fallback
before that retired body remains unchanged; a direct-branch audit found no
outside entries into the reclaimed body. Saved registers, stack and existing
rendering behavior pass native ABI/queue/cleanup checks. These code/branch
changes can affect console execution and rendering. No DOL size, arena,
static memory reservation, heap allocation, backing dimensions, font or
other disc byte changes. The strict inverse restores0.1.2615 exactly.
Native tests model peripheral GPU/audio services and fade completion. They
do not validate natural chest navigation, the curse announcement's later
game-loop resume, scene memory pressure, a complete
playthrough, Dolphin's actual GPU output or physical GameCube execution.
No new Dolphin session or real-hardware test was performed.

Start the new ISO and load an in-game save.
ISO work/output/Tengai-Makyou-II-English-0.1.2620-test.iso
SHA-256 017e7757b572260485067c6de6ea9c63f67f400c8221cd504c0cc9aa0deb903d

## Province destinations and item actions


Province destinations
All17 province names are English in both native province-record tables.
This includes Hida, Owari, Ise and Kii in the screenshot. The three province
grid paths use a wider16x9 backing at20px, with two8-cell columns and matching
native highlight geometry. The frame is368x228 at136,120. The original
17 destination indices, visited checks, flags and coordinates are unchanged.
The separate village picker retains full English village/town names.

Field item actions
The missed Transformation Seal action now says the actor considered trying
it but decided against it. The related drawing action says the actor looked
at the item and it shows a poorly drawn boat. Actor/item names and every
original line/page/wait control are retained. Native kind5 and kind0 items
were audited through actual Item Use, including otherwise uncommon items
which share the original fallback action. No item effect is invented.

All10 older mouth-action/recovery streams now use a complete owner phrase:
their own mouth for self, or the recipient's English possessive name for
another party member. The Japanese self label and duplicate apostrophe-s
are removed. The newer shared mouth action and non-owner group suffixes
retain their existing behavior. Actual Seiryo Pill, Buckwheat Dumpling and
Kanro Pill effects/inventory changes exactly match0.1.2620.

Validation
Nine old/new province-construction cases cover three actual native opening
blocks with no visits, the pictured first four visits, and all17 visits.
Complete glyphs, bounds, highlights,44 directional inputs per case, native
cleanup and original cursor-index sequences passed. Both17-record tables
retain all12 non-display bytes. Every kind0/kind5 item, all four actors and
both line/character reveal modes were exercised through the native Item
handoff. Ten mouth variants cover all four actors with self/other targets
and full/line/character reveal. Actual item use compares native effects and
party bytes with the prior build. Password construction, both answers,
wrong answers and editing controls passed, as did existing village/travel
item and escape-scroll paths. Audio endpoints were intercepted and silent.
Both patches reproduce the entire ISO through Retro Trans Tools0.5.23.
The proof uses native glyph coordinates on schematic panels.

Hardware-sensitive changes and limits
Province backings grow from5x9 to16x9, requesting2376 additional live bytes
before allocator rounding. Province fonts change24 to20 and column/highlight
geometry changes with them. Display pointers change in both province tables,
two parser call sites use direct native ASCII, and two new item streams are
admitted to the existing actor/item lookup. A bounded owner adapter covers
the older recovery prefixes. These allocations, pointers and branches can
affect console heap pressure, timing and rendering. New strings/helpers use
verified unreferenced NOP padding after rewritten password return points;
all claimed padding has no existing direct branch or pointer references.
There is no DOL-size, arena, static-reservation, MAP, font-asset or other disc
byte growth/change. The strict inverse restores0.1.2620.

Native tests seed visit flags, execute original opening blocks and model
peripheral GPU/audio services and completed fade/message flags. They do not
validate natural access, the final teleport/scene load, memory pressure in
a live scene, memory-card write/reload or physical GameCube play. No new
Dolphin session or real-hardware test was performed.

Load an in-game save with the new ISO.
ISO work/output/Tengai-Makyou-II-English-0.1.2625-test.iso
SHA-256 d26caf6990e5598b9d84f42beeb34ed6799c69faf84781545a6c83e69e5eab1a

## Equipment curse notices


Equipment curse notices
The pictured post-equip discovery now displays the complete equipment name
on the first line and Cursed! on the second. This reports the item's cursed
status without implying that equipping cast a new curse. Existing canonical
equipment names, native equipment flags, eligibility and stat calculations
are retained.

Category-wide audit
Five source variants were audited: curse discovery at80189ae0, removal at
80189a88,8018a428 and8018a484, and storage at80187a88. The missed discovery
and alternate equipment removal now use the shared complete English name
formatter. The storage source is defensively covered by that formatter;
its actual Storage Counter path already uses a separate English formatter
and was verified as well. The two existing equipment/item cannot-be-sold
variants8018a44c and8018a468 retain their complete English names and warnings.
Enemy curse attacks/status effects are a different message family and were
not modified. Review records include accuracy, editorial and proofreading.

Validation
1547 native constructor/parser cases cover all237 equipment IDs in six
variants and all125 item IDs in the item-sale variant. Full names, suffixes,
durable source buffers, ABI, native glyph queues and free/guard checks pass.
The12 longest gear names were checked against all six gear variants for
both horizontal and vertical message-frame bounds. Native reveal/update and
Confirm completion pass in26 cases covering both ordinary and accelerated
reveal, Tacky Clothes and Queen's Crown, across all seven variants.

Actual native equipment callbacks equip Tacky Clothes on Kabuki and Queen's
Crown on Kinu, display Cursed!, and retain the0x80 curse flag. Their complete
400-byte party records before/after equip exactly match0.1.2625. Reopening
with those exact cursed records retains the English equipped name; attempts
to change the slot produce the translated refusal before a replacement
chooser can open, with no party mutation. Equipment modal dismissal is
modeled for fixture teardown rather than performed by the full game loop.

Actual Storage Counter entry rejects cursed Tacky Clothes, displays its
existing English warning, returns through state3 to Gear state2, then exits
and frees all four live allocations. Party/inventory/funds stay exact.
General Store actual entry, long highlights and scrolling, Buy/Sell
confirmations, funds, Back/Exit and four same-pool reopens pass. Actual Sell
refuses unsellable/cursed gear, then an ordinary sale changes funds once.
Password native construction, both accepted answers, wrong answers and
editing controls pass after reuse of retired password padding.

Retro Trans Tools0.5.23 Apply xdelta reproduces the entire ISO from both
the clean Japanese source and exact public Englishv0.8.3. Both patches also
pass complete independent xdelta decode/hash checks. Public release assets
are unchanged. The preview uses native glyph positions on schematic panels.
All tests are silent native-game-code fixtures with peripheral services
modeled. No Dolphin session or physical console test was performed.

Hardware-sensitive changes and limits
The CP932 constructor gate now recognizes seven exact message sources,
with the original fallback for all others. The old84-byte gate is reused
as a suffix selector, preserving default sale and earlier curse suffixes.
New text and the132-byte gate occupy verified unreferenced retired password
NOP padding. Pointer/branch scans found no code entry into the reclaimed
gate except the replaced constructor hook; one timed-caption data word
resembles a conditional branch and was explicitly classified/left exact.

The three newly admitted fallback sources use the existing64x3 backing,
4608 bytes rather than1656:2952 additional live bytes before rounding.
Actual Storage uses its existing separate formatter. New branches, pointer
choices and potentially larger temporary allocations may affect console
timing, memory pressure or rendering. The static256-byte refusal buffer
is reused; the fixture verifies stable text during delayed reveal. Natural
field/shop scene access, concurrent modal ownership, live-scene heap
pressure, memory-card write/reload and real GameCube behavior remain
unverified. Native passes are not hardware validation.

The DOL has no size/arena/static-reservation growth. All disc bytes outside
the DOL, MAP files and normal Balsamiq font assets match0.1.2625. A strict
inverse restores the previous DOL exactly. Start the new ISO and load an
in-game save.

ISO work/output/Tengai-Makyou-II-English-0.1.2630-test.iso
SHA-256 4780fedb0e97f706cb4856d5a226a5fe1134d6c91bae7f230f2b7196dd5d0e6f

## Shop titles


Shop title category
The reported title is now Traveling Merchant. All14 native title IDs were
audited through actual shop entry800e0af0 and callback800de650. Ten missed
titles are translated: Kimono Shop, Pharmacy, Women's Shop, Accessories
Shop, Traveling Merchant, Open-Air Market, Swordsmith, Doll Shop, Pick the
Winner!, and General Goods. Equipment Shop, Item Shop, General Store and
Tea House retain their existing terminology. The General Store table entry
now points to its existing English string directly. Only display pointers
change; title IDs, stock registrations, prices and transactions are retained.
The separate storage/inn interfaces are outside this fourteen-title family.

The existing shop layout did not consistently center these English strings.
After the title is parsed, row0 now uses the existing proportional Sell-quote
centering routine. All14 headings center within1 native pixel of320 and
retain complete English glyphs inside the600px frame. Buy/Sell/Cancel rows,
selectors and their input handling retain their original behavior.

Validation
All14 actual shop constructors/open callbacks and close/free paths passed.
Each verifies the real48x5 top backing, complete title and main labels,
normal English font page, glyph bounds and measured title center. The
Traveling Merchant native workflow executes11 highlights,44 repeated
highlights/scrolls, purchase confirmation/recipient/funds deduction, Sell
category/confirmation/funds update, Back and Exit. The General Store runs
the same transaction workflow and four same-pool reopens. This is real
constructor coverage, not a precreated larger header.

Native password construction, both correct answers, wrong answers and
editing passed after reuse of retired password padding. All audio endpoints
are silent. Stock/party are seeded, fades and peripheral services modeled;
natural map/NPC access was not exercised. The preview shows only the title
and action row using native glyph coordinates on a schematic panel.

Both original-source and publicEnglishv0.8.3 upgrade patches reproduce the
entire ISO with Retro Trans Tools0.5.23 Apply xdelta and independent complete
xdelta decode/hash checks. Immutable public release assets stay exact.

Hardware-sensitive changes and limits
Eleven title-table display pointers change, including the direct English
General Store pointer.138 bytes of complete strings and a24-byte alignment
wrapper use verified unreachable, unreferenced NOP padding after rewritten
password routines. A single branch replaces the shop callback's load at
800de924; the wrapper reloads the original context, calls existing helper
8037798c for title row0, reloads the context and returns to800de928. The
native outer callback already saves LR; the existing helper saves its
nonvolatile registers. Its code bytes are verified exact against2082.
Pointer/branch scans verify only the claimed padding ranges; original
password branch-to800b0048 remains exact and skips the added title data.

These display pointers and the scoped callback branch can affect console
rendering or timing. No DOL-size, arena, static-reservation, glyph-backing,
font-asset or other disc-byte growth occurs. All non-DOL bytes match2630;
strict inverse restores its complete DOL. Native fixture passes do not
validate live-scene heap pressure, natural scene transitions, memory-card
write/reload or physical GameCube behavior. No Dolphin or hardware test was
performed. Start the new ISO and load an in-game save.

ISO work/output/Tengai-Makyou-II-English-0.1.2635-test.iso
SHA-256 3f8e99810c573c3c8867274857d592a5a514f0b78bd65a3e16259773b86dc7ff

## Complete field-item audit


Cause and correction
Earlier checks covered selected recovery/no-effect/action families and
item descriptions. They did not enumerate the entire Item Use dispatcher
or every native fallback. Those checks could pass while other item-use
branches still displayed Japanese. Claims of broad category completeness
were therefore overstated. Description/name coverage is not effect-message
coverage.

This pass enumerates all125 native item descriptors, all73 indexed message
entries and the adjacent auxiliary declined-use fallback.35 remaining
Japanese entries are fully translated, including all five Takako letters,
incense use/wear-off, elixir reactions, compass/results, novelty actions and
group-use text. Hell's Tama's separate fallback is linked to the existing
complete English declined-use message:36 missed entries corrected in total.
The real125-item menu scan discovered this fallback outside the indexed73;
it was not silently counted as a pass. The four compass directions are
English, with original indices and distances retained. The short shared
collective result label is The party; both individual and party-wide
expiration inserts are checked, with travel-group wording regressed.

The pictured action reads: Manjimaru lit the Aphrodisiac Censer.
Its next page says: The presence of enemies grew stronger!
Native item effects, encounter-related writes, inventory and stat logic
are retained. Full1792-byte party/field records for Censer and both rewrapped
items match2635 before/after use for two actors. Harmful elixir outcomes and
sexual wording are retained, as are complete letter pages and their voice.
Runtime actor/recipient/item inserts are covered, including the separate
expiration-message name paths. Original sounds and page/wait controls are
retained; line breaks may move/add for English fit.

Coverage and limits
The final DOL passes the reusable literal completeness gate across74 text
entries and125 descriptors: zero untranslated literal entries.358 native
complete-message cases cover every entry, four actors for the35 new streams,
normal incremental parser reveal and native Update/Confirm traversal, full
names, page completion, glyph bounds, ABI and cleanup. Direct message tests
seed values; they do not prove every natural effect branch was reached.

The actual Use/User/Item scan attempted all125 IDs. It initially recorded
120 passes, one untranslated fallback and four generic-fixture gaps. The
Hell's Tama fallback is corrected and its real use/reveal/cleanup rerun in
both reveal modes, with native party effects exact to2635:121 ordinary
handoffs passed. Return Stone, Wind Talisman and Storm Talisman have separate
native producer/reveal checks; destination selection/natural teleport is
not claimed. Kaiten Elixir's native group effects and cleanup match2635
with intermediate completion flags modeled; intermediate healing pages
are covered by direct text tests rather than that effect fixture. No item
ID is omitted from the report. Every random result text is direct-tested;
all random effect distributions/natural map conditions are not exercised.

The125-ID scan ran on the pre-wrap candidate. The final build differs from
that candidate only in111 bytes inside two fixed-size text slots (kinds62
and63) and3 bytes of one auxiliary display pointer for item125, plus9 bytes
of the short shared group display label. All code,
other data outside these four display ranges and allocation settings are exact. The affected115/116 paths
were rerun after wrapping;125 was rerun after its pointer correction. All74
direct message tests were rerun against the final DOL. This provenance is
explicit in the coverage receipt, not relabeled as a fresh125-ID run.

General Store actual entry, long highlights/scrolling, Buy/Sell confirmation,
funds, Back/Exit and four same-pool reopens pass, as do both password answers,
wrong answers and editing. Extra scene/native allocator replay completes
and restores all cells. Both xdelta routes reproduce the entire ISO through
Retro Trans Tools0.5.23 and independent full decode/hash checks. Audio is
silent in every native fixture. No Dolphin or physical-console test occurred.

Hardware-sensitive changes and evidence
The DOL grows4216 bytes for relocated strings, name-scope adapters and the
new constructor/name insertion paths. The private arena reservation grows
8192 bytes to8038b000, reducing scene space from1060704 to1052512 bytes.
The native captured-scene/model/256KiB-reserve allocation replay still
completes with359424 free bytes, compared with367616 before. The earlier
fixed360000-byte margin check fails by576 bytes; this is explicitly retained
as a diagnostic, not presented as a passed unchanged margin check. All native
requests and exact free restoration pass in the paired measured replay.
Native allocator replay is not real-hardware validation.

Direct CP932 constructors for new complete messages use64x3/4608 backing
instead of23x3/1656, potentially2952 more live bytes before rounding. Actual
field Item Use already creates64x3. Two constructor gates, actor/item scope
gates and alternate expiration inserts admit only the new range, retaining
the previous chains for other sources. The auxiliary fallback changes one
display-table pointer. The12-byte collective display-label slot keeps its
address and is replaced by the shorter English The party label; this can
affect other field results which share it. Collective expiry/travel tests
cover the known related paths. Normal Balsamiq assets, native effect handlers, save
format, all FST assets, movies and audio remain exact. Enlarged DOL bytes
occupy verified zero disc padding; no asset offsets change. A strict inverse
restores2635. Pointer/branch changes and reduced memory headroom can affect
console behavior. Live-scene pressure, scene transitions, save/write/reload,
natural NPC/map access and physical GameCube behavior remain unverified.

Use the new ISO and load an in-game save.
ISO work/output/Tengai-Makyou-II-English-0.1.2640-test.iso
SHA-256 0d80b8f47aa0eae2aef6b608b19f96204bee75e828a8b440f52e12cb9ce64fd1

## Save labels, Scroll warnings, Lottery and newspapers


Installed corrections
1. Merchant apology: Sorry about that. The English draft at MAP-076-02-0001c4
had remained behind an unresolved-review gate. Read the preceding offer of
ordinary goods and follow-up invitation, resolved the apology in context,
and relocated the full row. All three identical-source sibling rows were
already installed; all four callers/payloads and both reveal modes pass.
2. Save locations: add Kyoto and all ten province-qualified Ninja Village
labels, including Kyo Ninja Village. Audit all121 native save-name records,
94 distinct labels. Existing195 bare-name lookup is retained as fallback.
Aliases affect the copied name only when drawing this Save list. Original
location strings, save buffers, checksums, IDs and disk format stay exact.
3. Scroll warnings: Manjimaru cannot use Autumn Gale. Audit the adjacent
restriction/error family and translate the other eight missed templates:
location restriction, exhaustion, paralysis, general seal, Yaksha's Black
Robe seal, Helmet of Silence seal, insufficient MP and exhausted recipient.
Existing outside-battle Scroll/Art warnings remain. Complete approved actor,
recipient and Scroll names are expanded; native decisions/effects stay exact.
4. Lottery actions: Buy / Cancel / Instructions. Prizes use full color and
approved item names, including Kaiten Elixir, Seven Fortunes Orb and Lottery
Dango Skewer. The non-item consolation remains Attendant's Smile, distinct
from the generic item-name Smile. All11 labels are translated. Both popups
are wider; all three state-dependent room variants in maps31/32/33 are fixed.
Original packed source, choice IDs/order, branch targets and reward logic
stay exact. There is no new reward or encounter behavior.
5. Newspapers: all16 complete English headline pointers,18px Balsamiq text,
titles and90-ryo prices on separate lines. Preserve the native2x8 selection
IDs;36px logical row pitch,300px column pitch and280px highlights.600x384
frame starts at20,76. Money and ryo are English; the original formatted
amount updates after purchase. No headline or article ending is cut to fit.

Review
Accuracy: apology reviewed with surrounding rows4437..4439; source restriction
roles and actor/recipient direction retained; approved item/equipment/location
spellings reused. All16 existing headline translations retained, with ASCII
spacing and UFO width normalized. Editorial: complete natural English warnings,
parallel actions, color/prize separation and legible full headlines. Proofreading:
ordinary spaces, capitalization, punctuation, complete names and all choice order
checked. Five native-quad proofs visually inspected; panels are schematic, not
Dolphin screenshots. Save proof shows only the changed location label; unchanged
date/time are omitted. No extensive Japanese dialogue export was created.

Validation and limits
All6 actual native Lottery constructors/callbacks,11 labels, all3/8 option IDs,
normal atlas/bounds and native manager cleanup pass. Source packed list and
reward/event branches stay byte-exact. Reward distribution/natural NPC traversal
are not tested. All121 saved-location records/94 distinct display labels pass
name bounds, two-line fit and exact neighboring date/time packet checks.
Four seeded30-slot list producers execute the native checksum/calendar path;
save buffers remain byte-exact. Their packet backing is a seeded fixture, not
a new real card/window-constructor or physical save/write/restart/reload test.

308 complete native warning Update/Confirm reveals pass:69 eligibility names
for each of4 actors plus the other8 warning templates for each actor. Includes
complete recipient names and multiline output. Actual Use -> User -> Scroll
handoff reproduces Manjimaru/Autumn Gale; HP/MP/inventory bytes remain exact.
Other warning decisions are source-qualified seeded direct constructor tests;
not every natural equipment/status/map condition is reached. Both retained
outside-battle templates are regressed. Earlier test-only line stepping was
replaced with actual native Update/Confirm, which handles line breaks correctly.

Two actual newspaper entries execute all16 headline/price draws, native selector
construction, seeded selection IDs,90-ryo purchase/funds updates, retry and native
cleanup/reopen. A separate64-case directional-input pair matches original IDs
exactly. Article completion/fades are modeled; complete article reading/scrolling,
every availability history and natural NPC entry are not claimed. General Store
actual entry, long highlights, Buy/Sell/funds, Back/Exit and four reopens pass.
All4 apology rows execute in fast/typewriter modes, and every typed-room binding,
descriptor and integrity checksum validates. All74 field-item message slots and
125 descriptors retain the prior complete English literal coverage gate.

Hardware-sensitive changes
DOL grows6304 bytes; private boot reservation grows4096 to8038c000.
Scene space becomes1048416 bytes. Native captured scene allocations plus
201376-byte complete-model budget,256KiB reserve and failed1KiB request pass,
with355328 bytes free at peak and exact release restoration.
The test's documented lower-bound margin is300000; it is not the historical
400000 threshold. General/save allocation replay also passes with an additional
32640-byte newspaper text buffer. Allocation replay is not hardware validation.

Actual newspaper backing changes from23x9/4968 to80x17/32640 bytes, +27672 live
bytes before allocator rounding. Initial frame backing is23x14 before resize.
Lottery action backing grows3x3 to10x3 (+504 bytes); prize backing7x8 to16x8
(+1728 bytes). Source-qualified warning messages use64x3/4608 backing, with
persistent existing per-header buffers; owner/recipient lookup shares bounds
and ID validation. New branches, display pointer rewrites and larger allocations
can affect physical-console play. Native ABI/guard/cleanup and heap replay pass.

MAP rooms31/19,32/19,33/19 change only two width bytes each; no decoded growth.
Room76/2 adds32 decoded bytes for the relocated apology and redirects its native
display caller. Existing typed descriptors/integrity and cached map header are
rebased as needed. Strict inverse restores the prior DOL and decoded room bytes.
ISO asset offsets do not move: verified zero padding accommodates growth. The
1391 other FST assets, including normal font, movies and audio, remain exact.
Both original-source and public0.8.3 upgrade patches reproduce the whole ISO
through independent xdelta decode/hash checks and Retro Trans Tools0.5.23.

No Dolphin or real GameCube test occurred. All native tests were silent.
Natural scene transitions, full-game peaks and real card I/O remain unverified.

Test ISO: work/output/Tengai-Makyou-II-English-0.1.2646-test.iso
SHA-256: 253a7557037fe32cb8ec0c2ca60b16106200dc7f0047bc5968b18ebb17158842
Use this ISO and load an in-game save; old emulator states do not update code.

## Tickets, broker and Commodity Exchange


Installed corrections and family audit
- Both direct engraved lottery-ticket messages now read: The lottery ticket has
  33/34 engraved on it. The complete indexed field-item table remains English:
  all74 text slots and125 descriptors pass. The new direct-source constructor
  tests supplement that indexed gate; one does not establish the other's coverage.
- The information broker's offer is installed in maps31/32/33, room18:
  Hey, pal! Hey! I've got a hot tip. / How does ten ryo sound?
  The unchanged payment command contains immediate0x00000a. All48 exchange-NPC
  rows in the three rooms, including8 buy/sell tips and payment/refusal variants,
  are installed and replayed in both text reveal modes. Three previously held
  offer rows were relocated. No price, outcome or event branch was changed.
- Commodity table: complete Rice, Mugi Grain, Beans and Salt names, headings
  Commodity / Current Price / Record High / Record Low, and all12 original
  current/high/low values with English ryo units. The old first-cell-only native
  repositioning no longer scrambles expanded English words. Each cell owns
 20 slots with144px pitch, using18px normal Balsamiq, inside the original frame.
- Rebind all11 previously reviewed Commodity prompts with ordinary ASCII
  punctuation. The old direct adapter demanded exactly3 rows, so it fell back
  to Japanese when the actual parent had5. It now preserves actual row count,
  restores the English money row after backing growth, and preserves choices.
  Confirmations, purchase-more, sale receipt/continue, Help, insufficient funds,
  full bag and exit persuasion are included. Popup text commands/pages remain.
- Commodity purchase uses its separate four-name English recipient table with
  Free followed by the native capacity count. All four IDs and counts0/1/2/3
  are exercised. All native inventory limits and receipt IDs stay unchanged.
- All7 standard-shop/Commodity money producers use the same complete English
  Money/amount/ryo path. Three older producers had retained Japanese fragments.
  Commodity Sell has two additional real child constructors; both now allocate
 48x5 backing before row4 money is drawn. No fake larger fixture is substituted.
- Kyoto was already translated in2646. This build retains that fix and rechecks
  all121 saved-location records/94 distinct labels plus four native30-slot list
  producers. Original save names, save bytes/checksums and IDs are unchanged.

Review and verification
Accuracy review, editorial review, accuracy recheck and proofreading completed.
The broker's slang was localized using its native fee10; complete source meaning,
colloquial voice and approved Mugi Grain terminology are retained. Earlier full
Commodity wording is retained, with !/?/ellipsis punctuation made readable.
No extensive Japanese script export was created.

Silent native checks pass for12 real purchases and sales (4 goods x quantities
1/10/100), exact funds deduction/refund and receipt IDs, confirmation, recipient,
continue/back, actual Sell child construction, cleanup and same-pool reopen.
A separate canceled-sale path executes the alternate48x5 child constructor.
All12 table cells are complete and nonoverlapping for prices0/100/999/1000/32767;
rendering leaves gameplay bytes exact. Four multi-page warning/Help/exit prompt
families pass native slow and fast Update/Confirm with complete glyph order and
bounds. All48 related field rows pass both reveal modes, and every typed room
binding, compressed descriptor and FNV integrity value matches the rebuilt MAP.
Actual General Store entry, long highlights, Buy/Sell confirmations, funds,
Back/Exit and four reopens also pass. Five native glyph proofs were inspected;
backgrounds are schematic, not Dolphin screenshots. The Save proof is label-only.
The Sell proof demonstrates the money change; it does not certify the separate
legacy item-description/eligibility overlay. Natural NPC traversal, all economic
histories, full gameplay, physical card writes/restart/reload are not certified.

Hardware-sensitive changes and validation limits
DOL grows2688 bytes. New branches, display pointer rewrites and saved
volatile/nonvolatile register conventions were checked in native fixtures, not
on a console. Boot private reservation grows4096 bytes to
0x8038d000; scene space becomes1044320 bytes, with
3208 unused private bytes. Scene allocation replay includes
1151 captured requests,201376 bytes of complete-model budget,256KiB reserve and
an extra failed1KiB request. It leaves351232 bytes at peak,
with exact release restoration. This exceeds the documented300000 test margin,
not the older400000 margin. General/save heap pressure replay also passes with
an extra32640-byte newspaper buffer. These are allocation replays, not hardware
validation, exact gameplay allocation histories or full-game peak guarantees.

Commodity table backing:23x6/3312 ->80x6/11520, +8208 live bytes.
Commodity parent prompt backing can grow48x5/5760 ->96x5/11520, +5760.
The two Sell child entry paths grow32x4/3072 ->48x5/5760, +2688 per live child.
New direct-ticket contexts grow23x3/1656 ->64x3/4608, +2952 when used.
Broader menu allocation, fragmentation and native queue pressure remain hardware
risks. Native bounds, ABI, queues and balanced cleanup passed these scenarios.

MAP rooms31/18,32/18,33/18 grow96 decoded bytes each; only offer display references
and appended text change. Strict inverse checks recover the preceding DOL and
all decoded room bytes. Typed descriptors/integrity and cached headers were
rebased. ISO asset offsets stay fixed using verified zero padding. All unrelated
assets, including normal fonts, movies and audio, remain exact. Both original-
source and public0.8.3 upgrade patches fully decode to the same ISO and pass
Retro Trans Tools0.5.23 Apply xdelta. Automatic discovery/public release metadata
was not changed because this is a local test build, not a new GitHub release.

No Dolphin playback or real GameCube testing occurred. Native tests were silent;
audio endpoints were intercepted. Real card I/O and natural scene transitions
remain unverified. Load an in-game save with the new ISO; old emulator states
retain old code. Public v0.8.3 assets remain unchanged.

Test ISO: work/output/Tengai-Makyou-II-English-0.1.2651-test.iso
SHA-256: 24631312ba51f4e901b527e2dc83821d11a24d6744c3e3ad9e508ffefe23d2f7

## Inherited release evidence

Earlier password, subtitle, dialogue and travel-result tests remain documented in [v0.8.3 testing notes](https://github.com/retro-trans/Tengai-Makyou-II/blob/v0.8.3/docs/TESTING.md). Those historical tests are not new gameplay or hardware validation.
