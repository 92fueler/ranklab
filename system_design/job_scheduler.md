# General – Job scheduler (Mercor workflow-inspired practice variant)

## References

- [Reported Mercor workflow topic](mercor_system_design_reports.md): user-supplied reports; original public URLs unavailable.
- [Public workflow practice question](https://prachub.com/interview-questions/design-a-workflow-orchestration-system-that-runs-multi-step-jobs-reliably).
- [Workflow-orchestration exercise](workflow_orchestration.md).

## Evidence status

The available evidence supports workflow or work orchestration, not a separate Mercor job-scheduler interview question. This document narrows that related topic to independent jobs. Its product behavior and operational constraints are original practice assumptions; do not count it as another reported interview round.

## Problem statement

Design a service that accepts independent jobs, starts eligible work, and reports execution outcomes. Decide whether the exercise includes immediate jobs, delayed jobs, recurring jobs, or a subset. Dependencies between jobs belong to the separate workflow exercise.

## Functional requirements

For the proposed scope:

- Submit work with inputs, ownership, and an eligibility time or condition.
- Expose accepted, waiting, running, and completed or failed outcomes, with your precise state definitions.
- Allow cancellation and, if supported, rescheduling.
- Retry eligible failures under a declared policy without hiding previous attempts.
- Recover accepted work after a scheduler or worker interruption.
- Distinguish retries from new occurrences of a recurring job.
- Define overlapping occurrences, missed schedules, and time-zone changes if recurrence is included.

## Non-functional requirements

Set explicit exercise targets for submission volume, concurrent execution, job duration, scheduling accuracy, and recovery time. Clarify:

- Whether successful submission implies durable acceptance.
- Fairness among tenants and priorities under sustained demand.
- Resource limits and behavior when capacity is unavailable.
- Inspectability of overdue or repeatedly failing jobs.
- Which execution guarantees apply to external side effects.

These targets are not source facts.

## Optional failure conditions

A worker continues after losing ownership; cancellation arrives as execution begins; a job changes an external system before crashing; a long-running recurring job overlaps its next occurrence. Define required outcomes rather than choosing scheduling algorithms or coordination mechanisms.
