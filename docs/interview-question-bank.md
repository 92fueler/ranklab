# Engineering Interview Question Bank

A company-neutral preparation bank organized by interview type.

## Scope and evidence

This bank paraphrases 13 user-supplied interview-report screenshots, grouped into eight distinct report clusters after removing overlapping captures. The reports are candidate recollections, not official interview specifications, verified scoring rubrics, or guarantees about a future interview.

- **Reported prompt/details** means the information is visible in the supplied source material.
- **Added practice** means an exercise, clarification, test case, or answer direction added for preparation. It must not be represented as something an interviewer asked.
- **Unspecified** identifies missing requirements. Do not silently fill these gaps when reproducing a reported prompt.
- The same topic can appear in more than one interview type. Cross-references avoid counting it as a new independent report.
- Source identifiers such as **R04** refer to the anonymous coverage register at the end. No source images, personal identifiers, private links, or lengthy quotations are included.

## Contents

1. [Coding](#coding)
2. [Debugging](#debugging)
3. [System Design](#system-design)
4. [AI Project](#ai-project)
5. [Uncategorized Questions](#uncategorized-questions)
6. [Anonymous source coverage](#anonymous-source-coverage)

## Coding

### C01. Referral-network data model

**Reported prompt/details — R05**

Implement a directed referral network that records who referred whom. This is the first stage of a larger graph implementation exercise.

**Unspecified**

The screenshots do not establish whether a person may have multiple referrers, whether cycles are allowed, whether edges can be removed, or which exact API signatures are required.

**Added practice**

- Define node creation, edge insertion, duplicate-edge behavior, and invalid-input handling before coding.
- State and enforce the chosen graph invariants.
- Test a single node, a chain, a branching graph, duplicate referrals, and disconnected components.
- If supporting multiple parents, add a diamond graph; if supporting cycles, test cycle-safe traversal.

### C02. Referral reach and flow-based top-k ranking

**Reported prompt/details — R05**

Extend the referral network with two user-ranking functions:

1. Rank users by the number of directly and indirectly referred candidates.
2. Rank users using a flow-centrality concept described as how often a user occurs on paths through the network.

Both functions return the top k users.

**Unspecified**

The report does not give a complete mathematical definition of flow centrality. It does not say whether paths must be shortest or simple, whether endpoints count, how multiple paths are weighted, or how ties are resolved. It also does not settle whether reach counts unique descendants or paths.

**Added practice**

- For reach, implement an explicitly documented unique-descendant interpretation first.
- Ask for a worked flow-centrality example rather than assuming standard betweenness centrality.
- Select a precise path definition before implementing the second ranking.
- Discuss deterministic tie-breaking, invalid k, complexity, caching, and updates to a large graph.
- Test overlapping descendants so that path counts are not accidentally substituted for user counts.

### C03. Expected referral-network growth with a lifetime cap

**Reported prompt/details — R05**

Estimate the expected network size after N days. Each referrer has daily probability p of making a successful referral, and each person may make no more than 10 successful referrals during their lifetime.

**Unspecified**

The starting population, when newly referred people become eligible to refer, and dependence between referral events are not specified.

**Added practice**

- Make the initial state and daily update order explicit.
- Track expected populations by the number of successful referrals already made, including a saturated state at 10.
- Compare a small deterministic-state calculation with a seeded simulation for validation.
- Test N = 0, p = 0, p = 1, and the lifetime cap.
- Do not use unbounded exponential growth as the final model when the cap matters.

### C04. Top-k selection with a persistently unreliable comparator

**Reported prompt/details — R06; abbreviated recurrence in R07**

Find the top k among n items using a comparator with a stated 10% error rate. Errors are deterministic for the same pair: repeatedly asking about an incorrectly compared pair produces the same incorrect result.

Reported follow-ups:

- Minimize the number of comparator calls.
- Minimize elapsed runtime when an individual comparison takes approximately five seconds.

R06 describes a 45-minute coding round. R07 mentions a 30-minute algorithm round referring back to a previously discussed comparator problem, without restating its full specification.

**Unspecified**

The report does not define how erroneous pairs are selected, whether errors are independent across pairs, what other information about item values is available, or whether an approximate ranking is acceptable.

**Added practice**

- Clarify the error model and required success guarantee before choosing an algorithm.
- Explain why majority voting on repeated calls to the same pair does not fix persistent errors.
- Separate correctness or approximation quality, query count, and wall-clock latency.
- Explore caching pair results, using different opponents, tournament or ranking heuristics, and parallelizing independent calls.
- Discuss the limits of exact recovery when the only evidence is an arbitrarily inconsistent deterministic comparator.
- Use synthetic rankings with fixed corrupted pairs to measure quality and latency.

### C05. Find a connection through a constrained social-graph API

**Reported prompt/details — R03**

Discuss a friend-network search problem at a whiteboard, aiming to use fewer API calls. The API has restrictions.

**Unspecified**

The exact goal, endpoint contract, graph direction, pagination, and API restrictions are not visible. The report does not explicitly require a shortest path or a particular search algorithm.

**Added practice**

- Ask what constitutes a successful connection and what each API call returns.
- Compare ordinary breadth-first search with bidirectional search when both directions are available.
- Consider caching, batching, pagination, rate limits, and termination conditions.
- Measure API calls separately from in-memory time complexity.

### C06. Parking feasibility with preferred positions

**Reported prompt/details — R03**

Given a sequence of cars, each with a preferred parking position, decide whether they can all park. A follow-up was described as a standard depth-first-search or backtracking problem.

**Unspecified**

The screenshots do not reveal the complete parking rules, arrival-order constraints, legal fallback positions, or the exact follow-up.

**Added practice**

- First specify the number of spaces, arrival order, and permitted alternatives when a preference is occupied.
- Implement feasibility for that explicit version.
- For a separate practice extension, enumerate valid assignments or arrival orders using backtracking and pruning.
- Test repeated preferences, insufficient spaces, boundary positions, and a case in which a locally convenient choice blocks a later car.

### C07. Sorting implementation and complexity discussion

**Reported prompt/details — R02, R04, R08**

Related rapid-fire variants include:

- Explain a sorting algorithm faster than quadratic time; one report mentions merge sort as the candidate's example.
- Describe a deliberately much slower sorting method and how permutations would be generated.
- Explain the n log n comparison-sorting complexity bound.

One report uses factorial shorthand for the slow method; another mentions checking permutations with an additional linear factor. These are recollections, not a precise complexity specification.

**Added practice**

- Derive merge sort's recurrence and its O(n log n) running time.
- Explain the worst-case Ω(n log n) lower bound for comparison sorting of arbitrary distinct elements using a decision tree.
- Distinguish a lower bound from a claim that every comparison sort always takes exactly n log n time.
- For a deliberate exhaustive-permutation algorithm, state the cost of generating and checking each permutation. A straightforward implementation can take O(n · n!) time.
- Distinguish exhaustive enumeration from repeatedly shuffling at random; their guarantees and runtime descriptions are not interchangeable.

## Debugging

### D01. Review an unbounded memoization cache

**Reported prompt/details — R04**

Review a small Python-style function that uses a global dictionary: return a cached value if present; otherwise run an expensive computation, store the result, and return it.

The report specifically raises:

- Missing eviction policy and capacity limit.
- Concurrency around expensive computations.
- Failure handling when the computation errors.
- Input validation.

**Added practice**

- Distinguish thread safety from duplicate in-flight work for the same key.
- Discuss per-key single-flight behavior, bounded storage, expiration, and cache-key validity.
- Decide whether errors are cached and under what conditions.
- Test concurrent misses, exceptions, invalid keys, eviction, and cached falsey values.
- Fix behavior and test coverage rather than treating formatting in a screenshot as authoritative source code.

### D02. Review a CSV-building function

**Reported prompt/details — R02**

Review a Java-style routine that repeatedly concatenates cell strings, appends a comma after every cell, and appends a newline after every row. The interviewer asks what should be improved.

**Added practice**

- Address repeated immutable-string concatenation and output-size costs.
- Handle delimiters without adding an unintended empty trailing column.
- Define escaping for commas, quotation marks, and embedded newlines.
- Decide null, empty-row, and line-ending behavior.
- Prefer a well-tested CSV writer when appropriate.
- Test cells containing special characters as well as empty input and large outputs.

### D03. Diagnose an interrupted external-payment operation

**Reported prompt/details — R02; related integration discussion in R04**

Review a service that charges through an external provider, then inserts a payment record into a database, then returns success. Discuss a client or process failing during the operation.

The related integration report explicitly mentions error handling, retries, and idempotency.

**Added practice**

- Enumerate failure windows: before the external call, after an externally successful charge but before local persistence, and after persistence but before the response reaches the client.
- Explain why a timeout can mean an unknown outcome, not a confirmed failure.
- Use a durable operation identifier and provider-supported idempotency semantics.
- Model pending, succeeded, failed, and unresolved outcomes as appropriate.
- Discuss reconciliation through provider status queries or verified events.
- Explain why a local database transaction alone cannot make an unrelated external charge atomic.
- Test duplicate requests, lost responses, transient provider failures, and database-write failures.

See [S05](#s05-reliable-payment-integration) for the architecture-oriented version.

### D04. Oral review of two unspecified code snippets

**Reported prompt/details — R08**

A technical screen included two code snippets presented in a document, with an oral explanation of their problems.

**Unspecified**

Neither snippet's content is visible in this report. Do not assume they were the cache, CSV, or payment examples from other reports.

**Added practice**

Use a short review checklist: intended behavior, correctness, failure modes, resource use, concurrency, test cases, and the smallest useful fix.

## System Design

### S01. Cloud-agent system

**Reported prompt/details — R01**

Design a cloud-agent system. This appears in a short follow-up comment rather than a full problem statement.

**Unspecified**

The agent's capabilities, task model, scale, permissions, and required interfaces are not given.

**Added practice**

Clarify the user workflow, then discuss task submission, durable execution, workers, state and checkpoints, retries, cancellation, tool permissions, isolation, and observability. These topics are preparation extensions, not confirmed interview requirements.

### S02. Workflow or work-orchestration platform

**Reported prompt/details — R03, R07**

Design a workflow system. A separate report names work orchestration as a system-design topic associated with a data-product role.

R07 reports a 45-minute system-design round.

**Unspecified**

No exact workflow language, task graph, service-level objective, or scale is supplied.

**Added practice**

- Define a task and dependency model, state transitions, scheduling, and worker coordination.
- Discuss durable state, retry policies, idempotent task execution, cancellation, and timeouts.
- Explain recovery from a worker crash and how users inspect a stalled workflow.
- Cover priority, backpressure, resource quotas, and observability only after establishing the core design.

### S03. Candidate-search architecture from a job description

**Reported prompt/details — R06**

Given a job description, design a system that searches for suitable candidates. The reported round lasts 45 minutes.

**Unspecified**

The architecture-only report does not specify candidate count, a required top-k value, scoring metrics, or an evaluation endpoint.

**Added practice**

Separate structured hard constraints from relevance ranking. Discuss candidate ingestion, indexing, retrieval, ranking, evaluation, latency, freshness, and explainability. Use synthetic data for practice.

The separate hands-on search project in [A01](#a01-end-to-end-candidate-search-project) supplies more concrete implementation requirements. Do not attribute those requirements to this design report.

### S04. Event-ticketing platform

**Reported prompt/details — R07**

An event-ticketing system is named as a system-design topic for a marketplace-oriented role. The screenshot names the topic but does not provide a detailed prompt.

**Added practice**

Define inventory, seat selection, temporary holds, checkout, and hold expiration. Explain concurrent attempts to buy the same seat, traffic spikes, queueing, and failure recovery. Treat all of these as practice elaborations rather than recovered source requirements.

### S05. Reliable payment integration

**Reported prompt/details — R04**

Discuss integration with a payment provider:

- How should error handling, retries, and idempotency work?
- What data must be stored?
- What database should be used, and how do transaction guarantees and availability affect the choice?

This was reported within a technical screen, not necessarily a standalone system-design round.

**Added practice**

Define operation state, request identifiers, provider identifiers, reconciliation, auditability, and recovery. Explain the boundary between local transactional guarantees and external side effects. Compare database choices against explicit access patterns and correctness requirements rather than selecting one by slogan.

See [D03](#d03-diagnose-an-interrupted-external-payment-operation) for failure-window analysis.

## AI Project

### A01. End-to-end candidate-search project

**Reported prompt/details — R05**

Build a search system that takes a job title, job description, and hard criteria, and returns the ten most suitable candidates from a supplied candidate database.

Reported workflow:

- A 90-minute round: approximately 75 minutes of independent implementation followed by 15 minutes of discussion.
- LLM assistance is allowed for this project.
- Produce a working end-to-end implementation.
- Use a provided evaluation endpoint, inspect results, and iterate.
- Submit all evaluation results.

The candidate described using retrieval followed by ranking, and a runtime LLM to translate job-description requirements into filtering logic. That is the candidate's reported approach, not a mandated architecture.

Reported review questions:

- How did you use LLM assistance?
- How did you design the system?
- How did you discover and resolve implementation problems?

**Unspecified**

The report does not disclose the database schema, evaluation metric, endpoint contract, permitted external services, or a passing score.

**Added practice**

- Build a simple baseline early, then improve it based on measured errors.
- Preserve an experiment log with the change, metric, latency, and observed failure cases for each run.
- Make hard-filter behavior inspectable and testable.
- Compare retrieval quality separately from final ranking quality.
- Handle malformed generated filters, empty candidate sets, duplicate results, and missing fields.
- Be ready to explain and test generated code rather than treating model output as correct by default.
- Use synthetic candidate profiles for a standalone reproduction; this exercise is not authorization to make real employment decisions.

### A02. Small autoregressive language-model training project

**Reported prompt/details — R06; related implementation round in R07**

Implement an autoregressive language model and train it on a Shakespeare text dataset. The implementation must run end to end.

R06 describes a 60-minute mini-project with a coding agent allowed.

R07 separately describes an ML round with one hour of coding and a 30-minute review, referring to a small GPT-style implementation and Transformer knowledge. The screenshots do not establish that the two schedules are identical.

Reported technical follow-ups in R06:

- Transformer architecture.
- Pre-normalization versus post-normalization.
- Self-attention.
- Positional embeddings.
- Greedy decoding, beam search, top-k sampling, and top-p sampling.

**Added practice**

- Make tokenization, batching, next-token targets, and causal masking explicit.
- Verify tensor shapes and run a small forward/backward pass before a longer training run.
- Overfit a tiny batch to catch data or optimization bugs.
- Report training and validation loss, save a checkpoint, and demonstrate generation.
- Explain the role of residual connections and normalization.
- Test decoding separately from training and describe the differences between search and sampling methods.
- Keep the model small enough for a timed, reproducible end-to-end demonstration.

## Uncategorized Questions

### U01. Two-coffee-shop probability puzzle

**Reported prompt/details — R02**

Two drinks are sampled from each of two coffee shops. What is the probability that both drinks from the first shop score higher than both drinks from the second? The candidate report gives 1/6.

**Unspecified**

The screenshot does not state the statistical assumptions needed to make that answer valid.

**Added practice**

Under an exchangeable, no-ties model, there are six equally likely ways to place the two first-shop labels among four ranked drinks, and only one places both at the top. This gives 1/6. If shop quality distributions differ or ties are possible, the answer need not be 1/6; ask for the model before calculating.

### U02. Behavioral introduction and project stories

**Reported prompt/details — R05**

A roughly 20-minute behavioral phone screen asked for:

- A personal or professional introduction.
- Work the candidate was especially proud of.
- A particularly intense work experience.

**Added practice**

Prepare concise stories explaining context, your own contribution, the difficult choice or constraint, the outcome, and what you learned. Use actual experience rather than invented metrics or commitments.

### U03. Reported format and communication observations

**Reported details — R04, R05, R07, R08**

- R04 and R08 describe approximately 30-minute technical screens, including rapid oral discussion or code review.
- R05 describes a 90-minute coding exercise in three parts: an initial 60-minute independent period for the first two parts, then a 30-minute interviewer review and final part. That report says screen recording was required, web search was allowed, and LLM assistance was not allowed in this coding round.
- In the same R05 account, LLM assistance was allowed in the separate search project.
- R07 emphasizes communication as the candidate's impression, not a verified scoring rubric.

These are historical report-specific observations. Confirm the actual schedule and tool policy for the interview being prepared for. Do not generalize one report's rules to every role or round.

**Added practice**

Practice explaining assumptions and trade-offs briefly while preserving implementation time. For an assisted project, be able to distinguish your design decisions from generated suggestions and demonstrate how you validated the result.

## Anonymous source coverage

The grouping below tracks coverage, not interview frequency or independent corroboration. Overlapping screenshots from one report count once.

| Report | Captures | Reported topics included |
| --- | ---: | --- |
| R01 | 1 | Cloud-agent system-design comment |
| R02 | 3 | Slow sorting and permutations; coffee probability; CSV review; interrupted payment operation |
| R03 | 1 | Workflow design; constrained friend-network API search; parking feasibility and backtracking follow-up |
| R04 | 2 | Sorting discussion; memoization-cache review; payment integration; rapid technical-screen format |
| R05 | 3 | Behavioral questions; referral graph, reach, flow ranking, and capped growth; candidate-search project; round-specific assistance rules |
| R06 | 1 | Persistent-error comparator and latency follow-ups; candidate-search design; autoregressive-model project and Transformer follow-ups |
| R07 | 1 | Work orchestration; event ticketing; abbreviated comparator reference; small-GPT implementation/review format |
| R08 | 1 | Comparison-sorting bound; oral review of two unspecified snippets |
| **Total** | **13** | **Eight report clusters** |

## Using this bank

Start with the reported prompt, list what is missing, and choose explicit assumptions for a practice version. Keep an implementation, tests or failure scenarios, a complexity or architecture explanation, and a short record of what changed after review.

Do not present added practice, candidate speculation about outcomes, or missing specifications as verified interview facts.
