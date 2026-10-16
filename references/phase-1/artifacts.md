# The Twelve Canonical CRISP-DM Phase-1 Outputs

Synthesised from CRISP-DM 1.0 (Chapman et al. 2000), IBM's operational guide (IBM 2021), CRISP-ML(Q) quality additions (Studer et al. 2021), Domino's product-orientation extensions (Domino 2017), Gebru et al. (2021) on datasheets, and Mitchell et al. (2019) on model cards.

Each is **binary** — either it exists and is signed off, or the team is not yet out of Phase 1. A vague paragraph in a doc does not count as done; each should be specific enough that a stranger could pick up the project and act on it.

---

## 1. Project background brief (≤ 1 page)

Context, antecedents, why now. Names the decision and the decision-maker (not "the user" — the named role at the named organization).

**Done when:** a reader new to the project can answer "what is this for, for whom, and why now" without asking.

---

## 2. Decision statement (1 sentence)

> *"This data product will help [decision-maker role] at [organization] decide [decision] at [cadence] by [mechanism]."*

The single most load-bearing artifact in Phase 1. If the team cannot fill all five slots, they have not yet begun.

**Done when:** five slots filled with concrete content. No "stakeholders," no "explore," no "as needed."

---

## 3. Business objectives

What the sponsoring organization will *do differently* if the project succeeds. Stated as observable changes in behavior, not as KPIs.

**Done when:** each objective is a verb + an actor + an observable change.

---

## 4. Business success criteria (SMART)

The measurable conditions under which the project will be judged a success. Each criterion is a **number with a deadline and an owner** (Doran 1981). The Achievable test is the one most often skipped: requires a defensible argument that the threshold *can* be hit with available data and resources.

**Done when:** every criterion is Specific, Measurable, Achievable, Relevant, Time-bound. No adjectives.

---

## 5. Inventory of resources

People (named, with roles and time commitments), data (named primary sources, not generic categories), compute, software, budget.

**Done when:** no entry says "the team" or "the data." Every resource has a name and an owner.

---

## 6. Requirements, assumptions, constraints

Schedule, comprehensibility (does the output need to be explainable to non-technical decision-makers?), legal and ethical (intended use, intended user, prohibited uses), security, deployment environment. Must include **explicit out-of-scope items**.

**Done when:** what is in scope and what is *out* of scope are both named.

---

## 7. Risk register

At least the top five risks, each with likelihood, impact, owner, mitigation. **Per CRISP-ML(Q) (Studer et al. 2021), this must include at least one cancellation criterion** — the explicit condition under which the project should be stopped rather than continued. Most Phase-1 templates assume the project will go forward; the cancellation criterion is the cleanest safeguard against sunk-cost continuation.

**Done when:** ≥ 5 risks; ≥ 1 cancellation criterion with a concrete trigger condition.

---

## 8. Terminology glossary

Bilingual: the sponsor's domain vocabulary and the data-team's technical vocabulary, with cross-references. Reduces the surface area for the "two teams speaking past each other" failure mode (Chapman et al. 2000, Task 2).

**Done when:** every term used differently by the sponsor and the data team has both meanings recorded and one chosen.

---

## 9. Cost-benefit analysis

Even a back-of-envelope version. The discipline forces explicit value claims that can be challenged.

**Done when:** the expected benefit is quantified in the same unit the sponsor cares about (€, hours saved, decisions improved, lives affected).

---

## 10. Data-mining / data-product goals (output specification)

The business objective restated in technical terms. **For a pipeline project (no model), this is the output specification:** what dataset, map, dashboard, or report will exist, with what schema, at what resolution, covering what extent, refreshed at what cadence, distributed how, licensed how. This is the most concrete and verifiable Phase-1 artifact for pipeline work (Domino 2017; Wilkinson et al. 2016 for the FAIR posture).

**Done when:** the schema is named field-by-field, with types and units. Resolution is at least as fine as the decision unit. CRS named if spatial. License chosen.

---

## 11. Data-mining / data-product success criteria

Technical thresholds — completeness, freshness, accuracy versus a reference, coverage gaps tolerated — at which the output is considered acceptable. For a pipeline project, replaces "F1 ≥ 0.85" with criteria like "≥ 95% of decision units have non-null values; input data ≤ 18 months old; each value reproducible from published code."

**Done when:** each criterion is a number with a verification method.

---

## 12. Project plan + initial tool assessment

Phased plan with decision gates, plus an initial position on tooling. **CRISP-ML(Q) requires this plan to name explicit quality gates, not only milestones.**

**Done when:** every phase has a duration, a decision gate, and a tool posture. The plan names which phase ends the project if its exit criteria are not met.

---

## Data-product extension (gate-enforced)

### 13. Product card draft (gate-enforced)

Adapted from Gebru et al. (2021) datasheet template plus Mitchell et al. (2019) model card template. For a pipeline data product, the equivalent of a model card. Phase 1 produces the draft; Phase 2 (`earn-the-data`) extends it with data-source-specific limitations; Phase 6 finalises it.

Required sections at Phase 1:
1. What is this artifact?
2. Intended use (decisions it supports)
3. Intended user (named role)
4. Out-of-scope uses (≥ 2)
5. Known limitations (initial set)
6. Provenance summary (placeholder; filled by later phases)
7. Versioning and contact

**Done when:** intended use and intended user are written; ≥ 2 out-of-scope uses are named.

---

## Verification test

For each artifact, apply the **stranger test**: could a stranger pick up the artifact and act on it without contacting the team? If not, the artifact is not done — it is a placeholder.

For the project as a whole, apply the **cancellation test**: if you were told today that the project must be cancelled, could you point to the artifact that says under what conditions cancellation is the correct call? If not, Artifact 7's cancellation criterion is missing.
