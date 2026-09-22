2026-09-08 21:16

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]]

# Race Condition

A race condition occurs when a program's result depends on the timing or interleaving of concurrent operations. Unsynchronized read-modify-write sequences can lose updates even when each individual read and write appears simple.

Races are prevented by removing shared mutable state, partitioning ownership, using immutable data, or applying an appropriate synchronization primitive. Tests may fail to reproduce them consistently because scheduling changes from run to run.

The design-patterns source demonstrates that making an inventory context a singleton does not make `Quantity += amount` atomic. Two threads can read the same old quantity and overwrite one another's updates. Locking the read-modify-write section protects that invariant, while constructing the singleton itself needs a separate one-time creation guarantee.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
[[hands-ondesignpatternswithcandnetcore.pdf]]
