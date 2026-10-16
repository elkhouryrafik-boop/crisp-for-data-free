# Phase-1 Anti-Patterns — Diagnostics and Block Responses

These are the modal failure modes documented across the CRISP-DM literature. They are not exotic — they are the *common* failures. The skill detects each and refuses to advance until corrected.

For each: the **pattern**, the **diagnostic** (how to detect it in user input or in the skill's own draft artifacts), the **source**, and the **block response** (what the skill says when it triggers).

---

## 1. Solutionism

**Pattern.** The subject of the project is a technology, not a decision. *"We want to use LLMs / GIS / satellite imagery / GNNs to do something."*

**Diagnostic.** Slot 1 of the required inputs starts with a tool name. The Heilmeier Q1 answer ("what are you trying to do, no jargon") cannot be given without referencing the tool. Q4 ("who cares") has no answer outside the project team.

**Source.** Stefanovskyi (2023).

**Block response.** *"That is a technology, not a problem. What decision does someone need to make better with it? I will not write the decision statement until slot 1 of the inputs is a problem, not a tool."*

---

## 2. Missing decision-maker

**Pattern.** Decision statement names "stakeholders," "users," "the team," or "the city."

**Diagnostic.** The role slot of the decision statement cannot be replaced with an individual's job title at a specific organization. Heilmeier Q4 ("who cares") returns generic answers.

**Source.** Taylor (2017).

**Block response.** *"'Stakeholders' is not a decision-maker. Give me a named role at a named organization — e.g. 'a capital planning analyst at Ajuntament de Barcelona's Espais Verds division.' I will not write `decision-statement.md` until this is supplied."*

---

## 3. Adjective success criteria

**Pattern.** A success criterion uses any of: *useful, actionable, insightful, better, more accurate, novel, interesting, valuable, impactful.*

**Diagnostic.** The success-criteria table contains a row with no number, no deadline, or no owner.

**Source.** Doran (1981); Studer et al. (2021).

**Block response.** *"'X' is not a success criterion. What number, by when, owned by whom? A criterion expressed as an adjective cannot fail at Evaluation — and therefore cannot succeed either, because no result distinguishes a success from a failure."*

---

## 4. Pre-emptive data hunting

**Pattern.** User wants to start with *"let me show you the data we have"* before the decision is framed.

**Diagnostic.** The Phase-2 skill (`earn-the-data`) is invoked or referenced before Phase-1 exit criteria pass.

**Source.** Hoerl, Kuonen & Redman (2022): *"Too often, teams skip right to analyzing the data before agreeing on the problem to be solved."*

**Block response.** *"Phase 1 is not done. We have not defined the decision. Data comes later. `earn-the-data` will refuse to start without `decision-statement.md`, `decision-unit.md`, `output-spec.md`, `product-card-draft.md`, and `risks.md`. Let's finish Phase 1 first."*

---

## 5. Vocabulary drift

**Pattern.** The same term is used with two different meanings inside the Phase-1 artifacts. Common offenders: *block, zone, intervention, user, region, unit, segment.*

**Diagnostic.** Cross-read the artifacts; any term used differently in two places triggers the block.

**Source.** Chapman et al. (2000), Task 2.

**Block response.** *"The term 'X' is being used to mean two different things — [meaning A] in `decision-statement.md` and [meaning B] in `output-spec.md`. Both go in the glossary. Then choose one and propagate."*

---

## 6. Missing cancellation criterion

**Pattern.** Risk register has no row marked *"Triggers cancellation = Yes."*

**Diagnostic.** Read `phase-1/risks.md`; if no cancellation row exists, the artifact is incomplete.

**Source.** Studer et al. (2021): "the absence of a cancellation criterion is itself a Phase-1 defect."

**Block response.** *"Under what finding would we stop the project rather than continue? Phase 1 is not done until the risk register names at least one cancellation condition. Most Phase-1 templates assume the project goes forward — this is the cleanest safeguard against sunk-cost continuation."*

---

## 7. No out-of-scope uses

**Pattern.** Product card draft lists zero out-of-scope uses.

**Diagnostic.** Read `phase-1/product-card-draft.md`; section 4 is empty or trivial.

**Source.** Gebru et al. (2021); Mitchell et al. (2019).

**Block response.** *"The product card has no out-of-scope uses. Name at least two. Examples: 'not for individual-property-level decisions', 'not for regulatory or legal use', 'not for cross-jurisdictional comparison'. If you cannot think of misuse paths, you have not thought hard enough about how the artifact will be used."*

---

## 8. Scope creep through ambiguity

**Pattern.** Constraints section names what is in scope but not what is out.

**Diagnostic.** `phase-1/situation.md` Constraints section has no explicit out-of-scope items.

**Source.** Chapman et al. (2000).

**Block response.** *"You have named what is in scope but not what is out. Scope creep is now pre-installed. Add an explicit out-of-scope list before proceeding."*

---

## 9. Hand-off mentality

**Pattern.** The sponsor / decision-maker was not in the room (or in the loop) for Steps 1, 3, 5, 6, 8.

**Diagnostic.** The artifacts were produced *for* the sponsor rather than *with* them.

**Source.** Taylor (2017); Saltz (2021).

**Block response.** *"These artifacts will need sponsor sign-off before Phase 2. Flagging now so it does not surface as a surprise at Evaluation. Schedule the review."*

---

## 10. Vanity metrics

**Pattern.** Success measured in counts of inputs ("number of data sources integrated," "number of features engineered," "lines of code") rather than decisions changed.

**Diagnostic.** Success-criteria table contains a row whose subject is the project's own work product, not a downstream behavior change.


**Block response.** *"That counts the work, not the outcome. Rewrite the criterion in decision-changed terms: what does the decision-maker do differently if this number is hit?"*

---

## 11. Skipping the pre-mortem

**Pattern.** Risk register contains only risks the team is comfortable discussing. Obvious risks the team has been avoiding are absent.

**Diagnostic.** Compare the risk register against the Heilmeier Q5 answer; if Q5 names risks not in the register, the register is incomplete.

**Source.** Klein (2007).

**Block response.** *"Run a pre-mortem. Imagine it is six months from now and the project has clearly failed. What happened? The risks you instinctively want to avoid naming are the ones most likely to actually kill the project."*

---

## 12. Counterfactually-null criterion

**Pattern.** A success criterion that, if met, would not cause anyone to act differently.

**Diagnostic.** For each criterion, ask: *"What would the decision-maker do differently if the product met spec vs. failed spec?"* If the answer is "nothing," the criterion is wrong (Domino 2017).

**Source.** Counterfactual reasoning from causal inference, applied to data-product evaluation.

**Block response.** *"If the project hits this number, what changes? If nothing changes, the criterion is wrong. Replace it with one whose pass/fail outcome would change someone's behavior."*

---

## How the skill enforces these

Each anti-pattern is a **refuse-to-proceed** condition, not a warning. The skill stops, names the pattern, names the source, and offers the block response. The user must correct the pattern before the skill advances to the next step. This is the discipline; soft warnings are how Phase 1 fails.
