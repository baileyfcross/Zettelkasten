2026-09-27 00:11

Status: #baby

Tags: [[.NET Server Concurrency and Parallel Patterns]]

# Thread Pool Starvation Avoidance

Thread-pool starvation occurs when queued work cannot obtain workers because existing workers remain occupied, often by blocking waits. A runtime can detect inadequate progress and inject additional threads so the queue does not remain stalled.

Injection is a recovery mechanism with ramp-up time and resource cost, not permission to block without limit. Asynchronous I/O and bounded concurrency address the workload cause more directly by returning workers while operations wait.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
