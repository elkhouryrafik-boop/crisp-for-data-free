# Quantification — From Fuzzy Goals to Measurable Criteria (Including Cancellation Criteria)

Translating a stakeholder's natural-language goal into a measurable success criterion is the single most error-prone step in Phase 1. The CRISP-DM 1.0 guide (Chapman et al. 2000) names the artifact ("Business Success Criteria") but provides only the example *"reduce churn to 5%."* The literature has since converged on a small set of techniques. The skill uses all of them in combination at Steps 6 and 8.

The empirical finding (Studer et al. 2021; Schröer, Kruse & Gómez 2021): projects with documented, numerical success criteria at Phase 1 are markedly more likely to reach a defensible Evaluation phase. Projects whose success criteria are qualitative ("useful," "actionable," "insightful") effectively cannot fail at Evaluation — and therefore effectively cannot succeed either, because no result distinguishes a success from a failure.

---

## 1. SMART criteria

**Origin.** George Doran, *Management Review* (1981).

**Acronym.** Specific, Measurable, Achievable, Relevant, Time-bound.

**Worked through:**

| Letter | Test | Common failure |
|---|---|---|
| Specific | Is the subject of the criterion an unambiguous noun? | "improve user experience" — improve what, for whom? |
| Measurable | Is there a unit of measure? | "high quality" — measured by what scale? |
| **Achievable** | Is there a defensible argument it *can* be hit with available data and resources? | **Most often skipped.** Requires showing the threshold is feasible, not only desirable. |
| Relevant | Does hitting this criterion move the decision the project exists to support? | "increase data sources integrated to 20" — relevant to what decision? |
| Time-bound | Is there a deadline? | "eventually" / "ongoing" — not a deadline. |

**Use at:** Step 6, every row of the business success criteria table.

**The Achievable trap.** Achievability is the SMART letter most often skipped in data projects. The discipline: write the criterion, then write *one sentence* explaining why the threshold can be hit. If you cannot write the sentence, the criterion is aspirational, not SMART.

---

## 2. Translation table (business → data-product success)

A two-column document — business goal on the left, data-product success criterion on the right, with an arrow and a **rationale paragraph** in between. The rationale paragraph is the load-bearing element; without it, the threshold is arbitrary.

**Template:**

| Business goal | → | Data-product success criterion | Rationale |
|---|---|---|---|
| *"Reduce churn"* | → | *"Identify 80% of customers who will churn in next 30 days at precision ≥ 60%, refreshed weekly"* | *"The retention team can act on ~200 contacts per week; precision below 60% wastes their capacity. Recall below 80% leaves money on the table at the volume the team can absorb."* |

**For pipeline / data-product projects (no model):**

| Business goal | → | Data-product success criterion | Rationale |
|---|---|---|---|
| *"Direct greening budget to blocks where intervention is feasible"* | → | *"Top-15 shortlist with non-null sub-scores in ≥ 95% of decision units; each entry mapped to an existing Ajuntament budget line; input data ≤ 18 months old"* | *"Planner can review 15 entries per cycle; sub-score completeness below 95% means the ranking is comparing apples and oranges; freshness > 18 months means inputs predate the last Eixos Verds rollout."* |

**Use at:** Step 6, between the two tables.

---

## 3. Counterfactual quantification

**Origin.** Causal inference; popularised in data-product literature (Domino 2017).

**Mechanic.** For each candidate success criterion, ask:

> *"What would the decision-maker do differently if the product met spec vs. failed spec?"*

If the answer is **"nothing,"** the criterion is wrong.

**Use at:** Step 6 (filter step) and Step 8 (criterion for cancellation triggers).

**Worked example.**
- Candidate criterion: *"output published as CC-BY GeoJSON."*
- Counterfactual: if we publish as GeoJSON, planner uses it; if we publish as PDF, planner... also uses it.
- Verdict: not load-bearing for the *primary* decision. Demote to a sub-criterion (Distribution), don't make it a top-line success criterion.

