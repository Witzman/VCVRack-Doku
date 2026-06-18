# Waveshaper & Distortion

Waveshapers and distortion modules transform the shape of an audio waveform, adding harmonic content and changing timbre. Unlike a filter, which removes frequencies, distortion adds new ones that weren't in the original signal. At low amounts, distortion produces warmth and analog grit. At high amounts, it creates aggressive, buzzing, or chaotic textures. Waveshapers apply a mathematical function to the waveform — bending, clipping, or folding it — while traditional distortion typically means hard or soft clipping.

## Befaco Crush Delay (Befaco)

Despite the name "delay," Crush Delay is primarily a bit-crusher and sample-rate reducer with a feedback delay. The bit-crush section reduces bit depth for digital distortion, while the sample-rate section creates aliasing artifacts. These are classic lo-fi and industrial textures.

| Parameter | Description |
|-----------|-------------|
| CRUSH | Bit depth reduction |
| FREQ | Sample rate reduction |
| TIME | Delay time |
| FEEDBACK | Delay feedback amount |
| MIX | Wet/dry blend |

**Patching tips:** Apply to a drum bus for gritty, compressed electronic percussion. Use at low CRUSH amounts for subtle analog-feeling warmth. Full CRUSH with high FEEDBACK produces chaotic, self-oscillating noise — use a VCA to gate it.

## Squinky Labs Stairway (Squinky Labs)

A wavefolder combined with a soft-clipper. A wavefolder "folds" the waveform back on itself when it exceeds a threshold, creating new harmonics at a rate proportional to how far past the threshold the signal goes. Feeding a sine wave through a wavefolder with a slow amplitude modulator produces complex, evolving timbres.

| Parameter | Description |
|-----------|-------------|
| FOLD | Fold amount — how aggressively the waveform folds |
| GAIN | Input level before folding |

**Patching tips:** Start with a sine wave input for the cleanest fold behavior. Modulate FOLD with an LFO to get the waveform morphing in real time. Stacking two wavefolders in series produces increasingly complex harmonic content.

## Bogaudio SHAPER (Bogaudio)

A waveshaper with multiple transfer function modes: overdrive, clip, fold, and others. Each mode applies a different mathematical transformation to the waveform shape. The module is clean and predictable, making it suitable for precise harmonic addition rather than rough distortion.

| Parameter | Description |
|-----------|-------------|
| SHAPE | Amount of waveshaping applied |
| MODE | Transfer function type |

**Patching tips:** Use SHAPE at low amounts with the overdrive mode on a pad to add harmonic warmth without obvious distortion. Sweep SHAPE with an envelope for a distortion that opens up on transients.

### VCV Free VCF DRIVE

The VCV Free VCF has a built-in DRIVE parameter that applies soft saturation before filtering. It is not a standalone waveshaper, but at higher settings it adds audible harmonic distortion to the filtered signal. This is the simplest way to add warmth without adding an extra module.

### AS WaveFolder (AS)

AS provides a free wavefolder module that applies the classic folder algorithm. Simple interface — one knob, audio in, audio out. Good starting point for experimenting with wavefolding before exploring more complex modules.

### Count Modula Saturator (Count Modula)

Count Modula's saturator applies tape-style soft saturation. Useful on busses and individual voices to add analog glue without obvious distortion. Works well on drum groups and bass voices.

## Where to go next

- [VCO](vco.md) — the source signal to distort
- [VCF](vcf.md) — filter the harmonics added by distortion
- [Delay, Reverb & Chorus](delay-reverb-chorus.md) — add space after distortion
- [Patching Use Cases](patching-use-cases.md) — distortion in context

---
*Version: 2026-06-17.*
