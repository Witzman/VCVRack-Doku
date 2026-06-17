# Audio Output

The Audio Output module connects your patch to your computer's audio interface, routing the final mixed signal to speakers or headphones. Without this module, no sound leaves VCV Rack regardless of what you build. Audio Output is almost always the last module in the signal chain.

## Audio (VCV Core)

The VCV Core Audio module is included with VCV Rack Free. It appears in the module browser under the VCV menu. It supports stereo output (and input for recording or processing external audio) and connects to whatever audio device is selected in VCV Rack's Engine settings.

| Input | Type | Description |
|-------|------|-------------|
| 1 (L) | Audio | Left channel audio input |
| 2 (R) | Audio | Right channel audio input |
| Additional inputs | Audio | Map to interface channels 3+ if available |

| Parameter | Description |
|-----------|-------------|
| AUDIO DEVICE | Select which audio interface to use |
| SAMPLE RATE | Set the audio processing rate |
| BLOCK SIZE | Set the buffer size — lower = less latency |

**Patching tips:** Connect your final Mixer's L and R outputs to Audio's inputs 1 and 2. If your patch is mono, connect the mono output to input 1 — it will play through the left channel only. For centered mono, connect the same mono signal to both inputs 1 and 2. Keep the level into Audio below clipping: VCV Rack's audio engine clips at ±10V. Use a VCA or mixer level to keep peaks comfortable.

**Latency settings:** Lower BLOCK SIZE reduces latency but increases CPU load and risk of audio glitches. Start at 256 samples and reduce if you need more responsive real-time performance. 64 samples is achievable on most modern computers with a good audio interface; 512 is safer for complex patches.

**Audio interface setup:** VCV Rack works with any ASIO (Windows), CoreAudio (Mac), or ALSA/JACK (Linux) device. Built-in laptop audio works for getting started but introduces latency. A dedicated USB audio interface (even a basic one) dramatically improves latency and sound quality.

### VCV Rack audio routing (no module needed)

On Mac, audio can be routed from VCV Rack to a DAW using a virtual audio driver (BlackHole, Loopback, etc.). This allows recording or processing VCV Rack output in real time inside a DAW without Rack Pro.

### Audio 16 (VCV Core)

An extended Audio module supporting up to 16 input and output channels — useful for multichannel audio interfaces or when routing audio between VCV Rack and a DAW via a multichannel interface.

## Setting up audio for the first time

1. Open VCV Rack and add the Audio module from the VCV menu in the module browser.
2. Click the AUDIO DEVICE display on the module and select your audio interface.
3. Set SAMPLE RATE to 44100 Hz or 48000 Hz (match your interface's native rate if known).
4. Set BLOCK SIZE to 256 to start.
5. Connect your patch's final output to Audio inputs 1 and 2.
6. Turn your system volume to a moderate level before running the patch.

If you hear clicks or dropouts, increase the BLOCK SIZE. If VCV Rack shows a high CPU meter, reduce the number of active modules or increase BLOCK SIZE.

## Where to go next

- [Mixer](mixer.md) — the module immediately before Audio Output
- [Using VCV Rack](userguide.md) — full interface setup guide
- [Your First Patch](first-patch.md) — step-by-step from VCO to Audio Output
- [MIDI to CV](midi-cv.md) — adding MIDI input alongside audio output

---
*Version: 2026-06-17.*
