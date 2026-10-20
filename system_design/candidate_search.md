# Mercor – Candidate-search architecture (reported system-design topic)

## References

- [Mercor report collection](mercor_system_design_reports.md): user-supplied report; original public URL unavailable.
- [Public candidate-search overview](https://prachub.com/interview-questions/build-a-candidate-search-system): related implementation exercise, with limited publicly visible detail.
- [Separate hands-on project](../ai_projects/candidate_search.md).

## Evidence status

A supplied candidate report describes a 45-minute system-design round about finding suitable candidates from a job description. It does not establish collection size, result count, evaluation metrics, or an evaluation endpoint. The separate hands-on project must not supply purported requirements for this round. All expanded requirements below are practice assumptions, not recovered interview instructions.

## Problem statement

Design a system that accepts a job description and returns relevant matches from a collection of fictional candidate profiles. Use synthetic data for practice, not a live hiring system or automated employment decisions.

## Functional requirements

For the proposed exercise:

- Accept a job description and distinguish mandatory criteria from preferences.
- Return an ordered set of matching profiles, with the requested result count clarified first.
- Explain matches using evidence present in the profiles.
- Handle missing information, contradictory requirements, duplicate profiles, and no qualifying results.
- Support profile additions and corrections, with defined search visibility.
- Let an evaluator compare results against synthetic relevance judgments and inspect individual errors.

## Non-functional requirements

Choose these constraints before designing the system:

- Collection size, profile update rate, query volume, and response-time objective.
- Search freshness and availability expectations.
- Relevant quality measures, hard-constraint correctness, and acceptable operating cost.
- Reproducibility of comparisons and access limits for profile data.

No numerical targets are established by the report.

## Optional failure conditions

A profile update has not reached search results; all matching profiles lack a required field; an ambiguous phrase changes the apparent eligibility rule; aggregate relevance improves while one important query category worsens. Define what users and evaluators should observe, leaving the architecture open.
