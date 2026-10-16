# CRISP-DM Phase 1 — Business Understanding

> **Packaging note.** This file is the core of the free **crisp-dm-phase-1-business-understanding** skill. Phases 2–6 (data understanding, preparation, the analytical core, evaluation, release handoff) are in the full **crisp-for-data** suite by the same author.

The principle is in the name: a data project that does not start by understanding the *business* — the decision, the decision-maker, the difference success would make — produces artifacts that look professional and fail the moment a stakeholder asks "what do we actually do with this?" This skill blocks that failure mode by forcing twelve specific artifacts onto disk before any data is touched.

This is the upstream of the entire CRISP-DM cycle. The Phase-2 skill (full suite) insists: "anyone can find data; this skill is about earning the right to use it." This one insists: "anyone can build a data pipeline; this skill is about earning the right to build one."

## The anti-pattern this skill exists to prevent

> Open the dataset → run a notebook → produce a chart → invent the decision the chart supports → present.

This produces work that is technically defensible in isolation and strategically useless in context. The empirical record is unflattering. Widely-cited industry surveys put big-data project failure near 85% and data-science production failure near 87% (Gartner 2017; VentureBeat 2019) — vendor-adjacent figures rather than peer-reviewed ones, but the peer-reviewed record points the same way: the modal failure in surveyed CRISP-DM applications is not technical but definitional: the team produced what was asked for and discovered, at evaluation, that what was asked for was not what was needed (Saltz 2021; Schröer, Kruse & Gómez 2021).

Every step below exists to block that anti-pattern. Skipping any of them does not save time — it defers the work to a phase where it costs an order of magnitude more.

## When invoked, run this pipeline end-to-end

The pipeline is a single pass. Steps may iterate internally but the pass does not stop partway. Do not skip a step because the user "just wants to get started" — getting started is the failure mode the skill exists to prevent. Each step produces a named artifact under `phase-1/` at the project root.

## Required inputs from the user

The skill cannot start without these five. If any is missing, the first action is to elicit it — not to proceed.

1. **A problem statement in the user's own words** — one to three sentences. The looser the framing, the more important Phase 1 becomes.
2. **A candidate decision-maker** — a named role at a named organization that will use the output. "Stakeholders," "users," or "the team" is not an answer.
3. **A candidate decision** — the action the decision-maker will take differently if the project succeeds.
4. **A rough domain** — what kind of data product (dataset, map, dashboard, report) and what subject area (urban, environmental, biodiversity, mobility, etc.).
5. **A timebox and resource constraint** — how long the project has, how many people, what the budget is (zero is a valid answer).

If the user supplies a technology ("we want to use LLMs / GIS / satellite imagery to …") in slot 1 instead of a problem, treat this as the solutionism anti-pattern. Respond: *"That is a technology, not a problem. What decision does someone need to make better?"* Refuse to proceed until slot 1 is a problem, not a tool.

## Specialist lenses

Adopt the lens — spawn it if your agent can. Multi-agent platforms (Claude Code Task tool, Hermes delegate_task) spawn the listed specialist per step; single-agent CLIs (Codex) reason through the step in that specialist's voice instead. For genuinely independent verification (e.g. Phase-5 review), a fresh session primed with the specialist role beats in-context self-review.

**Curated for Phase 1:**
- `Product Manager` — outcome framing, success-metric quantification, scope
- `Discovery Coach` — stakeholder question design (Heilmeier, JTBD, 5-Whys)
- `Workflow Architect` — system-level mapping of who decides what and when


## Steps

### Step 1 — Frame the decision

**Action.** Collapse the user's problem statement into a single, unambiguous decision sentence. Write to `phase-1/decision-statement.md`:

> *"This data product will help [decision-maker role] at [organization] decide [decision] at [cadence] by [mechanism]."*

**Specialist lens.** `Product Manager`.

**Socratic prompts.**
- Who is the named individual or role? Not "stakeholders." A name.
- What is the specific decision? Not "understand" or "explore" — what action gets taken?
- At what cadence? (Annual budget cycle, weekly meeting, on-demand?)
- What is the current mechanism? (Intuition? Spreadsheet? Existing tool?)

