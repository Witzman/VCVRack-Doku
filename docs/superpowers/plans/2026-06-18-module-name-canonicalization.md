# Module Name Canonicalization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix all module names in `VCVRack-Doku/src/*.md` to match the display names and plugin names shown in the VCV Rack module browser.

**Architecture:** File-by-file manual edit, grouped by file type. No code — pure markdown text substitution guided by a correction map derived from `rack/library/manifests/`. Verification at the end of each task via grep.

**Tech Stack:** Markdown files, Edit tool, Bash grep for verification.

## Global Constraints

- Module display names must match `rack/library/manifests/Fundamental.json` (plugin name: "VCV Free"), `Core.json` (plugin name: "VCV Core"), `Bogaudio.json`, etc.
- Section headings format: `## ModuleName (PluginName)` — use display name, not slug
- Do NOT change Bogaudio, Impromptu, Valley, Alright Devices, Befaco, Surge XT, or Vult module names
- Do NOT change knob/port/jack label names (FREQ, RES, SAW, V/OCT, etc.)
- Do NOT change code blocks or CLAUDE.md

## Master Correction Map

| Old text | New text | Notes |
|---|---|---|
| `Fundamental VCO-1` | `VCV Free VCO` | |
| `Fundamental VCO` | `VCV Free VCO` | |
| `VCO-1` (standalone, referring to module) | `VCO` | not inside port descriptions |
| `WTVCO (Fundamental)` | `Wavetable VCO (VCV Free)` | heading |
| `WTVCO` | `Wavetable VCO` | inline |
| `VCO-2 (Fundamental)` | `VCO 2 (VCV Free)` | verify this module exists in manifest |
| `Fundamental VCF` | `VCV Free VCF` | |
| `VCF (Fundamental)` | `VCF (VCV Free)` | heading |
| `Fundamental VCA` | `VCV Free VCA` | = VCA-1, the simpler single-channel VCA |
| `VCA (Fundamental)` | `VCA (VCV Free)` | heading (VCA-1 = display name "VCA") |
| `VCA-1 (Fundamental)` | `VCA (VCV Free)` | heading — VCA-1 is the slug, "VCA" is display name |
| `Fundamental ADSR EG` | `VCV Free ADSR EG` | |
| `Fundamental ADSR` | `VCV Free ADSR EG` | fix to full display name |
| `ADSR (Fundamental)` | `ADSR EG (VCV Free)` | heading |
| `Fundamental LFO` | `VCV Free LFO` | |
| `LFO (Fundamental)` | `LFO (VCV Free)` | heading |
| `WTLFO (Fundamental)` | `Wavetable LFO (VCV Free)` | heading; slug LFO2 = "Wavetable LFO" |
| `WTLFO` | `Wavetable LFO` | inline |
| `Fundamental SEQ-3` | `VCV Free SEQ 3` | |
| `SEQ-3 (Fundamental)` | `SEQ 3 (VCV Free)` | heading |
| `SEQ-3` (standalone, referring to module) | `SEQ 3` | |
| `Fundamental 8vert` | `VCV Free 8vert` | |
| `8vert (Fundamental)` | `8vert (VCV Free)` | heading |
| `Fundamental Mixer` | `VCV Free Mix` | display name is "Mix", slug is "Mixer" |
| `Mixer (Fundamental)` | `Mix (VCV Free)` | heading |
| `Fundamental's mixer` | `VCV Free's Mix` | possessive form |
| `VCMixer (Fundamental)` | `VCA Mix (VCV Free)` | heading; slug VCMixer = "VCA Mix" |
| `VCMixer` | `VCA Mix` | inline |
| `CVMix (Fundamental)` | `CVMix (VCV Free)` | slug CVMix = "CV Mix" display name; heading |
| `Fundamental Noise` | `VCV Free Noise` | |
| `Noise (Fundamental)` | `Noise (VCV Free)` | heading |
| `Fundamental Quantizer` | `VCV Free Quantizer` | |
| `Quantizer (Fundamental)` | `Quantizer (VCV Free)` | heading |
| `Fundamental WTVCO` | `VCV Free Wavetable VCO` | |
| `SHASR (Fundamental)` | `Sample & Hold ASR (VCV Free)` | slug SHASR = "Sample & Hold Analog Shift Register" — abbreviate to "Sample & Hold ASR" for heading readability |
| `MIDI-GATE (Fundamental)` | `MIDI to Gate (VCV Free)` | slug MIDITriggerToCVInterface = "MIDI to Gate" |
| `Split (Fundamental)` | `Split (VCV Free)` | heading; slug Split = "Split" ✓ |
| `Merge (Fundamental)` | `Merge (VCV Free)` | heading; slug Merge = "Merge" ✓ |
| `Mult (Fundamental)` | `Mult (VCV Free)` | heading; slug Mult = "Mult" ✓ |
| `AUDIO-8` | `Audio 8` | VCV Core module; slug AudioInterface = "Audio 8" |
| `MIDI-CV (VCV Core)` (heading) | `MIDI to CV (VCV Core)` | slug MIDIToCVInterface = "MIDI to CV" |
| `MIDI-CV` (referring to VCV Core module) | `MIDI to CV` | only when referring to the VCV Core module |
| `(from Core)` | `(VCV Core)` | parenthetical plugin attribution |
| `(also in Core)` | `(VCV Core)` | parenthetical plugin attribution |
| `(in Core)` | `(VCV Core)` | parenthetical plugin attribution |
| `AudioInterface2` | `Audio 2` | slug AudioInterface2 = "Audio 2" |
| `Fundamental Clock` | investigate — no "Clock" in VCV Free manifest | likely third-party; leave or note |
| `VCV MIDI-CV` (sequencer.md heading) | `VCV Core MIDI to CV` | |

