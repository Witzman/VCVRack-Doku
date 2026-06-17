# Befaco Modules

Reference for all modules in the Befaco plugin. Befaco modules are hardware clones of the Befaco Eurorack module range. For each module: what it does, its parameters, inputs, and outputs.

---

## Even VCO

Analog-style VCO featuring an even-harmonic waveform output in addition to the standard set. Polyphonic.

| Parameters | |
|-----------|---|
| Octave | Octave offset (−5 to +4) |
| Tune | Fine tune in semitones (±7) |
| Pulse Width | Square wave pulse width |

| Inputs | |
|--------|---|
| Pitch 1 | 1V/oct pitch CV input 1 |
| Pitch 2 | Second 1V/oct pitch CV input (summed with Pitch 1) |
| FM | Frequency modulation CV |
| Hard Sync | Resets oscillator phase |
| PWM | Pulse width modulation CV |

| Outputs | |
|---------|---|
| Triangle | Triangle wave |
| Sine | Sine wave |
| Even | Even harmonic wave (distinct character from standard shapes) |
| Sawtooth | Sawtooth wave |
| Square | Square/pulse wave |

---

## Rampage

Dual ramp generator — a versatile module that functions as a dual function generator, slew limiter, envelope generator, LFO, and more. Polyphonic.

| Parameters | |
|-----------|---|
| Ch 1/2 Range | Speed range: Medium, Fast, or Slow |
| Ch 1/2 Shape | Waveform shape of the ramp (logarithmic to exponential) |
| Ch 1/2 Trigger | Manual trigger button |
| Ch 1/2 Rise | Rise time |
| Ch 1/2 Fall | Fall time |
| Ch 1/2 Cycle | Looping mode — ramp repeats continuously |
| Balance | Output balance between the two channels' combined output |

| Inputs | |
|--------|---|
| A / B | Input signal for each channel |
| Trigger A / B | Gate or trigger to start the ramp |
| Rise CV A / B | CV control of rise time |
| Fall CV A / B | CV control of fall time |

| Outputs | |
|---------|---|
| A Rising | Gate while channel A is rising |
| A Falling | Gate while channel A is falling |
| A Endof | Trigger at end of channel A cycle |
| A Out | Channel A ramp output |
| B Out | Channel B ramp output |
| B Rising | Gate while channel B is rising |
| B Falling | Gate while channel B is falling |
| B Endof | Trigger at end of channel B cycle |
| Comparator | Gate when channel A output exceeds channel B |
| Logic AND | Gate when both channels are active |
| Logic OR | Gate when either channel is active |

---

## A*B+C

Dual four-quadrant multiplier. Computes A×B+C for two channels. Useful as a ring modulator, VCA, mixer, or offset generator. Polyphonic.

| Parameters | |
|-----------|---|
| B1 Level | Attenuverter for the B1 input |
| C1 Level | Attenuverter for the C1 (offset) input |
| B2 Level | Attenuverter for the B2 input |
| C2 Level | Attenuverter for the C2 input |

| Inputs | |
|--------|---|
| A1, B1, C1 | Three inputs for channel 1 computation |
| A2, B2, C2 | Three inputs for channel 2 computation |

| Outputs | |
|---------|---|
| Out 1 | Result of A1 × B1 + C1 |
| Out 2 | Result of A2 × B2 + C2 |

---

## Spring Reverb

Spring reverb tank driver — emulates the sound of a physical spring reverb tank.

| Parameters | |
|-----------|---|
| In 1 Level | Level of input 1 |
| In 2 Level | Level of input 2 |
| Dry/Wet | Mix between dry and wet signal |
| High Pass Filter | Cutoff of the HPF applied to the wet signal |

| Inputs | |
|--------|---|
| CV 1 | CV control for input 1 level |
| CV 2 | CV control for input 2 level |
| In 1 | Audio input 1 |
| In 2 | Audio input 2 |
| Mix CV | CV control for dry/wet mix |

