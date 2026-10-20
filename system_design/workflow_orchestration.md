# Mercor – Workflow orchestration (reported system-design topic)

## References

- [Mercor report collection](mercor_system_design_reports.md): user-supplied reports; original public URLs unavailable.
- [Expanded public practice question](https://prachub.com/interview-questions/design-a-workflow-orchestration-system-that-runs-multi-step-jobs-reliably).

## Evidence status

Supplied candidate reports name workflow design and work orchestration; one describes a 45-minute system-design round. They do not establish a specific workflow language, graph model, scale, or service-level target. The public practice page elaborates the topic. The requirements below are inferred exercise assumptions, not a verbatim interview contract.

## Problem statement

Design a platform where users define multi-step work, start a run, and inspect its progress until completion or failure. Clarify how dependencies, inputs, outputs, and successful completion are expressed before selecting an architecture.

## Functional requirements

For the proposed practice scope:

- Accept a workflow definition and start executions with supplied inputs.
- Begin each task only when its declared prerequisites are satisfied.
- Expose task and workflow progress, outputs, and failure information.
- Handle timeouts and retryable failures according to a declared policy.
- Recover interrupted executions without silently losing accepted work.
- Allow cancellation with explicit behavior for running tasks and completed external actions.
- Explain why a workflow is waiting, blocked, failed, or complete.

Conditional branches, dynamic tasks, human approval, and workflow-version changes are optional extensions.

## Non-functional requirements

Choose targets for workflow volume, task duration, dispatch delay, availability, and recovery. Clarify accepted-work durability, tenant isolation, resource budgets, and fairness under overload. Define what the platform guarantees when task execution is repeated and what remains the responsibility of the task itself. No numerical targets are established by the reports.

## Optional failure conditions

Two independent tasks feed a third task. One predecessor fails; a completion response is lost; a task runs twice; cancellation arrives mid-execution; a prerequisite never finishes. Specify the correct visible outcome for each case without prescribing a workflow engine, database, queue, or coordination protocol.
