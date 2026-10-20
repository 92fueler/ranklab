# Evaluation metrics

## Define what is being counted

Before selecting a metric, specify the task, prediction unit, reference-label
policy, matching rule, and deployment decision. A frame label, object instance,
temporal event, retrieved clip, and completed robot episode are different units.
Changing units changes the denominator and potentially the conclusion.

Require supporting evidence for reference labels: a visible region, timestamped
event, or adjudicated task outcome. Preserve ambiguous, unobservable, and
unlabeled cases explicitly. Missing annotation is not evidence of a negative.
State which cases are excluded, scored separately, or require review.

For event or object detection, predeclare class compatibility, confidence cutoff,
spatial intersection-over-union (IoU), temporal IoU, or boundary tolerances.
Specify whether every condition must hold and how competing matches are resolved.
Use deterministic one-to-one matching: one prediction cannot satisfy multiple
references, and additional predictions for an already matched reference count
as false positives. Report the matching algorithm; confidence-ordered matching
and maximum-cardinality matching need not produce identical results.

## Precision, recall, and F1

At a fixed operating threshold:

- True positive (TP): a correctly predicted positive or matched reference.
- False positive (FP): an incorrect positive, including unmatched duplicates.
- False negative (FN): a reference positive that was missed.
- True negative (TN): a correctly predicted negative, when negative units are
  meaningfully enumerable.

Precision = TP / (TP + FP)

Recall = TP / (TP + FN)

F1 = 2 × precision × recall / (precision + recall)

Equivalently, F1 = 2TP / (2TP + FP + FN), when the denominator is positive.

Example: a video contains 12 reference pickup events. The model produces 10
predictions; eight match distinct reference events under the declared timing
rule. Therefore TP = 8, FP = 2, FN = 4:

- Precision = 8/10 = 0.80.
- Recall = 8/12 ≈ 0.667.
- F1 = 16/22 ≈ 0.727.

If one extra prediction repeats an already matched pickup, TP stays eight and
FP increases to three. Frame-level accuracy could look high simply because most
frames contain no pickup; it answers a different question.

F1 balances precision and recall through a harmonic mean, but ignores TN and
does not encode unequal consequences of misses and false alarms. Choose an
operating constraint such as minimum recall or a false-alarm budget when it
better reflects the application.

## Aggregation and thresholds

Compute per-class and relevant slice metrics first. Macro averaging gives each
included class equal weight; micro averaging pools TP, FP, and FN before
computing the metric. Support-weighted averaging weights class scores by their
reference frequency. State the class set and weighting: frequent easy classes
can conceal rare-class failures.

Sweep thresholds to inspect precision-recall curves. Select the operating
threshold on validation data, then freeze it for the test comparison. Define any
average-precision convention; average precision is not F1 at a single threshold.
Report class prevalence and the sampling scheme. Precision can change with
prevalence even when class-conditional error rates are unchanged, so balanced
evaluation samples may not predict production precision.

Use uncertainty estimates appropriate to the sampling unit. Correlated frames
from one episode are not independent trials; episode-level resampling may be
more appropriate than frame-level resampling.

## Retrieval is a different measurement

For a query, precision@k measures relevant results among the first k returned
positions, conventionally divided by k. Recall@k divides retrieved relevant
items by all relevant items in the defined candidate universe. Declare relevance
judgments, duplicate handling, candidate filters, and what happens when fewer
than k results exist. Incomplete relevance labels make recall uncertain.

Aggregate across queries explicitly. Retrieval precision@k differs from
classifier precision at a probability threshold. Hit@k records whether any
relevant item appears among k results. Some temporal-localization
benchmarks likewise define recall@k at a temporal IoU threshold as the fraction
of queries with at least one qualifying segment among k proposals. State that
definition rather than conflating it with item recall.

## Other tasks and reporting conventions

Measure human or automated-judge agreement on independently reviewed examples.
Agreement is not correctness; inspect systematic disagreements, rubric
ambiguity, judge drift, and adjudicated error rates. Validate judge scores
rather than assuming ground truth.

Robot task success measures completed episodes under explicit success,
termination, and safety criteria. Report safety failures, time, and intervention
separately; per-action F1 does not substitute for closed-loop success.
World models need separate temporal, geometric, action-consistency, uncertainty,
and downstream-utility evaluations.

State missing-data and zero-denominator conventions. With no predicted positives,
precision is undefined; with no reference positives, recall is undefined.
The count-based F1 is zero if FP or FN is positive and TP is zero; an entirely
empty positive case is undefined. Report undefined values as N/A or disclose
another convention and its effect on aggregation. Never silently convert
timeouts or missing predictions into successful negatives; report failure
coverage and any predeclared scoring penalty.

## Related exercises

- [Video vision-language model evaluation](../system_design/vlm_evaluation.md)
- [World-model evaluation](../system_design/world_model_evaluation.md)