**Exit check.** All five slots filled with concrete content (role, organization, decision, cadence, mechanism). If any slot is empty, do not proceed — the missing slot *is* the Phase-1 problem.

**Artifact.** `phase-1/decision-statement.md` (one sentence + 3–4 sentences of context).

### Step 2 — Run the Heilmeier catechism

**Action.** Pose the eight Heilmeier questions one at a time and write the answers to `phase-1/heilmeier.md`. (1) What are you trying to do, no jargon? (2) How is it done today, what are the limits? (3) What is new in your approach, why will it succeed? (4) Who cares — what difference will it make? (5) What are the risks? (6) How much will it cost? (7) How long will it take? (8) What are the mid-term and final exams for success? (DARPA n.d.)

**Specialist lens.** `Discovery Coach`.

**Socratic prompts.**
- Plain-language test: would a councillor or a parent understand the answer to Q1?
- Q4 is the solutionism flush — if "who cares" is the project team, restart.
- "I don't know" is an acceptable answer *only* if it becomes a Phase-1 task with an owner.

**Exit check.** Eight answers, each ≥ 2 sentences, no unowned "I don't know"s.

**Artifact.** `phase-1/heilmeier.md` (eight Q&A blocks).

### Step 3 — Apply Five Whys to the surface request

**Action.** Take the user's original request (slot 1) and ask "why?" five times in succession. Write the chain to `phase-1/five-whys.md`. If the fifth answer surfaces a different decision than `decision-statement.md`, update Step 1 (root-cause analysis, per the IIBA BABOK Guide v3, technique 10.40).

**Specialist lens.** `Discovery Coach`.

**Socratic prompts.**
- "You said X. Why? … And why does *that* matter? … And why does *that* matter?"
- If the chain terminates in a feeling ("the boss wants it") rather than a decision, keep going until it terminates in an action.

**Exit check.** Five "why" levels, terminating in a stated decision or action. Decision statement updated if the chain revealed a different one.

**Artifact.** `phase-1/five-whys.md` (five-step chain + revised decision statement if needed).

### Step 4 — Determine the decision unit