**Note on MIDI-CV in generic context:** Some occurrences of "MIDI-CV" are used as a generic concept (e.g., "a MIDI-CV converter") or as a subsection referring to Bogaudio's module. Do NOT change:
- Generic/concept uses: "MIDI-CV connection", "any MIDI-CV module"
- Bogaudio module: `Bogaudio MIDI-CV` — leave as-is, Bogaudio naming not in scope

---

### Task 1: Fix first-patch.md and intermediate-patch.md

**Files:**
- Modify: `VCVRack-Doku/src/first-patch.md`
- Modify: `VCVRack-Doku/src/intermediate-patch.md`

- [ ] **Step 1: Grep first-patch.md for all patterns**

```bash
grep -n "Fundamental\|VCO-1\|SEQ-3\|MIDI-CV\|AUDIO-8\|from Core\|in Core\|ADSR EG" /home/witzman/rack/VCVRack-Doku/src/first-patch.md
```

Expected: matches on lines 21, 27, 29, 37, 45, 53.

- [ ] **Step 2: Edit first-patch.md**

Apply these exact changes:

Line 21: `Search for **AUDIO-8** or just **Audio**. Add the AUDIO-8 module (from Core).`
→ `Search for **Audio 8** or just **Audio**. Add the **Audio 8** module (VCV Core).`

Line 27: `## Step 3 — Add MIDI-CV`
→ `## Step 3 — Add MIDI to CV`

Line 29: `Open the browser again and add **MIDI-CV** (also in Core).`
→ `Open the browser again and add **MIDI to CV** (VCV Core).`

Line 29 (second occurrence): `Click its display...`  
No change needed on this line.

Line 37: `Add the **VCO** module (from VCV Free). Connect the MIDI-CV's **V/Oct** output`
→ `Add **VCO** (VCV Free). Connect the **MIDI to CV**'s **V/Oct** output`

Line 45: `Add **ADSR EG** (from VCV Free).` 
→ `Add **ADSR EG** (VCV Free).`

Line 45 (second occurrence): `Connect MIDI-CV's **Gate** output`
→ `Connect **MIDI to CV**'s **Gate** output`

Line 50: `Add **VCA** (from VCV Free).`
→ `Add **VCA** (VCV Free).`

Line 53: `Connect the VCA's **CH** output to the AUDIO-8's **L** input`
→ `Connect the VCA's **CH** output to the **Audio 8**'s **L** input`

