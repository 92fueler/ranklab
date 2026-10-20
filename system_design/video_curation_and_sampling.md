# Video curation and sampling

## Core prompt

Design an offline curation service accepting recording manifests and a policy
version, then publishing clip manifests and sharded assets for training jobs.
The workload is hypothetical.

Which task matters: recognizing actions, answering visual questions, predicting
future observations, or learning control? Which events make a low-quality clip
valuable?

## Small example

A collection contains 100 ten-minute manipulation recordings. A baseline samples
two frames per second in four-second clips. A failed grasp lasts 150 milliseconds;
several minutes contain similar successes.

Compare event-aware windows containing context before and after contact.
Which policy misses failures, cuts actions at boundaries, or overrepresents
successes? Preserve source timestamps for audits against original footage.

## Choose the transformation contract

- Order splitting, transcoding, cropping, captioning, filtering, deduplication,
  and sharding. Which operations change evidence available to later decisions?
- Will segmentation use fixed windows, scene changes, action boundaries, or a
  combination? What minimum context and overlap are required?
- Should cropping follow a hand or object, and what happens when the relevant
  object leaves the crop? Keep mappings to original coordinates and timestamps.
- Which cached assets and manifests allow reproducible reruns?
- Would speeding up a trajectory distort contact phases or action timing?
  How are temporal transformations propagated to aligned labels, state, and actions?

## Choose annotation and acceptance rules

- How will a vision-language model propose weak labels or captions, and which
  claims require visual evidence with a time interval or region?
- Version taxonomy, instructions, model, confidence, and human corrections.
  Confidence is not measured accuracy: which reviewed sample establishes
  reliability by class and condition?
- Which examples receive human audits: random samples, rare labels, threshold
  boundaries, disagreements, and rejected clips? Auditing only accepted clips
  cannot reveal all useful examples the filter removed.
- Which confidence thresholds or quality checks exclude clips versus assigning
  tags or sampling weights? Avoid removing dark, occluded, or unsuccessful examples
  that matter to the task. Keep objective-specific views instead of permanently
  deleting every rejected example.

## Choose diversity and release checks

Distinguish exact duplicates, overlaps, and similar repetitions. Choose similarity
thresholds and diversity quotas; near duplicates can contain different outcomes.
Group related recordings before train, validation, and test assignment.

Report retained duration, class and environment coverage, audited label precision,
useful-event recall against a reviewed reference set, rejection reasons, and
processing cost. Did filtering improve downstream performance or merely simplify
the collection?

## Execution and interfaces

At 10,000 uploaded hours/day, how do CPU decoding, accelerator captioning, and
human review share backpressure? Specify job submission/status interfaces,
idempotent retries, persistent decisions, and atomic manifest publication.
Can training readers ever see a partially processed release?

## Validation scenarios

1. Event detection misses rare failures.
2. A taxonomy change splits one action into two incompatible labels.
3. A new crop policy removes evidence needed to audit old captions.
4. Deduplication removes legitimate environmental variation.

Explain detection, affected manifests, re-review, and rollback.

## Related exercises

- [Robotics video ingestion](robotics_video_pipeline.md)
- [Annotation quality control](annotation_quality_control.md)
- [Sampling and visual tokens](../questions/video_sampling_and_visual_tokens.md)
