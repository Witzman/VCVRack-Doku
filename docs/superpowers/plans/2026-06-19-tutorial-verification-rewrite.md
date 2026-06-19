# Tutorial Verification & Rewrite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Verify every instruction in all VCV Rack tutorials against C++ source code, fix every error (wrong params, wrong value formats, non-existent module features), and update all .vcv patch files to match corrected tutorials.

**Architecture:** Four sequential phases — Phase 1 clones 3rd-party repos and extracts param specs from C++ `configParam()` calls into `modules.md` as sole ground truth; Phase 2 fixes all tutorial markdown using that ground truth; Phase 3 runs adversarial grillme verification until zero findings; Phase 4 creates/updates all .vcv patch files to match corrected tutorials.

**Tech Stack:** Markdown, JSON (.vcv), C++ source reading, bash, git, Python (`VCVRack-Doku/generate.py`)

## Global Constraints

- All param specs in `modules.md`: sourced from `configParam()` calls only — no assumptions, no docs
- All tutorial values: state in **UI display format** (%, Hz, ms, dB) — never raw internal 0–1
- .vcv port IDs: from `modules.md` only — verify against table before writing any cable
- .vcv format: plain JSON (not zstd), version field `"2.5.2"`, module IDs sequential from 1
- SurgeXT plugin slug in .vcv files: `"SurgeXTRack"` — model name from cloned source only
- Chronoblob2 (AlrightDevices): every param entry must carry "(observed UI — source proprietary)" caveat
- No `[file:line]` citations in tutorial prose
- No confidence markers (`[high]`/`[low]`) in output
- Use model `claude-opus-4-8` for all subagent dispatches
- Reference files before starting any task: `rack/patch.md`, `rack/modules.md`, `rack/VCVRack-Doku/docs/superpowers/specs/2026-06-19-tutorial-verification-rewrite-design.md`, `rack/VCVRack-Doku/docs/superpowers/specs/2026-06-19-vcv-step-patches-design.md`

---

### Task 1: Clone Third-Party Plugin Repos

**Files:**
- Create: `/home/witzman/rack/BogaudioModules/` (git clone)
- Create: `/home/witzman/rack/ImpromptuModular/` (git clone)
- Create: `/home/witzman/rack/ValleyRackFree/` (git clone)
- Create: `/home/witzman/rack/SurgeXTRack/` (git clone)

**Interfaces:**
- Produces: local source trees consumed by Tasks 2, 3, 4

- [ ] **Step 1: Clone Bogaudio**
```bash
cd /home/witzman/rack
git clone --depth=1 https://github.com/bogaudio/BogaudioModules.git
```
Expected: `BogaudioModules/` created, contains `src/` directory.

- [ ] **Step 2: Verify Bogaudio ADSR source present**
```bash
ls /home/witzman/rack/BogaudioModules/src/ | grep -i adsr
```
Expected: at least one file with "ADSR" in the name.

- [ ] **Step 3: Clone ImpromptuModular**
```bash
cd /home/witzman/rack
git clone --depth=1 https://github.com/MarcBoule/ImpromptuModular.git
```
Expected: `ImpromptuModular/` created.

- [ ] **Step 4: Clone ValleyRackFree**
```bash
cd /home/witzman/rack
git clone --depth=1 https://github.com/ValleyAudio/ValleyRackFree.git
```
Expected: `ValleyRackFree/` created.

- [ ] **Step 5: Clone SurgeXTRack**
```bash
cd /home/witzman/rack
git clone --depth=1 https://github.com/surge-synthesizer/surge-rack.git SurgeXTRack
```
Expected: `SurgeXTRack/` created.

- [ ] **Step 6: List SurgeXTRack source files to locate filter module**
```bash
ls /home/witzman/rack/SurgeXTRack/src/ | grep -i "filter\|vcf\|filt"
```
Note the filename(s) — needed in Task 4.

- [ ] **Step 7: Verify all repos present**
```bash
ls -d /home/witzman/rack/{BogaudioModules,ImpromptuModular,ValleyRackFree,SurgeXTRack}
```
Expected: all four directories listed without error.

---

### Task 2: Extract Fundamental Plugin Param Specs → modules.md

Add a `### Params` subsection after the port table for each Fundamental module. Values are already known from source and are included below verbatim.

**Files:**
- Modify: `/home/witzman/rack/modules.md`

**Interfaces:**
- Produces: param tables for VCO, VCF, VCA-1, VCA-2, ADSR, SEQ3, LFO, 8vert, VCMixer — consumed by Tasks 5, 6, 7, 9, 10, 11

- [ ] **Step 1: Verify source matches known values**
```bash
grep "configParam" /home/witzman/rack/Fundamental/src/VCO.cpp
grep "configParam" /home/witzman/rack/Fundamental/src/VCF.cpp
grep "configParam" /home/witzman/rack/Fundamental/src/ADSR.cpp
```
Expected (confirm matches before proceeding):
- VCO: `FREQ_PARAM, -76.f, 76.f, 0.f, "Frequency", " Hz", dsp::FREQ_SEMITONE, dsp::FREQ_C4`
- VCF: `RES_PARAM, 0.f, 1.f, 0.f, "Resonance", "%", 0.f, 100.f`
- ADSR: `SUSTAIN_PARAM, 0.f, 1.f, 0.5f, "Sustain", "%", 0, 100`

If any line doesn't match, read the actual output and adjust the tables below accordingly.

- [ ] **Step 2: Add VCO Params section**

In `modules.md`, after the VCO port table (the `| Square | output | 3 |` row), insert:

```markdown

**FINE_PARAM: removed.** Exists in source enum as `FINE_PARAM, // removed` — no `configParam()` call, no UI knob. Do not reference in tutorials.

### Params (VCV VCO)

