# Slow Psybient — Starter Patch

This page walks you through building the patch manually from scratch, offers a downloadable .vcv file if you prefer to skip the build, explains the signal flow, and shows how to extend it into the full psybient setup described in the [Slow Psybient](slow-psybient.md) tutorial.

---

## Build it manually

All modules are from **VCV Free**, which ships with VCV Rack by default. No extra plugins needed.

### Step 1 — Add modules

Open VCV Rack with a blank patch. Double-click an empty rack area to open the module browser. Add these modules in order from left to right — placing them left to right in two rows makes the cabling cleaner:

**Top row**

1. **VCO** — first drone oscillator
2. **VCO** — second drone oscillator (detuned)
3. **Noise** — texture layer
4. **LFO** — slow filter sweep

**Bottom row**

5. **VCA Mix** — blends the three sources
6. **VCF** — lowpass filter
7. **VCA** — amplitude, always open
8. **Delay** — dub echo
9. **Audio 2** (VCV Core) — stereo output to your soundcard

### Step 2 — Set the parameters

**VCO 1** (drone root):
- **FREQ** knob: turn fully counterclockwise, then nudge up to about 7 o'clock. This puts it at G2 (roughly −17 semitones from the centre C4 default). The exact position is not critical — you can tune by ear.
- Leave all other knobs at centre.

**VCO 2** (detuned voice):
- **FREQ** knob: same position as VCO 1, then turn it a tiny fraction higher — the goal is about 12 cents of detune, which is just a hair of movement. The beating between the two oscillators should pulse slowly (about once every 3–4 seconds at this detuning).

**Noise**: no knobs to set.

**LFO**:
- **FREQ** knob: turn to roughly 8 o'clock (well left of centre). This gives an 8-second sweep period. If you move it further left, the sweep slows down; further right, it speeds up.

