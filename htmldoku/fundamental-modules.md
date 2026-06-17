# Fundamental Modules

Reference for all modules included with VCV Rack Free (the VCV Fundamental plugin). For each module: what it does, its parameters, inputs, and outputs.

---

## VCO — Voltage-Controlled Oscillator

Generates four simultaneous waveforms at audio rate. Polyphonic.

| Parameters | |
|-----------|---|
| Frequency | Center frequency of the oscillator (in Hz, via 12-TET scaling) |
| FM | Attenuverter for the FM input — scales how much the FM signal shifts the frequency |
| Pulse Width | Width of the square wave (0.01–0.99, default 0.5 for symmetric) |
| PW CV | Attenuverter for the pulse width CV input |
| Sync Mode | Hard or soft sync on the Sync input |
| FM Mode | 1V/octave (exponential) or linear FM |

| Inputs | |
|--------|---|
| PITCH | 1V/octave pitch CV |
| FM | Frequency modulation CV |
| SYNC | Resets oscillator phase — hard or soft depending on Sync Mode |
| PW | Pulse width modulation CV |

| Outputs | |
|---------|---|
| SIN | Sine wave |
| TRI | Triangle wave |
| SAW | Sawtooth wave |
| SQR | Square/pulse wave |

---

## Wavetable VCO

Wavetable oscillator that scans through a set of waveforms. Polyphonic.

| Parameters | |
|-----------|---|
| Frequency | Center frequency |
| Wavetable position | Which waveform in the wavetable (0–100%) |
| FM | FM attenuverter |
| POS CV | Wavetable position CV attenuverter |
| Sync | Hard or soft sync |
| FM Mode | 1V/oct or through-zero linear FM |

| Inputs | |
|--------|---|
| PITCH | 1V/octave pitch CV |
| FM | Frequency modulation |
| SYNC | Sync input |
| POS | Wavetable position CV |

| Outputs | |
|---------|---|
| WAVE | Wavetable output |

---

## VCF — Voltage-Controlled Filter

Ladder filter with lowpass and highpass outputs. Polyphonic.

| Parameters | |
|-----------|---|
| Cutoff | Filter cutoff frequency |
| Resonance | Resonance / Q (0–100%) |
| Freq CV | Attenuverter for cutoff frequency CV input |
| Drive | Input drive / saturation amount |
| Res CV | Attenuverter for resonance CV input |
| Drive CV | Attenuverter for drive CV input |

| Inputs | |
|--------|---|
| Frequency | Cutoff frequency CV |
| Resonance | Resonance CV |
| Drive | Drive CV |
| Audio | Audio signal to filter |

| Outputs | |
|---------|---|
| LPF | Lowpass output |
| HPF | Highpass output |

---

## VCA — Voltage-Controlled Amplifier

Single-channel VCA. Polyphonic.

| Parameters | |
|-----------|---|
| Level | Base level (0–100%) |
| Response Mode | Exponential or linear response to CV |

| Inputs | |
|--------|---|
| CV | Control voltage — scales the output level |
| CH | Audio or CV input |

| Outputs | |
|---------|---|
| CH | Scaled output |

---

## VCA-2

Two-channel VCA (same as VCA but dual channel). Hidden from browser by default; use VCA instead.

---

## ADSR EG — Envelope Generator

Generates an ADSR envelope. Polyphonic.

| Parameters | |
|-----------|---|
| Attack | Attack time |
| Decay | Decay time |
| Sustain | Sustain level (0–100%) |
| Release | Release time |
| Attack CV | Attenuverter for Attack CV input |
| Decay CV | Attenuverter for Decay CV input |
| Sustain CV | Attenuverter for Sustain CV input |
| Release CV | Attenuverter for Release CV input |

| Inputs | |
|--------|---|
| Attack | Attack time CV |
| Decay | Decay time CV |
| Sustain | Sustain level CV |
| Release | Release time CV |
| Gate | Gate signal — high = envelope runs; falling edge triggers release |
| Retrigger | Retrigger the attack from current level on each rising edge |

| Outputs | |
|---------|---|
| Envelope | ADSR envelope output (0–10 V) |

