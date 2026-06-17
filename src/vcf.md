# VCF — Voltage Controlled Filter

A VCF removes frequencies from an audio signal based on a cutoff point set by a knob or CV. It is the primary tonal shaping tool in subtractive synthesis: start with a harmonically rich source (a saw or square wave), then sculpt the brightness with the filter. The most common type is a low-pass filter, which lets frequencies below the cutoff through and attenuates those above it. Resonance adds a peak at the cutoff frequency, producing the characteristic sweeping "wah" character.

## VCF (Fundamental)

The VCF bundled with Rack Free is a state-variable filter with simultaneous low-pass, high-pass, and band-pass outputs. It covers the core subtractive synthesis use cases and responds well to CV modulation.

| Parameter | Range | What it does |
|-----------|-------|--------------|
| FREQ | 20 Hz – 20 kHz | Cutoff frequency |
| RES | 0–1 | Resonance — peak at cutoff |
| FREQ CV | ±1 | Amount of CV applied to cutoff |
| DRIVE | 0–1 | Input gain — adds saturation at high amounts |

| Input/Output | Type | Description |
|-------------|------|-------------|
| IN | Input | Audio signal to filter |
| FREQ | Input | CV modulates cutoff frequency |
| RES | Input | CV modulates resonance |
| LP, BP, HP | Output | Low-pass, band-pass, high-pass outputs |

**Patching tips:** For a classic synth sweep, connect an ADSR envelope to the FREQ CV input and set FREQ CV amount to taste. The LP output handles most bread-and-butter sounds. Use BP for nasal, mid-forward tones. Patch HP through a second VCF to create a band-pass with independently adjustable slopes. At high RES with low FREQ, the filter self-oscillates and produces a pure sine tone — useful as a secondary sound source.

## Vult Freak (Vult — free tier)

Freak is a zero-delay-feedback filter based on several classic hardware filter topologies. The model can be switched between Ladder (Moog-style), Steiner-Parker, and others. Each topology has a distinctly different character. The free tier of Vult includes Freak.

| Parameter | Description |
|-----------|-------------|
| FREQ | Cutoff frequency |
| RES | Resonance |
| TYPE | Filter topology (Ladder, Steiner, etc.) |
| IN GAIN | Input level |

**Patching tips:** The Ladder mode has the warm, bouncy resonance of classic Moog-style filters. Switch to Steiner for a more aggressive, electronic character. At high resonance, all modes self-oscillate — detune against another oscillator for beating textures.

## Surge XT Filters (Surge XT)

Surge XT provides multiple filter modules including LP/HP/BP variations of Ladder, Comb, and other algorithms. The Comb filter in particular is not commonly available in free plugins — it creates flanging, chorusing, and metallic resonance effects by adding a delayed copy of the signal to itself.

| Notable filter types | Character |
|---------------------|-----------|
| LP Ladder | Warm, musical, self-oscillates |
| Comb | Flanging, metallic, chorus-like |
| OB-Xd style | Bright, snappy, less warm than Ladder |
| Cutoff | All types share standard FREQ + RES controls |

**Patching tips:** Use the Comb filter on a noise source with a short delay time for metallic percussion sounds. Modulate comb delay time slowly for a sweeping flanger effect without needing a dedicated flanger module.

### Bogaudio LMHR (Bogaudio)

A four-output state-variable filter (LP, HP, BP, notch) with a clean, accurate response. Good for precise frequency sculpting when the Fundamental VCF's DRIVE character isn't wanted.

### Count Modula Filter (Count Modula)

Count Modula includes a multi-mode filter consistent with their other modules. Useful in Count Modula-heavy patches. Offers standard LP/HP/BP modes with CV inputs.

### Befaco Rampage as filter

Rampage is technically an envelope/function generator, but its slew inputs can behave as a first-order low-pass filter at audio rates when used creatively. Not a typical filter use, but worth knowing.

## Where to go next

- [VCO](vco.md) — the audio source you're filtering
- [VCA](vca.md) — volume shaping after the filter
- [Envelopes](envelope.md) — automate filter cutoff sweeps
- [LFO](lfo.md) — rhythmic filter modulation
- [How a Patch Works](how-a-patch-works.md) — VCF's place in the signal chain

---
*Version: 2026-06-17.*
