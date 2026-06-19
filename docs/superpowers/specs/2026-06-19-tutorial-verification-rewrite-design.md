# Tutorial Verification & Rewrite Design

**Date:** 2026-06-19
**Status:** Approved

## Problem

VCV Rack tutorials contain errors that block users from following steps:

- **Removed params:** VCO `FINE_PARAM` was removed from source but tutorial says "use FINE to detune +7 cents"
- **Wrong display format:** VCF RES displays as `%` (0–100) but tutorials write raw 0–1 values (e.g. "RES at 0.2" → should be "20%")
- **Wrong display format:** ADSR Sustain displays as `%` but tutorials write "Sustain 1.0" → should be "100%"
- **Non-existent mode:** VCV VCF has no bandpass output. Part 4 slow-psybient says "bandpass mode" — impossible
- **Unverified param formats** throughout all tutorial and reference pages

## Approach: Two-Phase Parallel (B)

### Phase 1 — Build ground truth (parallel agents)

**Agent A:** Extract ALL Fundamental plugin param specs from local C++ source.
Read every `configParam()` call in `Fundamental/src/*.cpp` for modules used in tutorials:
VCO, VCF, VCA-1, VCA-2, ADSR, SEQ3, LFO, 8vert, VCMixer, Noise, Quantizer.

**Agent B:** Clone third-party plugin repos, extract param specs from source:

| Plugin | Repo | Local folder |
|--------|------|-------------|
| Bogaudio | `https://github.com/bogaudio/BogaudioModules` | `BogaudioModules/` |
| ImpromptuModular | `https://github.com/MarcBoule/ImpromptuModular` | `ImpromptuModular/` |
| Valley | `https://github.com/ValleyAudio/ValleyRackFree` | `ValleyRackFree/` |
| SurgeXT | `https://github.com/surge-synthesizer/surge-rack` | `SurgeXTRack/` |

**AlrightDevices / Chronoblob2:** Proprietary license, no source URL. Params documented as "observed from UI — source proprietary" with explicit caveat.

Both agents write into `modules.md` under a new **Params** subsection per module.

### Phase 2 — Fix all tutorials

Using complete `modules.md` as sole ground truth. Every `.md` in `VCVRack-Doku/src/` that states specific knob values gets audited and fixed. Scope includes:
- Step-by-step tutorials: `slow-psybient.md`, `first-patch.md`, `intermediate-patch.md`
- Reference pages with specific values: `vco.md`, `vcf.md`, `adsr.md`, `lfo.md`, `envelope.md`, `sequencer.md`, `vca.md`, `sample-hold.md`, `noise.md`, `quantizer.md`, `clock.md`, `delay-reverb-chorus.md`, `mixer.md`, `attenuverter.md`

### Phase 3 — Adversarial grillme

Separate adversarial agent reads all fixed tutorials + complete `modules.md`. Tries to break every step. Loop until clean.

## modules.md Extension Format

New **Params** subsection under each module entry. Sourced exclusively from `configParam()` calls.

```markdown
### Params

| Param | Internal range | Display unit | Display scale | Default (internal) |
|-------|---------------|--------------|---------------|--------------------|
| Frequency | -76 – 76 | Hz | logarithmic (2^(1/12) base, C4 offset) | 0 (= C4 = 261.63 Hz) |
| Resonance | 0 – 1 | % | ×100 | 0 (= 0%) |
```

Rule: **always state values in UI display format** in tutorials, not internal values.

## SurgeXT Alternative Rule

During audit, check if a tutorial step requires functionality absent in the stated module. If a SurgeXT module covers it correctly and is the genuinely better tool, offer as preferred alternative with note:
> *Better choice: **[Module]** (SurgeXT) — [reason]*

Primary case: bandpass filter. VCV VCF has only LPF and HPF outputs. SurgeXT filter has bandpass. `slow-psybient.md` Part 4 must either switch to SurgeXT or use LPF with high resonance as approximation.

