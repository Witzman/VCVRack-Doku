# Envelopes

An envelope generates a shaped CV signal in response to a gate or trigger. When a note starts (gate goes high), the envelope rises and falls through a predefined contour; when the note ends (gate goes low), it releases. Envelopes are used primarily to control VCA volume and VCF cutoff, but they can modulate anything that accepts a CV input. The most common shape is ADSR: Attack, Decay, Sustain, Release.

## ADSR EG (VCV Free)

The VCV Free ADSR EG is the standard envelope module included with Rack Free. It generates an ADSR contour in response to a gate signal and outputs both a positive (ENV) and inverted (INV) version.

| Parameter | Range | What it does |
|-----------|-------|--------------|
| ATTACK | 1ms – 10s | Time to rise from 0 to peak when gate opens |
| DECAY | 1ms – 10s | Time to fall from peak to sustain level |
| SUSTAIN | 0–1 | Level held while gate remains open |
| RELEASE | 1ms – 10s | Time to fall from sustain to 0 after gate closes |

| Input/Output | Type | Description |
|-------------|------|-------------|
| GATE | Input | Gate signal — high = note on, low = note off |
| TRIG | Input | Retrigger envelope without retriggering gate |
| ENV | Output | Envelope CV (0–10V) |
| INV | Output | Inverted envelope (10V – ENV) |

**Patching tips:** For a plucky sound: fast ATTACK (near minimum), medium DECAY (100–300ms), SUSTAIN at zero, and short RELEASE. For a pad: slow ATTACK (1–3s), no DECAY, full SUSTAIN, slow RELEASE (2–5s). Use the INV output to close a filter as the amplitude opens — this creates a tone that gets darker as it gets louder, useful for plucked string simulations. Patch the ENV output to both VCA and VCF for coordinated amplitude and tonal shaping.

## Befaco Rampage (Befaco)

Rampage is a dual function generator — each channel can act as an envelope, LFO, slew limiter, or oscillator depending on how it is patched. As an envelope, it produces a customizable rise/fall contour with adjustable response curves (log, linear, exponential). Unlike ADSR, Rampage does not have a sustain stage: it rises when triggered and falls when the trigger ends or after a set time.

| Parameter | Description |
|-----------|-------------|
| RISE | Attack time |
| FALL | Release time |
| SHAPE | Curve shape (log → linear → exp) |
| CYCLE | When active, loops the envelope as an LFO |

**Patching tips:** The SHAPE knob's ability to change curve type is its key advantage over ADSR — exponential curves feel more natural for amplitude; logarithmic curves feel faster. Use CYCLE to turn Rampage into an LFO without patching a separate module. The two channels have a logical comparator output useful for rhythmic triggering — see the [Logic](logic.md) page.

## Bogaudio ADSR (Bogaudio)

Bogaudio's ADSR adds a linear/exponential mode switch and separate CV inputs for all four parameters. This allows all stages to be modulated in real time — you can sweep attack time with an LFO or modulate sustain level from a sequencer.

| Input | Description |
|-------|-------------|
| GATE | Gate signal |
| A, D, S, R CV | Per-parameter modulation inputs |

**Patching tips:** Patch a slow random S&H signal to the ATTACK CV input to give each note a slightly different attack time — the variation adds organic feel to repeated notes.

### Count Modula ADSR (Count Modula)

Count Modula's envelope includes all standard ADSR controls with a retrigger mode and optional looping. Consistent with their other sequencer modules — useful in Count Modula-heavy patches.

### ML Modules ADSR (ML Modules)

A clean, minimal ADSR with standard parameters. Good starting point for simple patches where no per-parameter CV modulation is needed.

### Befaco ADSR (Befaco)

A compact ADSR from Befaco, smaller than VCV Free's. Behaves similarly to VCV Free ADSR EG with the addition of a VEL input for velocity-sensitive amplitude scaling.

## Where to go next

- [VCA](vca.md) — the most common envelope destination
- [VCF](vcf.md) — envelope-driven filter sweeps
- [LFO](lfo.md) — continuous modulation vs. triggered envelopes
- [How a Patch Works](how-a-patch-works.md) — envelope's role in a complete voice

---
*Version: 2026-06-17.*
