# Ranklab

A personal workspace for understanding LLM.

## Setup

Install Python 3.14 and uv, then run:

```sh
cd src
uv sync --locked
cp .env.example .env
```

Fill in `.env` with your settings as needed.

## Engineering workspace

Independent implementation starters, debugging examples, and design questions
live alongside the application. Each file states its problem and calls out
choices or missing requirements before implementation. The folders do not
change the application in `src/` or its setup.

- [Coding](coding/): one Python starter per problem, with statements, explicit
  assumptions, TODOs, and test expectations. Algorithms are not implemented.
- [Debugging](debugging/): one Python file per concrete problem, with an
  intentionally buggy runnable example and a TODO repair entry point.
- [System design](system_design/): one Markdown file per scenario, with questions
  about requirements, architecture, and failure handling.
- [AI projects](ai_projects/): end-to-end project specifications. These stay in
  Markdown because dataset, model, and evaluation choices span multiple files.
- [Questions](questions/): probability, technical communication, and code-review
  questions that are not standalone implementation tasks. A generic checklist
  replaces unspecified snippets rather than inventing code for them.

### Coding

- [Referral-network data model](coding/referral_network.py)
- [Referral reach and flow ranking](coding/referral_rankings.py)
- [Capped referral-network growth](coding/referral_growth.py)
- [Top-k with a persistently unreliable comparator](coding/unreliable_comparator.py)
- [Full ordering with independent comparator errors](coding/independent_error_sort.py)
- [Connection search through a constrained API](coding/social_graph_connection.py)
- [Friendship neighborhood with minimal API calls](coding/social_graph_neighborhood.py)
- [Parking feasibility with explicit fallback sets](coding/parking_feasibility.py)
- [Forward-only parking](coding/parking_forward_only.py)
- [Chained currency conversion](coding/currency_conversion.py)
- [Sorting algorithms and complexity](coding/sorting_algorithms.py)

### Debugging

- [Memoization cache](debugging/memoization_cache.py)
- [CSV builder](debugging/csv_builder.py)
- [Interrupted payment operation](debugging/interrupted_payment.py)
- [Asynchronous refund retries](debugging/async_refund.py)

### Design and project questions

- [Cloud agents](system_design/cloud_agents.md)
- [Job scheduler](system_design/job_scheduler.md)
- [Workflow orchestration](system_design/workflow_orchestration.md)
- [Dataset deep-copy API](system_design/dataset_deep_copy.md)
- [Atomic membership and insertion](system_design/atomic_membership.md)
- [Robotics video pipeline](system_design/robotics_video_pipeline.md)
- [Egocentric video data platform](system_design/egocentric_video_data_platform.md)
- [VLM evaluation](system_design/vlm_evaluation.md)
- [Annotation and quality control](system_design/annotation_quality_control.md)
- [Evaluation platform](system_design/evaluation_platform.md)
- [Candidate-search architecture](system_design/candidate_search.md)
- [Event ticketing](system_design/event_ticketing.md)
- [Payment integration](system_design/payment_integration.md)
- [Candidate-search project](ai_projects/candidate_search.md)
- [Autoregressive language-model project](ai_projects/autoregressive_language_model.md)
- [Local model evaluation](ai_projects/local_model_evaluation.md)
- [Coffee-shop probability](questions/coffee_shop_probability.md)
- [LLM application engineering](questions/llm_application_engineering.md)
- [Systems fundamentals](questions/systems_fundamentals.md)
- [Technical communication](questions/technical_communication.md)
- [Code-review checklist](questions/code_review_checklist.md)

### Working with the Python files

The new Python files use only the standard library. From the repository root,
run a file directly, for example:

```sh
python coding/referral_network.py
python debugging/csv_builder.py
```

Coding entry points print a reminder; their algorithms deliberately raise
`NotImplementedError` until implemented. Debugging entry points demonstrate
intentional defects safely with synthetic data or local fakes. Do not use those
buggy implementations in the application. Add focused tests as each TODO is
completed, and keep each chosen contract next to the code.
