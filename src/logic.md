# Logic

Logic modules perform Boolean operations on gate and trigger signals: AND, OR, NOT, XOR, and comparators. They combine or transform rhythmic signals to create new patterns from existing ones. An AND gate fires only when two gates are simultaneously high; an OR gate fires when either gate is high; a NOT gate inverts a gate signal (fires when the gate is off). Logic modules are the basis of polyrhythmic drum programming and complex trigger routing.

## Befaco Rampage comparator output

Rampage's comparator output fires a gate when channel A's output exceeds channel B's. When both channels are running as LFOs at different frequencies, the comparator output produces a gate that opens and closes based on the phase relationship between the two — an emergent rhythmic pattern derived from two simple waveforms.

**Patching tips:** Set channel A to a fast rate and channel B to a slow rate. The comparator output fires in a pattern that combines both frequencies, producing rhythms that are related to but not identical to either source. Change either rate to create dramatically different patterns without reprogramming anything.

## Count Modula Logic (Count Modula)

Count Modula provides a comprehensive logic module with AND, OR, NOT, XOR, and NAND/NOR functions. Multiple inputs per gate type, gate length control, and clean trigger outputs.

| Operation | Behavior |
|-----------|----------|
| AND | Output fires only when all inputs are high simultaneously |
| OR | Output fires when any input is high |
| NOT | Output is the inverse of the input |
| XOR | Output fires when exactly one input is high (not both) |

**Patching tips:** Run a kick pattern AND a snare pattern through an AND gate — the output fires only on steps where both fire simultaneously, creating a new accent pattern. OR two different hi-hat patterns for a busier, combined rhythm. NOT a gate pattern to create a "fill on the off-beats" layer.

## Bogaudio CMP (Bogaudio)

A voltage comparator: outputs a gate when input A is greater than input B. Unlike logic gates that work with digital gates, CMP compares continuous voltages. Useful for triggering events when a modulation signal crosses a threshold — for example, triggering a drum hit whenever an LFO exceeds 3V.

| Input/Output | Type | Description |
|-------------|------|-------------|
| A, B | Input | Voltages to compare |
| OUT | Output | Gate: high when A > B |

**Patching tips:** Set B to a fixed voltage (using an offset or attenuverter) as a threshold. Patch a slow LFO to A. The output produces a gate that opens and closes as the LFO crosses the threshold — the gate duration depends on how long the LFO stays above it.

### ML Modules Bernoulli Gate (ML Modules)

Routes triggers randomly to one of two outputs. Related to logic in that it makes routing decisions, but based on probability rather than Boolean conditions. See [Sample & Hold](sample-hold.md) for details on probabilistic gate routing.

### Count Modula Gate Delay (Count Modula)

Delays a gate signal by a defined time before outputting it. Combined with AND gates, you can create rhythmic offsets — fire a trigger slightly after the beat to produce a dragging, behind-the-beat feel.

### Impromptu Gate (Impromptu)

Impromptu's gate utilities include gate-to-trigger converters, trigger extenders, and pulse shapers. Useful when a module needs a specific gate length or trigger format that your source doesn't naturally produce.

## Where to go next

- [Clock](clock.md) — the gate sources that logic operates on
- [Sequencers](sequencer.md) — gate patterns to combine with logic
- [Envelopes](envelope.md) — trigger envelopes from logic gate outputs
- [Sample & Hold](sample-hold.md) — probabilistic gate routing

---
*Version: 2026-06-17.*
