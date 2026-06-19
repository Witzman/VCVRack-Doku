# Tutorial Rewrite — Port Names, Manufacturer Labels, Mermaid Diagrams

**Date:** 2026-06-19  
**Scope:** `src/first-patch.md`, `src/intermediate-patch.md`, `src/slow-psybient.md`

---

## Goal

Rewrite all three tutorial files so that:
1. Every port name matches the actual label shown in VCV Rack (tooltip from `configInput`/`configOutput`)
2. Module manufacturer references use the brand name "VCV" (not "VCV Free")
3. Each tutorial has a full-patch overview Mermaid diagram plus inline cumulative diagrams per wiring step

---

## Port Name Corrections

Verified from `Fundamental/src/` local source.

### first-patch.md

Tutorial uses **VCA-1** (slug `VCA-1`, name "VCA") — single-channel variant. Ports: `IN_INPUT ("Channel")`, `CV_INPUT ("CV")`, `OUT_OUTPUT ("Channel")`.

| Current (wrong) | Correct | Source |
|---|---|---|
| "ADSR EG" | "ADSR" | `createModel<ADSR, ADSRWidget>("ADSR")` |
| VCA "CH" input | "Channel" | `IN_INPUT` → `configInput(IN_INPUT, "Channel")` in `VCA-1.cpp` |
| VCA "CV" input | already correct ("CV") | `CV_INPUT` → `configInput(CV_INPUT, "CV")` in `VCA-1.cpp` |
| VCA "CH" output | "Channel" | `OUT_OUTPUT` → `configOutput(OUT_OUTPUT, "Channel")` in `VCA-1.cpp` |

Other ports in this file (VCO PITCH/SAW, ADSR Gate/Envelope, VCF IN/LPF/Freq) are correct or close enough.

### intermediate-patch.md

| Current (wrong) | Correct | Source |
|---|---|---|
| SEQ3 "CLK input" | "Clock" | `CLOCK_INPUT` → `configInput(CLOCK_INPUT, "Clock")` |
| SEQ3 "ROW1 output" | "CV 1" | `CV_OUTPUTS+0` → `configOutput(CV_OUTPUTS+j, "CV %d")` |
| SEQ3 "GATE output" | "Trigger" | `TRIG_OUTPUT` → `configOutput(TRIG_OUTPUT, "Trigger")` |
| 8vert "channel" | "Row N" | `IN_INPUTS+i` → `configInput(IN_INPUTS+i, "Row %d")` |
| 3rd-party (Bogaudio, Impromptu) | Verify via web lookup before editing | GitHub repos |

### slow-psybient.md

| To verify | Action |
|---|---|
| Bogaudio VCO, ADSR, LFO, S&H ports | Web lookup from Bogaudio GitHub |
| Impromptu Clocked ports | Web lookup from Impromptu Modular GitHub |
| Valley Plateau ports | Web lookup from Valley GitHub |
| Alright Devices Chronoblob2 ports | Web lookup from Alright Devices GitHub |

---

## Manufacturer Naming Convention

Use `(VCV)` — the brand field in `plugin.json` — not `(VCV Free)` (the plugin package name).  
Format: **ModuleName (Brand)**, e.g. "VCO (VCV)", "ADSR (VCV)", "SEQ3 (VCV)".

Third-party modules: "Clocked (Impromptu)", "Plateau (Valley)", etc. — confirm brand names during web lookup.

---

## Mermaid Diagram Structure

### Overview diagram

- Placed after the "What you'll build" section, before Step 1
- Type: `flowchart LR`
- Nodes: each module as `ID["ModuleName\n(Brand)"]`
- Edges: labeled with the exact port name the cable leaves/enters, e.g. `-->|"Sawtooth"|`
- Shows final complete patch including all steps (including optional filter modulation)

### Inline step diagrams

- Appear at the end of each step that adds at least one new cable
- Cumulative: show all modules and connections made so far (not just the new one)
- Same `flowchart LR` format as overview
- Steps with no new wiring (plugin install, save, set knobs only) get no diagram

### Steps that get inline diagrams

**first-patch.md:** Steps 4, 5, 6, 7, 8  
**intermediate-patch.md:** Steps 2, 3, 4, 5, 6, 7  
**slow-psybient.md:** Each "Build it" numbered block that adds connections

---

## Execution Order

1. **`first-patch.md`** — no web lookup needed; fix + diagram immediately
2. **`intermediate-patch.md`** — web lookup Bogaudio + Impromptu ports first, then fix + diagram
3. **`slow-psybient.md`** — web lookup Valley + Alright Devices (Bogaudio + Impromptu already known), then fix + diagram

---

## Out of Scope

- No changes to `docs/` HTML (generator rebuilds from `src/`)
- No other `src/` files touched
- No changes to knob names, parameter ranges, or tutorial narrative/structure
- No changes to `slow-psybient-starter.md` (no wiring instructions)