**VCA Mix**:
- CH 1 and CH 2 level knobs: full up (5 o'clock).
- CH 3 level knob (Noise channel): turn down to about 7–8 o'clock — about 25 % level. The noise should be felt more than heard.
- MIX knob: full up.

**VCF**:
- **FREQ** (cutoff) knob: just below centre — around 10 o'clock. This gives a warm, filtered tone.
- **RES** knob: slightly past the minimum — about 8 o'clock. A touch of resonance adds character without getting sharp.
- **FREQ CV** attenuverter (small knob near FREQ CV input): turn to about 9–10 o'clock — this controls how much the LFO moves the cutoff. Start conservative; you can increase it once the patch is running.

**VCA**:
- **LEVEL 1** knob: full up. The drone sustains continuously with no envelope.

**Delay**:
- **TIME** knob: just above centre — about 1 o'clock. At 89 BPM this lands near a dotted eighth note (≈ 506 ms).
- **FEEDBACK** knob: just above centre — around 2 o'clock (55 %). Higher gives more repeats; lower is subtler.
- **TONE** knob: slightly left of centre — about 11 o'clock. Darkens the delay repeats.
- **MIX** knob: about 10 o'clock (35 % wet). The dry signal should dominate; the delay is a tail.

**Audio 2**: no knobs to set here — just right-click it later to select your audio device.

### Step 3 — Connect the cables

Drag from output port to input port. The outputs are on the right side of each module (or bottom), inputs on the left (or top).

| From module | Output port | To module | Input port |
|-------------|-------------|-----------|------------|
| VCO 1 | **SAW** | VCA Mix | **CH 1** |
| VCO 2 | **SAW** | VCA Mix | **CH 2** |
| Noise | **PINK** | VCA Mix | **CH 3** |
| LFO | **SIN** | VCF | **FREQ CV** |
| VCA Mix | **MIX** | VCF | **IN** |
| VCF | **LPF** | VCA | **IN 1** |
| VCA | **OUT 1** | Delay | **IN** |
| Delay | **MIX** | Audio 2 | **L** |
| Delay | **MIX** | Audio 2 | **R** |

For the last two cables: you can stack two cables on the same Delay MIX output by holding the existing cable's output port and dragging a second cable from it, or by clicking the output and pulling again — VCV Rack allows multiple cables from one output.

### Step 4 — Set your audio device

Right-click **Audio 2** and choose your output device from the list. You should now hear a low, slowly sweeping drone.

---

## Download the patch

**[slow-psybient-starter.vcv](slow-psybient-starter.vcv)**

Save the file and open it in VCV Rack via **File → Open**. You need the VCV Free plugin installed — it ships with VCV Rack by default.

---

## What is in the patch

Nine modules, all from VCV Free:

| Module | Role |
|--------|------|
| VCO (×2) | Dual drone oscillators, tuned to G2 and detuned by 12 cents |
| Noise | Pink noise for texture layer |
| LFO | Slow 8-second filter sweep |
| VCA Mix | Blends the two oscillators and noise |
| VCF | Lowpass ladder filter with LFO modulation |
| VCA | Signal level, permanently open for a continuous drone |
| Delay | Dub echo at dotted-eighth time (≈ 506 ms at 89 BPM) |
| Audio 2 | Stereo output to your audio device |

---

## Signal flow

```
VCO 1 (G2)  ─┐
VCO 2 (G2+12¢)─┤ VCA Mix → VCF → VCA → Delay → Audio 2
Noise (Pink) ─┘

LFO (8s) ──────→ VCF freq CV
```

The two VCOs produce a slow-beating drone — the 12-cent offset creates a gentle chorus-like shimmer. Pink noise mixed at 25 % adds breathiness. The LFO sweeps the filter cutoff over eight seconds, giving the pad its characteristic slow, evolving texture. The VCA is wide open; the drone sustains continuously. Delay feeds back at 55 % with a slightly dark tone for the dub echo tail.

---

## First steps after loading

1. **Set your audio device.** Right-click Audio 2 and choose your output device. The patch is silent until a device is selected.
2. **Listen.** You should hear a low G drone with a slowly moving filter.
3. **Adjust the VCF knobs** to taste — cutoff at around 9 o'clock, resonance at around 10 o'clock is a good starting point.
4. **Nudge the Delay feedback** up if you want longer echoes, down for a subtler tail.

---

## Extending to the full patch

The starter covers the drone layer. The full [Slow Psybient](slow-psybient.md) patch adds:

### Add reverb

Install the **Valley** plugin for the **Plateau** reverb. Connect VCA output to Plateau input, and Plateau output to Delay input (or to a second mixer channel). Set decay long (0.9 +) and size large.

### Add a bass line

Add a second VCO (or any VCV Free VCO) tuned 1–2 octaves below, driven by a sequencer. A VCV Free **SEQ 3** works for a simple repeating bass pattern. Add an **ADSR** with a short attack and medium decay to shape the bass notes.

### Add a clock and gate

Install **Impromptu Modular** for the **Clocked** master clock. Connect Clocked's clock output to ADSR gates and any other trigger destinations. At 89 BPM, Clocked sets the tempo master for the whole patch.

### Add modulation depth control

Add a VCV Free **VCA** as an attenuverter for the LFO → VCF path. This lets you dial in exactly how much filter movement you want. Put it between the LFO output and the VCF FREQ CV input; map its level to a MIDI CC for live control.

### Add pattern switching

Four instances of **Impromptu PhraseSeq16** (one per voice layer) handle pattern storage and bar-locked switching. See the [Maschine MK2 Live Control](maschine-mapping.md) guide for how to wire pad hits to pattern changes.

---

## Module connection reference

For wiring the modules listed above, the connections are:

| From | Output | To | Input |
|------|--------|-----|-------|
| VCO 1 | SAW | VCA Mix | CH 1 |
| VCO 2 | SAW | VCA Mix | CH 2 |
| Noise | PINK | VCA Mix | CH 3 |
| LFO | SIN | VCF | FREQ CV |
| VCA Mix | MIX | VCF | IN |
| VCF | LPF | VCA | IN 1 |
| VCA | OUT 1 | Delay | IN |
| Delay | MIX | Audio 2 | L |
| Delay | MIX | Audio 2 | R |

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
