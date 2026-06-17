# Glossary

Definitions for terms used throughout this handbook, in alphabetical order.

---

| Term | Definition |
|------|-----------|
| **ADSR** | Attack-Decay-Sustain-Release. The four stages of a common envelope shape. Attack is the rise time, Decay is the fall to Sustain level, Sustain is the held level while a gate is open, Release is the fall after the gate closes. |
| **Attenuator** | Reduces the level of a signal. An attenuverter can also invert the signal (negative values). |
| **Attenuverter** | A knob or module that scales a signal from −1× (full inversion) to +1× (full pass-through), with 0 at center for silence. |
| **Audio rate** | Signals oscillating fast enough to be heard as pitch — typically 20 Hz and above. Contrast with CV rate. |
| **Bipolar** | A signal that swings both positive and negative, typically −5 V to +5 V or −10 V to +10 V. An LFO is usually bipolar. |
| **BPM** | Beats per minute. The tempo of a clock or sequencer. |
| **Cable** | In VCV Rack, a virtual patch cable connecting one module's output to another's input. Right-click a cable to delete it. Hold Ctrl while dragging to duplicate a connection. |
| **Channel** | One voice or signal lane. A polyphonic cable carries up to 16 channels. |
| **Clock** | A signal that generates regular pulses at a set tempo, used to advance sequencers, trigger envelopes, or sync LFOs. |
| **CV** | Control Voltage. Any signal used to modulate a parameter rather than be heard directly as audio. Pitch CV, filter CV, and envelope output are all CV signals. |
| **Cutoff** | The frequency at which a filter begins to attenuate signals. For a lowpass filter, signals below the cutoff pass through; above it they are reduced. |
| **DC offset** | A constant voltage added to a signal, shifting it away from 0 V. Can be useful for bias or cause problems when mixing with AC audio signals. |
| **Drone** | A sustained, continuous note or texture without rhythmic articulation. Common in ambient and experimental patches. |
| **Envelope** | A voltage that changes shape over time in response to a trigger or gate. ADSR is the most common form. Used to shape amplitude, filter, and other parameters. |
| **Envelope follower** | Tracks the amplitude of an audio signal and outputs a corresponding CV. Louder input = higher output voltage. |
| **Expander** | A module that attaches to the side of another module to add functionality, communicating via the Rack expander system rather than patch cables. |
| **FM** | Frequency Modulation. Using one oscillator (or LFO) to modulate the frequency of another, creating complex timbres. Linear FM and exponential FM behave differently. |
| **Gate** | A CV signal that stays high (+10 V) for a duration, indicating "key held." ADSRs typically use gates for their sustain stage. |
| **Generative** | A patch that produces evolving, semi-random output without continuous manual control — often using random CV sources, clock divisions, and logic. |
| **HP** | Highpass filter. Passes high frequencies, attenuates low ones. Useful for removing low-end rumble from signals. |
| **Hz** | Hertz. Cycles per second. A measure of frequency for both audio and CV signals. |
| **Knob** | A rotary control on a module panel. Right-click in VCV Rack for context menu options including setting exact values and MIDI mapping. |
| **LFO** | Low-Frequency Oscillator. An oscillator running below audio rate (below ~20 Hz), used as a modulation source. Common uses: vibrato, tremolo, filter wobble. |
| **Logic** | Modules that perform Boolean operations on gate signals: AND, OR, NOT, XOR, etc. Useful for combining rhythmic patterns. |
| **LP** | Lowpass filter. Passes low frequencies, attenuates high ones. The most common filter type in subtractive synthesis. |
| **Merge** | A utility module that combines multiple monophonic cables into one polyphonic cable. |
| **MIDI** | Musical Instrument Digital Interface. A standard protocol for communicating notes, controllers, and clock between devices. VCV Rack's MIDI modules convert MIDI signals to CV and vice versa. |
| **Module** | A single functional unit in a VCV Rack patch. Modules have inputs, outputs, and controls on their panel. |
| **Monophonic** | A single-channel signal carrying one voice. |
| **Mult** | Multiple. A utility that copies one signal to several outputs without changing it. |
| **Noise** | A signal with random values at every sample. White noise has equal energy at all frequencies. Pink noise has more energy in low frequencies. Useful for percussion, wind sounds, and random modulation sources. |
| **Octave** | A doubling of frequency. In 1V/oct pitch CV, one volt equals one octave. |
| **Oscillator** | A module that generates a periodic waveform. VCOs run at audio rate; LFOs run below audio rate. |
| **Pan** | Panning. The left-right position of a sound in a stereo field. |
| **Patch** | A complete VCV Rack setup — the set of modules placed and the cables connecting them. Saved as a .vcv file. |
| **Pitch CV** | A control voltage representing musical pitch, typically following the 1V/octave standard. |
| **Polyphonic** | A cable or module carrying multiple voices simultaneously. VCV Rack supports up to 16 channels in a single polyphonic cable. Polyphonic cables appear thicker. |
| **Port** | An input or output socket on a module panel. |
| **Quantizer** | A module that snaps incoming CV to the nearest note in a chosen scale, ensuring musical pitch output from continuous or random CV sources. |
| **Rack** | The virtual modular synthesizer environment in VCV Rack where modules are placed and connected. |
| **Resonance** | The emphasis of frequencies near a filter's cutoff point. High resonance causes the filter to ring at the cutoff frequency. Also called Q. |
| **Ring modulator** | Multiplies two signals together, producing sum and difference frequencies. Creates metallic, bell-like, or distorted timbres. |
| **Sample and hold** | Captures (samples) the value of an input signal when triggered, then holds that value until the next trigger. Often fed noise to produce random stepped voltages. |
| **Sawtooth** | A waveform that rises linearly then drops sharply, or the reverse. Rich in harmonics, characteristic of brass and string synthesis. |
| **Semitone** | One twelfth of an octave. In 1V/oct pitch CV, one semitone = 1/12 V ≈ 0.0833 V. |
| **Sequencer** | Steps through a series of programmed values over time, driven by a clock. Outputs pitch CV, gate, and other signals to drive a patch. |
| **Signal chain** | The path a signal takes from source to output, through processors and modifiers. |
| **Sine wave** | A smooth, pure waveform with a single frequency and no harmonics. |
| **Slew** | Gradual change. A slew limiter smooths abrupt voltage jumps, turning sharp steps into gliding transitions — the modular equivalent of portamento. |
| **Split** | A utility module that separates a polyphonic cable into individual monophonic cables. |
| **Square wave** | A waveform that alternates between two fixed voltages. Pulse width determines the on/off ratio. Rich in odd harmonics, hollow sounding. |
| **Step** | One position in a sequencer's cycle. Each step typically outputs a programmed pitch CV and gate. |
| **Sum** | Adds all channels of a polyphonic cable into a single monophonic output. |
| **Sync** | Hard sync resets an oscillator's phase to zero when a trigger arrives, creating a distinctive harsh tone. Soft sync is a gentler version. |
| **Tempo** | Speed of a clock or pattern, measured in BPM. |
| **Track & hold** | Like sample and hold, but continuously follows the input while a gate is high, then holds the value when the gate closes. |
| **Trigger** | A brief voltage pulse (a few milliseconds) indicating "fire now." Advances sequencers, fires drum hits, resets LFOs. |
| **Triangle wave** | A waveform that rises and falls linearly. Softer than sawtooth, with fewer harmonics. |
| **Unipolar** | A signal that stays positive, typically 0 V to +10 V. Envelope output is usually unipolar. |
| **V/Oct** | Volts per octave. The pitch CV standard where each 1 V increase raises pitch by one octave. See also: 1V/oct. |
| **VCA** | Voltage-Controlled Amplifier. Controls signal level using a CV input. Essential for shaping amplitude envelopes. |
| **VCF** | Voltage-Controlled Filter. Shapes the frequency content of a signal. Cutoff frequency and resonance are typically CV-controllable. |
| **VCO** | Voltage-Controlled Oscillator. An audio-rate oscillator whose frequency is set by a CV input, typically following the 1V/oct standard. |
| **Velocity** | In MIDI, how hard a key was pressed. MIDI modules in VCV Rack can output velocity as a CV (typically 0–10 V). |
| **Vibrato** | Periodic pitch modulation, created by patching an LFO to a VCO's FM input. |
| **Wavefolder** | A waveshaper that folds the waveform back on itself when it exceeds a threshold, adding harmonics and creating metallic or bell-like timbres. |
| **Waveform** | The shape of one cycle of an oscillator's output: sine, triangle, sawtooth, square, or custom wavetable. |
| **Wavetable** | A stored waveform that an oscillator scans through. Wavetable position can be modulated to morph between waveforms. |