---

## LFO — Low-Frequency Oscillator

Generates four simultaneous low-frequency waveforms. Polyphonic.

| Parameters | |
|-----------|---|
| Frequency | LFO rate in Hz |
| FM | FM attenuverter |
| Pulse Width | Square wave pulse width |
| PW M | Pulse width modulation attenuverter |
| Offset | Bipolar (−5 to +5 V) or unipolar (0 to +10 V) output |
| Invert | Flips the polarity of the output |

| Inputs | |
|--------|---|
| FM | Frequency modulation CV |
| Clock | External clock input — LFO syncs to clock rate |
| Reset | Resets LFO phase to start |
| PW | Pulse width modulation CV |

| Outputs | |
|---------|---|
| SIN | Sine |
| TRI | Triangle |
| SAW | Sawtooth |
| SQR | Square/pulse |

---

## Wavetable LFO

Wavetable oscillator running at LFO rates. Polyphonic.

| Parameters | |
|-----------|---|
| Frequency | LFO rate |
| Wavetable position | Waveform position |
| FM | FM attenuverter |
| POS CV | Position CV attenuverter |
| Offset | Bipolar or unipolar |
| Invert | Polarity flip |

| Inputs | |
|--------|---|
| FM | Frequency modulation |
| Reset | Phase reset |
| POS | Wavetable position CV |
| Clock | Clock sync |

| Outputs | |
|---------|---|
| WAVE | Wavetable output |

---

## Delay

Stereo delay effect with tone control.

| Parameters | |
|-----------|---|
| Time | Delay time |
| Feedback | Feedback amount (0–100%) |
| Tone | Tone of the repeats (0% = dark, 100% = bright, 200% = brighter than input) |
| Mix | Dry/wet mix |
| Time CV | Attenuverter for Time CV input |
| Feedback CV | Attenuverter for Feedback CV |
| Tone CV | Attenuverter for Tone CV |
| Mix CV | Attenuverter for Mix CV |

| Inputs | |
|--------|---|
| Time | Delay time CV |
| Feedback | Feedback CV |
| Tone | Tone CV |
| Mix | Mix CV |
| Audio | Audio input |
| Clock | Clock input — delay time snaps to clock divisions |

| Outputs | |
|---------|---|
| Mix | Dry + wet output |
| Wet | Wet-only output |

---

## Mix — 6-Channel Mixer

Mixes up to 6 signals with individual level controls. Polyphonic.

| Parameters | |
|-----------|---|
| Level | Master level (0–100%) |

| Inputs | |
|--------|---|
| Channels 1–6 | Signal inputs |

| Outputs | |
|---------|---|
| Mix | Mixed output |

---

## VCA Mix — 4-Channel Mixer with VCAs

4-channel mixer with individual VCA inputs per channel and a master level with VCA. Polyphonic.

| Parameters | |
|-----------|---|
| Mix Level | Master mix level in dB |
| Channel 1–4 Level | Per-channel level |

| Inputs | |
|--------|---|
| Mix CV | Master VCA CV |
| Channel 1–4 | Audio inputs |
| Channel 1–4 CV | Per-channel VCA CV |

| Outputs | |
|---------|---|
| Mix | Mixed output |
| Channel 1–4 | Individual channel outputs |

---

## 8vert

8-channel attenuverter. Each row independently scales a signal from −1× to +1×. If no input is connected, outputs a constant voltage from −10 V to +10 V set by the knob. Polyphonic.

| Parameters | |
|-----------|---|
| Gain 1–8 | Attenuverter knob per row (−1 to +1) |

| Inputs | |
|--------|---|
| Row 1–8 | Signal inputs (normalled so each row copies from the one above if unpatched) |

| Outputs | |
|---------|---|
| Row 1–8 | Scaled outputs |

---

## Mutes — 10-Channel Toggle Switch

Toggles up to 10 signals on or off with buttons. Polyphonic.

| Parameters | |
|-----------|---|
| Mute 1–10 | Toggle button per row |

| Inputs | |
|--------|---|
| Row 1–10 | Signal inputs |

| Outputs | |
|---------|---|
| Row 1–10 | Muted or passed-through outputs |

