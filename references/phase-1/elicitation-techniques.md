# Stakeholder Elicitation Techniques for Phase 1

Producing the twelve Phase-1 artifacts requires structured conversations with people who often cannot articulate what they need. The literature offers several established techniques; the strongest Phase-1 work uses two or three in combination. The empirical pattern is that they work best in **workshops, not interviews**, and that the workshop output is itself a Phase-1 artifact — not just the document that follows from it.

The skill uses these techniques as scaffolding for Steps 1–3 and Step 8.

---

## 1. The Heilmeier Catechism

**Origin.** George H. Heilmeier, then-director of DARPA, devised eight questions for evaluating program proposals. Now used by NASA, NSF, Stanford H4D, and corporate innovation teams (DARPA n.d.).

**The eight questions:**
1. What are you trying to do? Articulate your objectives using absolutely no jargon.
2. How is it done today, and what are the limits of current practice?
3. What is new in your approach and why do you think it will be successful?
4. Who cares? If you are successful, what difference will it make?
5. What are the risks?
6. How much will it cost?
7. How long will it take?
8. What are the mid-term and final "exams" to check for success?

**Why it works for data-pipeline projects.** Q1 forces plain-language framing — if the user cannot answer without jargon, the framing is hiding behind tools. Q4 is the **solutionism flush**: if "who cares, what difference" cannot be answered outside the project team, the project has no external decision to serve. Q8 is the **measurement flush**: the answer becomes the success criteria for Step 6.

**Used in this skill at:** Step 2.

**Common failure modes when running it:**
- Skipping Q1 ("we all know what we're doing") — never skip. The jargon test is the point.
- Conflating Q3 (novelty) with Q4 (impact) — novelty is not impact.
- Letting Q8 stay vague — Q8 answers must be numbers with deadlines.

---

## 2. Jobs-to-be-Done (JTBD)

**Origin.** Tony Ulwick; popularised by Clayton Christensen. Reframes user need from "what features they want" to "what they are trying to accomplish" (Ulwick / Strategyn 2024).

**Core JTBD question:** *"When [context], the [user] wants to [job-to-be-done] so they can [outcome]."*

**Why it works for data-pipeline projects.** The planner is not buying a map; they are "hiring" the map to make a defensible budget allocation under time pressure. JTBD surfaces the **social and emotional dimensions** of the job — e.g., the planner's need to defend the ranking to a councillor — which almost never appear in a written requirements document but heavily constrain what the data product must look like.

