# Mercor – Cloud-agent system (reported topic)

## References

- [Mercor report collection](mercor_system_design_reports.md): user-supplied report; original public URL unavailable.
- [Related workflow exercise](workflow_orchestration.md), which has a different scope.

## Evidence status

The supplied material contains a short follow-up comment naming a cloud-agent system-design topic. It does not specify agent capabilities, interfaces, permissions, scale, or execution guarantees. The problem and requirements below expand that topic into an original practice exercise; they are not a recovered interview specification or an official company rubric.

## Problem statement

Design a cloud-hosted service where users submit tasks for software agents and inspect their progress and results. First define which tasks an agent may perform and which actions, if any, can affect external systems.

## Functional requirements

Assume the practice service must:

- Accept a task with inputs, ownership, and a clear completion criterion.
- Show task status, progress, outputs, and understandable failure information.
- Let users cancel work, with defined behavior for actions already in progress.
- Respect each task's allowed tools, data access, and required user approvals.
- Recover interrupted tasks according to an explicit retry policy.
- Distinguish task completion from the outcome of any external action whose response is missing.

Interactive execution, scheduled tasks, and cooperation among agents are optional scope choices.

## Non-functional requirements

Proposed constraints to clarify:

- Concurrent tasks, duration distribution, submission rate, and progress-update latency.
- Availability, accepted-work durability, and recovery objectives.
- Tenant isolation, secret protection, retention, and auditable authorization.
- Per-task resource budgets and fair treatment under overload.
- Visibility into stalled work, repeated failures, and resource consumption.

No measured targets or architecture are established by the report.

## Optional failure conditions

An agent loses contact after changing an external system; cancellation races with a tool action; a task requests unauthorized access; one tenant exhausts available capacity. Specify the expected user-visible outcomes without assuming a particular execution framework.
