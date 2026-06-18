# Noise

Noise modules generate random, unpitched signals across a range of frequencies. In a patch, noise serves several roles: it can be a sound source for percussion and wind textures, a randomness source for CV modulation, or a component layered with a VCO to add grit and breathiness. Noise is always present in the signal path of electronic percussion and is one of the most versatile raw materials in modular synthesis.

## Noise (VCV Free)

The Noise module bundled with VCV Rack Free outputs five simultaneous noise colors, each with a different frequency distribution. No parameters — just outputs.

| Output | Character | Use case |
|--------|-----------|----------|
| White | Equal energy per frequency | Snare body, general texture |
| Pink | Equal energy per octave (-3dB/oct) | Natural-sounding ambience |
| Red | Heavy low-frequency emphasis (-6dB/oct) | Sub rumble, wind |
| Blue | High-frequency emphasis | Bright hiss, air |
| Violet | Very high-frequency emphasis | Extreme brightness, sizzle |

**Patching tips:** For a snare drum, mix the White output with a short VCA burst. Run Pink through a slow VCF sweep for a breathing pad texture. Feed any color through a sample-and-hold to create random stepped CV for modulation.

## Bogaudio NOISE (Bogaudio)

Bogaudio's NOISE module outputs white noise and also provides a separate SMOOTH output — a low-pass filtered version of white noise that produces slowly drifting random voltages. This makes it a combined noise + random CV source in a single module.

| Output | Description |
|--------|-------------|
| NOISE | White noise signal |
| SMOOTH | Filtered noise — slow random drift |

The SMOOTH output is particularly useful for organic modulation: patch it to filter cutoff or oscillator fine tune for a subtle, constantly-evolving texture without needing a dedicated S&H module.

**Patching tips:** Use the SMOOTH output as a lazy modulator — slower than most LFOs and more organic-feeling. The rate of drift is fixed, but attenuating it controls depth.

### Count Modula Noise (Count Modula)

Count Modula includes a noise source with white and pink outputs alongside a slew-limited random output similar to Bogaudio's SMOOTH. Useful in Count Modula-heavy patches to avoid switching between plugin namespaces.

### Valley Dexter / Topograph noise layer

Valley's Topograph drum module generates noise-based percussion internally. If you need noise as part of a drum voice rather than a standalone source, Topograph is worth examining — it combines noise generation with rhythmic triggering.

### ML Modules Noise (ML Modules)

ML Modules provides a noise source alongside other utilities in their free pack. Outputs white noise; useful as a compact addition when you need a noise source without taking up a full Bogaudio or VCV Free slot.

## Where to go next

- [VCF](vcf.md) — filter noise into tonal textures
- [VCA](vca.md) — shape noise bursts into percussion hits
- [Sample & Hold](sample-hold.md) — turn noise into random stepped CV
- [Envelopes](envelope.md) — trigger short noise bursts for snare and hi-hat
- [Patching Use Cases](patching-use-cases.md) — percussion patch recipes

---
*Version: 2026-06-17.*
