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
- [Connection search through a constrained API](coding/social_graph_connection.py)
- [Parking feasibility](coding/parking_feasibility.py)
- [Sorting algorithms and complexity](coding/sorting_algorithms.py)

### Debugging

- [Memoization cache](debugging/memoization_cache.py)
- [CSV builder](debugging/csv_builder.py)
- [Interrupted payment operation](debugging/interrupted_payment.py)

### Design and project questions

- [Cloud agents](system_design/cloud_agents.md)
- [Workflow orchestration](system_design/workflow_orchestration.md)
- [Candidate-search architecture](system_design/candidate_search.md)
- [Event ticketing](system_design/event_ticketing.md)
- [Payment integration](system_design/payment_integration.md)
- [Candidate-search project](ai_projects/candidate_search.md)
- [Autoregressive language-model project](ai_projects/autoregressive_language_model.md)
- [Coffee-shop probability](questions/coffee_shop_probability.md)
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
