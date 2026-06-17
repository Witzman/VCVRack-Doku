# Using VCV Rack

This page covers the VCV Rack interface: how to add and remove modules, draw cables, control parameters, save patches, and set up audio and MIDI. If you want a guided walkthrough of building your first patch, see [Your First Patch](first-patch.md).

---

## The rack

When you open VCV Rack, you see a scrollable rack — a virtual Eurorack case. Modules sit in the rack like hardware modules in a real case. You can scroll left and right to expand your patch as far as you need. The rack has unlimited horizontal space.

---

## Adding modules

Open the module browser by pressing the **+** button in the toolbar, pressing **Space**, or right-clicking an empty area of the rack and choosing **Add module**. The browser shows all installed plugins and modules. Search by name or tag. Double-click a module or press Enter to add it to the rack.

Modules snap to a grid. Drag them left and right to rearrange. Right-click a module for options including **Delete**, **Duplicate**, **Initialize** (reset all parameters to default), and **Bypass** (which passes audio through untouched and hides the module's processing).

---

## Drawing cables

Click any output port and drag to an input port to connect a cable. Each connection creates a new cable with a randomly assigned color. You can connect one output to multiple inputs by clicking the output again and dragging another cable — outputs are "stackable" but inputs accept only one cable at a time (unless the module explicitly merges internally).

To remove a cable, right-click it and choose **Delete**, or simply drag the cable's end away from a port and release it in empty space. To move a cable's destination, drag its connector end to a new input.

Cable colors can be changed: right-click a cable to pick a new color. Assigning colors intentionally — blue for audio, yellow for pitch, orange for gates — helps you read complex patches at a glance.

---

## Controlling parameters

Knobs, buttons, and switches make up most of a module's controls.

**Knobs** can be adjusted by dragging up (increase) or down (decrease). Hold Ctrl while dragging for fine control. Double-click a knob to type an exact value. Right-click any knob for a context menu with options to set the value, reset to default, enable MIDI learn, and connect the knob to a polyphonic CV source.

**Buttons** toggle or momentarily activate functions. Right-click for MIDI learn.

**Switches** flip between two or more positions. Click to toggle.

---

## Saving and loading patches

Save your patch with **Ctrl+S** (or Cmd+S on Mac). Patches are saved as `.vcv` files in the location you choose. Open a patch with **Ctrl+O**. VCV Rack also offers **File > Save a copy** for snapshots without overwriting.

The **Autosave** feature saves your patch automatically every few minutes. If VCV Rack crashes, the autosave file is offered on next launch.

---

## Audio settings

The **AUDIO** module connects VCV Rack to your sound card. Add it to your rack (it's in the Core category). Click the display on the module to select your audio interface and sample rate. A sample rate of 44100 Hz or 48000 Hz is standard. Higher buffer sizes reduce CPU load but add latency.

The AUDIO module's L and R inputs receive your patch's final stereo audio output. Without connecting to an AUDIO module, you won't hear anything.

---

## MIDI

The **MIDI-CV** module (in Core) converts incoming MIDI notes to pitch CV and gate signals. Select your MIDI device in the module's display. The V/Oct output sends pitch CV; the Gate output sends a gate that's high while a key is held. Additional outputs include Velocity, Aftertouch, and Mod Wheel CV.

For sending MIDI out, the **CV-MIDI** module does the reverse: converts CV signals to outgoing MIDI messages.

---

## Toolbar

The toolbar at the top of the screen has controls for:

- **Engine on/off** — starts and stops audio processing
- **BPM** — sets the master tempo for Rack's internal clock
- **Zoom** — scroll wheel or the zoom controls to make modules larger or smaller
- **Cables visible** — toggle cable visibility to declutter the view

---

## Where to go next

- [Your First Patch](first-patch.md) — put this into practice step by step
- [How a Patch Works](kernablauf.md) — understand why each connection matters
- [FAQ](faq.md) — solutions to common interface and audio problems

---

*Version: 2026-06-17.*
