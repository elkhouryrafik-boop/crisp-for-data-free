#!/usr/bin/env python3
"""crisp_status.py — where is this CRISP-DM pipeline project? (free wedge edition, Phases 0-1)

Scans a project root for the Phase 0 and Phase 1 artifacts, reports
DONE / IN PROGRESS / NOT STARTED for each plus the missing artifacts that
block advancement, then points at the next action. A phase is reported as
passed only when scripts/gate_check.py would exit 0 for it.

Usage:  python scripts/crisp_status.py [project_root]   (default: cwd)
Stdlib only. Exit code always 0 (informational).
"""
import re, sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):  # legacy consoles (cp437/cp932...) must not crash on '—'
    sys.stdout.reconfigure(errors="replace")
    sys.stderr.reconfigure(errors="replace")

GATE1 = ["phase-1/decision-statement.md", "phase-1/decision-unit.md",
         "phase-1/output-spec.md", "phase-1/success-criteria.md",
         "phase-1/situation.md", "phase-1/risks.md", "phase-1/glossary.md",
         "phase-1/product-card-draft.md", "phase-1/project-plan.md",
         "phase-1/heilmeier.md", "phase-1/five-whys.md",
         "phase-1/exit-checklist.md"]
CHECKLIST1 = "phase-1/exit-checklist.md"

def exists_nonempty(root, rel):
    p = root / rel
    return p.is_file() and p.stat().st_size > 0

def phase1_state(root):
    """Return (missing, present): blockers, and whether any artifact exists."""
    missing = [r for r in GATE1 if not exists_nonempty(root, r)]
    present = any(exists_nonempty(root, r) for r in GATE1)
    d = root / "phase-1"
    if d.is_dir() and any(f.is_file() for f in d.rglob("*")):
        present = True
    if (root / CHECKLIST1).is_file():
        boxes = re.findall(r"(?m)^\s*[-*+]\s*\[ \]", (root / CHECKLIST1).read_text(encoding="utf-8", errors="ignore"))
        if boxes:
            missing.append(f"{CHECKLIST1} ({len(boxes)} unticked boxes)")
    return missing, present

def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    print(f"CRISP-DM project status — {root}\n")
    current = None
    if exists_nonempty(root, "phase-0/calibration.md"):
        print("  [x] Phase 0  — DONE — calibration.md present")
    else:
        print("  [ ] Phase 0  — no calibration.md yet (audience / interaction mode)")
        current = 0
    missing, present = phase1_state(root)
    if not missing:
        print("  [x] Phase 1  — DONE — gate PASSED")
    else:
        state = "IN PROGRESS" if present else "NOT STARTED"
        print(f"  [ ] Phase 1  — {state}; missing/blocked:")
        for m in missing[:8]:
            print(f"        - {m}")
        if len(missing) > 8:
            print(f"        - ... and {len(missing)-8} more")
        if current is None:
            current = 1
    print()
    if current is None:
        print("Next action: complete Phase 2 -> load from the crisp-for-data skill")
    elif current == 0:
        print("Next action: complete Phase 0 (write phase-0/calibration.md).")
        print(f"  Gate: python scripts/gate_check.py --phase 0 --root \"{root}\"")
    else:
        print("Next action: complete Phase 1.")
        print("  Load references/phase-1-*.md from this skill.")
        print(f"  Gate: python scripts/gate_check.py --phase 1 --root \"{root}\"")

if __name__ == "__main__":
    main()