| Outputs | |
|---------|---|
| Mix | Dry + wet output |
| Wet | Wet-only reverb output |

---

## Mixer (Befaco)

Four-channel mixer for audio or CV with per-channel level controls.

| Parameters | |
|-----------|---|
| Ch 1–4 Level | Level for each channel |

| Inputs | |
|--------|---|
| Ch 1–4 | Signal inputs |

| Outputs | |
|---------|---|
| Main | Mixed output |
| Inverted | Polarity-inverted version of the main output |

---

## Slew Limiter

Voltage-controlled slew limiter. Smooths abrupt voltage jumps. Useful as a portamento, glide processor, or low-pass CV filter. Polyphonic.

| Parameters | |
|-----------|---|
| Shape | Curve shape of the slew (linear to exponential) |
| Rise | Rise time |
| Fall | Fall time |

| Inputs | |
|--------|---|
| Rise CV | CV control for rise time |
| Fall CV | CV control for fall time |
| In | Signal to slew |

| Outputs | |
|---------|---|
| Out | Slewed output |

---

## Dual Atenuverter

Two-channel attenuverter with offset. Each channel scales and offsets an input independently. Polyphonic.

| Parameters | |
|-----------|---|
| Ch 1/2 Gain | Attenuverter (−1 to +1) |
| Ch 1/2 Offset | Constant voltage offset (±10 V) |

| Inputs | |
|--------|---|
| In 1, In 2 | Signal inputs |

| Outputs | |
|---------|---|
| Out 1, Out 2 | Scaled and offset outputs |

---

## Percall

Quad percussive envelope generator and mixer. Four independent channels, each with trigger, decay, and level. Polyphonic.

| Parameters | |
|-----------|---|
| Channel 1–4 Level | Output level per channel |
| Channel 1–4 Decay | Decay time per channel |
| Choke 1–2 and 3–4 | Choke pair — triggering one channel stops the other |

| Inputs | |
|--------|---|
| Channel 1–4 | Audio or CV input per channel |
| Trigger 1–4 | Trigger for each channel's envelope |
| CV 1–4 | Decay time CV per channel |
| Overall gain | Scales the output of all channels (also affects envelope outputs) |

| Outputs | |
|---------|---|
| Channel 1–4 | Per-channel audio output shaped by decay envelope |
| Envelope 1–4 | Envelope CV output for each channel |

---

## Hex Mix VCA

Six-channel VCA with adjustable response curve per channel. Polyphonic.

| Parameters | |
|-----------|---|
| Response 1–6 | VCA response curve (logarithmic to linear to exponential) |
| Level 1–6 | Maximum output level per channel |

| Inputs | |
|--------|---|
| Channel 1–6 | Audio or CV inputs |
| Gain 1–6 | CV control for each channel's VCA |

| Outputs | |
|---------|---|
| Channel 1–6 | VCA outputs |

---

## Chopping Kinky

Dual wavefolder with voltage-controlled chop (hard gate between channels).

| Parameters | |
|-----------|---|
| Gain/Shape A | Gain and fold amount for channel A |
| Gain/Shape B | Gain and fold amount for channel B |
| CV A attenuverter | Scales the CV A input |
| CV B attenuverter | Scales the CV B input |

| Inputs | |
|--------|---|
| A | Channel A input |
| B | Channel B input |
| Chopp | Gate that switches between A and B outputs |
| CV A | Wavefold CV with attenuverter |
| VCA CV A | Direct VCA CV for channel A |
| CV B | Wavefold CV with attenuverter |
| VCA CV B | Direct VCA CV for channel B |

| Outputs | |
|---------|---|
| Chopp | Switches between A and B based on Chopp gate |
| A | Wavefolded channel A output |
| B | Wavefolded channel B output |

---

## Kickall

Kick drum synthesizer with pitch and volume envelopes.

| Parameters | |
|-----------|---|
| Tune | Base frequency of the kick |
| Wave Shape | Waveform shape (sine to more complex) |
| VCA Decay | Amplitude envelope decay time |
| Pitch Decay | Pitch envelope decay time |
| Pitch Bend | Amount of pitch drop from start to sustain |

