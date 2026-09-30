2026-09-14 02:44

Status: #baby

Tags: [[Operating System Security and Access Control]] [[Linux Virtual Memory Internals]]

# Virtual Memory Protection

Virtual memory gives each process a controlled address space that the operating system maps onto physical memory. The mapping can isolate process pages and attach permissions that distinguish readable, writable, or executable regions.

Because processes work through virtual rather than unrestricted physical addresses, one process cannot ordinarily name another process's memory directly. The mechanism contributes to [[Memory Protection]] alongside process isolation and hardware enforcement.

Linux describes mapped regions with [[Virtual Memory Area|virtual memory areas]] and realizes their page-level permissions through [[Page Table|page tables]]. Non-present mappings, execute restrictions, a deliberately unmapped null region, and the user/kernel access bit turn invalid or unauthorized references into faults rather than silent physical-memory access.

# References

[[cybersecurity.epub]]
[[linuxkernelprogramming_secondedition.pdf]]