---

## Third-Party Plugin Glossary

Terms specific to popular free VCV Rack plugins.

| Term | Definition |
|------|-----------|
| **Alright Devices** | Plugin maker known for Chronoblob2 delay — a high-quality dub-style stereo delay with tempo sync. |
| **Bernoulli Gate** | An ML Modules gate splitter that routes each incoming trigger randomly to one of two outputs based on a probability setting. Creates random gate patterns from a regular clock. |
| **Bogaudio** | A comprehensive free plugin providing VCOs, filters, envelopes, LFOs, mixers, S&H, and utilities. Known for clean behavior and CV inputs on all parameters. |
| **Chronoblob2** | Alright Devices' flagship delay module. Stereo, tempo-syncable, with a tone control on the feedback path for dark dub-style repeats. |
| **Count Modula** | A large free plugin (80+ modules) specializing in sequencers, Euclidean rhythm generators, logic, and utility modules. Per-step probability is its standout sequencer feature. |
| **Drone** | A sustained, non-rhythmic sound providing harmonic foundation. Created with slow attack/release envelopes and no gate-off event. Common in ambient and psybient music. |
| **Euclidean rhythm** | A rhythm that distributes a number of hits as evenly as possible across a number of steps. 3 hits in 8 steps produces the son clave pattern. Generates interlocking polyrhythms. |
| **Impromptu Modular** | Free plugin known for Clocked (master clock with swing and multiple divisions) and Phrase-Seq16 (phrase-chaining sequencer with slide and ties). |
| **ML Modules** | A small focused free plugin providing Bernoulli Gate, S&H, quantizer, and basic utilities. |
| **Morphader** | A Befaco crossfader that blends two signals using CV control. Useful for transition effects and live mixing. |
| **Muxlicer** | A Befaco step sequencer combined with a signal multiplexer. Each step has an independent clock division, enabling polyrhythmic step sequences. |
| **Plateau** | Valley's plate reverb based on the Dattorro algorithm. Produces long lush reverb tails; widely considered the best free reverb for VCV Rack. |
| **Polyrhythm** | Two or more rhythmic patterns running simultaneously at different rates or step counts, creating a shifting relationship between them that only resolves after a number of bars. |
| **Psybient** | Genre combining psychedelic and ambient electronic music. Characteristics: slow BPM (80–100), minor keys, enormous reverb, slowly evolving timbres, hypnotic repetition. |
| **Rampage** | A Befaco dual function generator that acts as envelope, LFO, slew limiter, or oscillator. Its comparator output produces rhythmic gates from two interacting waveforms. |
| **Slew limiter** | A module that smooths abrupt CV changes by limiting how fast the voltage can rise or fall. Creates portamento (pitch glide) and organic-feeling filter sweeps. |
| **Stoermelder PACK-ONE** | A free plugin with CV-MAP (map any CV to any parameter), Transit (preset morphing), and other performance utilities. Among the most useful free utility plugins. |
| **Surge XT** | A free plugin porting the Surge synthesizer's algorithms to VCV Rack. Provides high-quality wavetable, FM, and spectral oscillators plus multiple filter topologies including comb filters. |
| **Topograph** | Valley's drum sequencer based on the Mutable Instruments Grids algorithm. Generates kick/snare/hat patterns with a density control; ranges from sparse to busy. |
| **Valley** | A free plugin known for Plateau (reverb), Topograph (drum sequencer), and Dexter (wavetable/FM oscillator). |

---

## Where to go next

- [Signal Flow & Concepts](mental-model.md) — these terms in context
- [How a Patch Works](how-a-patch-works.md) — see how these concepts connect
- [VCO](vco.md) — oscillator modules in detail

---

*Version: 2026-06-17.*
