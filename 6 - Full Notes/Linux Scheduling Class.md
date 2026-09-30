2026-09-30 01:38

Status: #baby

Tags: [[Linux CPU Scheduling and Control Groups]]

# Linux Scheduling Class

A Linux scheduling class encapsulates the policy-specific operations used to enqueue, dequeue, account for, and select schedulable entities. Classes are ordered by precedence so stop, deadline, real-time, fair, and idle work can coexist behind the scheduler's common interface.

The core scheduler asks classes in priority order for the next eligible entity rather than embedding all policies in one algorithm. Ordinary time-sharing tasks are handled by the [[Completely Fair Scheduler]], while real-time policies use a higher-precedence class.

# References

[[linuxkernelprogramming_secondedition.pdf]]