| Inputs | |
|--------|---|
| Trigger | Trigger input to fire the kick |
| Gain | VCA level CV |
| Tune | Pitch CV (V/oct) |
| Shape CV | Waveform shape CV |
| Decay CV | VCA decay CV |

| Outputs | |
|---------|---|
| Kick | Kick drum audio output |

---

## ADSR (Befaco)

ADSR envelope generator with stage gate outputs, variable shape, and gate/trigger mode. Has its own character compared to the VCV Free ADSR.

| Parameters | |
|-----------|---|
| Mode | Gate or Trigger operation |
| Shape | Envelope curve shape |
| Attack | Attack time |
| Decay | Decay time |
| Sustain | Sustain level |
| Release | Release time |

| Inputs | |
|--------|---|
| Trigger | Gate or trigger input |
| Attack CV | Attack time CV |
| Decay CV | Decay time CV |
| Sustain CV | Sustain level CV |
| Release CV | Release time CV |

| Outputs | |
|---------|---|
| Envelope | Main ADSR output |
| Attack stage | Gate while in attack stage |
| Decay stage | Gate while in decay stage |
| Sustain stage | Gate while in sustain stage |
| Release stage | Gate while in release stage |

---

## STMix

Compact 4-channel stereo mixer with auxiliary input.

| Parameters | |
|-----------|---|
| Gain 1–4 | Per-channel gain |

| Inputs | |
|--------|---|
| Channel 1–4 Left | Left input per channel |
| Channel 1–4 Right | Right input per channel |
| Channel Left (aux) | Auxiliary left input |
| Channel Right (aux) | Auxiliary right input |

| Outputs | |
|---------|---|
| Left | Stereo left mix output |
| Right | Stereo right mix output |

---

## Muxlicer

VC-addressable sequential switch and sequencer. Steps through 8 positions, with per-step gain and gate outputs. Polyphonic.

| Parameters | |
|-----------|---|
| Play | Play once / stop / play continuously |
| Address | Manual step address (−1 = sequential) |
| Gate Mode | Gate pattern for each step |
| Clock Mult/Div | Clock multiplication or division |
| Gain 1–8 | Per-step gain |
| Step 1–8 | Step mode: Gate/Clock out, Muted, or All Gates |

| Inputs | |
|--------|---|
| Gate Mode CV | CV for gate mode |
| Address CV | CV to select step |
| Clock | Clock input |
| Reset | Resets to start |
| COM I/O | Common input/output |
| All | Broadcasts to all steps simultaneously |

| Outputs | |
|---------|---|
| Step 1–8 | Per-step signal output |
| Gate 1–8 | Per-step gate |
| End of cycle | Trigger at end of each cycle |
| Clock | Clock output |
| All gates | Gate on every active step |
| All | Sum of all step outputs |
| COM I/O | Common routed output |

---

## Mex

Gate expander for the Muxlicer. Attaches to the right side of Muxlicer to add additional gate outputs per step.

---

## Noise Plethora

Dual noise engine with filterable outputs. Three independent programmable noise generators (A, B, C) with built-in filter per channel.

| Parameters | |
|-----------|---|
| X A / Y A | Noise algorithm parameters for channel A |
| Resonance A | Filter resonance for channel A |
| Cutoff A | Filter cutoff for channel A |
| Cutoff CV A | Filter cutoff CV attenuverter |
| Filter Type A | Lowpass, Bandpass, or Highpass |
| Program/Bank | Selects the noise algorithm/bank |
| (Same for B and C) | |

| Inputs | |
|--------|---|
| Cutoff CV A/B/C | Filter cutoff CVs |

| Outputs | |
|---------|---|
| Output A/B/C | Filtered noise outputs per channel |

---

## Stereo Strip

Stereo channel strip with EQ, pan, VCA, and level control. Polyphonic.

