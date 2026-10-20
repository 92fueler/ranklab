# Robotics video ingestion and processing

## Core prompt

Design a large-scale pipeline that ingests video collected by robots, processes
it, and makes selected outputs available for downstream analysis or dataset creation.

Fleet size, recording volume, connectivity, latency, and retention are unspecified.
Distinguish required behavior from optional extensions.

## Questions to resolve

- What constitutes an ingestible unit: a recording session, clip, chunk, or frame?
- Are multiple cameras or sensors associated with each recording?
  Which timestamps, calibration data, and synchronization guarantees matter?
- How much processing happens on the robot, and what must reach the cloud?
- How should intermittent connectivity, limited local storage, and partial uploads behave?
- Which transformations are required, and how quickly must their results be available?
- Who consumes raw video, derived artifacts, and searchable metadata?
- What access controls, retention policies, and deletion requirements apply?

## Optional design directions

Trace capture to usable output. Consider:

- How resumable ingestion detects corruption, missing chunks, and duplicate uploads.
- How metadata identifies recordings independently of storage.
- How processing is scheduled across resources with different capabilities.
- How backpressure affects collection, upload, processing, and downstream consumers.
- How inputs, transformation versions, and output lineage are recorded.
- How reprocessing and partial failures affect previously published outputs.
- How completeness, processing lag, storage cost, and data quality are measured.

Which artifacts must be consistent before a recording or dataset version becomes
visible? An uploaded file need not mean a complete, usable recording.

## Validation scenarios

1. A robot disconnects midway through an upload and later retries it.
2. A camera stream arrives after the rest of its recording session.
3. A processing worker fails after producing only some outputs.
4. A transformation bug requires reprocessing an affected subset of recordings.
5. Upload volume exceeds processing capacity for a sustained period.
6. A source recording must be deleted after derived artifacts exist.

For each scenario, describe detection, authoritative metadata, recovery, and
downstream visibility.

## Related exercises

- [Job scheduler and task execution](job_scheduler.md) explores dispatch and worker recovery.
- [Human annotation and quality control](annotation_quality_control.md) covers downstream labeling.
