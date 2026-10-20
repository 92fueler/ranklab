# Physical-AI interview experience index

Reviewed: 2026-10-20.

Public interview reports and preparation leads for Figure AI, Physical
Intelligence, 1X Technologies, Agility Robotics, World Labs, Humanoid, and Skild
AI. This is a focused research index, not an exhaustive list of companies or a
ranking of market leaders. Backend, data, training, and evaluation-system
relevance is emphasized; robotics-algorithm reports are labeled separately.

## Evidence levels

1. **Candidate-reported:** an anonymous interview-platform narrative. This
   establishes what a person reported, not employer verification.
2. **Curated candidate account:** a preparation site has edited or republished a
   narrative. The original post and exact wording may be unavailable.
3. **Index-only report:** search results expose a narrative that the opened page
   did not reproduce. This is weaker evidence and may be stale.
4. **Editorial practice:** inferred questions, generated hints, and expanded
   requirements. These are not candidate reports, even when company-branded.
5. **Official challenge or public product/research context:** employer-published
   material. A verified recruiting challenge would establish that published
   challenge, not a particular candidate's experience; product and research pages
   do not establish interview questions. No accessible official recruiting
   challenge was verified in this pass.

Gated previews and inaccessible full reports are not used to claim exact
questions or hidden constraints.

Dates and durations below are report-specific, not a current universal interview
process. Local links point to preparation briefs or drills, not solutions. Added
functional requirements (FRs), nonfunctional requirements (NFRs), scale targets,
and failure cases are **synthetic practice extensions**, not undisclosed employer
requirements.

## Physical Intelligence

### PI-1 · Cache implementation and AI-assisted integration project

