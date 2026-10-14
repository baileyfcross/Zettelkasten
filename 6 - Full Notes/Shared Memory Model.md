2026-09-27 00:11

Status: #baby

Tags: [[.NET Distributed Memory and Message Passing]] [[Parallel Statistical Computing]]

# Shared Memory Model

In a shared-memory model, processors or threads communicate by reading and writing locations in a common address space. Exchange is inexpensive because participants need not serialize every value into a message.

The model exposes races, cache coherence effects, and synchronization overhead. Correctness depends on explicit ordering and ownership rules, while scalability eventually encounters contention for memory paths and shared data structures.

[[OpenMP]] expresses this model by creating threads that can share arrays while giving selected loop indices and temporary values private storage. A correct data-sharing clause prevents different threads from overwriting what should have been per-thread state.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
