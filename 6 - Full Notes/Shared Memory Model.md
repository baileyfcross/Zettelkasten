2026-09-27 00:11

Status: #baby

Tags: [[.NET Distributed Memory and Message Passing]]

# Shared Memory Model

In a shared-memory model, processors or threads communicate by reading and writing locations in a common address space. Exchange is inexpensive because participants need not serialize every value into a message.

The model exposes races, cache coherence effects, and synchronization overhead. Correctness depends on explicit ordering and ownership rules, while scalability eventually encounters contention for memory paths and shared data structures.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
