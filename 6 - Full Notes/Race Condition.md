2026-09-08 21:16

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]] [[.NET Synchronization and Thread Coordination]] [[Linux Kernel Locking]] [[Parallel Program Design]]

# Race Condition

A race condition occurs when a program's result depends on the timing or interleaving of concurrent operations. Unsynchronized read-modify-write sequences can lose updates even when each individual read and write appears simple.

Races are prevented by removing shared mutable state, partitioning ownership, using immutable data, or applying an appropriate synchronization primitive. Tests may fail to reproduce them consistently because scheduling changes from run to run.

The design-patterns source demonstrates that making an inventory context a singleton does not make `Quantity += amount` atomic. Two threads can read the same old quantity and overwrite one another's updates. Locking the read-modify-write section protects that invariant, while constructing the singleton itself needs a separate one-time creation guarantee.

In the Linux kernel, concurrent access can arise from multiple CPUs, preemption, or interrupts as well as ordinary threads. A data race exists when concurrent plain accesses reach the same object and at least one writes it without a valid synchronization relationship, so the analysis must cover every execution context that can reach the shared state.

The current source uses shared-memory threads to show why parallel design must include synchronization. Two activities can each be locally correct yet produce a wrong result when their accesses interleave, so the dependency and data-sharing analysis must precede the choice of locks, barriers, or another coordination mechanism.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
[[hands-ondesignpatternswithcandnetcore.pdf]]
[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]
[[linuxkernelprogramming_secondedition.pdf]]
