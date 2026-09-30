2026-09-30 01:38

Status: #baby

Tags: [[Linux CPU Scheduling and Control Groups]]

# Scheduler Preemption Flag

The scheduler preemption flag records that a rescheduling decision should occur at the next safe opportunity. A timer tick, wakeup, priority change, or other event can mark the current task as needing reschedule when another runnable entity should receive the CPU.

Setting the flag does not itself perform a [[Linux Context Switch]] at an arbitrary unsafe instruction. The kernel checks it at defined preemption points, such as returning to user mode or re-enabling preemption, so low-level critical sections remain coherent.

# References

[[linuxkernelprogramming_secondedition.pdf]]
