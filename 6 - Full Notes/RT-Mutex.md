2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Locking]]

# RT-Mutex

An RT-mutex is a sleeping mutual-exclusion primitive with priority inheritance. When a higher-priority task blocks on the lock, the owner's effective priority can be boosted, including through nested dependency chains, so unrelated medium-priority work does not prolong [[Priority Inversion]].

The mechanism is central to priority-inheritance futexes and [[Real-Time Linux]] locking transformations. It adds bookkeeping and does not make long or unbounded critical sections acceptable; it specifically addresses scheduling delay caused by lock ownership.

# References

[[linuxkernelprogramming_secondedition.pdf]]