| Param | Internal range | Display unit | Display scale | Default |
|-------|---------------|--------------|---------------|---------|
| Frequency (FREQ) | −76 – 76 | Hz | 2^(v/12) × C4 Hz (semitone scale); −76≈11 Hz, 0=C4≈261 Hz, 76≈4434 Hz | 0 (C4) |
| Frequency modulation | −1 – 1 | % | ×100; −1=−100%, 0=0%, 1=100% | 0 |
| Pulse width | 0.01 – 0.99 | % | ×100; 0.01=1%, 0.5=50%, 0.99=99% | 0.5 (50%) |
| Pulse width modulation | −1 – 1 | % | ×100 | 0 |

**Detuning tip:** No FINE knob exists. To detune two VCOs against each other, nudge one FREQ knob by the smallest perceptible amount (a fraction of a semitone) until you hear slow amplitude beating. Tune by ear — beating rate = detuning amount.
```

- [ ] **Step 3: Add VCF Params section**

In `modules.md`, after the VCF port table and the `**No bandpass output exists.**` note, insert:

```markdown

### Params (VCV VCF)

Source constants: `freqMin ≈ −0.003`, `freqMax ≈ 1.135`, `freqDefault = 0.5`; displayBase=2^10=1024, displayMultiplier=C4/32≈8.176 Hz.

| Param | Internal range | Display unit | Display scale | Default |
|-------|---------------|--------------|---------------|---------|
| Cutoff frequency | ~0 – ~1.14 | Hz | 1024^value × 8.176; ~0=8 Hz, 0.5≈262 Hz, ~1.14=22 kHz | 0.5 (~262 Hz) |
| Resonance | 0 – 1 | % | ×100; 0=0%, 1=100% | 0 (0%) |
| Resonance CV | −1 – 1 | % | ×100 | 0 |
| Cutoff frequency CV | −1 – 1 | % | ×100 | 0 |
| Drive | −1 – 1 | % | ×100 +100; −1=0%, 0=100%, 1=200% | 0 (100%) |
```

- [ ] **Step 4: Add ADSR Params section**

In `modules.md`, after the VCV ADSR port table, insert:

```markdown

### Params (VCV ADSR)

Source constants: `MIN_TIME = 0.001 s`, `MAX_TIME = 10 s`, `LAMBDA_BASE = 10000`.
A/D/R display formula: `10000^value × 1 ms` — logarithmic.

| Param | Internal range | Display unit | Display scale | Default |
|-------|---------------|--------------|---------------|---------|
| Attack | 0 – 1 | ms | 10000^v × 1; 0=1 ms, 0.5=100 ms, 1=10000 ms | 0.5 (100 ms) |
| Decay | 0 – 1 | ms | same scale | 0.5 (100 ms) |
| Sustain | 0 – 1 | % | ×100; 0=0%, 1=100% | 0.5 (50%) |
| Release | 0 – 1 | ms | same scale | 0.5 (100 ms) |

**Internal → display shortcuts:** 0.2≈4 ms, 0.3≈16 ms, 0.4≈40 ms, 0.6≈250 ms, 0.8≈1600 ms, 0.9≈4000 ms (≈4 s), 0.95≈6300 ms.
```

- [ ] **Step 5: Add 8vert Params section**

In `modules.md`, after the 8vert port table, insert:

```markdown

### Params (8vert)

| Param | Internal range | Display unit | Display scale | Default |
|-------|---------------|--------------|---------------|---------|
| Row N gain | −1 – 1 | % | ×100; −1=−100%, 0=0%, 1=100% | 0 (0%) |

In tutorials: state 8vert knob positions as % (e.g. "30%" not "0.3", "5%" not "0.05").
```

- [ ] **Step 6: Add VCMixer Params section**

In `modules.md`, after the VCMixer port table, insert:

```markdown

### Params (VCMixer)

| Param | Internal range | Display unit | Display scale | Default |
|-------|---------------|--------------|---------------|---------|
| Mix level | 0 – 2 | dB | −10^v × 20; 0=−∞ dB, 1=0 dB, 2≈+6 dB | 1 (0 dB) |
| Channel N level | 0 – √2 | dB | −10^v × 40 (custom); 0=−∞, 1=0 dB, √2≈+3 dB | 1 (0 dB) |

In tutorials: state channel levels in dB (e.g. "set level to −4 dB" not "0.6"). Unity = 0 dB (default knob center). For rough attenuation: 0.6≈−4 dB, 0.7≈−3 dB, 0.5≈−6 dB.
```

- [ ] **Step 7: Add LFO Params section**

```bash
grep "configParam" /home/witzman/rack/Fundamental/src/LFO.cpp
```
LFO FREQ uses `FrequencyQuantity`: displayBase=2, displayMultiplier=1. Range: −8 to 10.
Insert after VCV LFO port table:

```markdown

### Params (VCV LFO)

| Param | Internal range | Display unit | Display scale | Default |
|-------|---------------|--------------|---------------|---------|
| Frequency | −8 – 10 | Hz | 2^value × 1; −8≈0.004 Hz, 0=1 Hz, 1=2 Hz, 10=1024 Hz | 1 (2 Hz) |
| Frequency modulation | −1 – 1 | % | ×100 | 0 |
| Pulse width | 0.01 – 0.99 | % | ×100 | 0.5 (50%) |
| Pulse width modulation | −1 – 1 | % | ×100 | 0 |

Note: This is the VCV LFO. Tutorials primarily use Bogaudio LFO — see Bogaudio section.
```

- [ ] **Step 8: Add SEQ3 Params section**

SEQ3 CV step knobs: `−10 to 10, unit " V"`. TEMPO_PARAM: `2^v × 60 bpm`, but SEQ3 Tempo is unused in tutorials (Clocked drives clock). Insert after SEQ3 port table:

```markdown

### Params (SEQ3)

