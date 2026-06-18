# Sequencers

A sequencer stores a series of values and outputs them one at a time in response to a clock. The output is typically a V/Oct pitch CV for melodic sequences, but sequencers can also output gate signals, trigger patterns, and modulation values. Sequencers are the primary way to make a patch play musical patterns autonomously without a keyboard or MIDI input.

## SEQ 3 (VCV Free)

SEQ 3 is an 8-step sequencer included with Rack Free. Each step has a voltage knob and a gate button. When clocked, the module advances one step per clock pulse and outputs the current step's voltage and gate state.

| Parameter | Range | What it does |
|-----------|-------|--------------|
| STEPS | 1–8 | Number of active steps in the sequence |
| Per-step knob | ±5V | Voltage output for that step |
| Per-step button | on/off | Whether the gate fires on that step |
| RUN | toggle | Starts and stops the sequencer |
| RESET | trigger | Returns to step 1 |

| Input/Output | Type | Description |
|-------------|------|-------------|
| CLK | Input | Clock input — advances one step per pulse |
| RESET | Input | Resets to step 1 |
| GATE | Output | Gate signal for the current step's gate setting |
| ROW1/2/3 | Output | Three independent voltage rows per step |

**Patching tips:** Connect a clock's output to CLK. Patch ROW1 to a VCO's V/OCT input for a pitched sequence. Patch GATE to an ADSR's GATE input to trigger notes. The three rows allow independent pitch, modulation, and velocity sequences running in sync — program ROW1 for pitch, ROW2 for filter cutoff offsets, and ROW3 for VCA level variation. Use STEPS to create patterns shorter than 8 — a 5-step sequence over a 4/4 clock creates interesting polyrhythmic effects.

## Impromptu Clocked + Phrase-Seq (Impromptu)

Impromptu is a free plugin with a comprehensive sequencing ecosystem. Clocked provides a master clock with multiple divided outputs. Phrase-Seq16 is a 16-step, 2-row sequencer with phrase chaining — you can define up to 16 different phrases and chain them in order, allowing full song structures rather than a single repeating loop.

| Feature | Description |
|---------|-------------|
| Phrase chaining | Define multiple patterns, play them in sequence |
| CV inputs | Real-time control over most parameters |
| Note tie | Hold notes across steps for legato playing |
| Slide | Portamento between adjacent steps |

**Patching tips:** Use Phrase-Seq16's pattern chain to build a verse/chorus structure. Set an 8-bar phrase for the verse and a 4-bar phrase for the chorus, then define a chain that plays verse × 2, chorus × 1. Slide between steps for bass sequences that feel legato and natural.

## Count Modula Step Sequencer (Count Modula)

Count Modula provides a family of step sequencers — 8-step, 16-step, and modular building blocks. Their standout feature is per-step probability: each step has a chance of firing that can be set from 0% to 100%. This produces sequences that are recognizable but not perfectly repetitive — essential for generative music.

| Feature | Description |
|---------|-------------|
| Per-step probability | Random step skipping |
| Gate length | Per-step gate duration control |
| CV outputs | Pitch + multiple modulation rows |

**Patching tips:** Set most steps to 100% probability but add one or two at 50% for occasional variation. A 16-step sequence with 3 steps at 60% probability generates a different groove every few bars while maintaining the general pattern.

### Befaco Muxlicer (Befaco)

A step sequencer combined with a signal multiplexer. Each step has a voltage, gate, and a clock divider, making it possible to build polyrhythmic patterns where different steps run at different speeds. Its output routing capabilities are more complex than a standard sequencer — useful for advanced rhythmic applications.

### ML Modules SeqSwitch (ML Modules)

Routes an input signal to one of several outputs based on a clock step. Useful for switching between sound sources or effects routings rhythmically rather than for pitch sequencing.

### VCV Core MIDI to CV + keyboard

For live playing rather than sequenced patterns, a MIDI keyboard connected through MIDI to CV is the simplest approach. See [MIDI to CV](midi-cv.md) for setup details.

## Where to go next

- [Clock](clock.md) — the clock that drives sequencers
- [Quantizer](quantizer.md) — snap sequencer output to musical scales
- [MIDI to CV](midi-cv.md) — keyboard alternative to sequencer pitch
- [Patching Use Cases](patching-use-cases.md) — bassline and melodic patch recipes

---
*Version: 2026-06-17.*