---

## Pulses — 10-Channel Trigger/Gate Generator

Generates trigger and gate outputs for each of 10 buttons. No inputs required.

| Outputs | |
|---------|---|
| Row 1–10 Trigger | Short trigger pulse on button press |
| Row 1–10 Gate | High while button is held |

---

## SEQ 3 — 3-Channel 8-Step Sequencer

Three rows of 8 programmable steps, with built-in clock and gate outputs.

| Parameters | |
|-----------|---|
| Tempo | Internal clock BPM |
| Tempo CV | Attenuverter for tempo CV |
| Steps | Number of active steps (1–8) |
| Steps CV | Attenuverter for steps CV |
| CV 1–3, Steps 1–8 | Voltage value for each step on each row |

| Inputs | |
|--------|---|
| Tempo | Tempo CV |
| Clock | External clock input (overrides internal clock) |
| Run | Run/stop CV |
| Reset | Resets to step 1 |
| Steps | Steps CV |

| Outputs | |
|---------|---|
| CV 1–3 | Pitch or other CV per row |
| Step 1–8 | Trigger on the active step |
| Trigger | Trigger on every step |
| Steps | Steps CV passthrough |
| Clock | Clock output |
| Run | Run state output |
| Reset | Reset passthrough |

---

## Sequential Switch 1→4

Routes one input to one of four outputs, advancing each clock step.

| Inputs | |
|--------|---|
| Clock | Advances the active output |
| Reset | Returns to output 1 |
| Input | Signal to route |

| Outputs | |
|---------|---|
| 1–4 | Routed outputs |

---

## Sequential Switch 4→1

Routes one of four inputs to one output, advancing each clock step.

| Inputs | |
|--------|---|
| Clock | Advances the active input |
| Reset | Returns to input 1 |
| 1–4 | Signal inputs |

| Outputs | |
|---------|---|
| Output | Selected input |

---

## Octave

Shifts a 1V/oct pitch CV by whole octaves. Polyphonic.

| Parameters | |
|-----------|---|
| Shift | Octave shift (−4 to +4 octaves) |

| Inputs | |
|--------|---|
| Pitch | 1V/oct pitch CV input |
| Octave Shift CV | CV to shift the octave |

| Outputs | |
|---------|---|
| Pitch | Transposed pitch output |

---

## Quantizer

Snaps incoming pitch CV to the nearest note in a chosen scale. Polyphonic.

| Parameters | |
|-----------|---|
| Pre-offset | Shifts the input voltage by −12 to +12 semitones before quantizing |

| Inputs | |
|--------|---|
| Pitch | Unquantized pitch CV |

| Outputs | |
|---------|---|
| Pitch | Quantized pitch output |

Right-click to select the quantization scale.

---

## Split

Splits one polyphonic cable into up to 16 monophonic outputs.

| Inputs | |
|--------|---|
| Polyphonic | Polyphonic input cable |

| Outputs | |
|---------|---|
| Channel 1–16 | Individual channel outputs |

---

## Merge

Combines up to 16 monophonic cables into one polyphonic cable.

| Inputs | |
|--------|---|
| Channel 1–16 | Monophonic inputs |

| Outputs | |
|---------|---|
| Polyphonic | Combined polyphonic output |

---

## Sum

Sums all channels of a polyphonic cable into a single monophonic output. Polyphonic input.

| Parameters | |
|-----------|---|
| Level | Output level (0–100%) |

| Inputs | |
|--------|---|
| Polyphonic | Polyphonic input |

| Outputs | |
|---------|---|
| Monophonic | Summed output |

---

## Viz

Visualises all channels of a polyphonic cable as a bargraph. No audio output.

| Inputs | |
|--------|---|
| Polyphonic | Polyphonic input to visualise |

---

## Scope

Oscilloscope for inspecting waveforms. Polyphonic.

| Parameters | |
|-----------|---|
| Gain 1 | Vertical scale for Ch 1 |
| Offset 1 | Vertical offset for Ch 1 |
| Gain 2 | Vertical scale for Ch 2 |
| Offset 2 | Vertical offset for Ch 2 |
| Time | Horizontal time scale |
| Scope mode | Time (1 & 2 over time) or Lissajous (1 x 2) |
| Trigger threshold | Trigger level for display sync |
| Trigger | Enable or disable trigger |

