2026-09-30 01:38

Status: #baby

Tags: [[Linux CPU Scheduling and Control Groups]]

# Real-Time Linux

Real-time Linux focuses on bounded scheduling and interrupt latency rather than simply making the average case faster. Preemptible kernel paths, threaded interrupts, priority-aware locking, and careful workload configuration reduce the longest time a high-priority task can be delayed.

The PREEMPT_RT work converts many traditional spin-based critical sections into preemptible mechanisms and uses [[RT-Mutex]] priority inheritance where appropriate. Meeting a deadline still requires end-to-end analysis of hardware, drivers, memory behavior, scheduling policy, and competing tasks.

# References

[[linuxkernelprogramming_secondedition.pdf]]
