# VCV Step Patches — Design Spec

**Date:** 2026-06-19  
**Scope:** `src/first-patch.md`, `src/intermediate-patch.md`, `src/slow-psybient.md` + 19 new `.vcv` files in `docs/Rack-Doku/`

---

## Goal

For every tutorial step/section that produces meaningful patch state, create a downloadable `.vcv` file reflecting that exact state. Add a download link at the end of each section. Add or improve "you should now hear" text at each step. Port IDs must be verified against source code or live psy.vcv cables — no assumptions.

---

## Reference files (read before any implementation)

| File | Purpose |
|------|---------|
| `rack/patch.md` | .vcv file format, read/write rules, zstd decompression method |
| `rack/modules.md` | Verified inputId/outputId for all modules used in tutorials |
| `rack/VCVRack-Doku/docs/Rack-Doku/slow-psybient-starter.vcv` | Plain JSON format reference |

---

## .vcv file rules

- **Format:** plain JSON (NOT zstd-compressed, NOT TAR-wrapped)
- **Version field:** `"2.5.2"`
- **Module IDs:** sequential integers starting at 1
- **Port IDs:** from `modules.md` only — never assume
- **Output location:** `VCVRack-Doku/docs/Rack-Doku/`
- **psy.vcv:** read-only reference for 3rd party module configs/params. Read via ctypes+libzstd (see `patch.md`). Never overwrite.

---

## File inventory — 19 files

### first-patch.md (7 files — Fundamental + Core only)

| File | Modules present | Key wiring |
|------|----------------|------------|
| `first-patch-step2.vcv` | AudioInterface2 | none |
| `first-patch-step3.vcv` | AudioInterface2, MIDI-CV | none |
| `first-patch-step4.vcv` | AudioInterface2, MIDI-CV, VCO | MIDI-CV PITCH(0) → VCO PITCH_INPUT(0) |
| `first-patch-step5.vcv` | + ADSR | MIDI-CV GATE(1) → ADSR GATE_INPUT(4) |
| `first-patch-step6.vcv` | + VCA-1 | VCO SAW(2) → VCA-1 IN(1); ADSR ENV(0) → VCA-1 CV(0); VCA-1 OUT(0) → Audio L(0) + R(1) |
| `first-patch-step7.vcv` | + VCF | VCO SAW(2) → VCF IN(3); VCF LPF(0) → VCA-1 IN(1) |
| `first-patch-step8.vcv` | same | + ADSR ENV(0) → VCF FREQ(0) |

### intermediate-patch.md (6 files — adds Bogaudio + Impromptu)

| File | Modules present | Key wiring |
|------|----------------|------------|
| `intermediate-step2.vcv` | Clocked | none |
| `intermediate-step3.vcv` | + SEQ3 | Clocked CLK1(1) → SEQ3 CLOCK(1) |
| `intermediate-step4.vcv` | + Bogaudio-VCO, Bogaudio-ADSR | SEQ3 CV1(1) → BogVCO PITCH(?); SEQ3 TRIG(0) → BogADSR GATE(0) |
| `intermediate-step5.vcv` | + VCF, VCA-2, AudioInterface2 | BogVCO SAW(?) → VCF IN(3); VCF LPF(0) → VCA-2 IN1(2); BogADSR ENV(0) → VCA-2 EXP1(0); VCA-2 OUT1(0) → Audio L(0) |
| `intermediate-step6.vcv` | + Bogaudio-LFO, 8vert | BogLFO SINE(4) → 8vert Row1 in(0); 8vert Row1 out(0) → VCF FREQ(0) |
| `intermediate-step7.vcv` | + Bogaudio-SampleHold, Noise | Clocked CLK1(1) → S&H TRIG(0); Noise WHITE(0) → S&H SIG(1); S&H OUT(0) → 8vert Row2 in(1); 8vert Row2 out(1) → VCA-2 LIN1(1) |

