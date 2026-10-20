# End-to-end candidate search

## Core project

Build a working search system that accepts:

- A job title.
- A job description.
- Explicit hard criteria.
- A supplied database of synthetic candidate profiles.

Return the ten most suitable synthetic profiles according to the defined
criteria and relevance model.

Use fictional profiles only. This project must not automate real employment
decisions or connect to a live hiring workflow.

## Requirements to define

The profile schema, evaluation metric, evaluation endpoint contract, external
service dependencies, and quality threshold are not prescribed.

Document:

- Required and optional profile fields.
- What each hard criterion means and how missing data is handled.
- The relevance objective and deterministic tie-breaking behavior.
- What happens when fewer than ten eligible profiles exist. Do not fill the
  result set with ineligible or duplicate profiles to reach ten.
- How evaluation inputs, outputs, errors, and versioning are represented.

## Evaluation workflow

Produce an end-to-end baseline, evaluate it, inspect errors, and iterate.
Retain the results from every evaluation run rather than only the best score.

If an evaluation endpoint is supplied, use its documented contract. Otherwise,
an explicit implementation choice is to build a local evaluator over synthetic
queries and labels. Do not invent an external endpoint or claim that a local
metric is equivalent to an unspecified external one.

Record each experiment's configuration, change, metric, latency, and notable
failure cases so results can be compared and reproduced.

## Optional implementation directions

Retrieval followed by ranking is one possible architecture, not a requirement.
Compare a simple baseline with more complex approaches only when the
evaluation supports the change.

If using a language model to translate requirements into filters:

- Produce a restricted, typed filter representation.
- Validate fields, operators, values, and unsupported requirements.
- Keep explicit hard constraints separate from inferred preferences.
- Make each filter inspectable and test it independently.
- Do not execute arbitrary model-generated code or queries.

Compare retrieval coverage separately from final ranking quality. Validate
generated code and model outputs rather than assuming they are correct.

## Test cases

- Malformed or contradictory criteria.
- No eligible profiles, and fewer than ten eligible profiles.
- Missing fields and duplicate profiles.
- Malformed generated filters or unsupported fields.
- Stable result ordering for ties.
- Evaluation service errors or invalid evaluation responses, if a service is used.

## Deliverables

- A runnable end-to-end implementation and synthetic dataset.
- A concise schema and interface description.
- Tests for filtering, retrieval, ranking, and error handling.
- A reproducible evaluation log containing all runs.
- An explanation of architecture choices, observed errors, and changes validated by measurement.

## Related exercises

- [Candidate-search architecture](../system_design/candidate_search.md) focuses on system boundaries and trade-offs.
- [Technical communication and validation](../questions/technical_communication.md) covers explaining and checking implementation decisions.