| Param | Internal range | Display unit | Display scale | Default |
|-------|---------------|--------------|---------------|---------|
| CV step knobs | −10 – 10 | V | linear; −10=−10 V, 0=0 V, 10=10 V | 0 V |
| Steps | 1 – 8 | (count) | integer display | 8 |
| Tempo | −2 – 4 | bpm | 2^v × 60; −2=15 bpm, 1=120 bpm, 4=960 bpm | 1 (120 bpm) |

In tutorials: set CV step knobs in volts (e.g. "−2.5 V"). 1 V/oct: G2≈−1.42 V, F2≈−1.58 V, Eb2≈−1.75 V relative to C4=0 V.
```

- [ ] **Step 9: Verify all sections added**
```bash
grep "### Params" /home/witzman/rack/modules.md
```
Expected: lines for VCO, VCF, ADSR, 8vert, VCMixer, LFO, SEQ3 (minimum 7 Fundamental entries).

---

### Task 3: Extract Bogaudio Plugin Param Specs → modules.md

**Files:**
- Read: `BogaudioModules/src/ADSR.cpp`, `ADSR.hpp`, `LFO.cpp`, `SampleHold.cpp`
- Modify: `/home/witzman/rack/modules.md`

**Interfaces:**
- Consumes: cloned `BogaudioModules/` from Task 1
- Produces: Bogaudio ADSR, LFO param tables in modules.md — consumed by Tasks 5, 6, 7

- [ ] **Step 1: Extract Bogaudio ADSR configParam calls**
```bash
grep -n "configParam\|ATTACK\|DECAY\|SUSTAIN\|RELEASE" \
  /home/witzman/rack/BogaudioModules/src/ADSR.cpp | head -40
```
If ADSR is defined in a header, also check:
```bash
grep -rn "configParam" /home/witzman/rack/BogaudioModules/src/ --include="*.hpp" | grep -i adsr
```
Note: look for the 5th arg (label string), 6th (unit string), 7th (displayBase), 8th (displayMultiplier) for each A/D/S/R param.

- [ ] **Step 2: Add Bogaudio ADSR Params section to modules.md**

Find the `### Bogaudio-ADSR` section. After the port table, insert a `### Params (Bogaudio ADSR)` subsection using values from Step 1. The table format is:

```markdown
### Params (Bogaudio ADSR)

Source: `BogaudioModules/src/ADSR.cpp`

| Param | Internal range | Display unit | Display scale | Default |
|-------|---------------|--------------|---------------|---------|
| Attack  | [min]–[max] | [unit] | [formula] | [default] |
| Decay   | [min]–[max] | [unit] | [formula] | [default] |
| Sustain | [min]–[max] | [unit] | [formula] | [default] |
| Release | [min]–[max] | [unit] | [formula] | [default] |
```

Replace every `[…]` with actual values read from source. Do not leave placeholders.

- [ ] **Step 3: Extract Bogaudio LFO configParam calls**
```bash
grep -n "configParam" /home/witzman/rack/BogaudioModules/src/LFO.cpp | head -20
```
Focus on FREQ_PARAM: note display unit (Hz expected), range, scale.

- [ ] **Step 4: Add Bogaudio LFO Params section to modules.md**

After the `### Bogaudio-LFO` port table, insert:

```markdown
### Params (Bogaudio LFO)

Source: `BogaudioModules/src/LFO.cpp`

| Param | Internal range | Display unit | Display scale | Default |
|-------|---------------|--------------|---------------|---------|
| Frequency | [range] | [unit] | [scale] | [default] |
```

Fill from Step 3 output. The tutorial sets "0.05 Hz", "0.03 Hz", "0.08 Hz" — verify these are valid display values within range. If the range excludes 0.03 Hz, note the minimum and flag it as a tutorial error.

- [ ] **Step 5: Verify Bogaudio-LFO frequency range covers 0.03–0.1 Hz**
```bash
grep -n "FREQ_PARAM\|MIN_FREQ\|MAX_FREQ\|frequency" \
  /home/witzman/rack/BogaudioModules/src/LFO.cpp | head -20
```
The tutorial uses "0.05 Hz", "0.03 Hz", "0.08 Hz". If these fall outside the LFO's display range, note them as errors to fix in Task 5.

- [ ] **Step 6: Verify Bogaudio ADSR sustain is %-based**
If Step 1 shows Bogaudio ADSR Sustain displays as %, then tutorial values "Sustain 1.0" and "Sustain 0.0" must become "100%" and "0%". If it displays 0–1 unitless, the tutorial values may be correct — document accordingly.

---

### Task 4: Identify SurgeXT Filter Module for Bandpass Fix

VCV VCF has no bandpass output. `slow-psybient.md` Part 4 requires bandpass — use SurgeXT filter instead.

**Files:**
- Read: `SurgeXTRack/src/` (filter module source)
- Modify: `/home/witzman/rack/modules.md` — add SurgeXTRack section

**Interfaces:**
- Consumes: cloned `SurgeXTRack/` from Task 1
- Produces: SurgeXT filter model name + port IDs — consumed by Task 5 (Part 4 fix) and Task 9 (.vcv Part 4 file)

- [ ] **Step 1: Find SurgeXT filter module files**
```bash
ls /home/witzman/rack/SurgeXTRack/src/ | grep -i "filter\|vcf\|filt"
```
Note the filename(s).

- [ ] **Step 2: Find the model name (for .vcv files)**
```bash
grep -rn "createModel\|MODEL\|model" /home/witzman/rack/SurgeXTRack/src/ | grep -i "filter" | head -10
```
The model name is the string used in `.vcv` JSON as `"model": "..."`. Note it exactly.

- [ ] **Step 3: Extract SurgeXT filter port IDs**
```bash
grep -n "configInput\|configOutput" /home/witzman/rack/SurgeXTRack/src/[FILTER_FILE].cpp
```
Replace `[FILTER_FILE]` with the filename found in Step 1.
Find:
- Audio in: label and inputId
- Bandpass out: label and outputId
- Frequency CV in: label and inputId (if present)
- Resonance CV in: label and inputId (if present)

