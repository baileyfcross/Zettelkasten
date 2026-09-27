2026-09-27 00:11

Status: #baby

Tags: [[.NET Data Parallelism and PLINQ]]

# PLINQ Exception and Cancellation

Failures thrown by parallel query delegates can be collected from several partitions and reported together, while a cancellation token gives the query an external cooperative stop signal. Both outcomes travel through query enumeration because deferred execution is when the work actually runs.

A consumer must therefore place handling around materialization or iteration, not only around query construction. Delegates should avoid irreversible shared side effects because other partitions may have progressed before a fault or cancellation is observed.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
