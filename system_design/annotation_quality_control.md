# Human annotation and quality control

## Core prompt

Design a platform that distributes data-labeling tasks to human annotators,
evaluates annotation quality, resolves disagreements, and produces versioned
datasets for downstream consumers.

Define the data modality, label schema, contributor model, volume, and quality
targets before selecting assignment or review mechanisms.

## Questions to resolve

- What is the unit of work, and can multiple annotations refer to the same item?
- Are labels categorical, free text, spatial, temporal, or a combination?
- What instructions and examples define an acceptable annotation?
- Which work requires independent labels, review, or expert adjudication?
- How are tasks assigned according to availability, eligibility, and required expertise?
- What quality measurements are meaningful when reviewers can also disagree?
- How do contributors pause work, return tasks, or correct submissions?
- What data-access, privacy, retention, and audit requirements apply?

## Optional design directions

Trace import, assignment, submission, review, and inclusion in a dataset release. Consider:

- How assignment state prevents accidental duplicates while allowing independent labeling.
- How autosave, task expiry, reassignment, and concurrent edits interact.
- How label schemas and instructions are versioned alongside annotations.
- How review sampling, reference examples, and disagreement handling are chosen.
- How quality checks detect systematic errors without treating agreement alone
  as proof of correctness.
- How corrections propagate to affected items and future dataset releases.
- How throughput, review backlog, uncertainty, and provenance are exposed.

Explain release criteria, approval authority, and how consumers reproduce the
labels and rules used in a version.

## Validation scenarios

1. A contributor loses connectivity just before submitting completed work.
2. A task expires and is reassigned before the original submission arrives.
3. Two annotators disagree, and a reviewer identifies ambiguous instructions.
4. A schema change makes some existing labels invalid.
5. A quality audit discovers a systematic error in already released data.
6. Review capacity falls behind annotation throughput.

For each scenario, identify state transitions, human decisions, recovery, and
effects on dataset consumers.

## Related exercises

- [Robotics video ingestion and processing](robotics_video_pipeline.md) provides a possible data source.
- [Workflow orchestration](workflow_orchestration.md) explores multi-stage coordination.
