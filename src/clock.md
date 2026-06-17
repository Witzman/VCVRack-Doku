# Clock

A clock generates regular trigger or gate pulses at a defined tempo, measured in BPM. Everything rhythmic in a patch — sequencers, envelopes, LFOs synced to tempo, sample-and-hold rates — derives its timing from a clock signal. Without a master clock, all rhythmic elements run independently at their own rates and drift apart over time.

## Clocked (Impromptu)

Clocked is one of the most capable free clock modules for VCV Rack. It provides a master BPM control plus four output channels, each of which can output a different clock division or multiplication of the master tempo. This makes it possible to run a kick drum on the beat, a snare on half-time, hats on 1/8th notes, and a sequencer on dotted 1/4 notes all from a single module.

| Parameter | Description |
|-----------|-------------|
| BPM | Master tempo in beats per minute |
| RATIO (×4) | Per-output clock division or multiplication |
| SWING | Per-output swing amount |
| PW | Pulse width of gate output |

| Input/Output | Type | Description |
|-------------|------|-------------|
| RUN | Input | Start/stop the clock |
| RESET | Input | Reset all outputs to beat 1 |
| CLK 1–4 | Output | Four independently ratioed clock outputs |

**Patching tips:** Set CLK1 to ×1 (master beat), CLK2 to /2 (half notes), CLK3 to ×2 (eighth notes), CLK4 to dotted 1/8. Route CLK1 to a kick sequencer, CLK2 to snare, CLK3 to hi-hats, CLK4 to a delay module's time CV for tempo-synced echoes. The SWING parameter on each output allows independent groove feel per rhythmic layer — slightly swing the hi-hats while keeping the kick straight.

## Bogaudio CLKD (Bogaudio)

A straightforward master clock with four outputs, each with a fixed division ratio. Simpler than Clocked — no swing or per-output ratio control, but very clean and easy to set up quickly.

| Output | Fixed division |
|--------|----------------|
| /1 | Master beat |
| /2 | Half time |
| /4 | Quarter time |
| /8 | Eighth time |

**Patching tips:** Use CLKD for fast patch setup when you just need standard clock divisions and don't need swing or unusual ratios.

### Count Modula Clock Divider (Count Modula)

Takes a master clock input and outputs multiple divided rates. Useful as an extension when your master clock module doesn't have enough outputs — chain it after Clocked to get additional divisions.

### Fundamental Clock (if available)

VCV Rack Free's core modules don't include a dedicated clock generator. Clocked (Impromptu) or CLKD (Bogaudio) are the recommended free options.

### Befaco Burst (Befaco)

Not a standard clock, but a burst generator — outputs a defined number of rapid trigger pulses when triggered. Useful for generating drum rolls, ratcheting sequencer steps, or creating polymetric bursts of activity from a single trigger.

### Using an LFO as a clock

A square-wave LFO can serve as a simple clock. Set the rate to match your desired BPM (at 120 BPM, the clock fires twice per second — set the LFO rate to 2 Hz). This approach lacks precision and BPM readout but works for slow, tempo-free patches where exact BPM doesn't matter.

## Where to go next

- [Sequencers](sequencer.md) — the primary clock consumer
- [Envelopes](envelope.md) — trigger gates from clock for rhythmic envelopes
- [Sample & Hold](sample-hold.md) — clock the S&H for synchronized random CV
- [LFO](lfo.md) — sync LFOs to clock for locked modulation
- [Patching Use Cases](patching-use-cases.md) — drum pattern recipes

---
*Version: 2026-06-17.*