Do not swap modules blindly. Only replace when stated module genuinely cannot perform the described function.

## Grillme Agent Checklist

For every instruction in every tutorial, the adversarial agent verifies:

1. **Module exists** in stated plugin
2. **Knob/param exists** on module (no FINE knob on VCV VCO, no VEL on Bogaudio ADSR)
3. **Value in correct display format** (%, Hz, ms — not internal 0–1)
4. **Value within valid param range**
5. **Port exists** in correct direction (input/output)
6. **Connection is valid** (audio/CV polarity makes sense)
7. **Sonic result described** is achievable with stated settings
8. **Correct model variant** stated where multiple exist (VCA-1 single vs VCA-2 dual)
9. **SurgeXT alternative** available and better where stated module is wrong tool

Grillme reports all failures → coordinator fixes → re-grill. Loop until zero findings.

## Phase 4 — Update .vcv Patch Files

After Phase 3 grillme passes clean, all `.vcv` patch files must be updated to match the corrected tutorials.

**Reference spec:** `docs/superpowers/specs/2026-06-19-vcv-step-patches-design.md` — covers file inventory, port IDs, wiring logic, download link format, "you should now hear" text. That spec provides the structural framework; this spec's corrections take priority over any conflicting values in it.

**What changes in .vcv files after tutorial correction:**

1. **Param values** — `.vcv` JSON `params` array stores internal values (0–1 raw), not display values. After correcting tutorials to display format, ensure .vcv params use the correct internal value. Example: "RES 20%" in tutorial → `"value": 0.2` in .vcv params array (internal scale, unchanged). The display format fix is prose-only; internal .vcv values were already correct if they were ever written correctly.

2. **Module swaps** — if any tutorial step switches from a wrong module (e.g. VCV VCF for bandpass) to a correct module (e.g. SurgeXT filter), the corresponding .vcv file must use the replacement module with correct plugin slug, model, and port IDs. SurgeXT modules are fully supported in .vcv files:
   - Plugin slug: `"SurgeXTRack"` (from library manifest)
   - Model names and port IDs: extracted from cloned `SurgeXTRack/` source via `configInput`/`configOutput` calls — same rule as all other modules
   - Add verified SurgeXT port IDs to `modules.md` before writing any .vcv file that uses them

3. **Removed param references** — VCO FINE_PARAM: if any existing .vcv file references this param ID, verify it has no effect (param exists in enum for legacy but no UI) and document; do not add it to new .vcv files.

4. **Consistency rule:** every .vcv file must be buildable from following the corrected tutorial steps exactly, in order. Grillme agent spot-checks at least one .vcv file per tutorial for this property.

**Output location:** `VCVRack-Doku/docs/Rack-Doku/` (unchanged from vcv-step-patches spec).

---

## Known Issues Captured (pre-fix)

| File | Location | Issue |
|------|----------|-------|
| `slow-psybient.md` | Part 2 Step 2 | "use FINE to detune" — FINE_PARAM removed from VCO source |
| `slow-psybient.md` | Part 2 Step 4 | "RES at 0.2" — should be "20%" |
| `slow-psybient.md` | Part 2 Step 5 | "Sustain 1.0" — should be "100%" |
| `slow-psybient.md` | Part 4 Step 4 | "VCF bandpass mode" — VCF has no bandpass; use SurgeXT or LPF |
| `slow-psybient.md` | Part 3 Step 6 | "Sustain 0.0" — should be "0%" |
| All tutorials | Various | Bogaudio ADSR A/D/S/R display formats unverified — fix after Phase 1 |

## Constraints

- **Source only:** Every param spec in `modules.md` must cite its `configParam()` source. No assumptions, no docs.
- **No CLAUDE.md edits:** Port name conventions and module label formats already there — don't duplicate.
- **Chronoblob2:** "observed UI" mark required on every param entry. Not treated as source-verified.
- **Audit all pages:** Reference pages (vco.md etc.) get same rigour as step-by-step tutorials.
