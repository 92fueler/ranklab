# Candidate-search architecture

## Core prompt

Given a job description, design a system that searches a collection of synthetic
candidate profiles for relevant matches.

This is a retrieval and ranking exercise using fictional data. Do not connect it
to live hiring systems or automate real employment decisions.

The collection size, result count, ranking metrics, evaluation interface, and
latency targets are unspecified. The separate
[end-to-end candidate-search project](../ai_projects/candidate_search.md)
defines a more concrete implementation variant; its requirements do not
automatically apply here.

## Questions to resolve

- Which requirements are explicit hard constraints and which express relevance?
- What fields exist in each synthetic profile, and how are missing fields treated?
- What evidence should accompany a match?
- How will relevance be assessed using synthetic labels or judgments?
- How fresh must indexes and results be?
- What scale, latency, and cost limits matter?

## Optional design directions

Discuss ingestion, validation, indexing, retrieval, ranking, and presentation.
Possible approaches include keyword retrieval, structured filters, embeddings,
or a multi-stage retrieval-and-ranking pipeline. None is mandatory.

Keep filtering distinct from ranking:

- Make hard-filter decisions inspectable and testable.
- Do not silently convert an ambiguous preference into an exclusion rule.
- Distinguish a failed hard requirement from an unknown field.
- Show the synthetic profile evidence supporting a result.

If using a language model to extract requirements or produce filters, define a
restricted output schema, validate the output, and avoid executing arbitrary
generated expressions.

## Validation scenarios

- A query has conflicting requirements.
- All profiles fail the hard constraints.
- A profile has missing or contradictory fields.
- Duplicate profiles appear in retrieval results.
- An index is stale after a profile update.
- A generated filter is malformed or refers to an unsupported field.

Compare retrieval coverage separately from final ranking quality. Explain
latency, freshness, reproducibility, and failure behavior rather than relying on
a single aggregate score.

## Related exercises

- [End-to-end candidate-search project](../ai_projects/candidate_search.md) provides an implementation-focused variant with ten results.
- [Technical communication and validation](../questions/technical_communication.md) covers documenting assumptions and generated-code validation.
