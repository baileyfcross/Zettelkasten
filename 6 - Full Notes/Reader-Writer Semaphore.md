2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Locking]]

# Reader-Writer Semaphore

A reader-writer semaphore is a sleeping Linux lock that permits multiple readers or one exclusive writer. It is usable only in contexts allowed to block, making it different from the spin-based [[Reader-Writer Lock]] used in atomic contexts.

The abstraction can help when reads are long enough and sufficiently concurrent to repay its overhead. Writer latency, fairness, and read-side cache contention still matter, and [[Read-Copy-Update]] can be a better design when read-mostly access must be extremely cheap.

# References

[[linuxkernelprogramming_secondedition.pdf]]
