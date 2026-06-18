# MIDI to CV

MIDI to CV modules convert incoming MIDI messages — note on/off, pitch, velocity, modulation wheel, aftertouch, and other controllers — into control voltages that modular modules understand. This is the bridge between a MIDI keyboard, DAW, or controller and your VCV Rack patch. Without a MIDI-CV converter, the patch operates in isolation from external MIDI instruments.

## MIDI to CV (VCV Core)

The MIDI to CV module is included with VCV Rack Free as a core module (not part of any plugin — it appears under the VCV menu in the module browser). It accepts MIDI input from any device connected to your computer and outputs pitch CV, gate, velocity, aftertouch, and modulation wheel as separate signals.

| Output | Type | Description |
|--------|------|-------------|
| V/OCT | CV | Pitch — 1V per octave, C4 = 0V |
| GATE | Gate | High when a key is held down |
| VEL | CV | Note velocity (0–10V) |
| AFT | CV | Aftertouch pressure |
| PW | CV | Pitch bend wheel |
| MW | CV | Modulation wheel (CC1) |
| RETRIG | Trigger | Fires on each new note even during legato |

| Parameter | Description |
|-----------|-------------|
| MIDI device | Select which MIDI input device to use |
| Channel | MIDI channel (1–16 or All) |
| POLY | Switch to polyphonic mode (outputs polyphonic cables) |

**Patching tips:** For basic monophonic use: patch V/OCT to your VCO's V/OCT input and GATE to your ADSR's GATE input. This gives you keyboard-playable pitch and note on/off. Patch VEL to your VCA's CV input through an attenuverter for velocity-sensitive dynamics. Patch MW to VCF FREQ CV for modulation wheel filter control. For polyphonic patches, switch to POLY mode and use the [Split](mult-splitter.md) module to distribute polyphonic cables to individual voice chains.

## MIDI-CC (VCV Core)

A companion module to MIDI-CV that converts MIDI Control Change messages (knobs, faders, buttons on controllers) to CV outputs. You can assign up to 16 CC numbers, each appearing as an output jack outputting 0–10V.

| Parameter | Description |
|-----------|-------------|
| CC number | MIDI CC to monitor (0–127) |
| Output | 0–10V proportional to CC value |

**Patching tips:** Assign your controller's filter knob to CC74 (standard) and map it to MIDI-CC output 1. Patch that output to VCF FREQ CV for hands-on filter control from hardware. Use multiple MIDI-CC channels for a live performance setup with tactile hardware control.

### VCV Gate (VCV Core)

Converts MIDI notes to gate outputs — each note produces its own gate when that specific note is played. Useful for triggering drum voices from a MIDI keyboard where each key corresponds to a specific drum hit.

### Bogaudio MIDI-CV (Bogaudio)

Bogaudio provides their own MIDI-CV with additional output options and a different interface layout. The functionality overlaps with VCV Core's MIDI-CV — choose based on your preference for the module layout.

### Impromptu MIDI mapper (Impromptu)

Impromptu's plugin includes MIDI utilities for mapping external controller parameters to patch parameters with scaling and offset. More flexible than MIDI-CC for complex controller setups.

## Where to go next

- [VCO](vco.md) — pitch CV from MIDI-CV goes here
- [Envelopes](envelope.md) — gate from MIDI-CV triggers envelopes
- [Mult & Splitter](mult-splitter.md) — Split polyphonic MIDI-CV output into voices
- [Sequencers](sequencer.md) — alternative to MIDI for pitch input
- [Audio Output](audio-output.md) — setting up audio alongside MIDI

---
*Version: 2026-06-17.*
