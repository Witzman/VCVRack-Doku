# Your First Patch

This tutorial takes you from a blank VCV Rack canvas to a working, playable sound using only the modules included with VCV Rack Free. It should take about ten minutes.

---

## What you'll build

A basic synthesizer voice: an oscillator shaped by a filter and an amplitude envelope, played from your computer keyboard via MIDI.

---

## Step 1 — Open a new patch

Launch VCV Rack. If a patch is already open, choose **File > New** to start fresh.

---

## Step 2 — Add the AUDIO module

Press **Space** to open the module browser. Search for **Audio 8** or just **Audio**. Add the **Audio 8** module (VCV Core). This is your connection to your speakers.

Click the device display on the module and select your audio output device. If you don't see one, check that your audio interface or built-in speakers are connected and not in use by another application.

---

## Step 3 — Add MIDI to CV

Open the browser again and add **MIDI to CV** (VCV Core). Click its display and select your MIDI keyboard, or select **Computer keyboard** to use your computer's typing keys as a piano.

You now have a V/Oct output (pitch) and a Gate output on this module.

---

## Step 4 — Add VCO

Add **VCO** (VCV Free). Connect the **MIDI to CV**'s **V/Oct** output to the VCO's **PITCH** input. You've just told the oscillator to track your keyboard.

Run the engine (click the power button in the toolbar) and press a key. Nothing sounds yet — the oscillator is running, but nothing is carrying its signal to the output.

---

## Step 5 — Add ADSR

Add **ADSR EG** (VCV Free). Connect **MIDI to CV**'s **Gate** output to the ADSR's **Gate** input. The envelope will now fire when you press a key.

---

## Step 6 — Add VCA

Add **VCA** (VCV Free). Connect the VCO's **SAW** output to the VCA's **CH** input. Connect the ADSR's **Envelope** output to the VCA's **CV** input.

Connect the VCA's **CH** output to the **Audio 8**'s **L** input (and optionally also to **R** for mono-to-stereo).

Press a key. You should now hear a sawtooth note that fades with the release time of the envelope.

---

## Step 7 — Add VCF

Add **VCF** (VCV Free). Insert it between the VCO and the VCA: disconnect the VCO from the VCA, then connect the VCO's **SAW** output to the VCF's **IN** input, and the VCF's **LPF** output to the VCA's **CH** input.

Turn the VCF's **Cutoff** knob to a lower value — around 9 o'clock. Press a key. The sound is now darker. Turn Resonance up for a more nasal character.

---

## Step 8 — Modulate the filter

Connect a second cable from the ADSR's **Envelope** output to the VCF's **Freq** input. Turn the VCF's Freq CV knob (small knob next to the Freq input) up to about 3 o'clock.

Now each note attack briefly opens the filter before it closes back down. This is the classic subtractive synthesis "envelope filter" effect.

---

## Step 9 — Save your patch

Press **Ctrl+S** and save the patch somewhere you'll find it.

---

## Where to go next

- [How a Patch Works](how-a-patch-works.md) — understand what each connection is doing
- [Patching Use Cases](patching-use-cases.md) — extend this patch into a bassline or add effects
- [Fundamental Modules](fundamental-modules.md) — full parameter reference for every module you used here

---

*Version: 2026-06-17.*
