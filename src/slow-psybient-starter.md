# Slow Psybient — Starter Patch

This page walks you through the downloadable Fundamental-only starter patch, explains the signal flow, and shows how to extend it into the full psybient setup described in the [Slow Psybient](slow-psybient.md) tutorial.

## Download the patch

**[slow-psybient-starter.vcv](slow-psybient-starter.vcv)**

Save the file and open it in VCV Rack via **File → Open**. You need the Fundamental plugin installed — it ships with VCV Rack by default.

---

## What is in the patch

Nine modules, all from Fundamental:

| Module | Role |
|--------|------|
| VCO (×2) | Dual drone oscillators, tuned to G2 and detuned by 12 cents |
| Noise | Pink noise for texture layer |
| LFO | Slow 8-second filter sweep |
| VCMixer | Blends the two oscillators and noise |
| VCF | Lowpass ladder filter with LFO modulation |
| VCA | Signal level, permanently open for a continuous drone |
| Delay | Dub echo at dotted-eighth time (≈ 506 ms at 89 BPM) |
| AudioInterface2 | Stereo output to your audio device |

---

## Signal flow

```
VCO 1 (G2)  ─┐
VCO 2 (G2+12¢)─┤ VCMixer → VCF → VCA → Delay → AudioInterface2
Noise (Pink) ─┘

LFO (8s) ──────→ VCF freq CV
```

The two VCOs produce a slow-beating drone — the 12-cent offset creates a gentle chorus-like shimmer. Pink noise mixed at 25 % adds breathiness. The LFO sweeps the filter cutoff over eight seconds, giving the pad its characteristic slow, evolving texture. The VCA is wide open; the drone sustains continuously. Delay feeds back at 55 % with a slightly dark tone for the dub echo tail.

---

## First steps after loading

1. **Set your audio device.** Right-click AudioInterface2 and choose your output device. The patch is silent until a device is selected.
2. **Listen.** You should hear a low G drone with a slowly moving filter.
3. **Adjust the VCF knobs** to taste — cutoff at around 9 o'clock, resonance at around 10 o'clock is a good starting point.
4. **Nudge the Delay feedback** up if you want longer echoes, down for a subtler tail.

---

## Extending to the full patch

The starter covers the drone layer. The full [Slow Psybient](slow-psybient.md) patch adds:

### Add reverb

Install the **Valley** plugin for the **Plateau** reverb. Connect VCA output to Plateau input, and Plateau output to Delay input (or to a second mixer channel). Set decay long (0.9 +) and size large.

### Add a bass line

Add a second VCO (or any Fundamental VCO) tuned 1–2 octaves below, driven by a sequencer. A Fundamental **SEQ-3** works for a simple repeating bass pattern. Add an **ADSR** with a short attack and medium decay to shape the bass notes.

### Add a clock and gate

Install **Impromptu Modular** for the **Clocked** master clock. Connect Clocked's clock output to ADSR gates and any other trigger destinations. At 89 BPM, Clocked sets the tempo master for the whole patch.

### Add modulation depth control

Add a Fundamental **VCA** as an attenuverter for the LFO → VCF path. This lets you dial in exactly how much filter movement you want. Put it between the LFO output and the VCF FREQ CV input; map its level to a MIDI CC for live control.

### Add pattern switching

Four instances of **Impromptu PhraseSeq16** (one per voice layer) handle pattern storage and bar-locked switching. See the [Maschine MK2 Live Control](maschine-mapping.md) guide for how to wire pad hits to pattern changes.

---

## Module connection reference

For wiring the modules listed above, the connections are:

| From | Output | To | Input |
|------|--------|-----|-------|
| VCO 1 | SAW | VCMixer | CH 1 |
| VCO 2 | SAW | VCMixer | CH 2 |
| Noise | PINK | VCMixer | CH 3 |
| LFO | SIN | VCF | FREQ CV |
| VCMixer | MIX | VCF | IN |
| VCF | LPF | VCA | IN 1 |
| VCA | OUT 1 | Delay | IN |
| Delay | MIX | AudioInterface2 | L |
| Delay | MIX | AudioInterface2 | R |

---

## Maschine MK2 mapping

Once you have the full patch running, the [Maschine MK2 Live Control](maschine-mapping.md) guide maps:

- 4 × 4 pads → pattern selection per voice, quantized to bar end
- 8 encoders × 2 pages → filter, LFO, reverb, delay, and tempo control

---

## Where to go next

- [Slow Psybient](slow-psybient.md) — full tutorial for the complete patch
- [Maschine MK2 Live Control](maschine-mapping.md) — MIDI mapping guide
- [LFO](lfo.md) — understanding slow modulation sources
- [Delay, Reverb & Chorus](delay-reverb-chorus.md) — FX parameters and alternatives

---

*Version: 2026-06-17.*