| Parameters | |
|-----------|---|
| High shelf (2 kHz) | High frequency gain (±15 dB) |
| Mid band (1.2 kHz) | Midrange gain (±12.5 dB) |
| Low shelf (125 Hz) | Low frequency gain (±20 dB) |
| Pan | Stereo position |
| Pan CV | Attenuverter for pan CV |
| Level | Output gain (−60 to 0 dB) |
| In boost | +6 dB input boost switch |
| Out cut | −6 dB output cut switch |
| Mute | Mute switch |

| Inputs | |
|--------|---|
| Left | Left channel input |
| Right | Right channel input (normalises from Left if unpatched) |
| Level | VCA CV (10 V normalised) |
| Pan CV | Pan control voltage (±5 V) |

| Outputs | |
|---------|---|
| Left | Processed left output |
| Right | Processed right output |

---

## Pony VCO

Compact through-zero FM oscillator with integrated wavefolder and VCA. Polyphonic.

| Parameters | |
|-----------|---|
| Frequency | Pitch offset |
| Range | VCO Full / VCO Octave / VCO Semitone / LFO |
| Octave | Octave select (C1–C7) |
| Wave | Waveform: Sine, Triangle, Sawtooth, Pulse |
| Timbre | Controls wavefolding depth or pulse width depending on waveform |

| Inputs | |
|--------|---|
| Through-zero FM | TZFM input |
| Timbre | Timbre modulation CV |
| V/Oct | Pitch CV |
| Hard Sync | Sync input |
| VCA | Built-in VCA CV |

| Outputs | |
|---------|---|
| Out | Waveform output |

---

## Motion MTR

Three-channel CV/audio utility with per-channel mode switching and visualisation. Polyphonic.

| Parameters | |
|-----------|---|
| Channel 1–3 Mode | Attenuate, Attenuvert, or DC-block |
| Channel 1–3 Gain | Gain knob per channel |

| Inputs | |
|--------|---|
| Channel 1–3 | Signal inputs |

| Outputs | |
|---------|---|
| Channel 1, 2 | Per-channel processed outputs |
| Channel 3 (Mix) | Sum of all three channels |

---

## Burst

Trigger processor and generator. Takes one trigger and outputs a burst of triggers with configurable timing, quantity, and distribution. Useful for flams, rolls, and organic rhythmic variations.

| Parameters | |
|-----------|---|
| Mode | One-shot or Cycle |
| Number of bursts | Count of triggers to generate (1–max) |
| Quantity CV | Attenuverter for quantity CV |
| Distribution | Spacing between triggers in the burst |
| Time | Clock division/multiplication ratio |
| Probability | Probability that each burst trigger fires |

| Inputs | |
|--------|---|
| Quantity CV | CV to set number of triggers |
| Distribution | CV to control burst distribution |
| Ping | Clock reference input |
| Time | Time CV |
| Probability | Probability CV |
| Trigger | Main trigger input |

| Outputs | |
|---------|---|
| Tempo | Derived tempo output |
| End of cycle | Trigger at end of burst |
| (Individual trigger outputs for each burst step) | |

---

## Sampling Modulator

Multi-function module: oscillator, sample & hold, and 8-step trigger sequencer combined. Can self-clock or sync to an external clock.

| Parameters | |
|-----------|---|
| Rate | Oscillator/clock rate |
| Fine | Fine tune |
| Clock | Internal or external clock |
| Step 1–8 | Each step: Reset, Off, or On |

| Inputs | |
|--------|---|
| Sync | External sync input |
| V/Oct | Pitch CV for oscillator rate |
| Hold | Hold input — freezes output |
| Raw | Audio input to sample |

| Outputs | |
|---------|---|
| Clock | Clock output |
| Trigger | Trigger on each active step |
| Sampled | Sampled and sequenced output |

---

## Morphader

Four-channel CV/audio crossfader between two sets of signals. Polyphonic.

