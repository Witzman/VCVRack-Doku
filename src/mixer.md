# Mixer

A mixer combines multiple audio signals into one output, with individual level control for each channel. In a modular patch, mixers appear at several points: combining multiple oscillator waveforms, summing voices before a shared filter, blending dry and wet signals in an effects send, and at the final stage before the audio output. CV signals can also be mixed to combine multiple modulation sources.

## Mixer (Fundamental)

The Fundamental Mixer has four mono input channels each with a LEVEL knob, and two outputs: a mono sum and a stereo sum (channels 1-2 panned left, channels 3-4 panned right). Simple and immediately useful.

| Parameter | Description |
|-----------|-------------|
| CH1–CH4 LEVEL | Per-channel volume |

| Input/Output | Type | Description |
|-------------|------|-------------|
| CH1–CH4 | Input | Four mono audio inputs |
| MIX | Output | Mono summed output |
| L / R | Output | Stereo output with fixed pan positions |

**Patching tips:** The stereo output places channels 1-2 left and 3-4 right — put your bass and lead on 1-2 so they appear center, and pads on 3-4 for width. For a send effect, take the MIX output to your reverb input, then mix the reverb return with the dry signal in a second mixer channel.

## VCMixer (Fundamental)

An extended mixer with CV-controllable channel levels. Each channel has both a LEVEL knob and a CV input that scales the knob value. This allows dynamic volume control per channel — useful for automated fade-ins, envelope-shaped channel levels, or LFO-driven volume animation.

| Input | Description |
|-------|-------------|
| CV 1–4 | Per-channel volume CV — multiplies the knob value |

**Patching tips:** Patch an envelope to a channel's CV input to make that voice fade in from silence each time a note triggers. Use an LFO on a pad channel's CV for a slow tremolo on just that voice while other channels remain steady.

## Bogaudio Mixer (Bogaudio)

Bogaudio provides a more comprehensive mixer with stereo channels, per-channel pan controls, mute buttons, and optional solo. This is a better choice than Fundamental's mixer for patches with four or more voices that need proper stereo placement.

| Feature | Description |
|---------|-------------|
| Stereo channels | Each channel accepts L+R or mono-summed input |
| PAN | Per-channel stereo position |
| MUTE | Silence individual channels without disconnecting cables |
| CV inputs | Optional CV on level and pan |

**Patching tips:** Use pan CV inputs to automate stereo movement — a slow triangle LFO on pan produces a gradual side-to-side sweep (autopan effect). Mute buttons let you quickly A/B voices during patch building.

### CVMix (Fundamental)

A four-input CV mixer without audio features. Use this to combine multiple modulation sources — for example, summing an LFO and an envelope to create a compound modulation curve that is both rhythmically pulsing and shaped over time.

### 8vert (Fundamental)

Eight attenuverters that can function as a simple eight-input mixer when their outputs are connected to a multi-input module. See [Attenuverter](attenuverter.md) for full details.

### Befaco STMix (Befaco)

A four-channel stereo mixer with individual level controls and a simple, compact layout. The stereo capability makes it a good choice for mixing stereo effects returns. Each channel accepts a stereo input pair.

### Befaco HexmixVCA (Befaco)

Six VCA channels with individual CV inputs, functioning as a mixer with dynamic level control per channel. When you need both mixing and per-channel amplitude envelope control without wiring separate VCA and mixer modules.

## Where to go next

- [VCA](vca.md) — per-voice volume control before the mixer
- [Delay, Reverb & Chorus](delay-reverb-chorus.md) — effects send/return through a mixer
- [Audio Output](audio-output.md) — the final destination after mixing
- [Attenuverter](attenuverter.md) — scale signals before mixing

---
*Version: 2026-06-17.*
