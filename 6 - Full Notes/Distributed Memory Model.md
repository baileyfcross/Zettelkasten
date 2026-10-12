2026-09-27 00:11

Status: #baby

Tags: [[.NET Distributed Memory and Message Passing]] [[Parallel Statistical Computing]]

# Distributed Memory Model

In a distributed-memory model, each processing node owns a separate address space and exchanges data explicitly over a communication network. A participant cannot directly dereference another node's memory.

Separation removes accidental shared-memory races across nodes but makes data placement, serialization, latency, and partial failure part of the algorithm. Parallel speedup depends on keeping local computation large relative to communication and coordination.

With MPI, each process uses its [[Process Rank]] to determine which data it owns and exchanges explicit typed buffers through [[MPI Point-to-Point Communication]] or [[MPI Collective Communication]]. The decomposition must include both local calculations and the messages needed to assemble the final statistic.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