- [ ] **Step 4: Add SurgeXTRack section to modules.md**

After the AlrightDevices section, add:

```markdown
---

## SurgeXTRack plugin (`"plugin": "SurgeXTRack"`)

Source: `SurgeXTRack/src/`

### SurgeXT Filter (`"model": "[MODEL_NAME]"`)
Source: `SurgeXTRack/src/[FILTER_FILE].cpp`

| Port | Direction | ID | Label |
|------|-----------|-----|-------|
| Audio in | input | [N] | "[label]" |
| Bandpass out | output | [N] | "[label]" |
| [other key ports] | … | … | … |

### Params (SurgeXT Filter)

| Param | Internal range | Display unit | Display scale | Default |
|-------|---------------|--------------|---------------|---------|
| [FREQ param] | [range] | [unit] | [scale] | [default] |
| [RES param]  | [range] | [unit] | [scale] | [default] |
```

Replace all `[…]` with actual values from Steps 2–3.

- [ ] **Step 5: Verify bandpass port exists**
```bash
grep -in "bandpass\|bp\|band" /home/witzman/rack/SurgeXTRack/src/[FILTER_FILE].cpp | head -10
```
If no bandpass output exists, identify the correct SurgeXT module that has one and repeat Steps 1–4 for it. Do not proceed to Task 5 until a bandpass port is confirmed.

---

### Task 5: Fix slow-psybient.md — All Errors

All known errors plus any discovered via Tasks 2–4. The fixes below are firm; run the final verification step to catch any remaining issues.

**Files:**
- Modify: `/home/witzman/rack/VCVRack-Doku/src/slow-psybient.md`

**Interfaces:**
- Consumes: modules.md param tables from Tasks 2–4; SurgeXT model name + port label from Task 4
- Produces: corrected tutorial consumed by Tasks 8 (grillme) and 9 (.vcv files)

- [ ] **Step 1: Fix Part 2 Step 2 — FINE knob (does not exist)**

Find:
```
Set one VCO FREQ knob so it outputs G2 (roughly -1.5V from center). Set the other to the same pitch, then use FINE to detune it by about +7 cents.
```
Replace with:
```
Set one VCO **FREQ** knob to G2 (approximately 98 Hz shown on the display). Set the other VCO **FREQ** to the same pitch, then nudge its **FREQ** knob by the smallest perceptible amount until you hear slow amplitude beating between the two oscillators. Tune by ear — faster beating = more detuning, slower beating = less. There is no FINE knob on VCV VCO.
```

- [ ] **Step 2: Fix Part 2 Step 4 — RES display format**

Find:
```
Set VCF FREQ to about 600 Hz, RES at 0.2.
```
Replace with:
```
Set VCF **Cutoff frequency** to about 600 Hz, **Resonance** at 20%.
```

- [ ] **Step 3: Fix Part 2 Step 5 — Bogaudio ADSR Sustain format**

Find:
```
Set: Attack 4 seconds, Decay 0, Sustain 1.0, Release 8 seconds.
```
Replace with (adjust A/D/R units based on Bogaudio ADSR display from Task 3):
```
Set: Attack 4 s, Decay 0 s, Sustain 100%, Release 8 s.
```
If Task 3 reveals Bogaudio ADSR uses ms, change to "4000 ms" and "8000 ms".

- [ ] **Step 4: Fix Part 2 Step 9 — 8vert knob % format**

Find:
```
Set the knob to +0.3.
```
Replace with:
```
Set the knob to +30%.
```

- [ ] **Step 5: Fix Part 3 Step 5 — RES format**

Find:
```
Set VCF FREQ to 150 Hz, RES near zero.
```
Replace with:
```
Set VCF **Cutoff frequency** to 150 Hz, **Resonance** near 0%.
```

- [ ] **Step 6: Fix Part 3 Step 6 — Bogaudio ADSR Sustain format**

Find:
```
Attack 10ms, Decay 400ms, Sustain 0.0, Release 100ms.
```
Replace with (adjust A/D/R units if Task 3 reveals different display):
```
Attack 10 ms, Decay 400 ms, Sustain 0%, Release 100 ms.
```

- [ ] **Step 7: Fix Part 4 Step 4 — bandpass mode + switch to SurgeXT**

Read the SurgeXT filter model name and bandpass output label from `modules.md` (added in Task 4).

Find this entire step line:
```
VCO (set to TRI output for a softer character) → VCF (bandpass mode, FREQ at 1.5 kHz, RES 0.4) → VCA.
```
Replace with:
```
VCO (set to **Triangle** output for a softer character) → **[SurgeXT Filter model name]** (SurgeXTRack) in bandpass mode, FREQ at 1.5 kHz, Resonance at 40% → VCA.

> *Better choice: **[SurgeXT Filter model name]** (SurgeXTRack) has a true bandpass output. VCV VCF has only LPF and HPF — it cannot do bandpass.*
```

Also update the **Modules needed** line at the top of Part 4:
Find: `VCF (VCV)`
Replace with: `[SurgeXT Filter model name] (SurgeXTRack)`

Update the Part 4 Mermaid diagram node:
Find: `VCF["VCF\n(VCV)"]`
Replace with: `VCF["[SurgeXT model]\n(SurgeXTRack)"]`

Find edge label: `-->|"LPF"|`
Replace with: `-->|"[bandpass output label]"|`

- [ ] **Step 8: Fix Part 4 Step 5 — ADSR Sustain 0**

Find:
```
Attack 5ms, Decay 300ms, Sustain 0, Release 200ms.
```
Replace with (adjust units if Task 3 reveals ms ≠ Bogaudio display):
```
Attack 5 ms, Decay 300 ms, Sustain 0%, Release 200 ms.
```

