# Envelopes

An envelope generates a shaped CV signal in response to a gate or trigger. When a note starts (gate goes high), the envelope rises and falls through a predefined contour; when the note ends (gate goes low), it releases. Envelopes are used primarily to control VCA volume and VCF cutoff, but they can modulate anything that accepts a CV input. The most common shape is ADSR: Attack, Decay, Sustain, Release.

## ADSR EG (VCV Free)

The VCV Free ADSR EG is the standard envelope module included with Rack Free. It generates an ADSR contour in response to a gate signal and outputs it on a single Envelope (ENV) output.

| Parameter | Range | What it does |
|-----------|-------|--------------|
| ATTACK | 1ms – 10s | Time to rise from 0 to peak when gate opens |
| DECAY | 1ms – 10s | Time to fall from peak to sustain level |
| SUSTAIN | 0–100% | Level held while gate remains open |
| RELEASE | 1ms – 10s | Time to fall from sustain to 0 after gate closes |

| Input/Output | Type | Description |
|-------------|------|-------------|
| GATE | Input | Gate signal — high = note on, low = note off |
| TRIG | Input | Retrigger envelope without retriggering gate |
| ENV | Output | Envelope CV (0–10V) |

**Patching tips:** For a plucky sound: fast ATTACK (near minimum), medium DECAY (100–300ms), SUSTAIN at zero, and short RELEASE. For a pad: slow ATTACK (1–3s), no DECAY, full SUSTAIN, slow RELEASE (2–5s). To close a filter as the amplitude opens, route the ENV output through an attenuverter (such as 8vert at a negative setting) into the VCF cutoff CV — this creates a tone that gets darker as it gets louder, useful for plucked string simulations. Patch the ENV output to both VCA and VCF for coordinated amplitude and tonal shaping.

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

Bogaudio's ADSR adds a linear/exponential mode switch. Its attack, decay and release knobs display in seconds (sustain in percent), and it triggers from a single Gate input.

| Input | Description |
|-------|-------------|
| GATE | Gate signal — the only input |

**Patching tips:** Use the linear/exponential switch to tailor the envelope feel — exponential curves sound more natural for amplitude. Bogaudio's ADSR has no per-parameter CV inputs; to modulate a stage over time, automate the knob with another module or choose an envelope that exposes A/D/S/R CV (e.g. the VCV ADSR EG or Befaco ADSR).

### Count Modula ADSR (Count Modula)

Count Modula's envelope includes all standard ADSR controls with a retrigger mode and optional looping. Consistent with their other sequencer modules — useful in Count Modula-heavy patches.

### ML Modules ADSR (ML Modules)

A clean, minimal ADSR with standard parameters. Good starting point for simple patches where no per-parameter CV modulation is needed.

### Befaco ADSR (Befaco)

A compact ADSR from Befaco, smaller than VCV Free's. Behaves similarly to the VCV Free ADSR EG, with a trigger input and per-stage CV inputs (Attack, Decay, Sustain, Release CV). It has no dedicated velocity input — for velocity-sensitive amplitude, route a velocity CV to the VCA alongside the envelope.

## Where to go next

- [VCA](vca.md) — the most common envelope destination
- [VCF](vcf.md) — envelope-driven filter sweeps
- [LFO](lfo.md) — continuous modulation vs. triggered envelopes
- [How a Patch Works](how-a-patch-works.md) — envelope's role in a complete voice

---
*Version: 2026-06-17.*
