# crisp-for-data — Phase 1: Business Understanding (free)

**Earn the right to build the pipeline — before touching any data.**

[![Free on Agensi](https://img.shields.io/badge/Agensi-Free%20listing-6366f1)](https://www.agensi.io/skills/crisp-dm-phase-1-business-understanding)

A free agent skill that forces twelve decision artifacts onto disk *before* any data is downloaded, then refuses to let the project advance until every one of them exists. Works with any coding agent that reads the `SKILL.md` convention — Claude Code, Codex CLI, Hermes, Cursor, Gemini CLI, Copilot, Windsurf.

**▶ [Get this skill on Agensi](https://www.agensi.io/skills/crisp-dm-phase-1-business-understanding)** (free) — or clone it below.

---

## Why this exists

Most data projects fail before the first download — not technically, definitionally. The team builds exactly what was asked for, then discovers at evaluation that what was asked for was not what was needed. This skill blocks that failure at the only point where it is cheap to fix: the start.

The anti-pattern it exists to kill:

> Open the dataset → run a notebook → produce a chart → invent the decision the chart supports → present.

## What it produces

Twelve artifacts, each with a binary exit check, all written under `phase-1/`:

| Artifact | What it pins down |
|---|---|
| `decision-statement.md` | A named role at a named organization, the decision, its cadence, the mechanism it feeds. Not "stakeholders". |
| `heilmeier.md` | The DARPA catechism — including "who cares?" and "what are the mid-term and final exams?" |
| `five-whys.md` | Chain from symptom to root cause. |
| `decision-unit.md` | Spatial, temporal and thematic unit as numbers (30 m pixel, annual, census tract) — not adjectives. |
| `output-spec.md` | Schema, units, CRS, license, refresh cadence. |
| `success-criteria.md` | Numbers with a deadline and an owner. Adjectives are refused on entry. |
| `situation.md` | What exists, what does not, who holds it. |
| `risks.md` | A register **with a cancellation criterion** — its absence is itself a defect. |
| `glossary.md` | Every contested term defined once. |
| `product-card-draft.md` | Includes at least two named out-of-scope uses. |
| `project-plan.md` | Phases, artifacts, owners, dates. |
| `exit-checklist.md` | Signed. One unticked box means Phase 1 is not done. |

## What it refuses

- **Solutionism** — "we want to use LLMs / GIS / satellite imagery to…" is a tool, not a problem.
- **"Stakeholders"** — a named role at a named organization, or nothing.
- **Adjective success criteria** — "useful", "actionable", "better" are blocked. Numbers, deadlines, owners.
- **Pre-emptive data hunting** — Phase 1 is not done; data comes later.
- **No cancellation criterion** — a project with no written reason to be killed.

## Install

Clone or copy this folder into your agent's skills directory:

```bash
git clone https://github.com/elkhouryrafik-boop/crisp-for-data-free.git \
  ~/.claude/skills/crisp-dm-phase-1-business-understanding   # Claude Code
# ~/.codex/skills/...        Codex CLI
# ~/AppData/Local/hermes/skills/<category>/...   Hermes
```

Requires Python 3 (standard library only) for the two gate scripts. Without Python, the gates degrade to the same checklists run by hand.

## Use

Invoke it at the very start of a project — "frame this data project", "Phase 1", "scope this" — then run the gate before moving on:

```bash
python scripts/crisp_status.py <project-root>          # where does the project stand?
python scripts/gate_check.py --phase 1 --root <root>   # binary gate — exit 1 blocks
```

```
$ python scripts/gate_check.py --phase 1 --root .
[FAIL] phase-1/success-criteria.md contains adjectives: "actionable"
[FAIL] phase-1/risks.md has no row with "Triggers cancellation = Yes"
[FAIL] phase-1/decision-statement.md: decision-maker is "stakeholders"
GATE 1: FAIL (3 blocking defects) — exit code 1
```

Binary, not vibes.

## Get the full cycle

Phase 1 is the gate the whole cycle runs on. The complete suite — **Phases 0–6**: data acquisition, data understanding, preparation with a YAML data contract, the analytical core, evaluation with a go/no-go memo, and a FAIR/DOI release handoff — plus the contract validator, 52 deep-dive references and a fully worked example, is published on **Agensi**:

**→ [crisp-for-data — the full suite, $49](https://www.agensi.io/users/rafik-elkhoury)** · **→ [this free edition on Agensi](https://www.agensi.io/skills/crisp-dm-phase-1-business-understanding)**

The free edition is deliberately self-contained but visibly incomplete: `crisp_status.py` names the next phase on every run, and `quality-gates.md` stops at the Phase 1 → 2 boundary with a pointer to the suite.

## Built on

CRISP-DM 1.0 (Chapman et al. 2000) · CRISP-ML(Q) quality assurance (Studer et al. 2021) · the Heilmeier catechism (DARPA) · SMART criteria · project pre-mortems (Klein). Full citations ship in `references/phase-1/citations.md`.

## License

Proprietary — free to install and use through your own AI agent, for personal or commercial projects. **No redistribution, resale, or sublicensing.** See [LICENSE](LICENSE).

---

*by [Rafik Elkhoury](https://www.agensi.io/users/rafik-elkhoury) — urbanist and AI strategist for the built environment.*
