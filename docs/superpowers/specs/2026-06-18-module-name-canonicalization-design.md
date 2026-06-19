# Module Name Canonicalization

**Date:** 2026-06-18  
**Scope:** All `VCVRack-Doku/src/*.md` files (31 files)

## Problem

Module names in docs don't match what users see in the VCV Rack module browser:
- Plugin shipped with Rack is called **VCV Free** in the browser, but docs say "Fundamental"
- Several module display names are wrong (slug used instead of name, or old Rack v1 names)
- Core modules inconsistently labeled

## Correction Map

| Current in docs | Correct |
|---|---|
| `Fundamental VCO-1` / `Fundamental VCO` | `VCV Free VCO` |
| `Fundamental VCF` | `VCV Free VCF` |
| `Fundamental VCA` | `VCV Free VCA` |
| `Fundamental VCA-2` | `VCV Free VCA-2` |
| `Fundamental ADSR EG` / `Fundamental ADSR` | `VCV Free ADSR EG` |
| `Fundamental LFO` | `VCV Free LFO` |
| `Fundamental SEQ-3` / bare `SEQ-3` | `VCV Free SEQ 3` |
| `Fundamental 8vert` / bare `8vert` in Fundamental context | `VCV Free 8vert` |
| `Fundamental Mixer` | `VCV Free Mix` |
| `Fundamental Noise` | `VCV Free Noise` |
| `Fundamental Quantizer` | `VCV Free Quantizer` |
| `Fundamental WTVCO` | `VCV Free Wavetable VCO` |
| `VCMixer` (slug used as name) | `VCV Free VCA Mix` |
| `AUDIO-8` / `Audio 8 (from Core)` | `VCV Core Audio 8` |
| `MIDI-CV` / `MIDI to CV (Core)` | `VCV Core MIDI to CV` |
| `AudioInterface2` | `VCV Core Audio 2` |
| bare unqualified `VCO` where Bogaudio VCO also present | `VCV Free VCO` |

## VCA Disambiguation Rule

Two Fundamental VCA modules exist:
- Slug `VCA-1`, display name **VCA** — single channel, the simpler one
- Slug `VCA`, display name **VCA-2** — dual/stereo

All bare "VCA" or "Fundamental VCA" references = VCA-1 → `VCV Free VCA`.  
Any "VCA-2" reference → `VCV Free VCA-2`.

## What Is Not Changed

- Bogaudio module names (already correct)
- Impromptu, Valley, Alright Devices module names
- Knob/port label names in instructions (FREQ, RES, SAW, etc.)
- Code blocks, CLAUDE.md, generator files
- Module reference pages' parameter tables (separate pass if needed)

## Approach

File-by-file manual edit. Per file:
1. Grep for: `Fundamental`, `VCO-1`, `SEQ-3`, `VCMixer`, `MIDI-CV`, `AUDIO-8`, `AudioInterface2`, `(from Core)`
2. Fix each occurrence in full prose context
3. Verify no Bogaudio/Impromptu names accidentally altered

## Source of Truth

Library manifests at `rack/library/manifests/`:
- `Fundamental.json` — plugin name "VCV Free", slug "Fundamental"
- `Core.json` — plugin name "VCV Core", slug "Core"
- `Bogaudio.json` — plugin name "Bogaudio"
