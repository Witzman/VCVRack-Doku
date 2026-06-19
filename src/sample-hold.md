# Sample & Hold

A Sample & Hold (S&H) module captures ("samples") the current value of an input signal when it receives a trigger, then holds that value until the next trigger arrives. The output is a stepped, staircase-like CV that jumps to a new value with each clock pulse. When the input is a noise source, S&H produces random stepped voltages — one of the most useful sources of controlled randomness in a modular patch.

## Bogaudio S&H (Bogaudio)

Bogaudio's S&H is a clean, accurate sample-and-hold with a track mode (output follows input continuously while gate is high, then holds on falling edge) alongside the standard sample mode.

| Parameter | Description |
|-----------|-------------|
| MODE | Sample (trigger) or Track+Hold (gate) |

| Input/Output | Type | Description |
|-------------|------|-------------|
| IN | Input | Signal to sample — often a noise source |
| TRIG | Input | Trigger or gate to initiate sampling |
| OUT | Output | Held voltage |

**Patching tips:** Connect VCV Free Noise's White output to IN. Connect a clock divided by 4 or 8 to TRIG. The OUT now produces a new random pitch or CV value once per measure. Patch OUT to a VCO's V/OCT input through a Quantizer for random melodic fragments that stay in key. Patch to VCF FREQ CV for random filter jumps. Patch to delay feedback amount for organic, unpredictable echoes.

## Sample & Hold / Analog Shift Register (VCV Free)

The VCV Free **Sample & Hold** module (full name "Sample & Hold Analog Shift Register") is an 8-stage analog shift register — here "ASR" means *Analog Shift Register*, not attack-sustain-release. On each trigger it samples the input into the first stage and shifts every previously held value one stage down the chain, so the eight outputs carry the last eight sampled values in sequence. Used as a single stage it is an ordinary sample & hold; used across stages it produces delayed echoes of a CV — handy for canons and call-and-response melodies.

| Input/Output | Type | Description |
|-------------|------|-------------|
| Sample 1–8 | Input | Signal to sample into each stage |
| Trigger 1–8 | Input | Trigger that samples/shifts each stage |
| Sample 1–8 | Output | Held value of each stage (stage N = N triggers ago) |

It also has RND, PUSH, and CLEAR buttons for randomizing, manually advancing, and clearing the register.

**Patching tips:** Patch a noise source to Sample 1 and a clock to Trigger 1 for a basic random S&H on output 1. Take outputs 2, 3, 4… to additional voices to play the same pitch sequence delayed by one, two, three steps — an instant canon. Quantize each output for melodic results.

## ML Modules Bernoulli Gate (ML Modules)

Strictly a gate router rather than a sample-and-hold, but closely related in function: each incoming trigger has a 50% probability (adjustable) of being routed to one of two outputs rather than the other. This introduces randomness into gate patterns — notes are selectively triggered or skipped. Combined with a sequencer, it creates sequences that randomly drop notes.

| Parameter | Description |
|-----------|-------------|
| P | Probability of routing to output A vs. B |

**Patching tips:** Patch a sequencer's gate output to Bernoulli Gate's input, and both outputs to different voices or effects paths. Set P to 0.6–0.8 so most notes still fire but some are randomly rerouted. For a psybient texture, route occasional gates to a second voice with a different timbre for unpredictable moments.

### Count Modula Random Sampler (Count Modula)

An extended S&H with multiple outputs, each holding a different sample taken at the same trigger moment. Useful when you need several simultaneous but independent random values — for example, random pitch, random filter cutoff, and random reverb send all changing together on the same clock.

### Squinky Labs S&H (Squinky Labs)

A compact S&H with clean tracking. Minimal interface — input, trigger, output. Good choice when you just need a standard S&H without extra features.

## Where to go next

- [Noise](noise.md) — the random signal source fed into S&H
- [Quantizer](quantizer.md) — snap S&H output to musical scales
- [Clock](clock.md) — the trigger source that controls sampling rate
- [LFO](lfo.md) — continuous modulation alternative to stepped S&H
- [Slow Psybient](slow-psybient.md) — S&H patched to reverb send and delay feedback

---
*Version: 2026-06-17.*
