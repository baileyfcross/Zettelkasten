2026-09-27 00:11

Status: #baby

Tags: [[.NET Data Parallelism and PLINQ]]

# Parallel Break and Stop

`ParallelLoopState.Break` says that iterations beyond a relevant index need not begin, preserving a lowest-break notion for ordered index work. `Stop` instead says that no additional iterations are useful, without defining an ordered boundary.

Neither operation rewinds iterations that are already executing. Selecting between them depends on whether earlier indexes retain semantic importance, and loop bodies must tolerate a short period in which workers react to the termination request at different times.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
