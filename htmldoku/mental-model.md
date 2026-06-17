# Signal Flow & Concepts

Modular synthesis is built on one idea: everything is a voltage. Audio signals, musical notes, rhythms, filter cutoffs, effects levels — all of them are just voltages flowing through cables. Understanding how different kinds of voltages work is the foundation of everything you'll patch.

---

## Voltage is the universal language

In VCV Rack, every signal is a number between roughly −10 V and +10 V. That's it. There is no separate "CV world" and "audio world" at the hardware level — it's all just numbers. What differs is how those voltages are typically used and what range makes sense for each purpose.

This means you can do things that would be strange on a traditional synthesizer: run an audio signal into a filter's cutoff input to create ring-modulation-like effects, or use an envelope to pan a mixer, or sequence a filter cutoff the same way you sequence pitch. The patch cable doesn't know what the signal is "for."

---

## Audio signals

Audio signals carry sound. They typically swing between −5 V and +5 V at audio rates — anything from 20 Hz up to 20 kHz and beyond. When you connect an oscillator's output to the AUDIO module's input and press play, you're sending an audio-rate voltage to your sound card.

If the signal is too loud (peaks beyond roughly ±5–6 V), you'll hear clipping — a harsh, crunchy distortion. A VCA or mixer with its level turned down is the usual fix.

---

## CV — Control Voltage

CV signals move slowly relative to audio. They're used to control parameters: pitch, filter cutoff, reverb mix, envelope speed. There are several common CV conventions:

**1V/octave pitch CV.** Each volt represents one octave. Middle C (C4) is typically 0 V. C5 is 1 V. C3 is −1 V. This means a sequence or MIDI module outputs a voltage, and any VCO tracking at 1V/oct will play the right note. Most oscillators in VCV Rack follow this standard.

**Unipolar CV (0 V to +10 V).** Used for things that have no "negative" value — envelope output, for example. An ADSR outputs 0 V when silent and +10 V at peak.

**Bipolar CV (−5 V to +5 V or −10 V to +10 V).** Used for modulation that should swing in both directions, like an LFO that sweeps a filter up and down around a center frequency.

---

## Gates and triggers

Gates and triggers are CV signals used for timing and control.

A **gate** is a high voltage (+10 V, or similar) that stays high for as long as a key is held or a sequencer step is active. An ADSR envelope typically expects a gate: the attack begins when the gate goes high, sustain holds while the gate is up, and release begins when the gate drops.

A **trigger** is a very short pulse — just a few milliseconds — that says "now." It fires a drum hit, advances a sequencer, resets an LFO. Triggers don't have duration in the way gates do. Some modules accept either.

If a module seems to fire once and not repeat, or never sustain, check whether it wants a gate or a trigger.

---

## Module categories

VCV Rack modules fall into a handful of functional categories. Knowing these helps you find what you need in the module browser.

**VCO (Voltage-Controlled Oscillator).** Generates an audio-rate waveform — sine, triangle, sawtooth, square. The primary sound source. Takes a 1V/oct pitch CV input to track pitch.

**VCF (Voltage-Controlled Filter).** Shapes the frequency content of a signal. Lowpass is the most common type: it passes low frequencies and cuts high ones. Resonance emphasizes the cutoff frequency. Can be modulated by an envelope or LFO for classic filter sweeps.

**VCA (Voltage-Controlled Amplifier).** Controls the level of a signal. Patching an envelope to a VCA's CV input shapes the amplitude over time — the signature of any note-like sound. Without a VCA, your oscillator plays continuously at full volume.

**Envelope Generator (EG).** Generates a contour voltage over time, typically triggered by a gate. The ADSR shape — Attack, Decay, Sustain, Release — is the standard form. Output is usually 0–10 V.

**LFO (Low-Frequency Oscillator).** Like a VCO but running below 20 Hz — too slow to be heard as a pitch. Used as a modulation source: vibrato, tremolo, filter wobble, rhythmic panning.

**Sequencer.** Steps through a series of values over time, driven by a clock. Outputs pitch CV, gates, or both. The heart of melodic and rhythmic patterns.

**Mixer.** Combines multiple signals into one output. Audio mixing keeps levels balanced. CV mixing can blend two modulation sources.

**Utility.** Everything that doesn't fit a specific category: attenuators, inverters, logic, switches, multiples. Often the modules that make complex patches actually work.

**Effects.** Reverb, delay, chorus, distortion. Usually placed after VCAs in the signal chain, taking audio in and returning processed audio.

---

## Polyphony

VCV Rack supports polyphony through a single cable carrying up to 16 channels. A polyphonic cable appears thicker than a monophonic one. A MIDI module or sequencer can output all note pitches and gates as a single polyphonic cable. An oscillator, filter, and VCA that support polyphony will process all 16 channels in parallel.

The Split module separates a polyphonic cable into individual monophonic cables. The Merge module does the reverse. Sum adds all channels to a single mono output.

---

## Where to go next

- [How a Patch Works](kernablauf.md) — see signal flow in action from oscillator to output
- [Your First Patch](first-patch.md) — build a working patch step by step
- [Fundamental Modules](fundamental-modules.md) — reference for every module in this category
- [Glossary](glossary.md) — definitions for every term on this page

---

*Version: 2026-06-17.*
