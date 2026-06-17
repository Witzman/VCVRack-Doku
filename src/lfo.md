# LFO — Low Frequency Oscillator

An LFO is an oscillator running below audio rate — typically between 0.01 Hz and 20 Hz — whose output is used as a CV modulator rather than a sound source. LFOs add movement, variation, and life to otherwise static patches. A slow sine LFO on filter cutoff produces a gradual sweep; a faster triangle on oscillator pitch produces vibrato; a square wave into a VCA produces tremolo. Almost any parameter that accepts CV can be animated with an LFO.

## LFO (Fundamental)

The Fundamental LFO provides simultaneous sine, triangle, sawtooth, reverse sawtooth, and square wave outputs. It can sync to an external clock and has a reset input for phase-locking.

| Parameter | Range | What it does |
|-----------|-------|--------------|
| FREQ | 0.001 – 20 Hz | LFO speed |
| WAVE knob | selector | Selects which waveform is used for the INTERP output |

| Input/Output | Type | Description |
|-------------|------|-------------|
| FREQ CV | Input | CV control over speed |
| RESET | Input | Resets LFO phase to start |
| SIN, TRI, SAW, INV SAW, SQR | Output | Individual waveform outputs |

**Patching tips:** For vibrato, patch the SIN output through an [Attenuverter](attenuverter.md) to VCO FM — keep the depth small (a few semitones maximum). For filter animation, patch SIN or TRI to VCF FREQ CV. For rhythmic tremolo, use SQR at a musically related frequency and patch to VCA CV. Extremely slow LFOs (0.01–0.1 Hz) are essential for psybient and ambient patches — they provide gradual change that feels like the patch is "breathing" rather than obviously moving.

## WTLFO (Fundamental)

The WTLFO uses the same wavetable engine as the WTVCO oscillator but runs at LFO rates. You can select a wavetable bank and modulate position to produce unusual, non-standard modulation shapes — morphing between waveforms rather than switching between fixed ones. Useful when a standard sine or triangle doesn't produce the modulation character you want.

| Parameter | Description |
|-----------|-------------|
| FREQ | LFO rate |
| POS | Wavetable position |
| BANK | Wavetable bank selection |

**Patching tips:** Modulate POS itself with a second very slow LFO to produce a modulator that continuously changes its shape — this gives each cycle a slightly different character, useful for organic, non-repeating textures.

## Bogaudio LFO (Bogaudio)

A full-featured LFO with smooth knob interpolation, a dedicated slow range mode, and both unipolar (0 to +10V) and bipolar (-5V to +5V) outputs. The slow range mode extends down to fractions of a Hz — useful for very gradual changes over minutes rather than seconds.

| Parameter | Description |
|-----------|-------------|
| FREQ | Rate — with dedicated slow range toggle |
| WAVE | Waveform selection |
| OFFSET | Shifts output up or down (bias) |
| SCALE | Attenuates output |

**Patching tips:** Use the slow range for ambient patches where you want very gradual change. Use OFFSET to shift a bipolar LFO to unipolar (all positive) for modulating parameters that don't accept negative CV well.

### Count Modula Quad LFO (Count Modula)

Four LFOs in one module with phase offset control between them. Patching the four outputs to four different parameters at the same frequency but different phases creates an evolving, cycling modulation system without needing four separate LFO modules.

### Squinky Labs Shaper (Squinky Labs)

Produces shaped, step-like LFO curves rather than smooth waveforms. Useful for rhythmic or gate-like modulation that follows a defined envelope shape rather than a continuous oscillation.

### ML Modules LFO (ML Modules)

A clean, minimal LFO. Covers sine, triangle, sawtooth, and square waveforms with a simple interface. Good starting point for basic modulation needs.

### Befaco Rampage as LFO

When the CYCLE switch is engaged on Befaco Rampage, it loops its rise/fall contour continuously as an LFO. The SHAPE knob changes the curve type, allowing log, linear, and exponential slopes — shapes that Fundamental LFO's standard waveforms don't offer. See [Envelopes](envelope.md) for Rampage details.

## Where to go next

- [VCF](vcf.md) — LFO to filter cutoff for filter sweeps
- [VCO](vco.md) — LFO to FM for vibrato
- [VCA](vca.md) — LFO to CV for tremolo
- [Sample & Hold](sample-hold.md) — LFO as a stepped random source
- [Slow Psybient](slow-psybient.md) — multiple ultra-slow LFOs in a psybient patch

---
*Version: 2026-06-17.*
