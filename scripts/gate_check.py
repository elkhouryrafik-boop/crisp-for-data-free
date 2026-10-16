#!/usr/bin/env python3
"""gate_check.py — binary gate enforcement, free wedge edition (Phases 0-1).

Validates that a phase's required artifacts exist and are non-empty, parses
the checklist for unticked boxes, and refuses advancement on any red failure.

Usage:  python scripts/gate_check.py --phase N [--root PROJECT_ROOT]   (N = 0 or 1)
Exit codes: 0 = all red items pass, 1 = at least one red failure,
            2 = phase not covered by this edition (Phases 2-6 are in the paid suite).
Stdlib only.
"""
import argparse, re, sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):  # legacy consoles (cp437/cp932...) must not crash on '—'
    sys.stdout.reconfigure(errors="replace")
    sys.stderr.reconfigure(errors="replace")

RED = {
    0: ["phase-0/calibration.md"],
    1: ["phase-1/decision-statement.md", "phase-1/decision-unit.md",
        "phase-1/output-spec.md", "phase-1/success-criteria.md",
        "phase-1/situation.md", "phase-1/risks.md", "phase-1/glossary.md",
        "phase-1/product-card-draft.md", "phase-1/project-plan.md",
        "phase-1/heilmeier.md", "phase-1/five-whys.md",
        "phase-1/exit-checklist.md"],
}
CHECKLISTS = {1: "phase-1/exit-checklist.md"}

def check(root, rel):
    p = root / rel
    return p.is_file() and p.stat().st_size > 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", type=int, required=True, choices=range(0, 7))
    ap.add_argument("--root", default=".")
    a = ap.parse_args()
    if a.phase not in RED:
        print(f"Phase {a.phase} gates ship with the crisp-for-data suite (paid) — this free edition covers Phases 0-1.")
        sys.exit(2)
    root = Path(a.root).resolve()
    fails, details = [], {}

    rows = [(rel, check(root, rel)) for rel in RED[a.phase]]
    fails += [label for label, ok in rows if not ok]

    # checklist parsing: unticked boxes in the exit checklist
    cl = CHECKLISTS.get(a.phase)
    if cl and (root / cl).is_file():
        txt = (root / cl).read_text(encoding="utf-8", errors="ignore")
        open_boxes = re.findall(r"(?m)^\s*[-*+]\s*\[ \][ \t]*([^\n]*)", txt)
        if open_boxes:
            label = f"{cl} ({len(open_boxes)} unticked boxes)"
            fails.append(label)
            details[label] = open_boxes

    print(f"Gate check — Phase {a.phase} — {root}\n")
    for label, ok in rows:
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
    labels = dict(rows)
    for f in fails:
        if f not in labels:
            print(f"  FAIL  {f}")  # itemizes unticked boxes
            for item in details.get(f, [])[:10]:
                print(f"          - [ ] {item}")
            if len(details.get(f, [])) > 10:
                print(f"          - ... and {len(details[f]) - 10} more")
    print()
    if fails:
        print(f"RESULT: NEEDS WORK — {len(fails)} red failure(s). Do not advance.")
        sys.exit(1)
    print("RESULT: PASS — gate open, advance to the next phase.")

if __name__ == "__main__":
    main()