---

## 4. Cancellation thresholds (CRISP-ML(Q) requirement)

**Origin.** Studer et al. (2021), CRISP-ML(Q). The novel contribution beyond CRISP-DM 1.0.

**Mechanic.** For each Phase-1 success criterion, define the conditions under which the project should be **stopped rather than continued.** Document them in the risk register at Step 8 as rows where "Triggers cancellation? = Yes."

**Why it matters.** Most Phase-1 templates assume the project will go forward. The cancellation criterion is the cleanest safeguard against sunk-cost continuation — the situation where the team knows the project no longer makes sense but cannot find the institutional moment to say so.

**Template:**

| Finding | Why it triggers cancellation | What we do instead |
|---|---|---|
| *"No discretionary budget line exists for any recommended intervention type"* | The shortlist has no action pathway; product cannot move a decision | Reframe deliverable as institutional-blockage finding; produce policy memo |
| *"Decision unit cannot be supported by any available dataset at 2× resolution"* | Phase 2 will return "no" at the brief revisit; further work is wasted | Stop or rescope decision unit upward |
| *"Sponsor leaves the role and the new sponsor does not endorse the brief"* | No decision-maker = no decision to serve | Pause; re-do Phase 1 with new sponsor or close out |

**Use at:** Step 8. The skill refuses to advance Step 8 without at least one cancellation row.

**Diagnostic question for finding cancellation thresholds:** *"Under what specific finding from Phase 2, 3, 4, 5, or 6 should we stop this project rather than push through?"* The answer is the cancellation criterion.

---

## 5. Pre-mortem (risk surfacing for cancellation)

**Origin.** Gary Klein, *Harvard Business Review* (2007).

**Mechanic.** Imagine the project has failed at the 6-month mark. Work backwards: what happened? Why? Who knew? When did the team first ignore the signal?

**Use at:** Step 8 as an optional but recommended add-on to the risk register. Pre-mortems are particularly good at surfacing the risks that the team is **instinctively avoiding** — and those are usually the ones that become cancellation triggers.

**Prompt format.** *"It is six months from now. The project has clearly failed. Write the post-mortem paragraph. What is the first sentence?"* That first sentence usually names the cancellation criterion that was missed.

---

## 6. Composite quantification template (skill output)

The combination of techniques above produces, for each project goal, a row that looks like:

```
GOAL:        Direct greening budget to feasible blocks
SMART:       Top-15 shortlist used in ≥ 1 budget decision in next FY (owner: planning sponsor)
RATIONALE:   Budget cycle is annual; one use is the minimum signal of adoption
COUNTERFAC.: If hit: planner allocates differently. If missed: no change to status quo.
CANCEL IF:   No budget line exists for any recommended intervention type at the EOY review.
VERIFY:      Sponsor confirms in writing at end of next FY.
```

This is the structure the skill writes into `phase-1/success-criteria.md` and (for the cancellation row) into `phase-1/risks.md`.

---

## Anti-quantification patterns to refuse

- **Adjective criterion** ("useful," "actionable," "insightful") — see `anti-patterns.md` #3.
- **Vanity metric** ("number of data sources integrated") — see `anti-patterns.md` #10.
- **Counterfactually null** (would change no behavior) — see `anti-patterns.md` #12.
- **Aspirational achievability** ("we hope to achieve 99% accuracy") with no feasibility argument.
- **Deadline-free criterion** ("ongoing improvement") — not measurable.
- **Owner-free criterion** (passive voice — *"will be improved"*) — no one is accountable.

Each is a refuse-to-proceed pattern at Step 6.

---

## The bottom line

A success criterion that cannot fail cannot succeed. The discipline of quantification is the discipline of being willing to be **wrong on the record**. The cancellation criterion is the discipline of being willing to be wrong on the record about whether to *continue at all*. Both are non-negotiable for Phase-1 closure.
