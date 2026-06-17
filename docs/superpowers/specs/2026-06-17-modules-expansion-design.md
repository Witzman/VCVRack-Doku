---
name: modules-expansion-design
description: Design spec for VCVRack-Doku expansion — category-based module pages, tutorials, sidebar restructure
metadata:
  type: project
---

# Modules Expansion — Design Spec

*2026-06-17*

## Goal

Expand the patcher's handbook from a Fundamental/Befaco reference to a full free-module knowledge base. Primary use: AI-assisted patching conversations ("what should I use for X").

## Scope

Free modules only — Fundamental (bundled), Befaco (free plugin), free third-party from VCV Library. No disclaimers on training-knowledge modules — discovery-focused, not spec-accurate.

## Pages — delete

- `fundamental-modules.md` — replaced by category pages
- `befaco-modules.md` — replaced by category pages

## Pages — new category pages (19 total, fresh content)

Mixed depth: top 2-3 modules per category get full treatment (params, inputs, patching tips). Others get brief entries (name, one-liner, plugin). No length cap.

| Section | File | Slug |
|---------|------|------|
| Sound Generation | `vco.md` | vco |
| Sound Generation | `noise.md` | noise |
| Sound Generation | `wavetable.md` | wavetable |
| Sound Shaping | `vcf.md` | vcf |
| Sound Shaping | `vca.md` | vca |
| Sound Shaping | `waveshaper-distortion.md` | waveshaper-distortion |
| Sound Shaping | `delay-reverb-chorus.md` | delay-reverb-chorus |
| Modulation / Control | `envelope.md` | envelope |
| Modulation / Control | `lfo.md` | lfo |
| Modulation / Control | `sequencer.md` | sequencer |
| Modulation / Control | `sample-hold.md` | sample-hold |
| Utilities | `mixer.md` | mixer |
| Utilities | `attenuverter.md` | attenuverter |
| Utilities | `mult-splitter.md` | mult-splitter |
| Utilities | `quantizer.md` | quantizer |
| Utilities | `clock.md` | clock |
| Utilities | `logic.md` | logic |
| MIDI / I/O | `midi-cv.md` | midi-cv |
| MIDI / I/O | `audio-output.md` | audio-output |

## Pages — new tutorials

- `intermediate-patch.md` — intermediate tutorial using free third-party modules
- `slow-psybient.md` — hands-on Slow Psybient tutorial (Younger Brother / Shpongle style, 89 BPM, G minor, psychedelic dub atmosphere). Teaches: drone pad, sparse bass, psy fragments, half-time drums, slow modulation, large reverb/delay. Focus: build → hear → tweak. Not exact reconstruction.

## Pages — update

- `patching-use-cases.md` — add recipes using free third-party modules
- `glossary.md` — expand with third-party plugin terms (Bogaudio, Surge XT, Count Modula, Plateau, etc.)

## Sidebar restructure

```
Common         (existing 7 pages minus fundamental/befaco)
Tutorials
  · Your First Patch
  · Intermediate Patch
  · Slow Psybient
Modules
  Sound Generation
    · VCO
    · Noise
    · Wavetable
  Sound Shaping
    · VCF
    · VCA
    · Waveshaper & Distortion
    · Delay, Reverb & Chorus
  Modulation / Control
    · Envelopes
    · LFO
    · Sequencers
    · Sample & Hold
  Utilities
    · Mixer
    · Attenuverter
    · Mult & Splitter
    · Quantizer
    · Clock
    · Logic
  MIDI / I/O
    · MIDI to CV
    · Audio Output
```

CSS-only grouping — no JS. `build_sidebar()` needs to handle 3-level structure (section → subcategory → pages).

## generate.py changes

SIDEBAR structure extended to support nested subcategories:
```python
("Modules", {
    "Sound Generation": [...],
    "Sound Shaping": [...],
    ...
})
```

`build_sidebar()` detects dict vs list for second element and renders subcategory headers at smaller font/indent.

Add CSS for `.sub-section-title` — smaller than `.section-title`, indented.
