# Maschine MK2 — Live Control Setup

This guide maps a Native Instruments Maschine MK2 to the Slow Psybient patch for live performance. You get pattern switching on the pads, sound and FX control on the encoders, and mixer control on a second encoder page — all on a single MIDI channel with no laptop keyboard required during performance.

## What you need

- Maschine MK2 with NI Controller Editor installed
- VCV Rack with the Slow Psybient patch loaded
- Impromptu Modular plugin (free) — for PhraseSeq16 and Clocked

---

## Step 1 — NI Controller Editor setup

Open Controller Editor and select your Maschine MK2.

### MIDI channel

Set the global MIDI channel to **1** for all pads and encoders. One channel keeps the VCV Rack setup simple.

### Pad configuration

The 16 pads are split into four rows of four. Each row controls one voice, sending MIDI notes that trigger pattern switches in VCV Rack.

| Row | Pads | MIDI Notes | Voice | LED Color |
|-----|------|-----------|-------|-----------|
| 1 (top) | 1–4 | 36, 37, 38, 39 | Drums | Red |
| 2 | 5–8 | 40, 41, 42, 43 | Bass | Blue |
| 3 | 9–12 | 44, 45, 46, 47 | Pads / Texture | Green |
| 4 (bottom) | 13–16 | 48, 49, 50, 51 | Synth | Yellow |

For each pad in Controller Editor:
1. Click the pad
2. Set **Type** to Note
3. Set **Note** to the value from the table above
4. Set **On Color** to the row color at full brightness
5. Set **Off Color** to the same hue at around 20% brightness — this makes inactive patterns visually distinct without going dark

Each group of four pads represents patterns A, B, C, D for that voice. Hitting a pad queues the corresponding pattern, which switches at the end of the current bar.

### Encoder pages

The 8 encoders work across two pages, switched with the Left/Right direction buttons on the Maschine.

**Page 1 — Sound & Modulation**

| Encoder | CC | Controls |
|---------|-----|---------|
| 1 | CC1 | Drone filter cutoff |
| 2 | CC2 | Drone filter resonance |
| 3 | CC3 | Drone LFO rate |
| 4 | CC4 | Drone LFO depth (to filter) |
| 5 | CC5 | Bass filter cutoff |
| 6 | CC6 | Bass envelope decay |
| 7 | CC7 | Synth / texture filter cutoff |
| 8 | CC8 | Master reverb send |

**Page 2 — FX & Timing**

| Encoder | CC | Controls |
|---------|-----|---------|
| 1 | CC9 | Reverb decay time |
| 2 | CC10 | Reverb pre-delay |
| 3 | CC11 | Delay time |
| 4 | CC12 | Delay feedback |
| 5 | CC13 | Delay mix / send |
| 6 | CC14 | Master LFO rate |
| 7 | CC15 | S&H trigger rate |
| 8 | CC16 | Master tempo |

For each encoder, set **Type** to CC and assign the CC number from the table. Use **relative** mode if your encoders jump, **absolute** if they feel smooth.

Save the preset in Controller Editor before moving to VCV Rack.

---

## Step 2 — VCV Rack MIDI modules

Add these modules to your patch:

**MIDI to Gate** (VCV Free) — converts the pad note-ons into gate signals, one gate output per note. Use four instances, one per voice row, or one instance and route outputs by note number.

**MIDI-MAP** (VCV) — right-click any parameter in your patch, select "Map to MIDI CC", then move the corresponding encoder. Repeat for all 16 CCs across both encoder pages. MIDI-MAP can handle all 16 in two stacked modules (8 slots each).

---

## Step 3 — Pattern switching with PhraseSeq16

Add four instances of **Impromptu PhraseSeq16** — one for each voice (Drums, Bass, Pads, Synth).

Each PhraseSeq16 stores up to 16 patterns. You'll use patterns 1–4 (corresponding to pads A–D per row).

**Wiring per sequencer:**

1. Connect **Impromptu Clocked** master clock output → PhraseSeq16 clock input
2. Connect Clocked's **bar output** (or end-of-phrase trigger) → PhraseSeq16 reset/phrase-advance input — this is what makes switching wait for the bar end
3. Connect the MIDI to Gate output for that voice's pads → PhraseSeq16 phrase select CV input

When you hit pad 1 in the drums row, the gate fires, PhraseSeq16 queues pattern 1, and at the next bar boundary it switches cleanly.

**Programming patterns:** Click into each PhraseSeq16, select a pattern slot (1–4), and program the steps. The drums sequencer drives your kick/snare/hat trigger signals; the bass sequencer drives the bass VCO pitch and gate.

---

## Step 4 — MIDI-MAP routing

Right-click each target parameter and map it:

- Drone VCF cutoff knob → CC1
- Drone VCF resonance → CC2
- Drone LFO rate → CC3
- Drone LFO attenuverter (depth) → CC4
- Bass VCF cutoff → CC5
- Bass ADSR decay → CC6
- Synth/texture VCF cutoff → CC7
- Reverb send mixer level → CC8
- Plateau decay → CC9
- Plateau pre-delay → CC10
- Chronoblob delay time → CC11
- Chronoblob feedback → CC12
- Chronoblob mix → CC13
- Slow modulation LFO rate → CC14
- S&H trigger clock rate → CC15
- Clocked BPM → CC16

Move each encoder after mapping to confirm it moves the right parameter.

---

## Performing live

**Before the set:** load the patch, confirm MIDI is flowing (wiggle an encoder, watch the mapped parameter move), run through each pad row to confirm pattern switching works.

**During the set:**
- Use pad rows to build and break down the arrangement — start with just drums + bass, bring in pads and synth as the track evolves
- Page 1 encoders for tonal shaping — filter and LFO are the most expressive
- Page 2 encoders for space — reverb and delay feedback define the psychedelic character
- Encoder 16 (tempo) lets you nudge BPM if needed, but keep changes small at 89 BPM

**Pattern switching feel:** after hitting a pad, the switch happens at the bar end — at 89 BPM that's about 2.7 seconds. Hit the pad slightly early if you want the change to land on a specific moment.

---

## Where to go next

- [Slow Psybient](slow-psybient.md) — the full patch this mapping is built for
- [LFO](lfo.md) — understanding the modulation sources you're controlling
- [Delay, Reverb & Chorus](delay-reverb-chorus.md) — the FX parameters on encoder page 2
- [Sequencers](sequencer.md) — deeper look at PhraseSeq16 and pattern-based sequencing

---

*Version: 2026-06-17.*
