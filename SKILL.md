---
name: crisp-dm-phase-1-business-understanding
description: Use at the very start of any data-pipeline or data-product project — before any data has been touched — to produce the twelve Phase-1 artifacts the project depends on (decision statement, Heilmeier catechism, Five Whys, decision unit, output specification, success criteria, situation inventory, risk register with a cancellation criterion, glossary, product card with out-of-scope uses, project plan, binary exit checklist). Triggers on "Phase 1", "business understanding", "frame the problem", "frame this project", "start a data project", "kick off", "scope this", "define success", "where do we start", "what should we build", "we want to do something with X", or any sentence whose subject is a technology rather than a decision. Refuses to proceed while the subject is a tool, the decision-maker is "stakeholders", or success criteria are adjectives. Free component of the crisp-for-data suite (Phases 0–6).
version: 1.0.1
author: Rafik Elkhoury
license: Proprietary (see LICENSE)
metadata:
  hermes:
    tags: [crisp-dm, business-understanding, data-pipeline, framing]
    related_skills: [crisp-for-data]
---

# CRISP-DM Phase 1 — Business Understanding (free edition)

## Overview

The principle is in the name: a data project that does not start by understanding the *business* — the decision, the decision-maker, the difference success would make — produces artifacts that look professional and fail the moment a stakeholder asks "what do we actually do with this?"

This skill blocks that failure mode by forcing **twelve specific artifacts onto disk before any data is touched** (all under `phase-1/` as `.md`: `decision-statement`, `heilmeier`, `five-whys`, `decision-unit`, `output-spec`, `success-criteria`, `situation`, `risks`, `glossary`, `product-card-draft`, `project-plan`, `exit-checklist`). It is the free Phase-1 component of the **crisp-for-data** suite (Phases 0–6, same author) — the discipline that earns the right to build the pipeline.

The anti-pattern it exists to prevent:

> Open the dataset → run a notebook → produce a chart → invent the decision the chart supports → present.

## When to Use

- Starting any data-pipeline or data-product project, any domain.
- "Frame this project", "kick off", "scope this", "where do we start", "what should we build".
- Any brief whose subject is a technology ("we want to use LLMs / GIS / satellite imagery to…") — the skill treats that as the solutionism anti-pattern and asks for the decision instead.
- **Don't use for:** pure software builds with no data product; continuing an existing pipeline past Phase 1 (that's the full suite's job).

## Step 0 — Calibrate

Write two lines to phase-0/calibration.md before any artifact:

1. **Audience** — `reviewer` | `client` | `self`. Every "reviewer" in the artifacts means this audience.
2. **Interaction mode** — default `recommend, don't ask`: the skill drives with recommendations and rationale; you intervene with vetoes and blocking unknowns. The Socratic prompts in the phase file are reasoning checklists, not questionnaires.

## Run it

Load `references/phase-1-business-understanding.md` and run its ten steps end-to-end. Each step writes a named artifact under `phase-1/` at the project root:

- decision statement (named decision-maker, decision, cadence, mechanism)
- Heilmeier catechism, Five Whys
- decision unit (spatial / temporal / thematic, as numbers)
- output specification (schema, units, CRS, license, refresh cadence)
- numerical success criteria — numbers with deadline and owner; adjectives blocked
- situation inventory, risk register **with a cancellation criterion**
- glossary, product card (≥ 2 out-of-scope uses), project plan, exit checklist

## Gates (executable)

```
python scripts/crisp_status.py <project-root>          # where is the project?
python scripts/gate_check.py --phase 1 --root <root>   # binary gate — exit 1 blocks
```

Phase 1 is done when the exit checklist has no unticked boxes. Deep-dives: `references/phase-1/` (artifacts, anti-patterns, elicitation techniques, quantification, citations). Phase-gate definitions: `references/quality-gates.md`.

## What Phase 1 refuses

- **Solutionism** — "that is a technology, not a problem. What decision does someone need to make better?"
- **"Stakeholders"** — a named role at a named organization or nothing.
- **Adjective success criteria** — "useful / actionable / better" blocked; numbers, deadlines, owners.
- **Pre-emptive data hunting** — Phase 1 is not done; data comes later.
- **No cancellation criterion** — its absence is itself a defect.

## What's next

Phase 2 (data understanding — the earn-the-data discipline), Phase 3 (preparation → a YAML data contract), Phase 4 (the analytical core), Phase 5 (go / iterate / kill with the Monday test), Phase 6 (FAIR / DOI release handoff) — plus the contract validator and a worked example — are in the full **crisp-for-data** suite, same marketplace, same author.

## Common Pitfalls

1. Invoking Phase 2+ work while Phase-1 artifacts are missing — `gate_check.py` will refuse; believe it.
2. Skipping calibration — the artifacts' tone and sign-off depend on the audience.
3. Softening a gate — "mostly done" is not done. NEEDS WORK is a valid outcome.
4. Skipping the cancellation criterion because the project feels too small — that is exactly when it is cheapest.

## Verification Checklist

- [ ] All twelve `phase-1/` artifacts exist and are non-empty: `decision-statement`, `heilmeier`, `five-whys`, `decision-unit`, `output-spec`, `success-criteria`, `situation`, `risks`, `glossary`, `product-card-draft`, `project-plan`, `exit-checklist`
- [ ] `gate_check.py --phase 1` exits 0
- [ ] Success criteria contain zero adjectives
- [ ] Risk register has ≥ 1 row marked "Triggers cancellation = Yes"
- [ ] Decision statement names a real role at a real organization
