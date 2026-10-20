# Cloud-agent system

## Core prompt

Design a cloud-hosted system that runs agent tasks.

The agent's capabilities, task model, interfaces, scale, and permissions are open
design questions. Establish these before choosing an architecture.

## Questions to resolve

- Who submits a task, what inputs does it contain, and what counts as completion?
- Is execution interactive, asynchronous, scheduled, or a combination?
- Can agents call external tools or change external state?
- Which actions require user approval, and how is that approval scoped?
- What task duration, concurrency, latency, and availability should the system support?
- What execution state must survive a worker or service restart?
- What are the tenant, data-retention, and isolation boundaries?

## Optional design directions

Use the following questions to expand an explicitly chosen scope:

1. How do task submission, admission control, and scheduling work?
2. How are task status, checkpoints, outputs, and errors stored durably?
3. How does a worker claim work, renew its lease, and recover after a crash?
4. Which operations can safely be retried? How are duplicate external effects prevented?
5. How do cancellation, deadlines, and partial results behave?
6. How are tool permissions, secrets, sandboxing, and user approvals enforced?
7. How can a user inspect progress or diagnose a stalled task?
8. How do quotas, backpressure, logs, metrics, and traces expose resource use?

## Validation scenarios

Choose relevant scenarios and explain the expected state transitions:

- A worker stops after an external action but before recording its result.
- A task is delivered twice.
- A user cancels while a tool call is in progress.
- A task requests a tool outside its permissions.
- One tenant submits enough long-running tasks to exhaust shared capacity.

Describe where guarantees stop. Durable execution does not by itself make every
external effect exactly once.

## Related exercises

- [Workflow orchestration](workflow_orchestration.md) focuses on task dependencies and recovery.
- [Reliable payment integration](payment_integration.md) examines a consequential external effect.
- [Technical communication and validation](../questions/technical_communication.md) provides a structure for documenting assumptions and trade-offs.
