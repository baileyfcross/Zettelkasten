2026-09-30 01:38

Status: #baby

Tags: [[Linux Process and Task Internals]]

# Kernel Schedulable Entity

A kernel schedulable entity is the unit the [[Linux CPU Scheduler]] can place on a runqueue and select for execution. In ordinary cases the entity represents a thread, although scheduling groups can also be represented hierarchically for group scheduling.

Treating threads as scheduling entities separates CPU allocation from the user-level process abstraction. Threads that share memory and files can still have different states, priorities, CPU affinities, and accumulated runtime.

# References

[[linuxkernelprogramming_secondedition.pdf]]
