2026-09-30 01:38

Status: #baby

Tags: [[Linux Process and Task Internals]]

# Linux Kernel Thread

A Linux kernel thread is a schedulable task that executes kernel code without an ordinary user-space address space. It has a [[Linux Task Structure]] and participates in scheduling like other threads, but it performs background kernel work such as memory reclaim or device management.

Kernel threads are created and managed through kernel APIs rather than by entering from a user process. They must still obey synchronization, lifetime, stop-request, and scheduling rules, and their names and states are visible through normal process-inspection tools.

# References

[[linuxkernelprogramming_secondedition.pdf]]
