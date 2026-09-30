2026-09-30 01:38

Status: #baby

Tags: [[Linux CPU Scheduling and Control Groups]]

# POSIX Scheduling Policies

POSIX scheduling policies give applications interfaces for selecting normal and real-time scheduling behavior. Linux implements fixed-priority FIFO and round-robin real-time policies alongside normal time-sharing policies, with privileges and resource limits controlling who may request them.

FIFO tasks continue until blocking, yielding, or preemption by higher priority, while round-robin tasks of equal priority also rotate after a time quantum. These policies are mapped into a [[Linux Scheduling Class]] and must be used carefully because an unbounded real-time task can starve ordinary work.

# References

[[linuxkernelprogramming_secondedition.pdf]]