**Blocker:** Bogaudio-VCO PITCH input ID and SAW output ID marked `(?)` — implementation agent must look up from [Bogaudio GitHub](https://github.com/bogaudio/BogaudioModules) before writing intermediate files. Add verified IDs to `modules.md`.

### slow-psybient.md (8 files — all 3rd party + Fundamental)

All port IDs for these files are in `modules.md`. VCMixer used as "main mixer" (not MindMeld — tutorials don't require it).

| File | Modules added | Key new wiring |
|------|--------------|----------------|
| `slow-psybient-part1.vcv` | Clocked | none |
| `slow-psybient-part2.vcv` | VCO×2, VCF, VCA-1, Bogaudio-ADSR, Bogaudio-LFO, 8vert, VCMixer | VCO1 SAW(2)→Mix CH1(1); VCO2 SAW(2)→Mix CH2(2); Mix MIX(0)→VCF IN(3); VCF LPF(0)→VCA-1 IN(1); BogADSR ENV(0)→VCA-1 CV(0); VCA-1 OUT(0)→MainMix CH1(1); BogLFO SINE(4)→8vert R1in(0); 8vert R1out(0)→VCF FREQ(0) |
| `slow-psybient-part3.vcv` | + SEQ3, VCO, VCF, VCA-1, Bogaudio-ADSR | Clocked CLK3(3)→SEQ3b CLOCK(1); SEQ3b CV1(1)→BassVCO PITCH(0); SEQ3b TRIG(0)→BassADSR GATE(0); BassVCO SIN(0)→BassVCF IN(3); BassVCF LPF(0)→BassVCA-1 IN(1); BassADSR ENV(0)→BassVCA-1 CV(0); BassVCA-1 OUT(0)→MainMix CH2(2) |
| `slow-psybient-part4.vcv` | + Bogaudio-SampleHold, Noise, Quantizer, VCO, VCF, VCA-1, Bogaudio-ADSR | Clocked CLK2(2)→FragS&H TRIG(0); Noise WHITE(0)→FragS&H SIG(1); FragS&H OUT(0)→Quant IN(0); Quant OUT(0)→FragVCO PITCH(0); FragVCO TRI(1)→FragVCF IN(3); FragVCF LPF(0)→FragVCA-1 IN(1); FragADSR ENV(0)→FragVCA-1 CV(0); Clocked CLK2(2)→FragADSR GATE(0); FragVCA-1 OUT(0)→MainMix CH3(3) |
| `slow-psybient-part5.vcv` | + Noise (drum), VCA-1×3, Bogaudio-ADSR×3, SEQ3, VCMixer (drum) | One SEQ3 for kick+snare (Clocked CLK1(1)→DrumSEQ CLOCK(1), 4 steps, gates 1+3). Kick: DrumSEQ TRIG(0)→KickADSR GATE(0). Snare: DrumSEQ STEP3(6)→SnareADSR GATE(0) — STEP_OUTPUTS+2=outputId=6 fires step 3 only. Hats: Clocked CLK2(2)→HatADSR GATE(0). All Noise WHITE(0)→VCA IN(1); ADSR ENV(0)→VCA CV(0); VCA OUT(0)→DrumMix CHN; DrumMix MIX(0)→MainMix CH4(4) |
| `slow-psybient-part6.vcv` | + Bogaudio-LFO×2, Bogaudio-SampleHold×2, 8vert rows 2–4 | LFO-B SINE(4)→8vert R2in(1); 8vert R2out(1)→PadVCO1 FM(1); 8vert R2out(1)→PadVCO2 FM(1); LFO-C SINE(4)→8vert R3in(2); 8vert R3out(2)→FragVCA-1 CV(0) [offset CV]; ModS&H1 TRIG(0)←Clocked CLK3(3); Noise WHITE(0)→ModS&H1 SIG(1); ModS&H1 OUT(0)→8vert R5in(4); ModS&H2 TRIG(0)←Clocked CLK3(3); Noise WHITE(0)→ModS&H2 SIG(1); ModS&H2 OUT(0)→8vert R6in(5) |
| `slow-psybient-part7.vcv` | + Plateau, Chronoblob2 | MainMix MIX(0)→Plateau L(0) + R(1); Plateau L(0)→FinalMix CH1; Plateau R(1)→FinalMix CH2; FragVCA-1 OUT(0)→Chronoblob2 IN(0); Chronoblob2 OUT(0)→FinalMix CH3; 8vert R5out(4)→Plateau DECAY CV(9); 8vert R6out(5)→Chronoblob2 FEEDBACK CV(4) |
| `slow-psybient-part8.vcv` | same as part7 | identical wiring — only mixer level params differ |

---

## "You should now hear" additions

### first-patch.md

| Step | Text to add |
|------|-------------|
| Step 4 | "Nothing sounds yet — the oscillator is running but has no path to output." |
| Step 5 | "Still silent — the envelope fires when you press a key but there is no VCA carrying the signal through." |
| Step 7 | "You should now hear a darker sound. The VCF is rolling off the high frequencies." |
| Step 8 | "You should now hear the filter open briefly on each note attack, then close back down as the envelope falls." |

Step 6 already has correct text. Steps 2–3 no sound — no change.

### intermediate-patch.md

| Step | Text to add |
|------|-------------|
| Step 3 | "Still silent — clock and sequencer are running, producing CV and gate signals, but no voice module is connected yet." |
| Step 4 | "Still silent — the VCO is tracking the sequence pitches, but no filter, VCA, or output path exists yet." |
| Step 6 | "You should now hear the filter open and close in time with the beat, giving the sequence a rhythmic breathing quality." |
| Step 7 | "You should now hear velocity variation — some notes hit harder, some softer, with a different random level on each step." |

Steps 2 and 5 already have correct text.

### slow-psybient.md

| Part | Change |
|------|--------|
| Part 4 | Make implicit "listen" explicit: "You should now hear sparse random notes in G minor appearing on eighth notes. The triangle wave through the filter gives them a nasal, distant character." |
| Part 8 | Add: "You should now hear the same sounds as Part 7, but better balanced — pad prominent but not harsh, reverb generous and forward in the mix, bass felt more than heard, fragments subtle." |

Parts 1–3, 5–7 already have correct "you should now hear" text.

---

## Download link format

At end of each section, before the closing `---`, add:

```markdown
**[⬇ Download patch — Step N](filename.vcv)**
```

For parts with no meaningful download (first-patch Steps 1, 9 — skipped), no link added.

---

## Logical wiring verification (per file)

Implementation agent must, for each file:
1. List every cable as `ModuleName.outputId(N) → ModuleName.inputId(N)`
2. Resolve N against `modules.md` and confirm port label matches tutorial intent
3. Verify signal chain continuity: sound source → shape → VCA → output
4. Check no floating inputs on required paths (e.g. ADSR Gate must be connected for envelope to fire)

---

## Bogaudio-VCO blocker

Before creating any `intermediate-step*.vcv` file, look up Bogaudio VCO source at [https://github.com/bogaudio/BogaudioModules](https://github.com/bogaudio/BogaudioModules), find `configInput`/`configOutput` calls, add port IDs to `rack/modules.md`.

---

## Post-implementation

After all files written and markdown edited:
1. Run `python3 generate.py` from `VCVRack-Doku/`
2. Verify all new `.vcv` files appear as working download links in generated HTML
3. Commit to VCVRack-Doku repo
