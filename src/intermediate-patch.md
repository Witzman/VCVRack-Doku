# Beyond the Basics: Your First Third-Party Patch

This tutorial assumes you have worked through [Your First Patch](first-patch.md) and are comfortable with the basic VCO → VCF → VCA → Output signal chain. Here you will install your first free third-party plugins, build a more expressive voice using Bogaudio, and add a proper clock and sequencer using Impromptu Clocked. The result is a self-playing melodic patch that runs without a keyboard.

## What you will build

A four-step melodic sequence through a filter-swept lead voice with velocity variation and an automated tempo-synced LFO filter sweep. The patch plays itself and introduces three new concepts: installing plugins, using a clock module, and modulating with tempo-synced LFOs.

## Step 1 — Install the plugins

Before building, install two free plugins from the VCV Library:

1. Open VCV Rack and go to Library (top menu) → VCV Library.
2. Search for **Bogaudio** and click Subscribe.
3. Search for **Impromptu Modular** and click Subscribe.
4. Restart VCV Rack. The new modules will appear in the module browser.

## Step 2 — Build the clock

Add **Impromptu Clocked** from the module browser (search "Clocked"). This is your master tempo source.

- Set BPM to 120.
- CLK1 output: set ratio to ×1 (quarter notes — the main beat).
- CLK2 output: set ratio to ×4 (sixteenth notes — for a future hi-hat if you want one).
- Press RUN to start the clock.

You will hear nothing yet — the clock only outputs trigger pulses.

## Step 3 — Add a sequencer

Add **SEQ-3** (Fundamental) from the module browser.

- Connect Clocked's CLK1 output to SEQ-3's CLK input.
- Set STEPS to 4 (four-step loop).
- Set the four step knobs to C3, E3, G3, A3 (these are approximately -1V, -0.75V, -0.5V, -0.25V — tune by ear against the VCO you add next).
- Enable all four gate buttons.

## Step 4 — Add the voice

Add **Bogaudio VCO** (search "Bogaudio VCO" in the browser). This is a more flexible oscillator than Fundamental's VCO-1.

- Connect SEQ-3's ROW1 output to Bogaudio VCO's V/OCT input.
- Connect SEQ-3's GATE output to the next step's input (keep reading).
- Take the SAW output from Bogaudio VCO forward into the filter.

## Step 5 — Add filter and envelope

Add **Fundamental VCF** and **Bogaudio ADSR**.

- Connect Bogaudio VCO's SAW output to VCF IN.
- Take VCF's LP output to a VCA (add **Fundamental VCA**).
- Connect SEQ-3's GATE to Bogaudio ADSR's GATE input.
- Connect Bogaudio ADSR's ENV output to VCA's CV input.
- Connect VCA's OUT to the Audio module inputs.

Set the ADSR: Attack 10ms, Decay 200ms, Sustain 0.6, Release 300ms. You should now hear a four-note sequence.

**What to tweak first:** Adjust the SEQ-3 step knob voltages while the sequence runs to change the pitches. The four notes will drift through whatever intervals you set — use the VCO's built-in tuner display or tune by ear.

## Step 6 — Add a tempo-synced filter sweep

This is the step that makes the patch feel professional rather than static.

Add **Bogaudio LFO**.

- Set Bogaudio LFO's FREQ to match your tempo: at 120 BPM, one beat per second = 2 Hz.
- Take the SIN output through a **Fundamental 8vert** channel (attenuate to about 0.4).
- Connect the attenuated output to VCF's FREQ CV input.

Now the filter opens and closes in time with the beat, giving the sequence a rhythmic breathing quality.

**What to tweak:** Change the LFO rate. Halving it to 1 Hz gives a two-beat filter sweep — the filter opens slowly over two beats and closes again. Setting it very slow (0.1 Hz) produces a gradual sweep over ten seconds. Each rate changes the groove completely.

## Step 7 — Add velocity variation

Bogaudio ADSR has a separate GATE input and a VEL input. Add randomness to velocity:

- Add **Bogaudio S&H**.
- Connect Clocked's CLK1 to S&H's TRIG input.
- Connect **Fundamental Noise** (White output) to S&H's IN input.
- Connect S&H's OUT through an 8vert channel (attenuate to 0.3) to Bogaudio ADSR's VEL input.

The ADSR now receives a different random velocity on each step — some notes hit harder, some softer. This is the single biggest step toward making a sequenced patch feel alive.

## What you have learned

This patch introduced: installing free plugins, Impromptu Clocked as a master tempo source, Bogaudio's more flexible VCO and ADSR, tempo-synced LFO filter modulation, and random velocity using S&H. These techniques apply to every patch you build from here on.

## Where to go next

- [Sequencers](sequencer.md) — deeper sequencer options including phrase chaining
- [LFO](lfo.md) — more modulation techniques
- [Sample & Hold](sample-hold.md) — all the ways S&H adds randomness
- [Slow Psybient](slow-psybient.md) — a more complex patch using similar techniques
- [Patching Use Cases](patching-use-cases.md) — more patch recipes to try

---
*Version: 2026-06-17.*
