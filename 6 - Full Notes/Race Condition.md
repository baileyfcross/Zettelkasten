2026-09-08 21:16

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]]

# Race Condition

A race condition occurs when a program's result depends on the timing or interleaving of concurrent operations. Unsynchronized read-modify-write sequences can lose updates even when each individual read and write appears simple.

Races are prevented by removing shared mutable state, partitioning ownership, using immutable data, or applying an appropriate synchronization primitive. Tests may fail to reproduce them consistently because scheduling changes from run to run.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