**Source:** [PracHub's curated Software Engineer account](https://prachub.com/interview-experiences/physical-intelligence-software-engineer-interview-experience-hand-coding-a-cache-then-a-90-minute-mini-project-running-4-5-ai-agents).
Listed September 2026; published September 24, 2026. Publicly readable; original
candidate-post URL unavailable.

The narrative reports a 45-minute background conversation, a **one-hour cache
implementation** using a supplied backend skeleton, and a separate **90-minute
AI-assisted project**. The project supplied data and an embedding API, required a
working pipeline and UI, and reserved the last ten minutes for results and a
scaling discussion. The candidate describes coordinating several coding agents.

**Not recorded:** exact cache API/policies, what the pipeline computed, dataset,
metrics, or grading. Do not relabel the project as confirmed semantic search,
clustering, or candidate ranking.

### PI-2 · Linked practice expansions, not extra reports

- [Bounded-cache practice page](https://prachub.com/interview-questions/hand-write-a-bounded-cache-for-a-database-backed-backend-service):
  explicitly acknowledges that the original skeleton was not recorded. Capacity,
  TTL, invalidation, concurrency, and detailed test requirements are editorial
  extensions.
- [Embedding-project practice page](https://prachub.com/interview-questions/build-and-present-an-embedding-pipeline-in-90-minutes-using-ai-coding-agents):
  explicitly acknowledges that the pipeline's actual objective was not recorded.
  Semantic search, clustering, vector storage, and proposed operational follow-ups
  are possible practice choices, not recovered requirements.

**Local preparation:** [Cache review](../debugging/memoization_cache.py),
[AI-assisted search project](../ai_projects/candidate_search.md), and
[evaluation platform](evaluation_platform.md). These are analogous exercises,
not reproductions of PI's task. Its public training research is indexed separately
below.

## Figure AI

### FIG-1 · Multimodal training-data discussion

**Source:** [Screna interview entry](https://www.screna.ai/experience/aad0d809-9cc7-4e7b-aec2-48d6fa49b5cb).
Candidate-reported, not independently verified by the employer. The reviewed
entry was described as a Senior Software Engineer onsite; exact timing is not
needed to use this topic responsibly.

The reported topic concerns multimodal training-data ingestion, filtering, and
bias. The site's AI hints are separate from the candidate's account and must not
be treated as exact interviewer questions or required architecture. This is a
single report, not independent corroboration of Figure's production pipeline.

**Local preparation:** [Robotics video pipeline](robotics_video_pipeline.md) and
[video curation](video_curation_and_sampling.md) are related practice, not exact
reconstructions. Figure Index product-inspired briefs appear separately below.

### FIG-2 · Broader robotics interview context

**Source:** [Glassdoor's Figure AI interview reports](https://www.glassdoor.com/Interview/Figure-AI-Interview-Questions-E9642582.htm).
A directly readable Software Engineer report posted July 25, 2026 mentions
humanoid-robot scenarios but supplies no concrete backend prompt.

A Robot Learning Engineer entry posted July 21, 2026 appeared only in search
results during this check. It described approximately half an hour of behavior
cloning/reinforcement-learning discussion and a humanoid demonstration. Treat
that entry as **index-only**, and do not turn it into a reported data-platform or
system-design question.

**Use:** role-context preparation, with little evidence of exact backend tasks.

## 1X Technologies

### 1X-1 · Graph coding and an AI-assisted notes/tasks build

**Source:** [Glassdoor's 1X interview reports](https://www.glassdoor.com/Interview/1X-Technologies-Interview-Questions-E2346235.htm).
Full Stack Engineer; reported interview April 2026, post June 8, 2026.
**Index-only:** the search result exposed this account, but the directly opened
page did not reproduce it. Confidence is lower than for readable reports.

The account describes role-related graph coding, followed by a design-labeled
round conducted as AI-assisted implementation of a system organizing notes and
tasks. Exact graph rules, APIs, timebox, scale, and tests were not disclosed.
Robot-fleet, telemetry, and permission requirements cannot be inferred from the
company name.

**Local preparation:** [Technical communication and validation](../questions/technical_communication.md)
and [workflow orchestration](workflow_orchestration.md) offer adjacent skills,
not the reported application's exact specification.

### 1X-2 · Older directly readable reports

**Source:** [Glassdoor's older 1X reports](https://www.glassdoor.com/Interview/1X-Technologies-Interview-Questions-E2346235_P4.htm).
Candidate-reported; the following entries are separate accounts on one page.

- Senior Software Engineer, interview February 2025, posted August 23, 2025:
  asked how the candidate approaches debugging complex systems; no concrete
  incident or codebase was disclosed.
- Reinforcement Learning Research Engineer, interview April 2024, posted July 2,
  2024: mixed ML, robotics, math, and software screening, then coding and RL
  design. Bayes' theorem is named; the RL-design problem is not specified.

These older reports do not establish a universal current 1X interview loop.

### 1X-3 · Excluded as candidate evidence

[TechPrep's 1X guide](https://www.techprep.app/blog/1x-technologies-interview-process)
includes an in-memory database assessment and a representative large robot-fleet
cloud design example without an attributable dated candidate report. Treat
these as editorial preparation. Its purported official challenge-repository
lead returned 404 during this check; no available official challenge is claimed.

## Agility Robotics

### AGR-1 · Take-home, live extension, and whiteboard design

**Source:** [Glassdoor's Senior Software Engineer reports](https://www.glassdoor.co.in/Interview/Agility-Robotics-Senior-Software-Engineer-Interview-Questions-EI_IE1697238.0,16_KO17,41.htm).
Candidate-reported and directly readable.

An account posted April 29, 2026 reports a coding exercise, substantial take-home,
background presentation, live feature addition, whiteboard design, and behavioral
discussion. **Neither the take-home nor the design problem is disclosed.**

Separate accounts on that page mention SLAM optimization and an SE(3) pose update
(August 2025 interview, September 3 post), and a motion-planning framework
(October 28, 2022 post). These are robotics-oriented topics, not evidence of a
backend/data-platform prompt.

**Local preparation:** [Technical communication and validation](../questions/technical_communication.md)
helps practice extending and defending one's work; no exact Agility design
exercise is reconstructed here.

### AGR-2 · Whole-body-control discussion

**Source:** [Glassdoor's Agility reports](https://www.glassdoor.com/Interview/Agility-Robotics-Interview-Questions-E1697238.htm)
and the [whole-body-control question entry](https://www.glassdoor.com/Interview/They-asked-me-about-my-technical-concepts-regarding-whole-body-control-in-humanoid-robots-QTN_9012258.htm).
Software Engineer II; interview May 2026, posted June 3, 2026.

The candidate reports a role-related take-home, Python/C++ programming, robotics
discussion, and a culture interview. Humanoid whole-body control is named, but
neither the exact assignment nor the programming question is given. This
supports role-specific robotics preparation, not an inferred backend-system
question.

## Companies with no attributable target-role prompt established in this pass

These are **scoped search results**, not claims that no interview experiences
exist anywhere online.

### World Labs

[The Aced company page](https://www.aced.io/companies/world-labs) invited
contributions without displaying a candidate experience.
[Scoutify's guide](https://scoutify.com/companies/world-labs/interview/) derives
practice from job requirements, and [Extern's internship guide](https://www.extern.com/post/world-labs-internship-guide?code=tnc)
describes an expected/inferred process. None establishes a concrete candidate-reported backend, data, training, or evaluation question in the checked material.

Use [world-model evaluation](world_model_evaluation.md) as public-research-inspired
practice, **not** an “asked at World Labs” claim.

### Humanoid

[PracHub's Humanoid guide](https://prachub.com/interview-guide/humanoid-software-engineer-interview-questions-guide-2026)
is editorial; its checked candidate-research reference led back to the guide
rather than an underlying dated account.
[Interview Query's company guide](https://www.interviewquery.com/interview-guides/humanoid)
also did not supply an actionable attributable experience. No concrete target-role prompt was established from these sources.

### Skild AI

The bounded search did not establish a usable candidate narrative for the target
backend/data/training/evaluation topics. No interview-question source is linked
because no suitable one was verified. This is an evidence gap, not proof of absence.

## Separate track: official public context for synthetic design practice

These sources explain publicly described products or research. They do **not**
confirm interview prompts, complete internal architecture, or all details in the
linked exercises. Topic alignment is plausible preparation context only.

- **Figure AI Index:** [official introduction](https://www.figure.ai/news/introducing-index)
  → [human-video data platform](egocentric_video_data_platform.md) and
  [annotation quality control](annotation_quality_control.md).
- **Physical Intelligence π0.5:** [official research article](https://www.pi.website/blog/pi05)
  → [mixed-supervision training platform](multimodal_model_training.md).
- **NVIDIA GR00T N1:** [technical report](https://arxiv.org/html/2503.14734v1#A4.SS1)
  → [aligned episode data service](multimodal_dataset_join.md).
- **NVIDIA Cosmos:** [official data-curation documentation](https://nvidia-cosmos.github.io/cosmos-cookbook/core_concepts/data_curation/overview.html)
  → [video curation and sampling](video_curation_and_sampling.md).
- **World Labs real-to-sim-to-real:** [official research article](https://www.worldlabs.ai/blog/real-to-sim-to-real)
  → [world-model evaluation platform](world_model_evaluation.md).

- **1X World Model:** [official article](https://www.1x.tech/discover/world-model-self-learning)
  → [video-to-action learning platform](video_to_action_learning.md).
- **Humanoid KinetIQ:** [official technical overview](https://thehumanoid.ai/technology/kinetiq-ai-stack-overview/)
  → [data and policy training](humanoid_data_training.md).

Generic [evaluation-platform](evaluation_platform.md) and
[video VLM-evaluation](vlm_evaluation.md) briefs remain independent practice.
Do not convert their requirements into employer-reported questions.