**Action.** Ask the user to specify the *smallest spatial, temporal, and spectral / thematic unit at which claims will be made.* The decision unit is what the decision *requires*, not what the data the project happens to have can support. The 2× resolution rule in `earn-the-data` is applied against this number (Chapman et al. 2000; the full suite's Phase-2 core, Step 4).

**Specialist lens.** `Workflow Architect`.

**Socratic prompts.**
- Spatial: at what unit must the claim hold — building, block (~100 m), Superilla (~400 m), neighborhood (~500 m), municipality?
- Temporal: hourly, daily, seasonal, annual?
- Thematic / spectral: what specific quantity (heat, NDVI, species presence, modal share, intervention type)?
- For each, write a 1-sentence justification: *why this unit and not a coarser one?*

**Exit check.** Three units stated as numbers (not adjectives), each with a justification.

**Artifact.** `phase-1/decision-unit.md`.

### Step 5 — Specify the output

**Action.** Replace the missing "model specification" with a data-product specification. Write `phase-1/output-spec.md` with:
- Format (GeoJSON, CSV, PDF report, dashboard, etc.)
- Schema (fields, types, units, CRS if spatial)
- Resolution (must be at least as fine as the decision unit)
- Coverage (spatial and temporal extent)
- Refresh cadence
- Distribution mechanism (where it lives, how it is accessed)
- License (CC-BY, CC0, internal-only, etc.)
- FAIR posture per Wilkinson et al. (2016): findable identifier, accessible protocol, interoperable schema, reusable license

**Specialist lens.** `Workflow Architect`.

**Socratic prompt.** *"If a stranger downloaded this file in two years, what would they need to know to use it correctly?"* — the answer seeds the product card draft (Step 9).

**Exit check.** Every field in the schema named, with type and unit. CRS named if spatial. License chosen.

**Artifact.** `phase-1/output-spec.md`.

### Step 6 — Define success criteria (binary, numerical, dated)

**Action.** Produce two tables in `phase-1/success-criteria.md`. Refuse adjectives (Chapman et al. 2000; Doran 1981; Studer et al. 2021).

| Business Success Criterion | Numerical Threshold | Deadline | Owner |
|---|---|---|---|
| (e.g. shortlist used in budget decision) | (≥ 1 cycle) | (next FY) | (named sponsor) |

| Data-Product Success Criterion | Numerical Threshold | Verification Method |
|---|---|---|
| Coverage | ≥ 95% of decision units have non-null values | spatial coverage check |
| Freshness | input data ≤ N months old at publication | metadata audit |
| Reproducibility | each output value reproducible from published code | clean-clone re-run |

**Specialist lens.** `Product Manager`.

**Socratic prompts.**
- "What number, by when, owned by whom?"
- "What would the decision-maker do differently if the product met spec vs. failed spec?" If the answer is "nothing," the criterion is wrong (counterfactual test, Domino 2017).

**Exit check.** Every row is a number with a deadline and an owner. No adjectives. *"Useful," "actionable," "insightful," "better," "more accurate"* are blocked.

**Artifact.** `phase-1/success-criteria.md`.

### Step 7 — Inventory resources, requirements, assumptions, constraints

**Action.** Produce four short sections in `phase-1/situation.md` (Chapman et al. 2000, Task 2):
- **Resources** — people (named, with time commitments), data (named primary sources, not categories), compute, software, budget.
- **Requirements** — schedule, comprehensibility (explainable to non-technical sponsor?), legal, ethical (intended use, intended user, prohibited uses), security, deployment environment.
- **Assumptions** — things being taken on faith that, if wrong, would invalidate the project.
- **Constraints** — hard limits. Must include explicit out-of-scope items.

**Specialist lens.** `Workflow Architect`.

**Socratic prompts.**
- Names, not roles, for people. Sources, not categories, for data.
- "What is *not* in scope?" — if there is no answer, scope creep is pre-installed.

**Exit check.** All four sections non-empty. Every resource named. At least three explicit out-of-scope items.

**Artifact.** `phase-1/situation.md`.

### Step 8 — Build the risk register and define the cancellation criterion

**Action.** Produce a risk register in `phase-1/risks.md` with at least five rows. Per CRISP-ML(Q) (Studer et al. 2021), the absence of a cancellation criterion is itself a Phase-1 defect.

| Risk | Likelihood (L/M/H) | Impact (L/M/H) | Owner | Mitigation | Triggers cancellation? |
|---|---|---|---|---|---|

At least one row must have *"Triggers cancellation? = Yes"* with a stated condition.

Optional add-on: **pre-mortem** (Klein 2007). Ask: *"Imagine it is six months from now and the project has clearly failed. What happened?"* Fold the answers into the register.

**Specialist lens.** `Product Manager`.

**Socratic prompts.**
- "What finding would make us stop the project rather than continue?"
- "Which of these risks are we *avoiding* discussing?"

**Exit check.** ≥ 5 risks. ≥ 1 cancellation criterion with a clear condition. Every risk has an owner.

**Artifact.** `phase-1/risks.md` with a clearly marked "Cancellation criterion" section.

### Step 9 — Draft the terminology glossary and the product card

**Action A — glossary.** Produce `phase-1/glossary.md` with two columns: term, meaning. Include every term the sponsor and the data team have used differently, even informally. Cross-reference where the same concept has multiple names (e.g. "block" vs. "Superilla" vs. "Manzana") (Chapman et al. 2000, Task 2).

**Action B — product card draft.** Produce `phase-1/product-card-draft.md` adapted from Gebru et al. (2021) datasheet template plus Mitchell et al. (2019) model card template:
1. What is this artifact?
2. Intended use (what decisions it supports)
3. Intended user (named role)
4. Out-of-scope uses (at least two)
5. Known limitations (initial set; extended by Phase 2 in the full suite)
6. Provenance summary (inputs, transformations — filled by later phases)
7. Versioning and contact

**Specialist lens.** `Workflow Architect`.

**Socratic prompts.**
- "Where is the same word being used to mean different things?"
- "What is at least one way this artifact could be misused?"

**Exit check.** Glossary covers every contested term. Product card has ≥ 2 out-of-scope uses named.

**Artifacts.** `phase-1/glossary.md`, `phase-1/product-card-draft.md`.

### Step 10 — Produce the project plan and exit-criteria checklist

**Action.** Produce `phase-1/project-plan.md` covering Phase 2 through Phase 6 of CRISP-DM (plus any Phase-0 acquisition work): expected duration of each, decision gates between them, and the initial tool posture (e.g. *"Python + GeoPandas + DuckDB; no commercial tools"*). Then produce `phase-1/exit-checklist.md` — a copy of the binary exit criteria below, each ticked or open.

**Specialist lens.** `Product Manager`.

**Socratic prompts.**
- "Where are the explicit quality gates between phases?" (CRISP-ML(Q) requirement.)
- "Which phase ends the project if its exit criteria are not met?"

**Exit check.** Plan names every phase, its duration, its decision gate, and the tool posture. Exit checklist below is at the bottom of `exit-checklist.md` with each box explicitly ticked or open.

**Artifacts.** `phase-1/project-plan.md`, `phase-1/exit-checklist.md`.

## Exit criteria (binary — all must pass)

The skill refuses to hand off to `earn-the-data` until every box is ticked.

- [ ] **Decision statement** — one sentence, all five slots filled (role, organization, decision, cadence, mechanism).
- [ ] **Named decision-maker** — named role at a named organization, not "stakeholders."
- [ ] **Decision unit** — spatial, temporal, and thematic units written as numbers.
- [ ] **Output specification** — schema exists; units, CRS (if spatial), refresh cadence specified.
- [ ] **Numerical success criteria** — every criterion is a number with a deadline and an owner.
- [ ] **Intended use and intended user** — both written in the product card draft.
- [ ] **Out-of-scope uses** — at least two named in the product card draft.
- [ ] **Risk register** — at least five risks, each with likelihood, impact, owner, mitigation.
- [ ] **Cancellation criterion** — at least one risk marked "Triggers cancellation = Yes" with a clear condition.
- [ ] **Glossary** — every contested term covered.
- [ ] **Resources inventory** — every resource named (no "the team," no "the data").
- [ ] **Constraints** — hard limits named, including explicit out-of-scope items.

If any box is unticked, do not proceed. Return to the relevant step.

## Anti-patterns the skill must refuse to proceed past

The skill detects these in user input or in its own draft artifacts and refuses to advance until corrected.

**Solutionism.** Subject of the project is a technology, not a decision. *"We want to use LLMs / GIS / satellite imagery to do something."* Block: *"That is a tool, not a problem. What decision does someone need to make better?"* (Stefanovskyi 2023.)

**Missing decision-maker.** Decision statement names "stakeholders," "users," or "the team." Block: refuse to write `decision-statement.md` until a named role at a named organization is supplied (Taylor 2017).

**Adjective success criteria.** A success criterion uses any of: *useful, actionable, insightful, better, more accurate, novel, interesting.* Block: *"That is not a success criterion. What number, by when, owned by whom?"* (Doran 1981; Studer et al. 2021.)

**Pre-emptive data hunting.** User wants to start with "let me show you the data we have." Block: *"Phase 1 is not done. We have not defined the decision. Data comes later."* This is enforced on both sides — the Phase-2 core (full suite) refuses to start without the Phase 1 handoff (Hoerl, Kuonen & Redman 2022).

**Vocabulary drift.** The same term is used with two different meanings inside the Phase-1 artifacts. Block: stop and add both meanings to the glossary, then choose one (Chapman et al. 2000).

**Missing cancellation criterion.** The risk register has no row marked "Triggers cancellation = Yes." Block: require at least one. The absence is itself a defect (Studer et al. 2021).

**No out-of-scope uses.** Product card draft lists zero out-of-scope uses. Block: require at least two (Gebru et al. 2021).

**Scope creep through ambiguity.** Constraints section names what is in scope but not what is out. Block: require an explicit out-of-scope list (Chapman et al. 2000).

**Hand-off mentality.** The sponsor was not in the room (or in the loop) for Steps 1, 3, 5, 6, 8. Block: flag explicitly that the artifacts will need sponsor sign-off before Phase 2 begins (Taylor 2017; Saltz 2021).

**Vanity metrics.** Success measured in counts of inputs ("number of data sources integrated," "number of features engineered") rather than decisions changed. Block: rewrite the criterion in decision-changed terms (a common practitioner anti-pattern).

## Handoff to Phase 2 (Data Understanding)

Once all exit-checklist boxes are ticked, Phase 1 is complete. The five artifacts below are the handoff payload Phase 2 consumes — Phase 2 and everything after it live in the full **crisp-for-data** suite:

**Mandatory handoff payload (5 artifacts):**
1. `phase-1/decision-statement.md` — frames the brief revisit at `earn-the-data` Step 10.
2. `phase-1/decision-unit.md` — drives the 2× resolution rule at `earn-the-data` Step 4.
3. `phase-1/output-spec.md` — scores Resolution and Coverage on the rubric at `earn-the-data` Step 5.
4. `phase-1/product-card-draft.md` — fills the Uses section of the data sheets at `earn-the-data` Step 6.
5. `phase-1/risks.md` — including the cancellation criterion, used by `earn-the-data` Step 10 to trigger a no-go finding if data cannot support the decision.

**Recommended (strengthens Phase 2):**
- `phase-1/situation.md` — informs inventory of resources.
- `phase-1/glossary.md` — disambiguates field semantics.

**Next.** When the exit checklist passes, continue with the full crisp-for-data suite (Phases 0–6), or hand the artifacts to your Phase-2 process of choice.

If Phase 2 (full suite) returns at its Step 10 with a "No — question cannot be answered" finding, return to *Step 1 here* and reframe the decision against what the data can actually support. This is the iterative property CRISP-DM is built around; it is not a failure (Martínez-Plumed et al. 2021; Domino 2017).

## References

See `references/phase-1/citations.md` for the full bibliography. Anchor sources:

- Chapman et al. (2000). *CRISP-DM 1.0: Step-by-step data mining guide.* — original four-task / twelve-output reference model.
- Studer et al. (2021). Towards CRISP-ML(Q). *Machine Learning and Knowledge Extraction* 3(2). — quality-assurance overlay; cancellation criterion requirement.
- Martínez-Plumed et al. (2021). CRISP-DM twenty years later. *IEEE TKDE* 33(8). — exploratory vs goal-directed trajectories.
- Schröer, Kruse & Gómez (2021). A systematic literature review on applying CRISP-DM. *Procedia CS* 181. — empirical record of Phase-1 under-specification.
- Saltz (2021). CRISP-DM for data science. — Phase-1 weakness analysis.
- Taylor (2017). Four problems in using CRISP-DM. *KDnuggets.* — clarity, rework, hand-off, iteration failure modes.
- Hoerl, Kuonen & Redman (2022). Framing data science problems the right way. *MIT SMR.* — decision-back framing.
- Gebru et al. (2021). Datasheets for datasets. *CACM* 64(12). — product card structure.
- Mitchell et al. (2019). Model cards for model reporting. *FAccT.*
- Wilkinson et al. (2016). FAIR Guiding Principles. *Scientific Data* 3.
- DARPA. *The Heilmeier Catechism.*
- Ulwick / Strategyn. *Jobs-to-be-Done framework.*
- Doran (1981). SMART criteria. *Management Review* 70(11).
- Klein (2007). Performing a project premortem. *HBR* 85(9).
- IBM (2021). *SPSS Modeler CRISP-DM Guide.*

For deeper material, load:
- `references/phase-1/artifacts.md` — the twelve Phase-1 artifacts in full.
- `references/phase-1/anti-patterns.md` — diagnostic patterns + block responses.
- `references/phase-1/elicitation-techniques.md` — Heilmeier, JTBD, 5-Whys, decision-back.
- `references/phase-1/quantification.md` — SMART, translation table, cancellation thresholds, pre-mortem.
- `references/phase-1/citations.md` — full bibliography.
