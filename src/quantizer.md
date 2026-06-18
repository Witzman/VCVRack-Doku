# Quantizer

A quantizer snaps incoming CV voltages to the nearest note in a defined musical scale. Without a quantizer, a random CV source or a freely-turned knob will output arbitrary voltages that don't correspond to musical pitches. With a quantizer, those same voltages snap to the nearest note in C minor, pentatonic, or whatever scale you choose — making random or manual CVs immediately musical.

## Quantizer (VCV Free)

The VCV Free Quantizer allows you to select which individual notes of the chromatic scale are active. Any input voltage is snapped to the nearest active note. It is intentionally simple — no scale presets, just 12 note buttons you toggle on and off.

| Parameter | Description |
|-----------|-------------|
| Note buttons (12) | Toggle individual chromatic pitches as targets |

| Input/Output | Type | Description |
|-------------|------|-------------|
| IN | Input | Unquantized CV |
| OUT | Output | Quantized CV snapped to selected notes |

**Patching tips:** For a C minor scale, activate: C, D, Eb, F, G, Ab, Bb. Feed a random S&H output to IN — the OUT produces melodic fragments in C minor. For a pentatonic scale, activate only 5 notes; the output will feel more immediately musical with fewer dissonant possibilities. The VCV Free Quantizer fires a trigger on each output change — useful as a gate source for accompanying envelopes.

## Bogaudio ADDR-SEQ as quantizer

Bogaudio's ADDR-SEQ is an addressable step sequencer that can function as a quantizer substitute: store specific note voltages in each step and use an unquantized CV to address which step plays. The output is constrained to whatever voltages you manually set — a more hands-on approach to pitch constraint.

## Count Modula Quant (Count Modula)

Count Modula's quantizer provides scale presets (major, minor, pentatonic, blues, modes, etc.) alongside a custom note toggle interface. The preset system makes it faster to work than the VCV Free Quantizer when you want standard scales without manually toggling notes.

| Feature | Description |
|---------|-------------|
| Scale presets | One-click common scale selection |
| Custom notes | Override presets with individual note toggles |
| Octave range | Control which octaves are included |

**Patching tips:** Use a scale preset for fast setup, then refine by deactivating individual notes for modal variations. The blues scale preset produces naturally expressive random melodies when paired with a fast S&H.

### Surge XT Quantizer (Surge XT)

Surge XT includes a quantizer with scale and tuning system support — including microtonal scales. If you work outside standard Western 12-note scales, Surge XT's quantizer is worth exploring.

### ML Modules Quantum (ML Modules)

A clean quantizer with note selection and a trigger output on each new note change. The trigger output makes it easy to sync envelopes and arpeggios to the quantized pitch changes.

## Where to go next

- [Sample & Hold](sample-hold.md) — the random CV source quantizers work with
- [Sequencers](sequencer.md) — quantize manually tuned sequencer rows
- [VCO](vco.md) — the destination for quantized pitch CV
- [Patching Use Cases](patching-use-cases.md) — generative melody recipes using S&H + quantizer

---
*Version: 2026-06-17.*