- [ ] **Step 9: Fix Part 5 — Kick RES and Sustain 0**

Find:
```
Noise White → VCF (LP, 80 Hz, RES 0.1) → VCA.
```
Replace with:
```
Noise White → VCF (**Cutoff frequency** 80 Hz, **Resonance** 10%, LPF output) → VCA.
```

Find all three drum ADSR `Sustain 0` instances:
```
ADSR: Attack 2ms, Decay 80ms, Sustain 0, Release 50ms.
ADSR: Attack 1ms, Decay 120ms, Sustain 0, Release 60ms.
ADSR: Attack 1ms, Decay 40ms, Sustain 0, Release 20ms.
```
Replace each `Sustain 0` with `Sustain 0%`. (3 replacements total)

- [ ] **Step 10: Fix Part 6 — 8vert % format**

Find and replace each occurrence:

| Find | Replace |
|------|---------|
| `very low attenuation (0.05 — tiny amount)` | `very low attenuation (5% — tiny amount)` |
| `Row 2 input at 0.4` | `Row 2 input at 40%` |
| `Row 3 input (0.3)` | `Row 3 input (30%)` |
| `Row 4 input (0.2)` | `Row 4 input (20%)` |

- [ ] **Step 11: Fix Part 6 Mermaid — if 8vert labels changed**
No Mermaid changes needed — Part 6 diagram uses `-->|"Row N"|` labels, which are port names (unchanged).

- [ ] **Step 12: Verify all known errors are gone**
```bash
grep -n "FINE\|Sustain 0\.\|Sustain 1\.0\|RES at 0\.\|RES 0\.\|bandpass mode\| 0\.3\b\| 0\.05\b\| 0\.4\b\| 0\.2\b" \
  /home/witzman/rack/VCVRack-Doku/src/slow-psybient.md
```
Expected: 0 matches (or only matches in comments/non-instruction context). Investigate any remaining hit.

---

### Task 6: Audit and Fix first-patch.md and intermediate-patch.md

**Files:**
- Read + Modify: `/home/witzman/rack/VCVRack-Doku/src/first-patch.md`
- Read + Modify: `/home/witzman/rack/VCVRack-Doku/src/intermediate-patch.md`

**Interfaces:**
- Consumes: modules.md param tables from Tasks 2–3

- [ ] **Step 1: Scan first-patch.md for internal-format values**
```bash
grep -n "RES\|Sustain\|Attack\|Decay\|Release\|FINE\|0\.[0-9]\b" \
  /home/witzman/rack/VCVRack-Doku/src/first-patch.md
```
For each hit: check whether the value is stated in display format (%, Hz, ms, dB) or raw 0–1 internal. Fix any that use raw internal format.

- [ ] **Step 2: Verify VCO references in first-patch.md**
```bash
grep -n "FINE\|fine\|cent\|detun" /home/witzman/rack/VCVRack-Doku/src/first-patch.md
```
If "FINE" appears, remove it — FINE_PARAM was removed from VCV VCO source. Use FREQ nudge instead.

- [ ] **Step 3: Verify VCF references in first-patch.md**
```bash
grep -n "bandpass\|BP\|RES\|resonan" /home/witzman/rack/VCVRack-Doku/src/first-patch.md
```
If "bandpass" appears, it is an error — VCV VCF has no bandpass output. Rewrite to use LPF or HPF as appropriate.
If RES values appear as 0–1 decimals, convert to %.

- [ ] **Step 4: Verify ADSR references in first-patch.md**
```bash
grep -n "Sustain\|sustain\|ADSR\|attack\|decay\|release" \
  /home/witzman/rack/VCVRack-Doku/src/first-patch.md
```
Any Sustain value written as a decimal (not %) must be converted. Any A/D/R value without a unit (ms or s) must have the unit added.

- [ ] **Step 5: Apply all first-patch.md fixes found in Steps 1–4**

Edit the file with the specific changes identified. Each change must use display-format values from modules.md.

- [ ] **Step 6: Scan intermediate-patch.md for internal-format values**
```bash
grep -n "RES\|Sustain\|Attack\|Decay\|Release\|FINE\|VEL\|0\.[0-9]\b" \
  /home/witzman/rack/VCVRack-Doku/src/intermediate-patch.md
```
"VEL" is a known prior error (Bogaudio ADSR has no VEL input — already documented in modules.md note). Verify it's not present. If it is, remove it.

- [ ] **Step 7: Apply all intermediate-patch.md fixes**

Same approach as Steps 2–5 for first-patch.md. Verify all Bogaudio ADSR values use the display format confirmed in Task 3.

---

### Task 7: Audit and Fix Reference Pages

Audit all reference pages that state specific param values.

**Files:**
- Read + Modify: `VCVRack-Doku/src/vco.md`, `vcf.md`, `adsr.md`, `lfo.md`, `envelope.md`, `sequencer.md`, `vca.md`, `sample-hold.md`, `noise.md`, `quantizer.md`, `clock.md`, `delay-reverb-chorus.md`, `mixer.md`, `attenuverter.md`

**Interfaces:**
- Consumes: modules.md param tables from Tasks 2–3

- [ ] **Step 1: Check which reference pages exist**
```bash
ls /home/witzman/rack/VCVRack-Doku/src/*.md | grep -v "slow-psybient\|first-patch\|intermediate"
```
Note which of the reference pages from the spec actually exist. Audit only those that exist.

- [ ] **Step 2: Bulk scan all reference pages for suspect values**
```bash
grep -rn "RES\|Sustain\|FINE\|bandpass\| 0\.[0-9]\b\|VEL\b" \
  /home/witzman/rack/VCVRack-Doku/src/ \
  --include="*.md" \
  --exclude="slow-psybient.md" --exclude="first-patch.md" --exclude="intermediate-patch.md"
```
List every hit. For each: check against modules.md display format and fix if wrong.

