---
name: maschine-mapping-design
description: Design spec for mapping Maschine MK2 to VCV Rack Slow Psybient patch — pads, encoders, pattern switching, NI Controller Editor setup
metadata:
  type: project
---

# Maschine MK2 → VCV Rack Mapping — Design Spec

*2026-06-17*

## Goal

Live performance control of the Slow Psybient VCV Rack patch using a Maschine MK2 as MIDI controller. Pattern switching quantized to bar-end, 3 encoder pages, color-coded pad rows per voice.

## MIDI setup

- Single MIDI channel: **Ch 1** for all pads and encoders
- VCV Rack receives via MIDI-MAP + MIDI-GATE modules

## Pad layout (16 pads, 4×4)

| Row | Pads | Notes | Color | Voice | Patterns |
|-----|------|-------|-------|-------|---------|
| 1 | 1–4 | 36–39 | Red | Drums | A B C D |
| 2 | 5–8 | 40–43 | Blue | Bass | A B C D |
| 3 | 9–12 | 44–47 | Green | Pads/Texture | A B C D |
| 4 | 13–16 | 48–51 | Yellow | Synth | A B C D |

Active pattern pad: full brightness. Inactive: ~20% same color.

## Pattern switching mechanism

- Pad hit → MIDI Note On → MIDI-GATE → PhraseSeq16 pattern select CV input
- Switch quantized to **end of current bar** via Impromptu Clocked
- 4× PhraseSeq16 (one per voice): Drums, Bass, Pads, Synth

## Encoder pages

### Page 1 — Sound / Modulation

| Encoder | CC | Target |
|---------|-----|--------|
| 1 | CC1 | Drone filter cutoff |
| 2 | CC2 | Drone filter resonance |
| 3 | CC3 | Drone LFO rate |
| 4 | CC4 | Drone LFO depth (to filter) |
| 5 | CC5 | Bass filter cutoff |
| 6 | CC6 | Bass envelope decay |
| 7 | CC7 | Synth/texture filter cutoff |
| 8 | CC8 | Master reverb send |

### Page 2 — FX / Timing

| Encoder | CC | Target |
|---------|-----|--------|
| 1 | CC9 | Reverb decay time |
| 2 | CC10 | Reverb pre-delay |
| 3 | CC11 | Delay time |
| 4 | CC12 | Delay feedback |
| 5 | CC13 | Delay mix/send |
| 6 | CC14 | Master LFO rate |
| 7 | CC15 | S&H trigger rate |
| 8 | CC16 | Master tempo |

### Page 3 — Mixer (separate Maschine preset)

Channel volumes — defined later.

## VCV Rack modules required

- **MIDI-GATE** (Fundamental) — converts pad notes to gates per voice row
- **MIDI-MAP** (VCV) — maps CC1–16 to patch parameters
- **4× Impromptu PhraseSeq16** — pattern storage and switching per voice
- **Impromptu Clocked** — master clock, provides bar-end sync for quantized switching

## NI Controller Editor setup

- Mode: MIDI
- Channel: 1 (global)
- Pads: Note mode, notes 36–51, velocity fixed or expressive
- Pad LED On Color: row color at full brightness
- Pad LED Off Color: same hue, ~20% brightness
- Encoders: CC mode, relative or absolute
- Page switch: direction buttons (Left/Right) cycle encoder pages
