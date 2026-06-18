# VCA — Voltage Controlled Amplifier

A VCA controls the volume of a signal using a CV input. Without a VCA, a sound plays continuously at full volume the moment you connect the oscillator to the output — there is no way to start or stop individual notes. By patching an envelope into the VCA's CV input, you give each note a defined attack, sustain, and release. Every voice in a polyphonic patch needs at least one VCA; effects sends and mixer levels often use additional VCAs for dynamic control.

## VCA (VCV Free)

The VCV Free VCA is a clean, straightforward amplifier. It has two inputs — linear and exponential response — and applies a CV-controlled gain. The exponential mode better matches how humans perceive loudness; the linear mode is useful for modulation routing where mathematical precision matters.

| Parameter | Range | What it does |
|-----------|-------|--------------|
| LEVEL | 0–2 | Manual gain offset added to CV |

| Input/Output | Type | Description |
|-------------|------|-------------|
| IN | Input | Audio or CV signal to amplify |
| CV | Input | Gain control voltage |
| OUT | Output | Amplified signal |

There are two VCA channels on the module. The second channel follows the same pattern.

**Patching tips:** For a basic voice, connect your ADSR's ENV output to the VCA's CV input and your filtered oscillator to IN. The LEVEL knob acts as a manual volume offset — leave it at 0 if your envelope reaches full amplitude on its own. For a tremolo effect, replace the envelope with a slow LFO patched to CV. Use the linear input for modulation routing where you want predictable, proportional response.

## VCA-2 (VCV Free)

A simpler single-channel VCA with only one input and exponential response. Use this when you just need a basic gated amplifier and don't need the two-channel or linear mode features of the main VCA.

## Bogaudio VCA (Bogaudio)

Bogaudio's VCA offers linear and exponential modes with a dedicated level knob that sets the maximum gain independently of the CV. This makes it easy to set a ceiling on how loud the sound gets regardless of the incoming CV level — useful when controlling volume from an LFO or other non-standard modulator.

| Parameter | Description |
|-----------|-------------|
| LEVEL | Maximum gain (scaled by CV) |
| LIN/EXP | Response mode switch |

**Patching tips:** Set LEVEL to a comfortable maximum and let CV control the dynamics within that range. Patch a random S&H into CV for stochastic volume variation.

### 8vert (VCV Free)

Eight attenuverters — modules that scale and optionally invert a signal. When a VCA input is already at a fixed level, 8vert lets you scale the modulator before it reaches the VCA rather than turning down the VCA's CV input. See [Attenuverter](attenuverter.md) for full details.

### Befaco HexmixVCA (Befaco)

Six VCAs in a single module, each with independent level CV. Designed for mixing multiple voices with individual dynamic control — useful for complex patches where a standard mixer without CV control isn't enough.

### Count Modula VCA (Count Modula)

Count Modula provides VCA modules with both linear and exponential response. Their modules are well-suited for integration with Count Modula sequencers and utility modules.

## Where to go next

- [Envelopes](envelope.md) — the CV source that drives VCA dynamics
- [VCF](vcf.md) — filtering before the VCA
- [Mixer](mixer.md) — combining multiple VCA outputs
- [LFO](lfo.md) — use an LFO as a tremolo VCA modulator
- [How a Patch Works](how-a-patch-works.md) — VCA's role in the signal chain

---
*Version: 2026-06-17.*