- [ ] **Step 3: Verify vcf.md does not claim bandpass**
```bash
grep -n "bandpass\|BP\|band" /home/witzman/rack/VCVRack-Doku/src/vcf.md 2>/dev/null
```
If "bandpass" appears as a feature of VCV VCF, remove or rewrite the claim. VCV VCF has LPF and HPF only.

- [ ] **Step 4: Verify vco.md does not reference FINE**
```bash
grep -n "FINE\|fine\|cent" /home/witzman/rack/VCVRack-Doku/src/vco.md 2>/dev/null
```
If FINE is mentioned as a knob, remove it.

- [ ] **Step 5: Apply all reference page fixes**

Edit each affected file with the specific changes identified in Steps 2–4. Keep changes minimal — fix only errors found, no surrounding rewrites.

- [ ] **Step 6: Final bulk scan to confirm clean**
```bash
grep -rn "FINE\|bandpass\|Sustain [01]\.[0-9]\|RES at 0\.[0-9]\|VEL\b" \
  /home/witzman/rack/VCVRack-Doku/src/ --include="*.md"
```
Expected: 0 results.

---

### Task 8: Adversarial Grillme Verification

Dispatch a separate agent with zero prior context to adversarially verify every tutorial instruction.

**Files:**
- Read-only: all `VCVRack-Doku/src/*.md`, `modules.md`
- Modify (fixes only): any tutorial file where grillme finds a failure

**Interfaces:**
- Consumes: corrected tutorials from Tasks 5–7, complete modules.md from Tasks 2–4

- [ ] **Step 1: Dispatch grillme agent**

Dispatch a fresh `claude-opus-4-8` agent with this prompt:

> You are an adversarial verifier. Your job is to find every error in the VCV Rack tutorials in `/home/witzman/rack/VCVRack-Doku/src/`. Use `/home/witzman/rack/modules.md` as the SOLE source of truth for module capabilities and param display formats.
>
> For **every instruction** in every tutorial (`slow-psybient.md`, `first-patch.md`, `intermediate-patch.md`) and every reference page that states specific values, verify all 9 checks:
>
> 1. **Module exists** in stated plugin (cross-check plugin manifest if needed)
> 2. **Knob/param exists** on module — no FINE on VCV VCO, no VEL on Bogaudio ADSR
> 3. **Value in correct display format** — % not 0–1, Hz for frequencies, ms for times
> 4. **Value within valid param range** per modules.md
> 5. **Port exists** in correct direction (input/output)
> 6. **Connection is valid** — polarity makes sense, audio/CV correct
> 7. **Sonic result described** is achievable with stated settings
> 8. **Correct model variant** — VCA-1 (single) vs VCA-2 (dual), etc.
> 9. **SurgeXT alternative** used where VCV module genuinely cannot do the stated function (e.g. bandpass)
>
> Report every failure with: file, line number, the wrong text, and the correct text according to modules.md. If zero failures found, report "GRILLME CLEAN".

- [ ] **Step 2: Apply all grillme findings**

For each reported failure: open the file, find the exact line, make the exact correction specified by the grillme agent.

- [ ] **Step 3: Repeat until clean**

Re-dispatch grillme with the same prompt. Repeat until the agent reports "GRILLME CLEAN".

- [ ] **Step 4: Final scan before committing**
```bash
grep -rn "FINE\|bandpass\| VEL\b\|RES at 0\.[0-9]\|Sustain [01]\.[0-9]" \
  /home/witzman/rack/VCVRack-Doku/src/ --include="*.md"
```
Expected: 0 results.

---

### Task 9: Create slow-psybient .vcv Patch Files (8 files)

Read `rack/patch.md` before starting. Read `rack/VCVRack-Doku/docs/Rack-Doku/slow-psybient-starter.vcv` as format reference.
Wiring spec: `rack/VCVRack-Doku/docs/superpowers/specs/2026-06-19-vcv-step-patches-design.md` § slow-psybient.md.

**Files:**
- Create: `VCVRack-Doku/docs/Rack-Doku/slow-psybient-part1.vcv` through `slow-psybient-part8.vcv`

**Interfaces:**
- Consumes: verified port IDs from `modules.md`; SurgeXT filter model name + port IDs from Task 4

**Key Part 4 deviation from original spec:** Part 4 uses **SurgeXT filter** (bandpass output) instead of VCV VCF. All other parts unchanged from the wiring spec.

- [ ] **Step 1: Confirm SurgeXT filter port IDs are in modules.md**
```bash
grep "SurgeXTRack" /home/witzman/rack/modules.md
```
Expected: section present with model name, port IDs, param table. If missing, complete Task 4 first.

- [ ] **Step 2: Create slow-psybient-part1.vcv**

Modules: Clocked (ImpromptuModular) only. No cables. No audio output required.

```json
{
  "version": "2.5.2",
  "modules": [
    {
      "id": 1,
      "plugin": "ImpromptuModular",
      "model": "Clocked",
      "pos": [0, 0],
      "params": [
        {"id": 0, "value": 89.0}
      ]
    }
  ],
  "cables": []
}
```
Save to `/home/witzman/rack/VCVRack-Doku/docs/Rack-Doku/slow-psybient-part1.vcv`.

Note: Clocked BPM param ID and its internal→display mapping must be verified. Check:
```bash
grep -n "configParam\|TEMPO\|BPM" /home/witzman/rack/ImpromptuModular/src/Clocked.cpp | head -10
```
Use the confirmed internal value for 89 BPM in the params array.

- [ ] **Step 3: Create slow-psybient-part2.vcv**

