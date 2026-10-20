# Workflow orchestration

## Core prompt

Design a platform for defining and executing workflows.

The workflow language, dependency model, execution scale, and service-level
objectives are not fixed. Make those choices explicit.

## Questions to resolve

- Is a workflow a directed acyclic graph, a state machine, or another model?
- Can tasks create more tasks, branch conditionally, or wait for external events?
- What constitutes task and workflow success?
- What execution guarantees do task implementations need?
- How are dependencies, inputs, outputs, and workflow versions represented?
- Which workloads need priority, deadlines, or tenant-specific quotas?

## Optional design directions

Start with the task lifecycle and a small workflow, then consider:

- Scheduling ready tasks and coordinating workers.
- Durable state transitions and recovery after worker or scheduler failure.
- Retry policies, backoff, timeouts, and idempotent task execution.
- Cancellation propagation and treatment of tasks already in progress.
- Inspecting a stalled workflow and distinguishing waiting from failed work.
- Priority, backpressure, resource quotas, and observability.

Do not assume that a scheduler can guarantee exactly-once external effects.
Explain what the platform guarantees and what task implementations must handle.

## Validation scenarios

Trace a workflow with two independent tasks followed by a task that depends on both:

1. One predecessor fails transiently.
2. A worker crashes after producing an output but before acknowledging completion.
3. The final task is delivered more than once.
4. A workflow is cancelled while one task is running.
5. A dependency never completes.

For each scenario, show durable state, recovery behavior, and what the user sees.
If versioning or dynamic dependencies are in scope, add a scenario for them.

## Related exercises

- [Cloud-agent system](cloud_agents.md) adds tool permissions and agent execution concerns.
- [Reliable payment integration](payment_integration.md) explores idempotency across a service boundary.
- [Technical communication and validation](../questions/technical_communication.md) covers explaining guarantees and testing assumptions.