| Inputs | |
|--------|---|
| Ch 1 | Channel 1 signal |
| Ch 2 | Channel 2 signal |
| External trigger | External trigger for display sync |

| Outputs | |
|---------|---|
| Ch 1 | Passthrough of Ch 1 input |
| Ch 2 | Passthrough of Ch 2 input |

---

## Noise

Multicolor noise generator. No inputs.

| Outputs | |
|---------|---|
| White | White noise (equal energy per Hz) |
| Pink | Pink noise (equal energy per octave) |
| Red | Red / Brownian noise (heavy low-end emphasis) |
| Violet | Violet noise (high-end emphasis) |
| Blue | Blue noise |
| Gray | Gray noise (psychoacoustically flat) |
| Black | Near-silence with very slow random walk |

---

## Random

Random CV generator with internal or external triggering. Polyphonic.

| Parameters | |
|-----------|---|
| Rate | Internal trigger rate (Hz) |
| Probability | Chance that each trigger produces a new value |
| Spread | Range of random values |
| Shape | Distribution shape of random values |
| Offset | Bipolar or unipolar output |
| Rate CV | Attenuverter for Rate CV |
| Probability CV | Attenuverter |
| Spread CV | Attenuverter |
| Shape CV | Attenuverter |

| Inputs | |
|--------|---|
| Rate | Rate CV |
| Probability | Probability CV |
| Spread | Spread CV |
| Shape | Shape CV |
| Trigger | External trigger (overrides internal clock) |
| External | External audio input to sample |

| Outputs | |
|---------|---|
| Trigger | Internal trigger output |
| Stepped | New random value on each trigger |
| Linear | Linearly interpolated between values |
| Exponential | Exponentially interpolated |
| Smooth | Smoothly interpolated |

---

## CV Mix

Mixes 3 CV signals with attenuverters. Polyphonic.

| Parameters | |
|-----------|---|
| Level 1–3 | Attenuverter for each input (−1 to +1) |

| Inputs | |
|--------|---|
| CV 1–3 | Signal inputs |

| Outputs | |
|---------|---|
| Mix | Mixed output |

---

## Fade

Crossfader between two signals. Polyphonic.

| Parameters | |
|-----------|---|
| Crossfade | Position (0% = Ch 1, 100% = Ch 2) |
| Crossfade CV | Attenuverter for Crossfade CV |

| Inputs | |
|--------|---|
| Crossfade | CV to control fade position |
| Ch 1 | First input |
| Ch 2 | Second input |

| Outputs | |
|---------|---|
| Ch 1 | Faded output 1 (inverse of fade) |
| Ch 2 | Faded output 2 (follows fade) |

---

## Logic

Gate logic processor. Polyphonic.

| Inputs | |
|--------|---|
| A | First gate signal |
| B | Second gate signal |

| Outputs | |
|---------|---|
| NOT A | Inverted A |
| NOT B | Inverted B |
| OR | High if A or B is high |
| NOR | High if neither A nor B is high |
| AND | High only if both A and B are high |
| NAND | High unless both are high |
| XOR | High if exactly one of A or B is high |
| XNOR | High if A and B match |

---

## Compare

Compares two voltages. Polyphonic.

| Parameters | |
|-----------|---|
| B offset | Offset added to the B input |

| Inputs | |
|--------|---|
| A | Signal A |
| B | Signal B |

| Outputs | |
|---------|---|
| Maximum | The larger of A or B |
| Minimum | The smaller of A or B |
| Clip | A clipped to B's range |
| Limit | A limited to ±B |
| Clip gate | High while A is being clipped |
| Limit gate | High while A is being limited |
| A > B | Gate high when A exceeds B |
| A < B | Gate high when A is below B |

---

## Gates — Gate Processor

Detects rising and falling edges, generates fixed-length gates, and includes a flip/flop. Polyphonic.

