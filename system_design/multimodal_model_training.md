# Multimodal model training

## Core prompt

Design a shared training platform where researchers submit versioned video,
language, robot-state, and action datasets, launch GPU jobs, and compare resulting
checkpoints. Support queued jobs, progress inspection, cancellation, failure
recovery, and reproducible lineage. Clarify users, scale, budgets, and targets.

## Define the prediction target

- A vision-language model (VLM) may predict answers, captions, grounded regions,
  or event labels from images or video and language, without robot actions.
- A vision-language-action model (VLA) predicts actions from observations,
  instructions, and possibly proprioception or history. Define whether outputs
  are joint commands, end-effector motions, discrete skills, or action chunks.
- A world model predicts future observations or latent state from history and,
  when action-conditioned, proposed actions. Predicting futures differs from
  selecting a successful control policy.

These roles can share components without sharing objectives or evaluation.

## Dataset and model contracts

Pin an immutable manifest containing episode identifiers, source revisions,
splits, timestamps, annotations, filtering decisions, synchronization rules, and
transformation versions. Connect each checkpoint to that manifest, model
initialization, configuration, code revision, and preprocessing.

Define modality availability, padding, and loss masks. Examples need not have
every modality; missing actions are not zero actions. Human video lacks measured
robot actions: distinguish inferred or inverse-dynamics pseudo-actions from
recorded supervision. Standardize compatible action representations, specifying
absolute/delta commands, coordinate frames, units, rotations, control frequency,
horizon, calibration, and training-only normalization statistics. Incompatible
embodiments may need separate adapters or heads rather than a universal action space.

Choose sampling weights across tasks, embodiments, sites, sources, and rare
conditions. Track effective exposure: balanced batches do not imply balanced
deployment performance. Keep related
episodes, overlapping clips, near-duplicates, people, and sites together where
the intended generalization test requires it; declare which axes are held out.

## Objectives and adaptation

Select objectives by architecture and target: contrastive or generative
vision-language alignment, supervised grounding, action prediction, or future
state prediction. Continuous action heads may use regression, diffusion, or
flow-matching objectives; tokenized action heads may use autoregressive losses.
Some systems combine text generation with continuous action generation, or use
discrete action supervision during training without that decoding path at
inference. Do not assume every VLA generates actions autoregressively.

Compare frozen visual/language backbones plus adapters against partial or full
fine-tuning, considering supervision, compute, forgetting, and embodiment
transfer. Record objective weights. Use controlled ablations that fix downstream
data, architecture, optimization, and evaluation when isolating pretraining changes.

## Execution and release

What APIs and durable records represent a run, dataset snapshot, resource request,
checkpoint, and evaluation? Which state transitions are atomic, who may cancel
a run, and how do retries avoid launching duplicate expensive jobs?

Allocate distributed jobs by GPU memory, interconnect, parallelism strategy, and
priority. Measure decoding, object-store reads, augmentation, and host-to-device
transfer before assuming low GPU utilization requires more GPUs. Use sharding,
prefetching, caching, and bounded queues without changing sampling semantics.

Checkpoint model, optimizer, scheduler, mixed-precision state, random generators,
sampler position, and data-loader progress. Exact resume additionally depends on
worker ordering and deterministic kernels; otherwise document the reproducible
configuration and expected divergence. Publish checkpoints atomically.

Run controlled held-out evaluations before bounded closed-loop tests. Compare
matched baselines, important slices, latency, task success, and safety failures;
offline loss alone does not authorize deployment.

## Validation scenarios

1. A worker fails after consuming batches but before checkpoint publication.
2. An action stream changes units while its tensor shape stays unchanged.
3. Aggregate performance improves while an unseen-site slice regresses.

## Related exercises

- [Robotics video ingestion and processing](robotics_video_pipeline.md)
- [Video vision-language model evaluation](vlm_evaluation.md)
- [World-model evaluation](world_model_evaluation.md)
