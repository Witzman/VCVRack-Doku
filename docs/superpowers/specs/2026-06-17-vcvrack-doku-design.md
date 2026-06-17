---
name: vcvrack-doku-design
description: Design spec for VCV Rack patcher's handbook — audience, page set, source repos, output structure, generator overrides
metadata:
  type: project
---

# VCVRack-Doku — Design Spec

*2026-06-17*

## Goal

Patcher's handbook and module reference for VCV Rack. Audience: end users who patch and use the synth, not developers. Primary use case: knowledge base for AI-assisted patching conversations.

## Source repos

| Repo | Role |
|------|------|
| `Rack/` | Primary — platform concepts, UI, patch format |
| `Fundamental/` | Secondary — module parameter/IO accuracy |
| `Befaco/` | Secondary — module parameter/IO accuracy |
| `library/` | Secondary — ecosystem/category context |
| `Object/` | Skip — ABI internals, zero user value |

## Output

All files committed to `VCVRack-Doku/` (this repo), outside all upstream git repos.

```
VCVRack-Doku/
  htmldoku/             Markdown sources
  docs/
    index.html          GitHub Pages redirect → Rack-Doku/index.html
    Rack-Doku/          Static HTML site (GitHub Pages served from here)
  README.md
```

## Page set

| File | Audience track | Purpose |
|------|---------------|---------|
| `readme.md` | Start | Navigation by goal |
| `mental-model.md` | Start | Signal flow, CV/audio/gate, module categories |
| `kernablauf.md` | Start | How a patch works end-to-end |
| `glossary.md` | Start | Modular and VCV Rack terminology |
| `userguide.md` | Patcher | UI — cables, modules, browser, saving |
| `anwendungsfaelle.md` | Patcher | Use cases: bassline, drone, percussion, send FX, generative |
| `faq.md` | Patcher | Common problems: no sound, tuning, CPU, MIDI, polyphony |
| `first-patch.md` | Patcher | Tutorial: blank canvas to first sound |
| `fundamental-modules.md` | Modules | Reference: all Fundamental modules |
| `befaco-modules.md` | Modules | Reference: all Befaco modules |

Skipped: adrs.md, architecture.md, systemgrenzen.md, spezial-backends.md, konfiguration-betrieb.md, roles-permissions.md, notifications.md, getting-started.md

## Key presentation rules

- No Diátaxis labels in output (used internally as discipline only)
- No code citations in output (`[file:line]` stays in generator working only)
- No confidence markers in output
- No class names, file paths, or implementation details in output
- Prose over bullets; parameter tables allowed in module reference pages

## Generator config

Invocation: `Read rack-invoke.md and apply` from `rack/` workspace root.

`rack-invoke.md` contains all overrides. `generator.md` is the base process.

Pre-answered generator questions: output folder `VCVRack-Doku/Rack-Doku/`, language English, diagrams Mermaid.

Skipped generator steps: Klärungsdialog (pre-answered), git commit (manual), try-the-docs (n/a).