Modules: Clocked, VCO×2, VCF, VCA-1, Bogaudio-ADSR, Bogaudio-LFO, 8vert, VCMixer (main mix).
Cables from vcv-step-patches spec § slow-psybient Part 2:
- VCO1 SAW(2) → VCMixer CH1(1)
- VCO2 SAW(2) → VCMixer CH2(2)
- VCMixer MIX(0) → VCF IN(3)
- VCF LPF(0) → VCA-1 IN(1)
- BogADSR ENV(0) → VCA-1 CV(0)
- VCA-1 OUT(0) → [MainMix CH1 or AudioInterface2 L]
- BogLFO SINE(4) → 8vert R1in(0)
- 8vert R1out(0) → VCF FREQ(0)

Params:
- VCO1 FREQ_PARAM: internal value for ~98 Hz (G2) ≈ −17 semitones → internal = −17 (range −76–76)
- VCO2 FREQ_PARAM: same as VCO1 (detuning is done by ear, set same in .vcv)
- VCF RES_PARAM: 0.2 (displays as 20%) — internal value IS 0.2
- BogADSR: Attack/Sustain/Release internal values for 4 s sustain=100% release=8 s — derive from Bogaudio source (Task 3)
- BogLFO: internal value for 0.05 Hz — derive from Bogaudio LFO source (Task 3)
- 8vert Row1 gain: 0.3 (displays as 30%) — internal value IS 0.3

- [ ] **Step 4: Create slow-psybient-part3.vcv**

All Part 2 modules + SEQ3 (bass clock), VCO (bass), VCF (bass), VCA-1 (bass), Bogaudio-ADSR (bass).
Additional cables from spec § Part 3:
- Clocked CLK3(3) → SEQ3b CLOCK(1)
- SEQ3b CV1(1) → BassVCO PITCH(0)
- SEQ3b TRIG(0) → BassADSR GATE(0)
- BassVCO SIN(0) → BassVCF IN(3)
- BassVCF LPF(0) → BassVCA-1 IN(1)
- BassADSR ENV(0) → BassVCA-1 CV(0)
- BassVCA-1 OUT(0) → MainMix CH2(2)

Bass SEQ3 CV params: G1=−2.5 V (internal −2.5), F1=−2.75 V (−2.75), Eb1=−3.0 V (−3.0).
Bass ADSR: Sustain 0% → internal 0. A/D/R from Bogaudio source.

- [ ] **Step 5: Create slow-psybient-part4.vcv**

All Part 3 modules + Bogaudio-SampleHold (frag), Noise (frag), Quantizer, VCO (frag), **SurgeXT Filter** (bandpass), VCA-1 (frag), Bogaudio-ADSR (frag).

Key Part 4 deviation: VCF is replaced by SurgeXT Filter (bandpass). Use model name from Task 4 modules.md entry. Port IDs from Task 4.

Cables from spec § Part 4 (with SurgeXT substitution):
- Clocked CLK2(2) → FragS&H TRIG(0)
- Noise WHITE(0) → FragS&H SIG(1)
- FragS&H OUT(0) → Quantizer IN(0)
- Quantizer OUT(0) → FragVCO PITCH(0)
- FragVCO TRI(1) → SurgeXTFilter AudioIn([ID from modules.md])
- SurgeXTFilter BandpassOut([ID]) → FragVCA-1 IN(1)
- FragADSR ENV(0) → FragVCA-1 CV(0)
- Clocked CLK2(2) → FragADSR GATE(0)
- FragVCA-1 OUT(0) → MainMix CH3(3)

- [ ] **Step 6: Create slow-psybient-part5.vcv through part8.vcv**

Follow the same process for Parts 5–8. Wiring spec: vcv-step-patches design doc § slow-psybient Parts 5–8. Key notes:
- Part 5: Drum SEQ3 step gates — STEP_OUTPUTS start at outputId=4. Step 3 gate = outputId=6.
- Part 6: 8vert Row N internal gain values match 30%=0.3, 40%=0.4, 20%=0.2, 5%=0.05.
- Part 7: Plateau DECAY CV inputId=9; Chronoblob2 FEEDBACK CV inputId=4.
- Part 8: Same wiring as Part 7; mixer level params differ (lower levels for balance).

For each file, validate before saving:
1. Every cable's outputId and inputId appear in modules.md for the correct module
2. Signal chain continuity: source → filter/shape → VCA → output
3. No floating ADSR Gate inputs on voiced paths

- [ ] **Step 7: Verify all 8 files created**
```bash
ls -la /home/witzman/rack/VCVRack-Doku/docs/Rack-Doku/slow-psybient-part*.vcv
```
Expected: 8 files, each > 500 bytes.

---

### Task 10: Create first-patch .vcv Patch Files (7 files)

Wiring spec: `rack/VCVRack-Doku/docs/superpowers/specs/2026-06-19-vcv-step-patches-design.md` § first-patch.md.
All modules are Fundamental + Core only.

**Files:**
- Create: `VCVRack-Doku/docs/Rack-Doku/first-patch-step2.vcv` through `first-patch-step8.vcv`

- [ ] **Step 1: Create first-patch-step2.vcv**

Modules: AudioInterface2 (Core). No cables.

```json
{
  "version": "2.5.2",
  "modules": [
    {
      "id": 1,
      "plugin": "Core",
      "model": "AudioInterface2",
      "pos": [0, 0],
      "params": []
    }
  ],
  "cables": []
}
```

- [ ] **Step 2: Create first-patch-step3.vcv through first-patch-step8.vcv**

Follow spec wiring table exactly. Port IDs from modules.md. Key cables:
- step4: MIDI-CV PITCH(0) → VCO PITCH_INPUT(0)
- step5: + MIDI-CV GATE(1) → ADSR GATE_INPUT(4)
- step6: VCO SAW(2) → VCA-1 IN(1); ADSR ENV(0) → VCA-1 CV(0); VCA-1 OUT(0) → Audio L(0) + R(1)
- step7: VCO SAW(2) → VCF IN(3); VCF LPF(0) → VCA-1 IN(1)
- step8: + ADSR ENV(0) → VCF FREQ(0)

