2026-09-30 01:38

Status: #baby

Tags: [[Linux CPU Scheduling and Control Groups]]

# Linux Process State Machine

The Linux process state machine describes transitions among running or runnable, interruptible sleep, uninterruptible sleep, stopped or traced, and exited states. Events such as blocking for I/O, receiving a wakeup, being signaled, or terminating move a task between these conditions.

Only runnable tasks compete on a [[Linux Runqueue]]; a sleeping task consumes no CPU until its wait condition is satisfied. State values are kernel implementation details with combinations and special exit flags, so user-space summaries simplify a richer internal representation.

# References

[[linuxkernelprogramming_secondedition.pdf]]
