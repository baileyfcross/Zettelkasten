2026-09-27 00:11

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]]

# Task Work-Stealing Queues

The task scheduler can place recursively created work in a worker-local queue and let that worker take recent items in last-in-first-out order, preserving cache locality. An idle worker may steal older items from the opposite end of another worker's queue to keep processors occupied.

Work stealing balances load without funneling every operation through one global queue. It is an implementation optimization rather than an ordering promise, so task code must remain correct under different execution orders and thread assignments.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