| Parameters | |
|-----------|---|
| Gate length | Length of the generated gate output |

| Inputs | |
|--------|---|
| Gate length | CV to modulate gate length |
| Gate | Input gate or trigger signal |
| Reset | Resets the flip/flop |

| Outputs | |
|---------|---|
| Rising edge | Trigger on rising edge |
| Falling edge | Trigger on falling edge |
| Flip | Toggles on each rising edge |
| Flop | Toggles on each falling edge |
| Gate | Fixed-length gate triggered on rising edge |
| Gate delay | Gate output delayed by the gate length |

---

## Process — CV Processor

Sample & hold, track & hold, and slew in one module. Polyphonic.

| Parameters | |
|-----------|---|
| Slew | Slew rate for the Slew and Glide outputs |

| Inputs | |
|--------|---|
| Slew | Slew rate CV |
| Voltage | Input voltage |
| Gate | Gate for track & hold and hold & track modes |

| Outputs | |
|---------|---|
| Sample & hold | Samples input on gate rising edge, holds until next |
| Sample & hold 2 | Samples on gate falling edge |
| Track & hold | Follows input while gate is high; holds on falling edge |
| Hold & track | Holds while gate is high; tracks when gate is low |
| Slew | Slew-limited version of input |
| Glide | Smooth glide with different slew characteristics |

---

## Mult — 1-to-8 Multiple

Copies one input signal to eight outputs unchanged. Polyphonic.

| Inputs | |
|--------|---|
| Mult | Signal to copy |

| Outputs | |
|---------|---|
| Mult 1–8 | Identical copies of the input |

---

## Rescale

Scales and offsets a signal with range limiting. Polyphonic.

| Parameters | |
|-----------|---|
| Gain | Signal gain (−1 to +1, with 0 = silence) |
| Offset | Voltage offset added after gain |
| Maximum | Upper clamp for output |
| Minimum | Lower clamp for output |

| Inputs | |
|--------|---|
| Signal | Input signal |

| Outputs | |
|---------|---|
| Signal | Rescaled output |

---

## Mid/Side

Encodes stereo left/right to mid/side and decodes mid/side back to left/right. Polyphonic.

| Parameters | |
|-----------|---|
| Encoder width | Mid/side stereo width for the encoder |
| Decoder width | Stereo width for the decoder |

| Inputs | |
|--------|---|
| Encoder width | Width CV for encoder |
| Encoder left | Left channel input |
| Encoder right | Right channel input |
| Decoder width | Width CV for decoder |
| Decoder mid | Mid channel input |
| Decoder side | Side channel input |

| Outputs | |
|---------|---|
| Encoder mid | Mid output |
| Encoder side | Side output |
| Decoder left | Left output |
| Decoder right | Right output |

---

## Push — Button with Gate/Trigger

Manual button with gate and trigger outputs and a hold switch.

| Inputs | |
|--------|---|
| Hold | Holds the gate open while high |
| Push | CV input that triggers the button |

| Outputs | |
|---------|---|
| Trigger | Short pulse on press |
| Gate | High while button is held |

---

## Random Values

Generates 7 fixed random voltages. On each trigger, all 7 voltages are re-randomized simultaneously. Polyphonic.

| Inputs | |
|--------|---|
| Trigger | Trigger to generate new random values |

| Outputs | |
|---------|---|
| Random 1–7 | Fixed random output voltages, re-randomized on trigger |

---

## SHASR — Sample & Hold Analog Shift Register

8-channel sample & hold with a shift register mode. Each channel samples its input when triggered.

| Parameters | |
|-----------|---|
| Randomize | Randomizes the shift register contents |

| Inputs | |
|--------|---|
| Sample 1–8 | Input voltages to sample |
| Trigger 1–8 | Per-channel trigger inputs |

| Outputs | |
|---------|---|
| Sample 1–8 | Held output voltages |

---

## Where to go next

- [Befaco Modules](befaco-modules.md) — additional modules with more complex features
- [How a Patch Works](kernablauf.md) — how these modules connect in a signal chain
- [Patching Use Cases](anwendungsfaelle.md) — recipes using these modules

---

*Version: 2026-06-17.*
