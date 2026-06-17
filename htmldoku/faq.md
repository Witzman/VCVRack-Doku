# FAQ

Common questions and fixes, grouped by topic.

---

## No sound

**The engine is running but I hear nothing.**
Check that the AUDIO module is added to your patch, that the correct audio device is selected in its display, and that a cable is connected to its L input. Also confirm the Engine is on (toolbar power button).

**I connected everything but still no sound.**
Trace the signal chain manually: right-click each module and look for bypass mode being enabled. Check that the VCA's Level knob is above zero and that a CV signal (envelope or direct voltage) is reaching its CV input. A VCA with nothing in its CV input and Level at minimum produces silence.

**The ADSR fires but I hear only a click, not a sustained note.**
The Sustain knob is probably at zero. Raise it so the envelope holds a level while the gate is open.

**Sound plays for one note then stops.**
Check the ADSR's Release time. If Release is at minimum, the sound cuts off the moment the gate closes. Raise Release for a fade-out.

**I hear sound in the toolbar meters but not from my speakers.**
Select the correct audio output device in the AUDIO module. Also check system volume and that your audio interface is not routing to a different output.

**Patching a cable from VCO to AUDIO directly produces sound. Patching it through a VCA produces silence.**
The VCA's CV input has nothing in it, or the Level knob is at zero. Either raise the Level knob or connect a CV signal (like an ADSR or a constant +10 V voltage) to the CV input.

---

## Tuning and pitch

**My VCO sounds out of tune with everything else.**
The VCO is using an exponential FM input where a linear one (or V/oct) is expected, or vice versa. Also check for a DC offset or attenuverter between your pitch source and the VCO's PITCH input — any voltage scaling or offset here shifts pitch.

**Octave is right but the note is slightly off.**
A small offset is being added somewhere in the CV chain, or an attenuverter is scaling the 1V/oct signal slightly away from 1:1. Check all attenuverters and offset knobs between your pitch source and the VCO.

**The Quantizer doesn't seem to quantize.**
Check that a cable is connected to the Quantizer's Pitch input, not just its output. Also confirm the right scale is selected (right-click the module).

**Two VCOs are slightly detuned and I want them perfectly in tune.**
Right-click both VCOs, choose Initialize, then repatch. Or use the Octave module to shift pitch in exact octave increments without introducing detune.

---

## CPU and performance

**CPU usage is very high.**
Reduce the number of oversampling-heavy modules (some VCOs and effects use 8× or 16× oversampling). Lower the sample rate in the AUDIO module. Bypass modules you're not currently using. Close other CPU-heavy applications.

**VCV Rack crackles or stutters.**
Increase the buffer size in the AUDIO module. A buffer of 256 or 512 samples is a good starting point. Crackle usually means the buffer is too small for the CPU to fill in time.

**A specific module is causing a CPU spike.**
Bypass modules one at a time to identify the culprit. Effects modules (reverb, convolution) are common offenders at high buffer quality settings.

---

## MIDI

**My MIDI keyboard sends notes but I hear nothing in VCV Rack.**
Confirm the MIDI-CV module is added and your device is selected in its display. Check that V/Oct is connected to the VCO's PITCH input and Gate is connected to the ADSR's Gate input.

**Only one note plays at a time (no polyphony).**
MIDI-CV in its default mode is monophonic. To enable polyphony, right-click the MIDI-CV module and change the polyphony mode to a chord or poly mode. Then use polyphonic-capable modules (most VCV Free modules support polyphony) for the rest of the chain.

**Pitch bend doesn't work.**
Connect the MIDI-CV module's **Pitch Bend** output to the VCO's FM input. Set the FM attenuverter to a value that corresponds to your desired bend range (a full semitone is roughly 0.083 V, so for ±2 semitone bend, use an attenuverter that scales the ±5 V bend signal to ±0.17 V).

---

## Polyphony

**I want to play chords but the sound is still monophonic.**
Check that all modules in your chain support polyphony (most VCV Free modules do). The polyphonic signal is only as wide as the narrowest module in the chain. If one module in the middle is monophonic, it collapses the signal to one channel.

**I'm using a polyphonic oscillator but it outputs identical pitches for every voice.**
The pitch input to the VCO is monophonic — likely a single-channel cable. Make sure a polyphonic pitch CV is reaching the VCO's PITCH input.

**How do I check how many channels a cable carries?**
Hover over any cable or port to see a tooltip with the current channel count. A polyphonic cable appears thicker and slightly colored based on channel count.

---

## Common beginner mistakes

**I'm getting audio feedback / runaway loud noise.**
An output is connected back into an earlier input in the same chain, creating a feedback loop. Trace the signal path and find the loop.

**My LFO modulation is extremely fast.**
The LFO's rate knob is set high, or you're patching an audio-rate VCO output to a CV destination and getting audio-rate modulation. Turn the rate down or use the LFO module instead of VCO for slow modulation.

**Notes overlap or hang when playing fast.**
The ADSR's Release time is long. Short Release stops the previous note before the next one starts.

**I can't find a module I installed.**
Restart VCV Rack. If the plugin installed correctly, it will appear in the browser after restart. Check the plugin manager for any installation errors.

---

## Where to go next

- [Using VCV Rack](userguide.md) — interface guide
- [How a Patch Works](kernablauf.md) — signal chain fundamentals
- [Patching Use Cases](anwendungsfaelle.md) — step-by-step patching recipes

---

*Version: 2026-06-17.*
