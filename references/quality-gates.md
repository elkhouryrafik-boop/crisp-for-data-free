# Quality Gates — the CRISP-ML(Q) Overlay

> **Packaging note.** Free edition: this file covers the G0 and G1->G2 gates only; the full gate table ships with the crisp-for-data suite.

The principle: in canonical CRISP-DM, quality assurance is implicit. CRISP-ML(Q) (Studer et al. 2021) makes it explicit — quality is a **task in every phase**, not an audit at the end. This file defines the binary gates between phases, what red (blocking) vs amber (warning) means, and which script enforces each gate.

## How to use this file

- After completing a phase, run `scripts/gate_check.py --phase N --root .` — it prints PASS/FAIL per artifact.
- A **red** failure blocks advancement. No negotiation, no "temporary waivers". The fix is to return to the phase, not to soften the gate.
- An **amber** warning does not block, but must be **recorded** in the decision log with a reason and an owner. Silent amber-skipping is how pipelines rot.
- The default verdict at every gate is **NEEDS WORK**. Evidence flips it, not optimism.

## The gate table

**Legend.** *Script-enforced* reds are checked by `scripts/gate_check.py` — the exit code blocks. *Reviewer-enforced* reds are checked by the agent/reviewer following this table — they are not machine-checked. Amber lists in this table are indicative; the scripts warn on the subset listed in `scripts/gate_check.py` AMBER.

**G0 → G1 (calibration → business understanding)**
- RED *(script-enforced)*: `phase-0/calibration.md` exists (audience, interaction mode).
- RED *(reviewer-enforced)*: the problem statement is a decision, not a technology ("that is a tool, not a problem").

**G1 → G2 (business understanding → data understanding)**
- RED *(script-enforced)*: the 12 Phase-1 artifacts exist and are non-empty.
- RED *(reviewer-enforced)*: artifact content meets the bar (decision statement with 5 slots filled — role, organization, decision, cadence, mechanism; Heilmeier catechism; Five Whys; decision unit as numbers; output spec with schema/units/CRS/license; numerical success criteria with deadline + owner; situation inventory; risk register ≥ 5 rows with a cancellation criterion; glossary; product card draft with ≥ 2 out-of-scope uses; project plan; exit checklist).
- RED *(script-enforced)*: `phase-1/exit-checklist.md` has no unticked `- [ ]` boxes.
- AMBER: sponsor sign-off recorded for the decision statement (advisory; the reviewer must confirm sign-off in client contexts).

**G2 → G3 … G6 → release.** The remaining gates (G2->G3 through G6->release) ship with the full **crisp-for-data** suite.

## Gate hygiene rules

1. **Gates are binary.** "Mostly done" is not done. `gate_check.py` exits 1 on any red failure — believe it.
2. **No gate waivers.** Under deadline pressure the correct move is to descope or slip, in writing, in the decision log — never to wave a gate.
3. **Amber needs an owner.** Every amber skip gets a decision-log entry: what was skipped, why, who owns the risk, when it bites.
4. **Grade your own homework is the Phase-1 sin.** The sign-off needs the actual decision-maker or their named representative. A team reviewing its own artifacts against its own criteria is theatre.
5. **A clean no-go is a successful gate.** Killing or iterating a project on defensible evidence is the system working. Sunk cost is not a gate argument (Kahneman 2011).

## References

- Studer et al. (2021). Towards CRISP-ML(Q). *Machine Learning and Knowledge Extraction* 3(2) — the QA overlay this file implements.
- Chapman et al. (2000). *CRISP-DM 1.0* — the phase/task model the gates sit on.
- `scripts/gate_check.py` — the executable version of the script-enforced reds in this table (existence/non-empty and checklist checks; the reviewer-enforced reds are not machine-checked).
- `scripts/crisp_status.py` — phase-progress reporter.
- Each phase file's own exit criteria — this file is the between-phase summary, not a replacement.
