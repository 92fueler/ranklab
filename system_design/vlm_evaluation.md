# Video vision-language model evaluation

## Core prompt

How would you design an evaluation system for a vision-language model trained
on egocentric video, so that model and dataset changes can be compared and
failures can guide further data collection?

Which tasks, modalities, deployment context, scale, and quality objectives
must be clarified before selecting metrics or architecture?

## Questions to resolve

- Does the model answer video questions, ground language in frames or regions,
  identify temporal events, or perform another task?
- How are recordings, time windows, sampled frames, prompts, and reference labels versioned?
- How are splits separated across collectors, environments, sessions, overlapping
  clips, and near-duplicate footage to limit leakage?
- What spatial and temporal alignment is required between model inputs, outputs,
  and reference annotations?
- Which questions are answerable from the available footage, and when should the
  model express uncertainty or abstain?
- What privacy, access, and retention constraints apply to evaluation artifacts?

## Optional design directions

- How does an evaluation specification select cases, input transformations, model
  versions, inference settings, and scoring procedures?
- How are reference labels created, independently checked, and adjudicated when
  the footage or task wording is ambiguous?
- Which task-dependent measures capture answer correctness, visual grounding,
  temporal understanding, hallucination, and appropriate abstention?
- When are human reviewers needed, and how are automated judges calibrated against
  reviewed examples rather than assumed reliable?
- How do failure taxonomies and slices distinguish lighting, occlusion, motion,
  viewpoint, clip length, rare activities, and other relevant conditions?
- How do paired comparisons account for stochastic outputs, correlated clips,
  sample sizes, and measurement uncertainty?
- How are execution failures, incomplete runs, retries, latency, and cost presented
  separately from model quality?
- Which artifacts enable reproducibility, and what limitations remain if external
  dependencies change?
- How can findings inform recollection, relabeling, or training-data changes without
  repeatedly tuning to a supposedly held-out test set?

## Validation scenarios

1. What happens when near-duplicate training footage is discovered in an evaluation split?
2. How is a correct event label scored when its predicted time window is displaced?
3. How is a plausible answer handled when the video does not support it?
4. What happens when an automated judge disagrees systematically with human reviewers?
5. What can be concluded when aggregate scores improve but a slice regresses?
6. How are results revisited after a reference-label correction?

## Related exercises

- [Egocentric video data platform](egocentric_video_data_platform.md)
- [Evaluation platform](evaluation_platform.md)
