# VCA — Voltage Controlled Amplifier

A VCA controls the volume of a signal using a CV input. Without a VCA, a sound plays continuously at full volume the moment you connect the oscillator to the output — there is no way to start or stop individual notes. By patching an envelope into the VCA's CV input, you give each note a defined attack, sustain, and release. Every voice in a polyphonic patch needs at least one VCA; effects sends and mixer levels often use additional VCAs for dynamic control.

## VCA-1 (VCV Free)

The VCV Free VCA-1 is a clean, straightforward single-channel amplifier. It applies a CV-controlled gain to one signal and has a single CV input (linear response by default, switchable to exponential in the right-click menu).

| Parameter | Range | What it does |
|-----------|-------|--------------|
| LEVEL | 0–100% | Manual gain — multiplies the CV-controlled gain (default 100% = unity) |

| Input/Output | Type | Description |
|-------------|------|-------------|
| CV | Input | Gain control voltage |
| Channel | Input | Audio or CV signal to amplify |
| Channel | Output | Amplified signal |

**Patching tips:** For a basic voice, connect your ADSR's ENV output to the VCA-1's CV input and your filtered oscillator to the Channel input. The LEVEL knob scales the CV-controlled gain — keep it at maximum (its default) so the envelope sets the full dynamics, and lower it only to reduce overall output. For a tremolo effect, replace the envelope with a slow LFO patched to CV.

## VCA-2 (VCV Free)

The dual-channel VCA. It has two independent VCA channels, and each channel provides both an exponential CV input and a linear CV input. The exponential response better matches how humans perceive loudness; the linear input is useful for modulation routing where proportional precision matters. Use this when you need two amplifiers in one module or want both CV response curves available.

| Input/Output | Type | Description |
|-------------|------|-------------|
| Channel 1 exponential CV | Input | Exponential gain CV for channel 1 |
| Channel 1 linear CV | Input | Linear gain CV for channel 1 |
| Channel 1 | Input | Signal to amplify (channel 1) |
| Channel 1 | Output | Amplified signal (channel 1) |

Channel 2 follows the same pattern with its own set of ports.

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
