# Delay, Reverb & Chorus

Effects modules add space, depth, and movement to sounds. They are almost always used as send effects: the dry signal passes through your main voice chain, and a copy is sent to the effect module, with the wet output mixed back in at a lower level. This lets you adjust the dry/wet balance freely and apply the same effect to multiple voices through a shared send bus.

## Valley Plateau (Valley)

Plateau is one of the most highly regarded free reverb modules available for VCV Rack. It is based on the Dattorro plate reverb algorithm, which produces lush, diffuse reverberation similar to studio hardware units. Plateau is the first choice for ambient, cinematic, and psychedelic patches.

| Parameter | Range | What it does |
|-----------|-------|--------------|
| SIZE | 0–1 | Reverb room size / decay length |
| DIFF | 0–1 | Diffusion — how quickly echoes blur into wash |
| DECAY | 0–1 | Tail length — higher = longer reverb |
| DAMP | 0–1 | High-frequency damping — simulates air absorption |
| MOD SPEED | 0–1 | Speed of internal pitch modulation |
| MOD DEPTH | 0–1 | Amount of internal pitch modulation (shimmer/chorus) |
| PRE-DELAY | 0–1 | Time before reverb starts |
| DRY/WET | 0–1 | Mix of dry and wet signal |

| Input/Output | Type | Description |
|-------------|------|-------------|
| IN L/R | Input | Stereo audio input |
| OUT L/R | Output | Stereo reverb output |
| CV inputs | Input | CV control over most parameters |

**Patching tips:** For an ambient pad, set SIZE and DECAY near maximum, DAMP around 0.4, and keep PRE-DELAY at 20–50ms for definition. Modulate MOD SPEED and MOD DEPTH slightly for a shimmer effect. Use as a send: mix your dry signal with the Plateau output using a [Mixer](mixer.md). For psybient or ambient patches, reverb tails of 8–14 seconds are realistic — a DECAY near 0.95 and SIZE at max will approach this.

## Chronoblob2 (Alright Devices)

Chronoblob2 is a high-quality stereo delay module. It features tempo-syncable delay time, adjustable feedback, a tone filter on the feedback path, and a stereo spread control. The delay is clean and musical rather than lo-fi.

| Parameter | Description |
|-----------|-------------|
| TIME | Delay time (or tempo division when synced) |
| FEEDBACK | How much of the output feeds back into input |
| TONE | High-frequency cut on feedback path |
| SPREAD | Stereo width of delay taps |
| MIX | Dry/wet blend |

**Patching tips:** For dub-style delay, set TIME to dotted 1/8 at 89 BPM (roughly 505 ms), FEEDBACK 40–65%, and TONE around 0.4 to roll off harsh highs on repeats. Patch a random S&H into FEEDBACK CV for unpredictable, organic delay behavior. Send a sparse chord hit or melodic fragment through this for a classic dub echo effect.

## Delay (VCV Free)

The built-in VCV Free Delay is a straightforward mono delay (one Audio input; Mix and Wet outputs). TIME, FEEDBACK, TONE, and MIX controls with CV inputs. Not as feature-rich as Chronoblob2 but requires no extra plugin installation. Suitable for basic echo effects when starting out.

| Parameter | Description |
|-----------|-------------|
| TIME | Delay time in seconds |
| FEEDBACK | Feedback level |
| MIX | Wet/dry blend |

**Patching tips:** Keep FEEDBACK below 0.8 unless you want runaway feedback. Use MIX at 0.2–0.4 for subtle echoes that don't overwhelm the dry signal.

### Befaco Spring Reverb (Befaco)

A physical model of a spring reverb tank — the type found in vintage guitar amplifiers. Spring reverb has a distinctly metallic, boingy character quite different from plate or hall reverb. The Befaco version accurately models this character including the bouncy transient splash.

**Patching tips:** Apply to drums or a sharp plucked sound for a surf-rock or dub-techno character. The spring splash on transients is the defining feature — let it breathe rather than damping it with a gate.

### Vult Tangents (Vult — free tier)

A phaser effect from Vult's free tier. Phasers apply multiple notch filters with a sweeping cutoff to create comb-filtering effects. The result sounds like a moving, swirling filter sweep. More subtle than chorus, more rhythmic than reverb.

### AS Delay (AS)

A basic delay module from AS. Simple TIME/FEEDBACK/MIX interface. Good fallback when you need a delay but haven't installed dedicated delay plugins.

### Count Modula Chorus (Count Modula)

A stereo chorus module that thickens sounds by mixing slightly delayed, pitch-modulated copies of the signal. Adds width and movement without the obvious echo of a delay or the diffusion of a reverb.

## Where to go next

- [Mixer](mixer.md) — set up a send/return for effects
- [VCF](vcf.md) — filter the reverb return for darker tails
- [LFO](lfo.md) — modulate delay time for chorus/vibrato effects
- [Slow Psybient](slow-psybient.md) — tutorial built around Plateau + Chronoblob2

---
*Version: 2026-06-17.*