Line 59: `Add **VCF** (from VCV Free).`
→ `Add **VCF** (VCV Free).`

- [ ] **Step 3: Grep intermediate-patch.md for all patterns**

```bash
grep -n "Fundamental\|VCO-1\|SEQ-3\|MIDI-CV\|AUDIO-8\|from Core" /home/witzman/rack/VCVRack-Doku/src/intermediate-patch.md
```

Expected: matches on lines 31, 33, 40, 42, 43, 48, 51, 52, 58, 67, 80.

- [ ] **Step 4: Edit intermediate-patch.md**

Line 31: `Add **SEQ-3** (Fundamental) from the module browser.`
→ `Add **SEQ 3** (VCV Free) from the module browser.`

Line 33: `Connect Clocked's CLK1 output to SEQ-3's CLK input.`
→ `Connect Clocked's CLK1 output to SEQ 3's CLK input.`

Line 40: `This is a more flexible oscillator than Fundamental's VCO-1.`
→ `This is a more flexible oscillator than VCV Free's VCO.`

Line 42: `Connect SEQ-3's ROW1 output to Bogaudio VCO's V/OCT input.`
→ `Connect SEQ 3's ROW1 output to Bogaudio VCO's V/OCT input.`

Line 43: `Connect SEQ-3's GATE output to the next step's input`
→ `Connect SEQ 3's GATE output to the next step's input`

Line 48: `Add **Fundamental VCF** and **Bogaudio ADSR**.`
→ `Add **VCV Free VCF** and **Bogaudio ADSR**.`

Line 51: `Take VCF's LP output to a VCA (add **Fundamental VCA**).`
→ `Take VCF's LP output to a VCA (add **VCV Free VCA**).`

Line 52: `Connect SEQ-3's GATE to Bogaudio ADSR's GATE input.`
→ `Connect SEQ 3's GATE to Bogaudio ADSR's GATE input.`

Line 58: `Adjust the SEQ-3 step knob voltages`
→ `Adjust the SEQ 3 step knob voltages`

Line 67: `Take the SIN output through a **Fundamental 8vert** channel`
→ `Take the SIN output through a **VCV Free 8vert** channel`

Line 80: `Connect **Fundamental Noise** (White output) to S&H's IN input.`
→ `Connect **VCV Free Noise** (White output) to S&H's IN input.`

- [ ] **Step 5: Verify — no old names remain in either file**

```bash
grep -n "Fundamental\|VCO-1\|SEQ-3\|MIDI-CV\|AUDIO-8\|from Core\|also in Core\|in Core)" /home/witzman/rack/VCVRack-Doku/src/first-patch.md /home/witzman/rack/VCVRack-Doku/src/intermediate-patch.md
```

Expected: zero matches (only acceptable match: link text `[Fundamental Modules](fundamental-modules.md)` on line 85 of first-patch.md — this is a page link, not a module name, leave it).

- [ ] **Step 6: Commit**

```bash
cd /home/witzman/rack/VCVRack-Doku && git add src/first-patch.md src/intermediate-patch.md && git commit -m "docs: canonicalize module names in first-patch and intermediate-patch"
```

---

### Task 2: Fix slow-psybient.md and slow-psybient-starter.md

**Files:**
- Modify: `VCVRack-Doku/src/slow-psybient.md`
- Modify: `VCVRack-Doku/src/slow-psybient-starter.md`

- [ ] **Step 1: Grep slow-psybient.md for patterns**

```bash
grep -n "Fundamental\|VCO-1\|SEQ-3\|VCMixer\|AudioInterface\|MIDI-CV\|AUDIO-8" /home/witzman/rack/VCVRack-Doku/src/slow-psybient.md
```

- [ ] **Step 2: Edit slow-psybient.md**

Apply these corrections (read the file first to confirm line numbers, then edit):

