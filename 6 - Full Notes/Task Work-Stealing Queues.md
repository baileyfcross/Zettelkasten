2026-09-27 00:11

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]] · [[Java Concurrency and Reactive Streams]]

# Task Work-Stealing Queues

The task scheduler can place recursively created work in a worker-local queue and let that worker take recent items in last-in-first-out order, preserving cache locality. An idle worker may steal older items from the opposite end of another worker's queue to keep processors occupied.

Work stealing balances load without funneling every operation through one global queue. It is an implementation optimization rather than an ordering promise, so task code must remain correct under different execution orders and thread assignments.

Java's `ForkJoinPool` applies the same mechanism to recursively split-and-join work, including the tasks behind ordinary parallel streams. A worker that finishes early steals from another worker's queue, which helps when independent subtasks have unequal costs but cannot remove the overhead of splitting, coordination, and recombination.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
