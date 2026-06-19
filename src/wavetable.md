# Wavetable Oscillators

A wavetable oscillator reads through a stored table of waveform shapes rather than calculating a waveform mathematically. The key advantage is the ability to sweep through many different timbres using a single CV — position modulation moves the playback point through the table, morphing from one waveform to the next. This produces animated, evolving tones that a standard VCO cannot replicate.

## Wavetable VCO (VCV Free)

The Wavetable VCO is VCV Rack's built-in wavetable oscillator. It comes with a bank of wavetables covering analog, digital, vocal, and spectral shapes. A POS knob and CV input control which wavetable position is being read.

| Parameter | Range | What it does |
|-----------|-------|--------------|
| FREQ | ±75 semitones | Pitch, shown in Hz on the tooltip |
| POS | 0–100% | Wavetable position (timbre) |

The wavetable itself is chosen from the module's right-click context menu, not a panel knob.

| Input/Output | Type | Description |
|-------------|------|-------------|
| V/OCT | Input | Pitch CV |
| POS | Input | CV morphs through wavetable positions |
| OUT | Output | Audio output |

**Patching tips:** Modulate the POS input with a slow LFO for continuously morphing timbre. A fast LFO produces formant-like animation. Use an envelope to sweep position in sync with amplitude for evolving attack-decay textures. Loading a different wavetable from the right-click menu changes the entire character of the oscillator — try several before committing.

## Surge XT Wavetable VCO (Surge XT)

Surge XT includes a high-quality wavetable engine with hundreds of factory wavetables plus the ability to load custom wavetable files. It offers multiple playback modes (forward, backward, ping-pong), morph smoothing, and spectral processing options. For complex sound design, this is one of the best free wavetable sources available in VCV Rack.

| Parameter | Description |
|-----------|-------------|
| Position | Wavetable morph position |
| Skew | Asymmetry in wavetable scanning |
| Formant | Formant shift independent of pitch |
| Morph | Crossfade between adjacent tables |

The Formant parameter separates timbral character from pitch — raising formant produces vowel-like tones while keeping the note the same. Very useful for vocal pad textures.

**Patching tips:** Load a vocal or harmonics wavetable and modulate Position with a very slow envelope (8–16 second attack) for evolving pad textures. Pair with Plateau reverb and a long VCA release for cinematic soundscapes.

### Wavetable LFO (VCV Free)

Technically an LFO, but uses the same wavetable engine as Wavetable VCO at sub-audio rates. Useful for producing unusual modulation shapes rather than standard sine/triangle/square LFO waveforms. See [LFO](lfo.md) for context on using it as a modulator.

### Valley Dexter (Valley)

Dexter is a four-operator FM/wavetable hybrid oscillator. Each operator can use a wavetable or a standard waveform, and operators modulate each other in FM configurations. This places it somewhere between a wavetable oscillator and an FM synthesizer. Free from the Valley plugin.

### Count Modula Wavetable VCO (Count Modula)

Count Modula includes a wavetable oscillator with a set of built-in tables and CV-controllable position. Straightforward to patch and consistent with the rest of the Count Modula interface style.

## Where to go next

- [VCO](vco.md) — standard oscillators for comparison
- [VCF](vcf.md) — filtering wavetable output shapes the character further
- [LFO](lfo.md) — use an LFO to modulate wavetable position
- [Slow Psybient](slow-psybient.md) — tutorial using wavetable textures for pad sounds

---
*Version: 2026-06-17.*
