# Mercor system-design interview reports

Reviewed: 2026-10-20.

A source index of the Mercor design experiences shared for this preparation
collection, with relevant public references. This is not an official interview
specification or a prediction of future questions. Company names identify the
reported interview context, not the author of the practice exercises.

## How to read the evidence

- **Reported recollection:** a candidate account or short comment in the supplied
  material. Thirteen overlapping captures were deduplicated into eight source
  clusters, R01–R08. Multiple topics from one cluster are not independent reports.
- **Public curated account:** an edited account published by PracHub. It is a
  useful public reference, not the original forum post or an independently
  verified transcript. Similar accounts may overlap; no interview-frequency
  claim is made.
- **Editorial practice:** a site's expanded question, or this repository's
  preparation exercise. It must not be mistaken for a recovered interview prompt.
- Original public URLs for the supplied R01–R08 material are **unavailable**.
  Public corroborating links below are labeled separately; they do not restore
  missing original provenance.
- Local exercise links are preparation scaffolds, not solutions. Any added
  functional requirements (FRs), nonfunctional requirements (NFRs), scale targets,
  validation cases, and architecture choices are **synthetic practice extensions**
  unless explicitly identified below as reported.

## Reported standalone design topics

### R01 · Cloud agents

**Evidence:** short reported comment. Role, date, and round duration are not
established in the retained account.

The reported question is to design a cloud-agent system. The comment does not
specify agent capabilities, interfaces, workload, permissions, or scale. Durable
execution, sandboxing, approvals, quotas, and observability in the local exercise
are preparation extensions, not recovered requirements.

**Original public URL:** unavailable.  
**Practice:** [Cloud-agent system](cloud_agents.md).

### R03 · Workflow system

**Evidence:** reported onsite account; exact design-round duration unspecified.

The account names a workflow-system design round. It does not give a workflow
language, dependency model, throughput target, or reliability objective. The
friend-network API and parking questions in the same account are separate
algorithm exercises, not additional system-design reports.

