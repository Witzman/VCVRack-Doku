# Patching Use Cases

Each section below is a recipe for a common patching goal. They build on the foundation from [Your First Patch](first-patch.md) and [How a Patch Works](how-a-patch-works.md). Modules referenced are all from VCV Free or Befaco unless noted otherwise.

---

## 1 — Bassline with a sequencer

**Goal:** A repeating melodic pattern that plays without holding keys.

Add **SEQ 3** (from VCV Free). Set its Tempo knob to your preferred BPM. Set the Steps knob to 8. On the three rows of CV knobs (CV 1, CV 2, CV 3), use CV 1 to program a pitch sequence: each knob sets the pitch CV for that step in volts (0 V = C4, 1 V = C5, etc.).

Connect SEQ 3's **CV 1** output to the VCO's **PITCH** input (replacing any MIDI to CV connection for the pitch). Connect SEQ 3's **Trigger** output to the ADSR's **Gate** input. The sequencer now drives both pitch and envelope.

For a longer pattern, use two SEQ 3 modules and switch between them with a clock divider, or chain their Trigger/Clock outputs through a counter — a single SEQ 3 maxes out at 8 steps, so two are needed for anything longer.

Set the VCF cutoff low and crank the resonance to taste for an acid bass sound. Modulate the filter cutoff with a slowly rising LFO for sweep.

---

## 2 — Percussion hit

**Goal:** A short, punchy percussive sound without a melodic pitch.

Add a **VCV Free Noise** module. Noise has no inputs — it simply outputs several flavors of noise (white, pink, red, etc.). Connect the **White** output to a VCA's **CH** input.