| Parameters | |
|-----------|---|
| CV attenuator | Scales the CV input |
| A Level 1–4 | Level of the A side per channel |
| B Level 1–4 | Level of the B side per channel |
| Mode 1–4 | Audio or CV mode per channel |
| Fader | Main crossfade position |
| Fader Lag | Slew applied to fader movement |

| Inputs | |
|--------|---|
| A1–A4 | A-side signal inputs |
| B1–B4 | B-side signal inputs |
| CV channel 1–4 | Per-channel CV position |

| Outputs | |
|---------|---|
| Channel 1–4 | Crossfaded outputs |

---

## MIDI Thing V2

Bridge module for the Befaco MIDI Thing V2 hardware — a flexible MIDI-to-CV converter. Requires the physical Befaco MIDI Thing V2 hardware connected to your computer.

---

## Voltio

Precision voltage source and precision adder. Sets an exact output voltage defined by octave and semitone values, with an optional summing input.

| Parameters | |
|-----------|---|
| Octave | Integer octave (0–10 V) |
| Range | 0 to 10 V or −5 to +5 V |
| Semitones | Semitone offset (0–11) |

| Inputs | |
|--------|---|
| Sum | Voltage added to the panel-set value |

| Outputs | |
|---------|---|
| Main | Precise voltage output |

---

## Octaves

Additive oscillator with individual gain controls for the fundamental and five harmonics. Polyphonic.

| Parameters | |
|-----------|---|
| Octave | Base octave (C1–C7) |
| Tune | Fine tune (±1 semitone) |
| PWM | Pulse width |
| Range | VCO Full / Octave / Semitone |
| Gain Fundamental | Level of the fundamental frequency |
| Gain ×2 | Level of the 2nd harmonic |
| Gain ×4 | Level of the 4th harmonic |
| Gain ×8 | Level of the 8th harmonic |
| Gain ×16 | Level of the 16th harmonic |
| Gain ×32 | Level of the 32nd harmonic |
| PWM CV | Attenuverter for PWM CV |

| Inputs | |
|--------|---|
| V/Oct 1 | First pitch CV input |
| V/Oct 2 | Second pitch CV input |
| Sync | Oscillator sync |
| PWM | Pulse width modulation CV |

| Outputs | |
|---------|---|
| Out | Mixed additive output |

---

## Bypass

Stereo bypass/switching module for routing signals to and from an external effect. Polyphonic.

| Parameters | |
|-----------|---|
| Return Mode | Hard or soft bypass transition |
| FX Return Gain | Attenuverter for the returned FX signal |
| Launch Mode | Latch (toggle) or Gate (momentary) |
| Slew Time | Transition speed for soft bypass |

| Inputs | |
|--------|---|
| Left, Right | Dry signal inputs |
| From FX L, From FX R | Return from external effect |
| Launch | CV to trigger bypass switch |

| Outputs | |
|---------|---|
| To FX L, To FX R | Send to external effect |
| Left, Right | Output (dry or through-effect depending on bypass state) |

---

## Bandit

Spectral processing module — a four-band splitter that separates a signal into frequency bands, sends each band to an external effect, then recombines the returns.

| Parameters | |
|-----------|---|
| Low gain | Level of the low band send |
| Low mid gain | Level of the low-mid band send |
| High mid gain | Level of the high-mid band send |
| High gain | Level of the high band send |

| Inputs | |
|--------|---|
| Low, Low mid, High mid, High | Band inputs |
| Low return, Low mid return, High mid return, High return | Effect returns per band |

| Outputs | |
|---------|---|
| Low, Low mid, High mid, High | Band sends |
| (Mixed output available) | |

---

## Mixer (v2)

Utilitarian four-channel audio and CV mixer with individual gain knobs.

| Parameters | |
|-----------|---|
| Gain 1–4 | Per-channel gain |

| Inputs | |
|--------|---|
| Channel 1–4 | Signal inputs |

| Outputs | |
|---------|---|
| Mix 1+2 | Sum of channels 1 and 2 |
| Mix 3+4 (Master) | Sum of channels 3 and 4 |

---

