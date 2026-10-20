# Multimodal dataset joins

## Core prompt

Design an offline dataset service accepting modality manifests and a join
specification, publishing versioned episode shards for training readers.
Sources arrive asynchronously at different rates. Choose the learning objective
before the timeline.

What distinguishes an available observation from a future prediction target?
Matching timestamps do not establish availability at decision time.

## Small example

An episode has 30 Hz images, 100 Hz state, and 10 Hz commands.
At action time 1.100 seconds, the preceding image was exposed at 1.083 seconds;
the state sample at 1.100 is missing.

Would a 20-millisecond tolerance admit the image? Use state at 1.090,
interpolate between 1.090 and 1.110 for offline reconstruction, or mark missing?
Interpolation uses future evidence here, not an observation available to a
causal policy. Arrival times and sensor latency may impose stricter constraints.

How should the answer change if the camera clock is 40 milliseconds ahead,
or the action timestamp records command receipt rather than execution?

## Choose the temporal contract

- Which identifier binds an episode, device, camera, and recording segment?
  Which clocks are authoritative, and how are offset, drift, correction version,
  and uncertainty recorded?
- Will each modality use exact matching, nearest matching within a tolerance,
  backward-only matching, or interpolation? Define tie-breaking, gaps, and
  maximum staleness separately.
- Which quantities support interpolation? Continuous positions may; rotations
  need appropriate methods. Do not apply scalar interpolation indiscriminately
  to categorical events, image frames, or discrete action identities.
- How do exposure intervals, rolling shutter, dropped frames, and action duration
  affect the meaning of a sample?

## Choose the spatial and provenance contract

Which coordinate frame and units describe each pose or action? Pin calibration
versions, camera intrinsics and extrinsics, robot configuration, and transform
conventions. How are invalid or uncertain transforms surfaced rather than
silently producing plausible coordinates?

Keep source references, original and corrected timestamps, join rules, sample
IDs, interpolation provenance, missingness masks, and label versions.
Missing data must not become a valid zero. Represent image-only or text-image
examples without inventing telemetry or timestamps.

For a million episodes, choose partition keys, incremental recomputation,
submission/status interfaces, and an atomic publication boundary.
How do workers retry without duplicating shards or exposing partial snapshots?

## Separate reconstruction from streaming

What completeness condition closes an offline episode? Which late corrections
require new snapshots rather than overwriting published data?

A streaming consumer needs watermarks, allowed lateness, provisional results,
and corrections or retractions. An offline join does not automatically provide
these guarantees or reproduce deployment availability.

## Release checks and failure cases

Group related episodes, overlapping clips, repeated demonstrations, and relevant
collection sessions before splitting. Fit learned preprocessing only on training
data; never let future labels or targets enter observation features.

Test clock resets, missing calibration, out-of-order arrivals, long sensor gaps,
and a duplicated episode under a new filename. What timestamp residuals, coverage
rates, manual alignment audits, and causal-availability checks block release?

## Related exercises

- [Robotics video ingestion](robotics_video_pipeline.md)
- [Egocentric video platform](egocentric_video_data_platform.md)
- [Video curation and sampling](video_curation_and_sampling.md)
