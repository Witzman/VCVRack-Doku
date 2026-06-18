# VCO — Voltage Controlled Oscillator

A VCO is the sound source of your patch. It generates a continuous waveform at a pitch set by an incoming CV signal. Without a VCO (or another sound source), there is nothing to filter, shape, or amplify. Most patches start here. The standard pitch control format is V/Oct: one volt per octave, so middle C is typically 0V and the C one octave up is 1V.

## VCO (VCV Free)

The VCO is the oscillator bundled with every VCV Rack installation. It covers the full range of classic subtractive synthesis waveforms and accepts V/Oct pitch CV, FM, and pulse width modulation.

| Parameter | Range | What it does |
|-----------|-------|--------------|
| FREQ | ±5 octaves | Coarse pitch offset from center |
| FINE | ±1 semitone | Fine-tune for exact pitch |
| PW | 0–100% | Pulse width of the square wave |
| FM | ±1 | Amount of FM applied from the FM input |

| Input/Output | Type | Description |
|-------------|------|-------------|
| V/OCT | Input | Pitch CV — 1V per octave |
| FM | Input | Frequency modulation CV |
| SYNC | Input | Hard sync — resets waveform phase |
| SIN, TRI, SAW, SQR | Output | Individual waveform outputs |

**Patching tips:** Connect a MIDI to CV module's V/OCT output to VCO's V/OCT input to play it from a keyboard. Use the SAW output for a classic subtractive synth sound. Patch the SQR output with PW modulated by a slow LFO for animated pulse-width modulation. For thick unison, run two VCO instances slightly detuned using the FINE knob and mix their outputs.

## EvenVCO (Befaco)

The EvenVCO is a clean, low-aliasing oscillator based on the Befaco hardware module. It produces even harmonics alongside its main waveforms, giving it a warmer, more analog character than a mathematically pure oscillator.

| Parameter | Range | What it does |
|-----------|-------|--------------|
| TUNE | ±4 octaves | Coarse pitch |
| Octave switch | -2 to +2 | Octave transpose |

| Input/Output | Type | Description |
|-------------|------|-------------|
| V/OCT | Input | Pitch CV |
| PWM | Input | Pulse width modulation |
| Even | Output | Even-harmonic enriched output |
| Sine, Triangle, Saw, Pulse | Output | Standard waveforms |

**Patching tips:** The Even output has a distinctly warm character — useful as a second layer under a brighter saw. Use the Octave switch to quickly transpose without touching the TUNE knob.

## Bogaudio VCO (Bogaudio)

A full-featured oscillator with linear and exponential FM, soft sync, and a built-in sub-oscillator one octave down. Good choice when you need FM capability or a thicker sound without adding a second module.

| Parameter | Range | What it does |
|-----------|-------|--------------|
| FREQ | wide range | Coarse pitch |
| FINE | ±1 semitone | Fine pitch |
| FM depth | ±1 | Linear or exponential FM amount |

Sub output provides a sine wave one octave below the main pitch — useful for adding low-end weight to a bass patch without a second oscillator.

**Patching tips:** Use linear FM for cleaner FM tones; exponential FM tracks pitch better for musical intervals but can get harsh at high amounts.

### Surge XT VCO (Surge XT)

Surge XT provides a library of oscillator algorithms: Classic (virtual analog), Modern (anti-aliased), Wavetable, Window, FM2, FM3, String, Twist, and more. Each algorithm has its own set of parameters. The plugin is free and dramatically expands sound design range beyond standard waveforms. Find it in the VCV Library under "Surge XT."

### Wavetable VCO (VCV Free)

The Wavetable VCO is the wavetable oscillator included with VCV Free. It reads through a built-in wavetable bank and can be position-modulated by CV. More detail on the dedicated [Wavetable](wavetable.md) page.

### VCO 2 (VCV Free)

A simpler oscillator with fewer outputs but a morphing waveform knob that crossfades continuously between sine, triangle, sawtooth, and square. Useful when you want a single output with variable timbre rather than separate waveform outs.

### Vult Vco (Vult — free tier)

Vult's free oscillators include models with analog drift simulation. Their oscillators are known for subtle pitch and waveform instability that mimics hardware VCOs well.

### Squinky Labs EV3 (Squinky Labs)

Three oscillators in one module. Each has independent V/OCT, pitch offset, and waveform selection. Efficient for building thick, detuned unison sounds without wiring three separate modules.

## Where to go next

- [Signal Flow & Concepts](mental-model.md) — how oscillator outputs flow through a patch
- [VCF](vcf.md) — filter the oscillator output
- [VCA](vca.md) — shape the volume with an envelope
- [Wavetable](wavetable.md) — wavetable oscillators in detail
- [How a Patch Works](how-a-patch-works.md) — see the VCO's role in a complete voice

---
*Version: 2026-06-17.*