**Used in this skill at:** Step 1 (when the decision statement's "mechanism" slot is hard to fill), Step 9 (intended-use section of the product card).

**Worked example.**
- Surface request: *"We want a dashboard of canopy cover by neighborhood."*
- JTBD reframe: *"When the annual greening budget is being negotiated, the planner wants to defend a prioritization of streets for de-paving, so they can secure budget without being challenged on the ranking."*
- Implication: the product is not "a dashboard"; it is "a defensible ranked shortlist with rationales." Very different artifact.

---

## 3. Five Whys

**Origin.** Sakichi Toyoda, embedded in lean / Toyota Production System; codified in BABOK Guide for root-cause analysis (IIBA 2024).

**Mechanic.** Take the user's surface request. Ask "why?" Take the answer. Ask "why?" Continue five times. The fifth answer is usually the actual problem.

**Why it works for data-pipeline projects.** Its specific value in Phase 1 is to distinguish **symptom from decision**. A stakeholder who asks for *"a dashboard showing canopy cover by neighborhood"* may, under five-whys interrogation, reveal that the actual decision is *"which streets to prioritize for de-paving next budget cycle"* — a very different artifact.

**Used in this skill at:** Step 3.

**Worked example (Barcelona project).**
- Request: *"We want a barrier map for urban mycorrhiza."*
- Why? *"Because we want to know where intervention is most needed."*
- Why? *"Because the city has limited de-paving budget."*
- Why? *"Because the planner has to defend the allocation to the councillor."*
- Why? *"Because politically-allocated budget cycles are short and contested."*
- Why? *"Because no existing tool gives biophysical justification for ranking."*
- **Actual decision:** which Superilla cells to recommend for the next budget cycle, with biophysical justification the planner can defend.

**Common failure mode.** The chain terminates in a feeling ("the boss wants it") rather than a decision. Keep going. The terminus must be an *action*.

---

## 4. Decision-back framing

**Origin.** James Taylor (Decision Management Solutions); reinforced by Hoerl, Kuonen & Redman (2022) in *MIT Sloan Management Review*.

**Mechanic.** Refuse to discuss data or methods until the team can complete:

> *"This system exists to help [role] decide [decision]; the decision is currently made by [mechanism]; better information would change the decision by [delta]."*

**Why it works for data-pipeline projects.** Pipeline projects are particularly vulnerable to the inverse pattern — starting from "interesting data we have" and inventing decisions it might support. The decision-back discipline is **stricter for pipeline work than for model work**, because in a model project the loss function imposes its own backwards pressure; in a pipeline project, nothing does.

**Used in this skill at:** Step 1 (the decision statement *is* the decision-back sentence), Step 6 (counterfactual quantification).

**Diagnostic.** If the sentence cannot be completed, Phase 1 is not done. Full stop.

---

## 5. The 4Ws problem-scoping canvas

**Origin.** Lightweight design-thinking canvas (a widely used design-thinking canvas).

**Four questions.** Who is affected? What is the specific problem? Where does it occur? Why is it important?

**Why it works.** Lighter-weight alternative to the Heilmeier catechism, useful for early framing sessions before the team has enough material to answer the harder Heilmeier questions.

**Used in this skill at:** Optional pre-step before Step 1, if the user's initial framing is too vague to even attempt the decision statement.

---

## 6. Pre-mortem

**Origin.** Gary Klein, *Harvard Business Review* (2007).

**Mechanic.** The team imagines that the project has failed and works backwards to enumerate the reasons. The output is a forced ranking of risks that is then folded into the risk register.

**Why it works.** Pre-mortems are particularly effective at surfacing risks that the team is *avoiding* discussing — the "everyone knows but nobody says" risks that surface as Phase-6 disasters.

**Used in this skill at:** Step 8 (optional add-on to the risk register).

**Prompt.** *"Imagine it is six months from now and the project has clearly failed. What happened? Be specific. Name the risk, the trigger, the moment it became visible."*

---

## 7. Problem framing canvas (Design Sprint Academy)

**Origin.** Design Sprint Academy (DSA 2024).

**Mechanic.** A workshop artifact that captures the current state of the problem from multiple frames simultaneously — business / customer, inward / outward, past / future.

**Why it works.** More useful for ambiguous problem spaces (*"we want to do something with urban biodiversity data"*) than for already-scoped problems.

**Used in this skill at:** Optional, before Step 1, when the user genuinely cannot answer Q1 of the required inputs.

---

## Choosing techniques per situation

| Situation | Use |
|---|---|
| Crisp request, decision-maker named | Decision-back framing only (Step 1) |
| Crisp request, no clear success metric | Decision-back + Heilmeier (Steps 1–2) |
| Vague request, "do something with X data" | 4Ws → Five Whys → Decision-back (Steps 0–3) |
| User starts from a tool ("we want to use LLMs to …") | Refuse, then Five Whys to extract underlying decision |
| Decision is clear, but team is uneasy about feasibility | Heilmeier + Pre-mortem (Steps 2 + 8) |
| Genuinely ambiguous problem space | Problem framing canvas → 4Ws → Heilmeier |

---

## The meta-rule

The strongest Phase 1 work uses **two or three techniques in combination**, in workshops with the sponsor in the room. The workshop is itself an artifact. The technique without the workshop is theatre.
