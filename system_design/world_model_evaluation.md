# World Labs Real-to-Sim-to-Real: Evaluation platform

Published-system-inspired exercise; not a verified interview prompt.

## References

- [World Labs: Building Worlds That Train Robots](https://www.worldlabs.ai/blog/real-to-sim-to-real)

## Published System Context

World Labs describes reconstructed interactive worlds validated through matched open-loop actions in simulation and reality. It also reports closed-loop evaluation where simulated results preserve relative policy rankings and reveal similar failure regions. These are reported findings for demonstrated settings, not proof that every reconstructed world predicts every robot's performance.

## Problem Statement

Design an evaluation backend that helps researchers decide whether a reconstructed world is useful for comparing robot policies. It must manage simulated trials, corresponding hardware evidence, and reproducible reports. Support both replaying a fixed action sequence to assess alignment and running policies in closed loop to assess downstream usefulness.

All requirements below are proposed exercise scope, not claims about World Labs' backend.

## Functional Requirements

- Register versioned worlds, policy checkpoints, task definitions, robot/sensor configurations, and real-world reference trials with their usage restrictions.
- Let researchers submit evaluation suites specifying initial conditions, policy candidates, test distributions, repetition rules, and scoring definitions.
- Distinguish matched open-loop comparisons from closed-loop policy trials. Record residual setup differences so unmatched conditions are not presented as controlled comparisons.
- Execute and track distributed simulation jobs; accept authorized hardware-trial results. Support cancellation, retries, and explicit incomplete or invalid outcomes.
- Preserve observations, actions, outcomes, relevant timing, and trial metadata as inspectable artifacts linked to the exact evaluation configuration.
- Compare simulated and real policy rankings, progress across checkpoints, and failure regions. Report trial counts and uncertainty rather than collapsing all evidence into a visual-quality score.
- Let researchers inspect ranking reversals and regressions, compare report versions, and request additional evaluation on poorly covered conditions.
- Expose interfaces for suite submission, trial status, artifact retrieval, and report comparison. Hardware execution approval remains a separate workflow.

## Non-Functional Requirements

Proposed exercise assumptions, not World Labs' reported service guarantees:

- Trial failures and missing hardware evidence must remain distinguishable from policy failures.
- Reports must preserve provenance and prevent accidental reuse of tuning examples as held-out evidence.
- Parallel evaluation must respect agreed compute budgets and hardware capacity.
- Completed results must survive worker failures without double-counting retried trials.
- Access to customer environments, recordings, and policies must be restricted appropriately.

## Requirements to Clarify

Agree on tasks, embodiments, scenario coverage, repeat counts, and the tolerance for mismatched initial conditions. How much hardware evidence is available, and who may request more? Define the statistical evidence needed for useful ranking agreement, report latency, artifact retention, and maximum evaluation cost.
