2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Memory Allocation]]

# Out-of-Memory Killer

The Linux out-of-memory killer selects a process to terminate when the kernel cannot satisfy an allocation after permitted reclaim and other recovery attempts. It uses a badness heuristic influenced by memory use, administrator adjustments, and the scope of the shortage.

The goal is to free enough memory while preserving system recoverability, not to identify moral fault for the shortage. An OOM event can be system-wide or constrained to a memory control group, and [[Linux Memory Overcommit]] policy affects how readily workloads reach this state.

# References

[[linuxkernelprogramming_secondedition.pdf]]