For ADSR default params (step 5 onward): use internal 0.5 for all (A=100ms, D=100ms, S=50%, R=100ms — the module defaults). The tutorial adjusts params by ear, so defaults are appropriate.

- [ ] **Step 3: Verify all 7 files**
```bash
ls -la /home/witzman/rack/VCVRack-Doku/docs/Rack-Doku/first-patch-step*.vcv
```
Expected: 7 files.

---

### Task 11: Create intermediate-patch .vcv Patch Files (6 files)

Wiring spec: vcv-step-patches design doc § intermediate-patch.md.
Requires Bogaudio-VCO port IDs (verified from BogaudioModules source in Task 3 and already in modules.md).

**Files:**
- Create: `VCVRack-Doku/docs/Rack-Doku/intermediate-step2.vcv` through `intermediate-step7.vcv`

- [ ] **Step 1: Confirm Bogaudio-VCO port IDs are in modules.md**
```bash
grep -A 15 "Bogaudio-VCO" /home/witzman/rack/modules.md | head -15
```
Expected: port table with PITCH input and SAW output IDs. If not present, read from `BogaudioModules/src/VCO.hpp` and add to modules.md before proceeding.

- [ ] **Step 2: Create intermediate-step2.vcv**

Modules: Clocked (ImpromptuModular). No cables.

- [ ] **Step 3: Create intermediate-step3.vcv through intermediate-step7.vcv**

Follow spec wiring. Key cables:
- step3: Clocked CLK1(1) → SEQ3 CLOCK(1)
- step4: SEQ3 CV1(1) → BogVCO PITCH([ID from modules.md]); SEQ3 TRIG(0) → BogADSR GATE(0)
- step5: BogVCO SAW([ID]) → VCF IN(3); VCF LPF(0) → VCA-2 IN1(2); BogADSR ENV(0) → VCA-2 EXP1(0); VCA-2 OUT1(0) → Audio L(0)
- step6: BogLFO SINE(4) → 8vert R1in(0); 8vert R1out(0) → VCF FREQ(0)
- step7: Clocked CLK1(1) → S&H TRIG(0); Noise WHITE(0) → S&H SIG(1); S&H OUT(0) → 8vert R2in(1); 8vert R2out(1) → VCA-2 LIN1(1)

- [ ] **Step 4: Verify all 6 files**
```bash
ls -la /home/witzman/rack/VCVRack-Doku/docs/Rack-Doku/intermediate-step*.vcv
```
Expected: 6 files.

---

### Task 12: Run Generator, Verify Links, Commit

**Files:**
- Read: `VCVRack-Doku/generate.py` (or `rack-invoke.md` for generator invocation)
- Modify: any `.md` source file if generator reveals broken links

- [ ] **Step 1: Run the generator**
```bash
cd /home/witzman/rack
cat rack-invoke.md
```
Follow the instructions in `rack-invoke.md` exactly to invoke the generator.

- [ ] **Step 2: Verify .vcv download links in generated HTML**
```bash
grep -rn "slow-psybient-part\|first-patch-step\|intermediate-step" \
  /home/witzman/rack/VCVRack-Doku/docs/Rack-Doku/ --include="*.html" | head -30
```
Expected: 21 links present (8 psybient + 7 first-patch + 6 intermediate).

- [ ] **Step 3: Verify all .vcv files are present in output dir**
```bash
ls /home/witzman/rack/VCVRack-Doku/docs/Rack-Doku/*.vcv | wc -l
```
Expected: ≥21 files (may include pre-existing files like `slow-psybient-starter.vcv`).

- [ ] **Step 4: Commit to VCVRack-Doku repo**
```bash
cd /home/witzman/rack/VCVRack-Doku
git add src/ docs/ ../modules.md 2>/dev/null || git add src/ docs/
git status
```
Review staged files. Then:
```bash
git commit -m "$(cat <<'EOF'
fix: verify and correct all tutorials against C++ source; add 21 .vcv patch files

- Fix VCO FINE knob refs (param removed from source)
- Convert all RES/Sustain to UI display format (%, not 0-1)
- Replace VCF bandpass with SurgeXT filter in slow-psybient Part 4
- Convert 8vert knob values to % format
- Add param display specs to modules.md from configParam() source
- Create 21 downloadable .vcv step patch files

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
EOF
)"
```

- [ ] **Step 5: Push to origin**
```bash
cd /home/witzman/rack/VCVRack-Doku
git push
```
Expected: pushes `main` to `master` on origin (GitHub Pages branch). Verify at https://witzman.github.io/VCVRack-Doku/ after ~1 minute.

---

## Self-Review

**Spec coverage check:**

| Spec requirement | Task |
|-----------------|------|
| Clone Bogaudio, ImpromptuModular, Valley, SurgeXT repos | Task 1 |
| Extract Fundamental param specs → modules.md | Task 2 |
| Extract Bogaudio param specs → modules.md | Task 3 |
| Identify SurgeXT filter for bandpass replacement | Task 4 |
| Fix all slow-psybient.md errors (FINE, RES, Sustain, bandpass, 8vert) | Task 5 |
| Audit + fix first-patch.md and intermediate-patch.md | Task 6 |
| Audit + fix reference pages | Task 7 |
| Grillme adversarial verification loop | Task 8 |
| Create slow-psybient .vcv files (8) | Task 9 |
| Create first-patch .vcv files (7) | Task 10 |
| Create intermediate-patch .vcv files (6) | Task 11 |
| Run generator, verify links, commit + push | Task 12 |
| SurgeXT substitution in Part 4 .vcv file | Task 9 Step 5 |
| modules.md extended with source-only params | Tasks 2–4 |
| Chronoblob2 "observed UI" caveat | Global Constraints note; applied during Task 3 |

No gaps found.
