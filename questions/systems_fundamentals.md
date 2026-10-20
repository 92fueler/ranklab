# Systems fundamentals

Each section is a separate question. State assumptions before answering;
the follow-ups are additional engineering choices, not fixed requirements.

## 1. Processes and threads

Compare Linux processes and threads: address-space isolation, shared resources,
communication, scheduling, and failure behavior. How would you select a Python
concurrency approach for CPU-bound versus I/O-bound work?

Follow-up: State the Python implementation, version, and build assumptions.
How do those assumptions affect parallel execution, synchronization, and the
relevance of a global interpreter lock?

## 2. Web request lifecycle

Explain what happens when a browser opens a website, from name resolution and
connection establishment through TLS, HTTP, edge routing, application handling,
and rendering.

Follow-up: Which steps can be skipped or reused because of caching or an
existing connection? Where would you measure latency and diagnose failure?
State the protocol assumptions.

## 3. Virtual private cloud networking

Explain a virtual private cloud and distinguish public and private subnets.
How do routing and network controls determine which resources can communicate?
How can private workloads access internet services securely?

Follow-up: Separate outbound connectivity from unsolicited inbound access.
Explain your proposed access paths, address assumptions, and failure boundaries.

## 4. Kubernetes scaling and routing

Explain the difference between scaling pods and scaling nodes. Trace inbound
traffic to a workload, and compare ReplicaSet and StatefulSet responsibilities
and appropriate use cases.

Follow-up: What happens when additional pods cannot be scheduled, or when
traffic reaches an unready instance? Which identity and storage requirements
would change your controller choice?

## 5. Streaming systems

Compare two streaming frameworks for a stated workload. Define at-most-once,
at-least-once, and exactly-once guarantees and identify the boundaries where
each applies.

Follow-up: Explain how recovery, checkpoints, replay, and sink behavior affect
observable outcomes. Which mechanisms prevent duplicate external effects,
and what latency, storage, and coordination costs do they impose?

## 6. One-way functions and security goals

Define a one-way function and the assumptions behind practical inversion
difficulty. Discuss password verification, integrity checking, and digital
signatures without treating their requirements as interchangeable.

Follow-up: Which properties and additional mechanisms does each application
need? Distinguish inversion resistance, collision resistance, authentication,
and signature verification. State the attacker capabilities and what the
proposed construction does not guarantee.