- `2× Fundamental VCO-1` → `2× VCV Free VCO`
- `Fundamental VCF` → `VCV Free VCF`
- `Fundamental VCA` → `VCV Free VCA`
- `Fundamental 8vert` → `VCV Free 8vert`
- `Fundamental Mixer` → `VCV Free Mix`
- `Fundamental SEQ-3` → `VCV Free SEQ 3`
- `Fundamental VCO-1` (all occurrences) → `VCV Free VCO`
- `VCO-1` (standalone, referring to module) → `VCO` — check each: if in phrase like "VCO-1's FM inputs" change to "VCO's FM inputs"; if in "two VCO-1 modules" change to "two VCO modules"
- `Fundamental Noise` → `VCV Free Noise`
- `Fundamental Quantizer` → `VCV Free Quantizer`
- `SEQ-3` (standalone, referring to module) → `SEQ 3`
- bare `8vert` used as Fundamental module in sentence context → `VCV Free 8vert` (check: line 74 "8vert" without prefix — add `VCV Free ` prefix)

- [ ] **Step 3: Grep slow-psybient-starter.md for patterns**

```bash
grep -n "Fundamental\|VCO-1\|SEQ-3\|VCMixer\|AudioInterface2\|MIDI-CV\|AUDIO-8" /home/witzman/rack/VCVRack-Doku/src/slow-psybient-starter.md
```

- [ ] **Step 4: Edit slow-psybient-starter.md**

Apply these corrections:

- Line 9: `All modules are from **Fundamental**, which ships with VCV Rack by default.`
  → `All modules are from **VCV Free**, which ships with VCV Rack by default.`

- `VCMixer` → `VCA Mix` (all occurrences — in headings, prose, and connection tables)

- `AudioInterface2` → `Audio 2` (all occurrences — in headings, prose, and tables)

- Line 93: `You need the Fundamental plugin installed — it ships with VCV Rack by default.`
  → `You need the VCV Free plugin installed — it ships with VCV Rack by default.`

- Line 99: `Nine modules, all from Fundamental:`
  → `Nine modules, all from VCV Free:`

- `Fundamental SEQ-3` → `VCV Free SEQ 3`
- `Fundamental VCO` → `VCV Free VCO`
- `Fundamental VCA` → `VCV Free VCA`

- Line 28: `9. **AudioInterface2** (under Core) — stereo output to your soundcard`
  → `9. **Audio 2** (VCV Core) — stereo output to your soundcard`

Note: connection tables use bare names in columns (e.g., `| VCMixer | MIX | VCF | IN |`). Update VCMixer → VCA Mix and AudioInterface2 → Audio 2 in all table cells too.

- [ ] **Step 5: Verify**

```bash
grep -n "Fundamental\|VCO-1\|SEQ-3\|VCMixer\|AudioInterface2" /home/witzman/rack/VCVRack-Doku/src/slow-psybient.md /home/witzman/rack/VCVRack-Doku/src/slow-psybient-starter.md
```

Expected: zero matches. Acceptable exception: link `[Fundamental Modules]` if present — it's a page name, not a module name.

- [ ] **Step 6: Commit**

```bash
cd /home/witzman/rack/VCVRack-Doku && git add src/slow-psybient.md src/slow-psybient-starter.md && git commit -m "docs: canonicalize module names in slow-psybient tutorials"
```

---

### Task 3: Fix module reference pages — VCO, VCF, VCA, Envelope, LFO

**Files:**
- Modify: `VCVRack-Doku/src/vco.md`
- Modify: `VCVRack-Doku/src/vcf.md`
- Modify: `VCVRack-Doku/src/vca.md`
- Modify: `VCVRack-Doku/src/envelope.md`
- Modify: `VCVRack-Doku/src/lfo.md`

- [ ] **Step 1: Edit vco.md**