## Atte

Quad attenuator/inverter with individual mode switches. Can attenuate or invert each channel. Polyphonic.

| Parameters | |
|-----------|---|
| Gain A–D | Level for each channel (0–100%) |
| Mode A–D | Attenuation or inverse attenuation per channel |

| Inputs | |
|--------|---|
| A, B, C, D | Signal inputs |

| Outputs | |
|---------|---|
| A, B, C, D | Processed outputs |

---

## AxBC

Two-channel voltage-controlled processor. Computes A×B+C with per-channel gain mode switches and a mix/multiply mode. Polyphonic.

| Parameters | |
|-----------|---|
| B1, C1 | Attenuverters for B and C on channel 1 |
| B2, C2 | Attenuverters for B and C on channel 2 |
| Gain Mode B1/C1/B2/C2 | ×−1, ×1, or ×2 scaling |
| Mix mode | Mix (A+B+C) or Multiply (A×B+C) |

| Inputs | |
|--------|---|
| A1, B1, C1 | Inputs for channel 1 |
| A2, B2, C2 | Inputs for channel 2 |

---

## Slew

Voltage-controlled lag processor with slope detection. Polyphonic.

| Parameters | |
|-----------|---|
| Shape | Curve shape of the slew |
| Range | Fast, Medium, or Slow speed range |
| Rise | Rise slew time |
| Fall | Fall slew time |
| CV Mode | CV affects Rise, Rise/Fall, or Fall only |

| Inputs | |
|--------|---|
| In | Signal to slew |
| CV | CV control for slew rate |

| Outputs | |
|---------|---|
| Out | Slewed output |
| Rising | Gate while input is rising |
| Falling | Gate while input is falling |

---

## MuDi

Clock multiplier, conditioner, and divider in 2HP.

| Inputs | |
|--------|---|
| Clock | Clock input |
| Reset | Reset all dividers |

| Outputs | |
|---------|---|
| F | Fundamental clock frequency |
| 1/2 F | Half the input clock |
| 1/4 F | Quarter clock |
| 1/8 F | Eighth clock |
| 1/16 F | Sixteenth clock |

---

## Iroi

Atmospheric processing module combining a resonator, echo, and ambience (reverb) section in one module.

| Parameters | |
|-----------|---|
| Filter Cutoff | Filter cutoff frequency |
| Resonator Tune | Resonator pitch |
| Modulation Level | Depth of internal modulation |
| Resonance | Filter resonance |
| Resonator Feedback | Feedback in the resonator path |
| Modulation Speed | Rate of internal modulation |
| Echo Density | Echo time and density |
| Ambience Spacetime | Room size and complexity |
| Echo Repeats | Number/decay of echo repeats |
| Ambience Decay | Reverb tail length |
| Filter VCA | VCA for the filter section |
| Resonator Dry/Wet | Mix for the resonator section |
| Echo Dry/Wet | Mix for the echo section |
| Ambience Dry/Wet | Mix for the ambience section |
| Map Mode | How the CV input maps: Random, CV, or Mod |

---

## Random8

Eight-channel random voltage generator with per-channel looping, probability, scale, and slide controls.

| Parameters (per channel) | |
|--------------------------|---|
| Gain | Output level |
| Divider | Clock division for this channel |
| Probability | Chance of generating a new value |
| Style | Random distribution style |
| Offset | Voltage offset added to output |
| Scale | Quantization scale for output values |
| Slide | Portamento/slew on output |
| Steps | Number of steps in the loop |

| Inputs | |
|--------|---|
| Trigger 1–8 | Per-channel trigger inputs |

| Outputs | |
|---------|---|
| Ch 1–8 | Random voltage outputs |

---

## Where to go next

- [Fundamental Modules](fundamental-modules.md) — the modules included with VCV Rack Free
- [How a Patch Works](kernablauf.md) — signal chain context
- [Patching Use Cases](anwendungsfaelle.md) — recipes using Befaco modules

---

*Version: 2026-06-17.*
