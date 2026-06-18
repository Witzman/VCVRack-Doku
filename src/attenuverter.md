# Attenuverter

An attenuverter scales a CV signal up or down (attenuation) and optionally flips it to negative (inversion). The word combines "attenuate" and "invert." Attenuverters are utility modules — they don't generate or transform sound, but they make modulation practical by letting you dial in exactly how much a modulator affects its target, and in which direction.

Without attenuverters, a signal going from an LFO to a filter might swing the cutoff across the entire frequency range when you only want a subtle movement. An attenuverter scales that swing down to a useful range. If you want the filter to close as the LFO rises rather than open, an attenuverter inverts the signal.

## 8vert (VCV Free)

8vert provides eight independent attenuverter channels. Each channel has an input, a knob ranging from -1 to +1, and an output. At +1, the signal passes unchanged. At 0, the output is zero. At -1, the signal is inverted. Values between these points scale and optionally flip the signal.

| Parameter | Range | What it does |
|-----------|-------|--------------|
| Knob (×8) | -1 to +1 | Scale factor and inversion for that channel |

| Input/Output | Type | Description |
|-------------|------|-------------|
| IN 1–8 | Input | Signal to scale (if unpatched, uses +10V) |
| OUT 1–8 | Output | Scaled signal |

**Patching tips:** If a channel's input is unpatched, it defaults to +10V — so the output is the knob position × 10V. This makes 8vert useful as a manual CV source: an unpatched channel with the knob at +0.5 outputs +5V. Patch several LFOs to 8vert inputs and tune each knob to set the modulation depth for different destinations. Use negative knob values when you want the modulator to move a parameter in the opposite direction.

## Bogaudio OFFSET (Bogaudio)

Adds a fixed offset to a CV signal — shifts the entire voltage range up or down without scaling. Useful when a modulator or sequencer outputs voltages in the wrong range for your target. For example, an envelope that outputs 0–10V can be shifted down by 5V to produce a -5V to +5V range.

**Patching tips:** After an S&H random output, add an OFFSET to bias random voltages into a higher or lower range before sending to a quantizer. This shifts which octave or register the random pitches land in.

### VCV Free 8vert as CV source

With no inputs patched, 8vert's eight knobs become eight independent manual CV sources. Set knob positions for fixed offsets, pitch CV values, or modulation biases. This is a free way to create up to eight manually-tuned control voltages without dedicated offset or CV source modules.

### Bogaudio Attenuvert (Bogaudio)

A single-channel attenuverter with a cleaner panel layout than individual 8vert channels. Use when you need one attenuverter in a specific part of the signal path and don't want to use a full 8vert module for a single channel.

### Count Modula Attenuverter (Count Modula)

A four-channel attenuverter with per-channel knobs. Fits naturally into Count Modula-heavy patches and offers the same functionality as 8vert for four channels.

### AS Attenuator (AS)

A simple attenuator — scaling only, no inversion. Use when you need to scale a signal down but never need negative values. Takes up less mental overhead than a full attenuverter when inversion isn't required.

## Where to go next

- [LFO](lfo.md) — attenuate LFO outputs before patching to destinations
- [Mixer](mixer.md) — mix multiple attenuated CV signals
- [VCF](vcf.md) — scale envelope or LFO depth into filter CV input
- [Envelopes](envelope.md) — scale envelope output for modulation depth control

---
*Version: 2026-06-17.*