Changes:
- `## VCO-1 (Fundamental)` → `## VCO (VCV Free)`
- In the opening description: `The VCO-1 is the oscillator` → `The VCO is the oscillator`
- `### WTVCO (Fundamental)` → `### Wavetable VCO (VCV Free)`
- `The WTVCO is the wavetable oscillator included with Fundamental` → `The Wavetable VCO is the wavetable oscillator included with VCV Free`
- `### VCO-2 (Fundamental)` → Verify this module: open `rack/library/manifests/Fundamental.json` and confirm a module with a morphing waveform exists. If VCO2 slug has display name "Wavetable VCO" (which it does), then "VCO-2 (Fundamental)" is inaccurate. **This section describes a different module than WTVCO — the morphing/crossfade oscillator.** Check if any Fundamental slug has this behavior; if not found, flag the section as potentially hallucinated and change heading to `### VCO 2 (VCV Free)` while preserving the description.
- Inline `VCO-1` in patching tips line 23: `MIDI-CV module's V/OCT output to VCO-1's V/OCT` → `MIDI to CV module's V/OCT output to VCO's V/OCT`; `two VCO-1 instances` → `two VCO instances`

- [ ] **Step 2: Edit vcf.md**

Changes:
- `## VCF (Fundamental)` → `## VCF (VCV Free)`
- `Fundamental VCF` (all inline occurrences) → `VCV Free VCF`

- [ ] **Step 3: Edit vca.md**

Read file first, then apply:

Changes:
- `## VCA (Fundamental)` → `## VCA (VCV Free)` (this is VCA-1, display name "VCA")
- `## VCA-1 (Fundamental)` (if present as separate heading) → `## VCA (VCV Free)` — note: VCA-1 is the slug, the display name is just "VCA"
- `The Fundamental VCA is` → `The VCV Free VCA is`
- `8vert (Fundamental)` → `8vert (VCV Free)`
- All `Fundamental VCA` → `VCV Free VCA`

- [ ] **Step 4: Edit envelope.md**

Changes:
- `## ADSR (Fundamental)` → `## ADSR EG (VCV Free)`
- `The Fundamental ADSR is` → `The VCV Free ADSR EG is`
- `Fundamental ADSR` (all) → `VCV Free ADSR EG`
- `Fundamental's` (possessive, if present) → `VCV Free's`

- [ ] **Step 5: Edit lfo.md**

Changes:
- `## LFO (Fundamental)` → `## LFO (VCV Free)`
- `## WTLFO (Fundamental)` → `## Wavetable LFO (VCV Free)` (slug LFO2 = display name "Wavetable LFO")
- `Fundamental LFO` (all inline) → `VCV Free LFO`
- `Fundamental LFO's` → `VCV Free LFO's`

- [ ] **Step 6: Verify all five files**

```bash
grep -n "Fundamental\|VCO-1\|WTVCO\|WTLFO\|MIDI-CV" /home/witzman/rack/VCVRack-Doku/src/vco.md /home/witzman/rack/VCVRack-Doku/src/vcf.md /home/witzman/rack/VCVRack-Doku/src/vca.md /home/witzman/rack/VCVRack-Doku/src/envelope.md /home/witzman/rack/VCVRack-Doku/src/lfo.md
```

Expected: zero matches.

- [ ] **Step 7: Commit**

```bash
cd /home/witzman/rack/VCVRack-Doku && git add src/vco.md src/vcf.md src/vca.md src/envelope.md src/lfo.md && git commit -m "docs: canonicalize module names in VCO, VCF, VCA, ADSR, LFO reference pages"
```

---

### Task 4: Fix remaining module reference pages

**Files:**
- Modify: `VCVRack-Doku/src/mixer.md`
- Modify: `VCVRack-Doku/src/sequencer.md`
- Modify: `VCVRack-Doku/src/noise.md`
- Modify: `VCVRack-Doku/src/quantizer.md`
- Modify: `VCVRack-Doku/src/attenuverter.md`
- Modify: `VCVRack-Doku/src/mult-splitter.md`
- Modify: `VCVRack-Doku/src/sample-hold.md`
- Modify: `VCVRack-Doku/src/delay-reverb-chorus.md`
- Modify: `VCVRack-Doku/src/wavetable.md`
- Modify: `VCVRack-Doku/src/waveshaper-distortion.md`
- Modify: `VCVRack-Doku/src/clock.md`
- Modify: `VCVRack-Doku/src/maschine-mapping.md`

- [ ] **Step 1: Edit mixer.md**