Add a short ADSR: set Attack nearly to zero, Decay to a short value (around 9 o'clock), Sustain to zero, Release to zero. Connect a **Pulses** module (VCV Free) or a clock to the ADSR's **Gate** input to trigger it rhythmically. Connect ADSR's output to the VCA's CV.

For a kick-drum character, use a VCO set to a very low frequency (−2 to −3 on the Freq knob) instead of noise, and add a fast pitch envelope: a second short ADSR connected to the VCO's FM input with a very fast attack and decay, so the pitch drops sharply after the hit.

---

## 3 — Effects send and return

**Goal:** Apply reverb or delay to part of your signal while keeping a dry signal.

Add a **VCV Free Mix** module (6-channel mixer). Connect your VCA's output to channel 1 of the Mix module. Set channel 1's level to taste.

Add a **Delay** module. Connect the Mix's **Mix** output to the Delay's **Audio** input. Connect the Delay's **Wet** output to channel 2 of the Mix module. Now the delay receives the full mix, but you're blending the wet signal back in via channel 2's level knob. Keep channel 2's level low for a subtle effect.

The same approach works for reverb plugins: send your source to the effect, and return the wet output to a separate mixer channel. This avoids the effect "doubling" your signal's dry component.

---

## 4 — Drone and texture

**Goal:** A sustained, evolving ambient texture without rhythmic articulation.

Use two or three VCOs detuned slightly from each other. Set one to 0 V (center) on its Frequency knob. Set another a hair higher with a slight nudge on the Freq knob (the VCV VCO has no Fine knob). Set a third an octave higher. Connect all three to a VCV Free Mix module.

Patch an LFO at a very slow rate (0.1 Hz or slower) to the VCF's Freq CV input with a moderate attenuverter setting. The filter cutoff will drift slowly, creating movement without a fixed rhythm.

Patch a second LFO at a different rate to the Mix module's level for one of the VCOs, so it fades in and out. With two LFOs at prime ratios (e.g., 0.07 Hz and 0.11 Hz), the texture never exactly repeats.

Skip the ADSR — just keep the VCA fully open (CV input unpatched, Level knob up). Let the LFOs create all the movement.

---

## 5 — Generative random patch

**Goal:** A patch that generates evolving, semi-random melodies or textures on its own.

Add a **SEQ 3** module. Use its **Clock** output to drive its own timing. Add a **VCV Free Random** module. Connect Random's **Stepped** output to the VCO's PITCH input. The Stepped output holds a new random voltage each time a trigger fires. Connect SEQ 3's Trigger output to Random's **Trig** input so the Random module updates on each sequencer step.

Add a **VCV Free Quantizer** between Random and the VCO: Random → Quantizer In → VCO Pitch. The quantizer snaps random voltages to a musical scale. Select the scale by toggling notes on the Quantizer's note display (it has no scale presets). Now your random pitches are always in key.

For rhythmic variation, add a **Logic** module and combine two different clock divisions using an AND or OR gate to create irregular triggers instead of a simple steady beat.

---

---

## Recipe 6 — Generative Melody with Bogaudio S&H and Quantizer

**Goal:** A self-generating melodic line that stays in key and never exactly repeats.

Install **Bogaudio** if not already installed. Add **Bogaudio S&H**, **VCV Free Noise**, **VCV Free Quantizer**, **Impromptu Clocked**, and a basic VCO-VCF-VCA voice.

Set Clocked to 120 BPM. Connect CLK2 (eighth notes) to Bogaudio S&H's TRIG input. Connect VCV Free Noise's White output to S&H IN. Connect S&H OUT to Quantizer IN. In the Quantizer, select a pentatonic scale: activate C, D, E, G, A only. Connect Quantizer OUT to VCO V/OCT.

The patch now generates a new random note in the pentatonic scale on every eighth note. Pentatonic works especially well here because it has no dissonant intervals — every random note combination sounds musical.

**Tweak:** Slow the clock division to CLK3 (quarter notes) for a sparser, more deliberate melodic feel. Add a Bogaudio ADSR with short attack and medium decay for plucky note shapes. Layer a second quantized S&H at a different clock division for a second melodic voice.

---

## Recipe 7 — Textural Pad with Surge XT Wavetable and Plateau

**Goal:** A slowly evolving atmospheric pad using a wavetable oscillator and large reverb.

Install **Surge XT** and **Valley**. Add **Surge XT Wavetable VCO**, **VCV Free VCF**, **VCV Free VCA**, **Bogaudio ADSR**, **Bogaudio LFO**, **Valley Plateau**.

Tune the Surge XT VCO to a fixed pitch (no sequencer — this is a drone). Select a vocal or harmonics wavetable from the bank. Set a slow ADSR: 3 second attack, full sustain, 6 second release. Manually trigger the ADSR to start the pad.

Add Bogaudio LFO with its **Slow** button enabled (rates below ~0.064 Hz require Slow mode), set to 0.02 Hz (very slow). Route the SIN output through 8vert at 40% to the Surge XT VCO's Position CV input. The wavetable position morphs continuously through different timbres over a 50-second cycle.

Add Valley Plateau: SIZE 0.95, DECAY 0.93, DAMP 0.4. Route the VCA output to Plateau and mix the reverb return generously (0.5–0.7 wet level).

**Tweak:** Add a second LFO at a different rate (0.05 Hz) to the VCF cutoff for independent timbral and spatial evolution. This creates a pad that changes character in two independent dimensions simultaneously.

---

## Recipe 8 — Euclidean Rhythms with Count Modula

**Goal:** Interlocking polyrhythmic percussion patterns with a mathematical, hypnotic character.

Install **Count Modula**. Add **Count Modula Euclidean Rhythm Generator** (search "Euclidean" in the browser), **Impromptu Clocked**, and three noise-based drum voices (see [Slow Psybient](slow-psybient.md) for drum voice construction).

Set Clocked to 120 BPM. Connect the master clock to the Euclidean Rhythm Generator clock input. Configure three channels:
- Channel 1: 3 hits in 8 steps (kick pattern)
- Channel 2: 5 hits in 8 steps (hi-hat pattern)
- Channel 3: 2 hits in 7 steps (snare — intentionally odd to create polyrhythm)

Route each channel's gate output to a corresponding drum voice envelope.

**Tweak:** Rotate individual channel patterns (shift the starting point) while the patch runs to change which beats line up. Changing the step count from 8 to 16 creates the same density but at double the resolution — tighter, faster patterns. The channel with 7 steps will drift in and out of phase with the others every 7 beats — this is the core of polyrhythmic music.

---

## Where to go next

- [FAQ](faq.md) — common problems with effects, sequencers, and clocking
- [How a Patch Works](how-a-patch-works.md) — signal chain fundamentals
- [Sequencers](sequencer.md) — deeper sequencer techniques
- [Sample & Hold](sample-hold.md) — the S&H techniques used in Recipe 6
- [Slow Psybient](slow-psybient.md) — full tutorial combining many of these recipes

---

*Version: 2026-06-17.*
