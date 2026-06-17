# Mult & Splitter

A mult (multiple) copies one signal to several outputs so the same CV or audio can be sent to multiple destinations simultaneously. A splitter separates a polyphonic cable (a single cable carrying multiple independent signals) into individual monophonic outputs. These are routing utilities — they don't change the signal, they distribute it.

In VCV Rack, you can often connect one output to multiple inputs simply by clicking the output and adding more cables. The built-in mult behavior means you may not always need a dedicated mult module. However, explicit mult modules are useful for documentation clarity and when driving many destinations from a single source.

## Split (Fundamental)

Split takes one polyphonic cable and outputs up to 16 individual monophonic channels. Polyphonic cables in VCV Rack carry multiple signals in a single wire. When a polyphonic source (like a MIDI keyboard outputting polyphonic pitch CV) needs to feed multiple monophonic destinations, Split separates the channels.

| Input/Output | Type | Description |
|-------------|------|-------------|
| POLY | Input | Polyphonic cable input |
| 1–16 | Output | Individual channel outputs |

**Patching tips:** Connect the POLY output of a MIDI-CV module (in polyphonic mode) to Split's input. Each output then carries one voice's pitch CV. Route each to its own VCO for true polyphony.

## Merge (Fundamental)

The inverse of Split — takes up to 16 monophonic inputs and combines them into one polyphonic cable output. Used to feed polyphonic-aware modules from individual signals.

| Input/Output | Type | Description |
|-------------|------|-------------|
| 1–16 | Input | Individual channel inputs |
| POLY | Output | Polyphonic cable output |

**Patching tips:** Merge several separate LFO outputs into one polyphonic cable for use with polyphonic-capable modules. Or merge individual voices' outputs into a single polyphonic bus for a polyphonic VCF.

## Mult (Fundamental)

A simple passive mult: one input connected to multiple outputs. In VCV Rack, this is largely redundant since any output cable can be clicked repeatedly to add multiple destinations. However, explicit Mult modules make the signal flow visually clearer when one source drives many destinations.

**Patching tips:** Use a Mult to distribute a master clock signal to multiple sequencers, LFOs, and envelope triggers from a single source. Visual clarity is the main benefit.

### Count Modula Poly Channels (Count Modula)

Manipulates polyphonic channel counts — useful for building polyphonic patches where you need to manage how many voices are active. Complements Split and Merge for more complex polyphonic routing.

### Stoermelder STRIP (Stoermelder PACK-ONE)

While primarily a preset manager, Stoermelder PACK-ONE includes utilities for polyphonic cable manipulation. The free PACK-ONE plugin is essential for complex patching workflows.

### VCV built-in cable routing

For simple mult needs, just connect one output to multiple inputs by clicking the output and drawing additional cables. Each cable is a separate connection but carries the same signal — no module needed.

## Where to go next

- [MIDI to CV](midi-cv.md) — polyphonic MIDI setup using Split/Merge
- [Clock](clock.md) — distributing clock to multiple modules via Mult
- [Mixer](mixer.md) — collecting multiple signals into one output
- [Sequencers](sequencer.md) — running multiple sequencers from one clock

---
*Version: 2026-06-17.*
