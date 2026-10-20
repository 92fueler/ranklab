# Egocentric video data platform

## Core prompt

Design a platform where distributed human collectors upload first-person video
that is processed, indexed, and assembled into training datasets for vision-language
models.

Focus on human-collected training footage rather than robot telemetry.
Establish device, scale, connectivity, latency, and training requirements.

## Questions to resolve

- What identifies a collector, recording session, camera, and captured segment?
- Which capture timestamps and metadata are required and reliable?
- What consent, privacy, access, retention, and deletion constraints apply to
  collectors, bystanders, and recorded environments?
- Which video formats, recording lengths, and network conditions must be supported?
- What defines useful data: clarity, actions, language alignment, diversity, or coverage?
- How do consumers discover clips through structured or semantic queries?
- What dataset formats and read throughput do training jobs require?

## Optional design directions

Trace capture through a training-ready dataset snapshot. Consider:

- How resumable multipart uploads, manifests, checksums, and completion states
  identify missing, corrupted, or duplicate content.
- How immutable raw assets relate to decoded frames, transcoded videos, sampled
  clips, and later corrections or authorized deletions.
- How codec failures and backlogs affect availability and costs.
- How blur, motion, duplication, and coverage checks influence selection without
  removing valuable examples.
- How timestamps preserve temporal alignment across clips, audio, captions, and labels.
- How annotation and automated enrichment record versions and provenance.
- How metadata and embedding indexes combine semantic and structured constraints
  consistently with asset permissions.
- How versioned dataset snapshots record inclusion rules, transformations, and lineage.
- How train, validation, and test splits prevent leakage across related collectors,
  sessions, overlapping clips, or near-duplicate recordings.
- How sharded training formats, caching, and prefetching sustain the chosen throughput.
- How evaluation findings lead to targeted recollection, relabeling, or reprocessing.

Distinguish upload acceptance, processing completion, search visibility, and dataset
release. Define the guarantees at each boundary.

## Validation scenarios

1. A collector resumes an interrupted upload and resubmits an overlapping segment.
2. A codec error leaves only part of a recording decodable.
3. A timestamp correction invalidates existing clip-label alignment.
4. Near-duplicate footage appears in both training and evaluation sets.
5. Consent is withdrawn after derived artifacts and dataset snapshots exist.
6. Training readers outpace the dataset delivery layer.

Describe detection, recovery, provenance, and downstream effects.

## Related exercises

- [Robotics video ingestion and processing](robotics_video_pipeline.md) focuses on robot recordings.
- [Evaluation platform](evaluation_platform.md) covers measuring dataset-driven improvements.