Changes:
- `## Mixer (Fundamental)` → `## Mix (VCV Free)` (slug Mixer = display name "Mix")
- `The Fundamental Mixer has` → `VCV Free Mix has`
- `## VCMixer (Fundamental)` → `## VCA Mix (VCV Free)` (slug VCMixer = display name "VCA Mix")
- `### CVMix (Fundamental)` → `### CVMix (VCV Free)` (slug CVMix = display name "CV Mix" — but heading text uses "CVMix", just change plugin name)
- `### 8vert (Fundamental)` → `### 8vert (VCV Free)`
- `Fundamental's mixer` → `VCV Free's Mix`

- [ ] **Step 2: Edit sequencer.md**

Changes:
- `## SEQ-3 (Fundamental)` → `## SEQ 3 (VCV Free)` (slug SEQ3 = display name "SEQ 3")
- `SEQ-3 is an 8-step sequencer` → `SEQ 3 is an 8-step sequencer`
- `### VCV MIDI-CV + keyboard` → `### VCV Core MIDI to CV + keyboard`
- Inline `MIDI-CV` in the keyboard section → `MIDI to CV`

- [ ] **Step 3: Edit noise.md**

Changes:
- `## Noise (Fundamental)` → `## Noise (VCV Free)`
- Any `Fundamental Noise` inline → `VCV Free Noise`
- Any `Fundamental slot` reference → `VCV Free slot`

- [ ] **Step 4: Edit quantizer.md**

Changes:
- `## Quantizer (Fundamental)` → `## Quantizer (VCV Free)`
- `The Fundamental Quantizer` (all) → `The VCV Free Quantizer`
- `Fundamental Quantizer` (all) → `VCV Free Quantizer`

- [ ] **Step 5: Edit attenuverter.md**

Changes:
- `## 8vert (Fundamental)` → `## 8vert (VCV Free)`
- `### Fundamental 8vert as CV source` → `### VCV Free 8vert as CV source`
- Any `Fundamental 8vert` inline → `VCV Free 8vert`

- [ ] **Step 6: Edit mult-splitter.md**

Changes:
- `## Split (Fundamental)` → `## Split (VCV Free)`
- `## Merge (Fundamental)` → `## Merge (VCV Free)`
- `## Mult (Fundamental)` → `## Mult (VCV Free)`
- `MIDI-CV` in patching tips (referring to VCV Core module) → `MIDI to CV`

- [ ] **Step 7: Edit sample-hold.md**

Changes:
- `## SHASR (Fundamental)` → `## Sample & Hold ASR (VCV Free)` (slug SHASR = "Sample & Hold Analog Shift Register" — abbreviate in heading to "Sample & Hold ASR")
- `Fundamental Noise` inline → `VCV Free Noise`

- [ ] **Step 8: Edit delay-reverb-chorus.md**

Changes:
- `## Delay (Fundamental)` → `## Delay (VCV Free)` (slug Delay = display name "Delay" ✓)
- `Fundamental Delay` inline → `VCV Free Delay`
- `built-in Fundamental Delay` → `built-in VCV Free Delay`

- [ ] **Step 9: Edit wavetable.md**

Changes:
- `## WTVCO (Fundamental)` → `## Wavetable VCO (VCV Free)` (slug VCO2 = "Wavetable VCO")
- `### WTLFO (Fundamental)` → `### Wavetable LFO (VCV Free)` (slug LFO2 = "Wavetable LFO")
- Any inline `WTVCO` → `Wavetable VCO`
- Any inline `WTLFO` → `Wavetable LFO`

- [ ] **Step 10: Edit waveshaper-distortion.md**

