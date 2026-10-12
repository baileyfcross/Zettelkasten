2026-09-30 01:38

Status: #baby

Tags: [[Linux CPU Scheduling and Control Groups]]

# Linux Context Switch

A Linux context switch stops executing one task and resumes another chosen by the [[Linux CPU Scheduler]]. The kernel saves and restores architecture-specific register state, switches stack and address-space context when necessary, and updates scheduler bookkeeping.

Switching has direct overhead and indirect cache and translation costs, so excessive runnable competition or blocking can reduce throughput. Threads in the same process may share address-space state, but each still has its own execution state and [[Linux Kernel Stack]].

# References

[[linuxkernelprogramming_secondedition.pdf]]
