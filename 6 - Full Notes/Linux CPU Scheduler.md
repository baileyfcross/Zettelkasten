2026-09-30 01:38

Status: #baby

Tags: [[Linux CPU Scheduling and Control Groups]]

# Linux CPU Scheduler

The Linux CPU scheduler chooses which runnable [[Kernel Schedulable Entity]] executes on each CPU. It must balance throughput, latency, fairness, priority, affinity, energy use, and load distribution across processors under several different scheduling policies.

Each CPU maintains a [[Linux Runqueue]], and scheduling classes implement policy-specific selection. A switch can occur because a task blocks, exhausts its entitlement, is preempted by a more urgent task, or explicitly yields, leading to a [[Linux Context Switch]].

# References

[[linuxkernelprogramming_secondedition.pdf]]