Changes:
- `### VCV Rack DRIVE (Fundamental — via VCF)` → `### VCV Free VCF DRIVE` (it's a feature of VCF, not a standalone module; simplify heading)
- `The Fundamental VCF has` → `The VCV Free VCF has`

- [ ] **Step 11: Edit clock.md**

Read file, grep for "Fundamental Clock" (line 41). The VCV Free manifest has no "Clock" module. Change:
- `### Fundamental Clock (if available)` → `### VCV Free Clock (if available)` OR investigate: if this section describes a non-existent module, note it. Simply change "Fundamental" → "VCV Free" to fix the plugin name; leave rest of heading as-is.

- [ ] **Step 12: Edit maschine-mapping.md**

Changes:
- `MIDI-GATE (Fundamental)` → `MIDI to Gate (VCV Free)` (slug MIDITriggerToCVInterface = display name "MIDI to Gate")

- [ ] **Step 13: Verify all files in this task**

```bash
grep -n "Fundamental\|VCO-1\|SEQ-3\|VCMixer\|WTVCO\|WTLFO\|AUDIO-8\|AudioInterface\|MIDI-CV\|MIDI-GATE" \
  /home/witzman/rack/VCVRack-Doku/src/mixer.md \
  /home/witzman/rack/VCVRack-Doku/src/sequencer.md \
  /home/witzman/rack/VCVRack-Doku/src/noise.md \
  /home/witzman/rack/VCVRack-Doku/src/quantizer.md \
  /home/witzman/rack/VCVRack-Doku/src/attenuverter.md \
  /home/witzman/rack/VCVRack-Doku/src/mult-splitter.md \
  /home/witzman/rack/VCVRack-Doku/src/sample-hold.md \
  /home/witzman/rack/VCVRack-Doku/src/delay-reverb-chorus.md \
  /home/witzman/rack/VCVRack-Doku/src/wavetable.md \
  /home/witzman/rack/VCVRack-Doku/src/waveshaper-distortion.md \
  /home/witzman/rack/VCVRack-Doku/src/clock.md \
  /home/witzman/rack/VCVRack-Doku/src/maschine-mapping.md
```

Expected: zero matches.

- [ ] **Step 14: Commit**

```bash
cd /home/witzman/rack/VCVRack-Doku && git add src/mixer.md src/sequencer.md src/noise.md src/quantizer.md src/attenuverter.md src/mult-splitter.md src/sample-hold.md src/delay-reverb-chorus.md src/wavetable.md src/waveshaper-distortion.md src/clock.md src/maschine-mapping.md && git commit -m "docs: canonicalize module names in module reference pages"
```

---

### Task 5: Fix guide and navigation pages

**Files:**
- Modify: `VCVRack-Doku/src/midi-cv.md`
- Modify: `VCVRack-Doku/src/userguide.md`
- Modify: `VCVRack-Doku/src/faq.md`
- Modify: `VCVRack-Doku/src/patching-use-cases.md`

Pages `readme.md`, `mental-model.md`, `how-a-patch-works.md` contain only the link `[Fundamental Modules](fundamental-modules.md)` — this is a page link, not a module name. Leave these three files unchanged unless they contain other Fundamental/VCO-1/etc. occurrences (verify with grep first).

- [ ] **Step 1: Verify readme/mental-model/how-a-patch-works only have link occurrences**

```bash
grep -n "Fundamental\|VCO-1\|SEQ-3\|VCMixer\|MIDI-CV\|AUDIO-8" \
  /home/witzman/rack/VCVRack-Doku/src/readme.md \
  /home/witzman/rack/VCVRack-Doku/src/mental-model.md \
  /home/witzman/rack/VCVRack-Doku/src/how-a-patch-works.md
```

If matches are only `[Fundamental Modules](fundamental-modules.md)` links: no changes needed. If other occurrences found: fix them using the master correction map.

- [ ] **Step 2: Edit midi-cv.md**

Changes:
- `## MIDI-CV (VCV Core)` → `## MIDI to CV (VCV Core)`
- `The MIDI-CV module is included with VCV Rack Free as a core module` → `The MIDI to CV module is included with VCV Rack Free as a core module`
- All references to the VCV Core module by name "MIDI-CV" → "MIDI to CV"
- Leave `### Bogaudio MIDI-CV (Bogaudio)` unchanged — Bogaudio names not in scope
- Leave generic uses like "any MIDI-CV converter" unchanged — concept, not module name
- The section heading at line 59 `### VCV MIDI-CV + keyboard` → verify this is in sequencer.md not midi-cv.md; adjust accordingly

- [ ] **Step 3: Edit userguide.md**

Changes:
- Line 61: `The **MIDI-CV** module (in Core)` → `The **MIDI to CV** module (VCV Core)`

- [ ] **Step 4: Edit faq.md**

Read the file. Lines 61, 64, 67 reference `MIDI-CV`. These are how-to instructions referring to the VCV Core MIDI to CV module:

- `Confirm the MIDI-CV module is added` → `Confirm the MIDI to CV module is added`
- `MIDI-CV in its default mode is monophonic` → `MIDI to CV in its default mode is monophonic`
- `right-click the MIDI-CV module` → `right-click the MIDI to CV module`
- `Connect the MIDI-CV module's **Pitch Bend** output` → `Connect the MIDI to CV module's **Pitch Bend** output`

- [ ] **Step 5: Edit patching-use-cases.md**

Changes:
- `MIDI-CV connection` → `MIDI to CV connection` (if referring to VCV Core module)
- `Fundamental Noise` → `VCV Free Noise`
- `Fundamental Quantizer` → `VCV Free Quantizer`
- `Fundamental VCF` → `VCV Free VCF`
- `Fundamental VCA` → `VCV Free VCA`

- [ ] **Step 6: Verify**

```bash
grep -n "Fundamental\|VCO-1\|SEQ-3\|VCMixer\|MIDI-CV\|AUDIO-8" \
  /home/witzman/rack/VCVRack-Doku/src/midi-cv.md \
  /home/witzman/rack/VCVRack-Doku/src/userguide.md \
  /home/witzman/rack/VCVRack-Doku/src/faq.md \
  /home/witzman/rack/VCVRack-Doku/src/patching-use-cases.md
```

Expected: zero matches. Acceptable: `Bogaudio MIDI-CV` in midi-cv.md (Bogaudio subsection — leave), generic concept uses of "MIDI-CV" in faq.md if present.

- [ ] **Step 7: Commit**

```bash
cd /home/witzman/rack/VCVRack-Doku && git add src/midi-cv.md src/userguide.md src/faq.md src/patching-use-cases.md && git commit -m "docs: canonicalize module names in guide and navigation pages"
```

---

### Task 6: Global verification pass

**Files:** All `VCVRack-Doku/src/*.md`

- [ ] **Step 1: Grep for all patterns that should be gone**

```bash
grep -rn "Fundamental VCO\|Fundamental VCF\|Fundamental VCA\|Fundamental ADSR\|Fundamental LFO\|Fundamental SEQ\|Fundamental Mixer\|Fundamental Noise\|Fundamental Quantizer\|Fundamental 8vert\|Fundamental Delay\|Fundamental Clock\|VCO-1\|SEQ-3\b\|VCMixer\|WTVCO\|WTLFO\|AudioInterface2\|AUDIO-8\|MIDI-GATE" \
  /home/witzman/rack/VCVRack-Doku/src/
```

Expected: zero matches.

- [ ] **Step 2: Grep for "(from Core)" and "(in Core)" patterns that should be gone**

```bash
grep -rn "from Core\|in Core)\|also in Core" /home/witzman/rack/VCVRack-Doku/src/
```

Expected: zero matches.

- [ ] **Step 3: Grep for bare "(Fundamental)" plugin attributions that should be "(VCV Free)"**

```bash
grep -rn "(Fundamental)" /home/witzman/rack/VCVRack-Doku/src/
```

Expected: zero matches.

- [ ] **Step 4: Spot-check that Bogaudio/Impromptu/Valley names are untouched**

```bash
grep -rn "Bogaudio ADSR\|Bogaudio VCO\|Bogaudio LFO\|Impromptu Clocked\|Valley Plateau" /home/witzman/rack/VCVRack-Doku/src/ | wc -l
```

Expected: a non-zero count (these should still be present). If zero, something went wrong.

- [ ] **Step 5: Final commit if any cleanup needed, then push**

```bash
cd /home/witzman/rack/VCVRack-Doku && git log --oneline -6
```

Review the last 6 commits match what was done. Then:

```bash
git push
```
