2026-09-30 01:38

Status: #baby

Tags: [[Linux CPU Scheduling and Control Groups]]

# Linux Runqueue

A Linux runqueue is the per-CPU scheduler structure that tracks runnable entities and the state needed to select the next one. It contains scheduling-class-specific queues plus accounting, load, clock, and current-task information protected by low-level locking.

Per-CPU queues reduce global contention, but the scheduler must periodically balance runnable work among processors while respecting [[CPU Affinity Mask]] constraints and topology. Enqueue, wakeup, migration, and context-switch paths all coordinate through runqueue state.

# References

[[linuxkernelprogramming_secondedition.pdf]]
