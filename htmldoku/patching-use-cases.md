# Patching Use Cases

Each section below is a recipe for a common patching goal. They build on the foundation from [Your First Patch](first-patch.md) and [How a Patch Works](how-a-patch-works.md). Modules referenced are all from VCV Free or Befaco unless noted otherwise.

---

## 1 — Bassline with a sequencer

**Goal:** A repeating melodic pattern that plays without holding keys.

Add **SEQ 3** (from VCV Free). Set its Tempo knob to your preferred BPM. Set the Steps knob to 8. On the three rows of CV knobs (CV 1, CV 2, CV 3), use CV 1 to program a pitch sequence: each knob sets the pitch CV for that step in volts (0 V = C4, 1 V = C5, etc.).

Connect SEQ 3's **CV 1** output to the VCO's **PITCH** input (replacing any MIDI-CV connection for the pitch). Connect SEQ 3's **Trigger** output to the ADSR's **Gate** input. The sequencer now drives both pitch and envelope.

For a two-bar pattern, use two SEQ 3 modules chained together: connect the first sequencer's **EOC** (end of cycle) output to the second's **Clock** input, and the second back to the first, or simply program the full sequence across one module at 16 steps.

Set the VCF cutoff low and crank the resonance to taste for an acid bass sound. Modulate the filter cutoff with a slowly rising LFO for sweep.

---

## 2 — Percussion hit

**Goal:** A short, punchy percussive sound without a melodic pitch.

Add a **Noise** module (VCV Free). Noise has no inputs — it simply outputs several flavors of noise (white, pink, red, etc.). Connect the **White** output to a VCA's **CH** input.

Add a short ADSR: set Attack nearly to zero, Decay to a short value (around 9 o'clock), Sustain to zero, Release to zero. Connect a **Pulses** module (VCV Free) or a clock to the ADSR's **Gate** input to trigger it rhythmically. Connect ADSR's output to the VCA's CV.

For a kick-drum character, use a VCO set to a very low frequency (−2 to −3 on the Freq knob) instead of noise, and add a fast pitch envelope: a second short ADSR connected to the VCO's FM input with a very fast attack and decay, so the pitch drops sharply after the hit.

---

## 3 — Effects send and return

**Goal:** Apply reverb or delay to part of your signal while keeping a dry signal.

Add a **Mix** module (VCV Free, 6-channel mixer). Connect your VCA's output to channel 1 of the Mix module. Set channel 1's level to taste.

Add a **Delay** module. Connect the Mix's **Mix** output to the Delay's **Audio** input. Connect the Delay's **Wet** output to channel 2 of the Mix module. Now the delay receives the full mix, but you're blending the wet signal back in via channel 2's level knob. Keep channel 2's level low for a subtle effect.

The same approach works for reverb plugins: send your source to the effect, and return the wet output to a separate mixer channel. This avoids the effect "doubling" your signal's dry component.

---

## 4 — Drone and texture

**Goal:** A sustained, evolving ambient texture without rhythmic articulation.

Use two or three VCOs detuned slightly from each other. Set one to 0 V (center) on its Frequency knob. Set another to +2 cents (a very slight detune using the Fine knob, if present, or a slight nudge on Freq). Set a third an octave higher. Connect all three to a Mix module.

Patch an LFO at a very slow rate (0.1 Hz or slower) to the VCF's Freq CV input with a moderate attenuverter setting. The filter cutoff will drift slowly, creating movement without a fixed rhythm.

Patch a second LFO at a different rate to the Mix module's level for one of the VCOs, so it fades in and out. With two LFOs at prime ratios (e.g., 0.07 Hz and 0.11 Hz), the texture never exactly repeats.

Skip the ADSR — just keep the VCA fully open (CV input unpatched, Level knob up). Let the LFOs create all the movement.

---

## 5 — Generative random patch

**Goal:** A patch that generates evolving, semi-random melodies or textures on its own.

Add a **SEQ 3** module. Use its **Clock** output to drive its own timing. Add a **Random** module (VCV Free). Connect Random's **Stepped** output to the VCO's PITCH input. The Stepped output holds a new random voltage each time a trigger fires. Connect SEQ 3's Trigger output to Random's **Trig** input so the Random module updates on each sequencer step.

Add a **Quantizer** (VCV Free) between Random and the VCO: Random → Quantizer In → VCO Pitch. The quantizer snaps random voltages to a musical scale. Right-click the Quantizer to choose a scale. Now your random pitches are always in key.

For rhythmic variation, add a **Logic** module and combine two different clock divisions using an AND or OR gate to create irregular triggers instead of a simple steady beat.

---

## Where to go next

- [FAQ](faq.md) — common problems with effects, sequencers, and clocking
- [How a Patch Works](how-a-patch-works.md) — signal chain fundamentals
- [Fundamental Modules](fundamental-modules.md) — full reference for all modules used here
- [Befaco Modules](befaco-modules.md) — more complex sources and processors

---

*Version: 2026-06-17.*