**Original public URL:** unavailable.  
**Public corroboration:** [PracHub's curated Mercor MLE onsite account](https://prachub.com/interview-experiences/mercor-machine-learning-engineer-interview-experience-three-onsite-rounds-kicked-out-of-the-meeting-room-mid-interview),
listed as September 2026; this is not the original source URL.  
**Practice:** [Workflow orchestration](workflow_orchestration.md).

### R06 · Candidate-search architecture

**Evidence:** reported Machine Learning Engineer account; **45-minute design round**.

Given a job description, design a system that finds suitable candidates. The
report does not fix the result count, database schema, ranking metric, dataset
size, or evaluation endpoint. Its comparator exercise and autoregressive-model
project belong to other rounds. In particular, do not import the ten-result and
evaluation-submission requirements from R05 into this design question.

**Original public URL:** unavailable.  
**Public topic reference:** [PracHub's candidate-search and LLM-evaluation practice page](https://prachub.com/interview-questions/design-candidate-search-and-llm-evaluation-tasks)
is editorial practice, not an original candidate transcript.  
**Practice:** [Candidate-search architecture](candidate_search.md).

### R07 · Work orchestration or event ticketing, by team

**Evidence:** a separate reported Machine Learning Engineer account;
**45-minute system-design round**.

The account associates work orchestration with a data-product role and event
ticketing with a marketplace-oriented role. These are team-specific topic
alternatives within one source cluster, not proof that every candidate received
both. Detailed requirements, scale, and interfaces are not supplied. Its model
implementation/review round must not be combined with R06's different schedule.

**Original public URL:** unavailable.  
**Practice:** [Workflow orchestration](workflow_orchestration.md) and
[event ticketing](event_ticketing.md).

## Design inside a technical screen or debugging discussion

### R02 · Interrupted external-payment operation

**Evidence:** one reported account represented by overlapping captures; round
duration and role are not established in the retained summary.

The service calls an external payment provider, stores a local payment record,
and returns success. The discussion asks what happens when the client or process
fails during this sequence. This is a code-review/failure-analysis prompt with
architecture implications, not evidence of a separate full system-design round.
Sorting, probability, and CSV review from this account are not counted again here.

**Original public URL:** unavailable.  
**Practice:** [Reliable payment integration](payment_integration.md).

### R04 · Payment-provider integration and database trade-offs

**Evidence:** reported **30-minute rapid technical screen**.

The reported integration discussion covers errors, retries, idempotency, what to
store, database choice, and the relationship between transaction guarantees and
availability. Sorting and cache review are other topics in the same screen.
These details support a design-oriented payment exercise, but do not establish
a standalone design round or a mandatory database technology.

**Original public URL:** unavailable.  
**Practice:** [Reliable payment integration](payment_integration.md).

### P01 · Dataset deep copy, with payment discussion in the same screen

**Evidence:** [public curated PracHub account](https://prachub.com/interview-experiences/mercor-software-engineer-interview-experience-half-hour-online-round-of-code-review-and-design-questions),
Software Engineer, listed May 2026; approximately **30-minute online screen**;
published October 1, 2026.

The account reports an API to copy a dataset, tasks, model responses, and grades
so the copy can be edited independently. Reported discussion includes fresh ID
references, large asynchronous copies, progress and checkpoints, duplicate
requests, worker coordination, concurrent source edits, and failed-copy cleanup
or resumption. The same screen also includes payment failure analysis, cache
review, and CSV review. Those overlapping topics are not additional independent
corroboration of R02 or R04.

**Original candidate-post URL:** not supplied by the checked page.  
**Practice:** [Dataset deep-copy API](dataset_deep_copy.md) and
[payment integration](payment_integration.md).

### P02 · Membership check and insertion

**Evidence:** [public curated PracHub account](https://prachub.com/interview-experiences/mercor-software-engineer-interview-experience-technical-screen-with-bloom-filter-and-payment-idempotency-debugging),
Software Engineer technical screen, listed October 2026; published October 14,
2026. Duration unspecified.

The report asks how to check membership and add absent identifiers for roughly
one million user IDs, balancing latency, memory, and accuracy. The candidate's
set, Bloom-filter, and storage progression is their answer, not a mandated
architecture. Payment debugging, CSV review, sorting, and probability also
appear in this account. Concurrency, partitioning, and deletion extensions in
practice pages must not automatically be attributed to the original interview.

**Original candidate-post URL:** not supplied by the checked page.  
**Practice:** [Atomic membership and insertion](atomic_membership.md).

### P03 · Async refund review and LLM application design questions

**Evidence:** [public curated PracHub account](https://prachub.com/interview-experiences/mercor-software-engineer-interview-experience-applied-ai-tech-screen-with-an-async-refund-debugging-question-and-rapid-fire-llm-questions),
Applied AI technical screen, listed September 2026; published September 24,
2026. Duration unspecified.

The account reports refund code with retries and database status updates, plus
oral questions about idempotency, retrieval versus fine-tuning, context limits,
state around stateless LLM calls, and prompt injection. These are design-adjacent
technical-screen topics, not evidence that a complete agent-platform design was
asked. The detailed follow-ups on linked practice pages are editorial expansion.

**Original candidate-post URL:** not supplied by the checked page.  
**Related practice:** [Payment integration](payment_integration.md) and
[cloud agents](cloud_agents.md); neither is an exact reproduction of this screen.

## Related implementation round, not a standalone design report

### R05 · End-to-end candidate-search build

**Evidence:** reported Applied AI account; **90-minute project**, approximately
75 minutes of implementation and 15 minutes of discussion. LLM assistance was
allowed for this project.

Build a working search system using job title, description, and hard criteria;
return ten candidates from a supplied database. Use the supplied evaluation
endpoint, iterate, and submit all evaluation results. Review covers system
design, use of LLM assistance, and debugging. The candidate's retrieval/ranking
and runtime-LLM choices are not required architecture. The separate referral
coding round had a different assistance policy.

**Original public URL:** unavailable.  
**Public reference:** [PracHub's curated Applied AI report landing page](https://prachub.com/interview-experiences/mercor-applied-ai-engineer-interview-experience-referral-network-coding-and-a-live-search-system-build);
full content is access-gated, not independently reviewed here.  
**Practice:** [Candidate-search project](../ai_projects/candidate_search.md).

## Inferred practice and source gaps

- **Job scheduler:** [Job scheduling and task execution](job_scheduler.md) is an
  inferred preparation variant of orchestration, **not an independently reported
  Mercor interview question** in the reviewed evidence. Delays, recurrence,
  priority, leases, and timing guarantees are chosen practice scope.
- **R08:** the remaining supplied cluster records a 30-minute technical screen
  with sorting discussion and two unspecified code snippets. Their contents are
  unavailable, so no system-design prompt can responsibly be reconstructed.
- No source here proves Mercor's exact internal architecture. Similarity between
  interview topics and company work is useful preparation context, not that proof.
- This index covers the supplied recollections and the public pages checked on
  the review date. It does not claim to enumerate every Mercor interview online.
