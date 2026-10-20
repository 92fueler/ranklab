# World-model evaluation

## Core prompt

Design an evaluation system for a model that predicts future observations or
state from observation history and proposed actions. Decide whether its outputs
support visualization, planning, policy training, or policy evaluation: those
uses require different evidence.

Visually convincing frames do not establish temporal coherence, geometric
consistency, correct contact dynamics, or responsiveness to actions. A single
photorealism score cannot prove usefulness as a control simulator.

## Experimental contract

Hold out episodes and relevant combinations of objects, tasks, environments,
and embodiments. Pin model, policy, dataset, action interface, calibration,
sampling configuration, and scoring versions. Separate teacher-forced
next-step prediction from free-running rollouts, where errors accumulate.
Do not select checkpoints on the held-out evaluation rollouts.

Compare action-conditioned rollouts against held-out real trajectories at
several horizons. Where feasible, construct matched real and simulated scenarios
with comparable initial state, objects, instructions, sensing, and action timing.
Report residual mismatches rather than treating a visually similar scene as
the same experiment. Evaluate both replayed action sequences and closed-loop
policies; feedback changes the action distribution.

## Measurement dimensions

- Appearance and semantics: object identity, relevant attributes, and visibility,
  using task-appropriate reference comparisons and reviewed examples.
- Temporal and geometric consistency: persistence, motion, occlusion, viewpoint
  changes, depth, and spatial relations where trustworthy measurements exist.
- Action consistency: whether commanded direction, magnitude, timing, contact,
  and resulting state changes agree with available reference evidence.
- Long-horizon behavior: compounding error, recovery, state drift, and failure
  frequency, not just favorable short clips.

Probe counterfactual actions from similar initial conditions. Check whether
predictions change appropriately, but do not call an unobserved alternative
ground truth; use controlled real trials or validated constraints when possible.
Evaluate uncertainty against observed errors and coverage, with separate
out-of-distribution slices. Diverse samples alone do not establish calibrated
uncertainty.

## Validate the downstream proxy

If simulation ranks policies, compare multiple policy checkpoints on matched
real and simulated tasks. Test whether the simulator preserves the ordering of
real policy performance, with uncertainty and individual ranking reversals,
rather than only matching an average success rate. A policy may exploit model
errors; test candidates beyond those used to tune the simulator.

Report real task success, safety-relevant failures, sample size, and scenario
coverage alongside simulation results. Use episode-level paired comparisons
when appropriate. Restrict conclusions to tested tasks and distributions;
strong ranking agreement is evidence for that use, not universal validity.

## Validation scenarios

1. A rollout looks realistic while an object moves opposite to the command.
2. Short-horizon accuracy improves but long-horizon policy rankings reverse.
3. Low uncertainty accompanies frequent failures on an unseen object class.

## Related exercises

- [Multimodal model training](multimodal_model_training.md)
- [Evaluation metrics](../questions/evaluation_metrics.md)
