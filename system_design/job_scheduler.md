# Job scheduler and task execution

## Core prompt

Design a distributed service that accepts jobs, determines when they are eligible
to run, and assigns them to execution workers.

Focus on independent jobs rather than dependency graphs. Support for
immediate, delayed, and recurring jobs is a scope decision. Define the timing,
durability, and execution guarantees before choosing an architecture.

## Questions to resolve

- What makes a job eligible: its scheduled time, available resources, tenant
  quota, priority, or another condition?
- What timing accuracy, submission rate, concurrent execution, and job duration
  should the service support?
- Can recurring executions overlap? What happens to occurrences missed during
  downtime, or affected by time-zone and daylight-saving changes?
- How are submission, cancellation, rescheduling, and status inspection exposed?
- Which job states are durable, and when may a successful submission be acknowledged?
- Which failures are retryable, and who chooses backoff and attempt limits?

## Optional design directions

Trace a job from submission through eligibility, dispatch, execution, and a
terminal state. Consider:

- How schedulers discover due jobs without losing or repeatedly flooding work.
- How workers claim jobs, renew leases, and report progress or completion.
- How expired leases and late worker responses affect authoritative state.
- How priority, fairness, resource requirements, and backpressure interact.
- How retries differ from new occurrences of a recurring job.
- How operators diagnose jobs that are overdue, stuck, or repeatedly failing.

Distinguish delivery guarantees from guarantees about external side effects.
Explain what job implementations must do when execution can happen more than once.

## Validation scenarios

1. A scheduler restarts while making delayed jobs eligible.
2. A worker's lease expires, but that worker continues running.
3. A job performs an external action and crashes before recording completion.
4. A recurring job takes longer than its recurrence interval.
5. High-priority submissions continuously compete with older jobs.
6. Cancellation arrives just as a worker claims a job.

For each scenario, identify durable state, recovery, and the visible outcome.

## Related exercises

- [Workflow orchestration](workflow_orchestration.md) adds dependencies between tasks.
- [Cloud-agent system](cloud_agents.md) adds permissions and agent execution concerns.
