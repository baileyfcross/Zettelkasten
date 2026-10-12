2026-09-27 00:11

Status: #baby

Tags: [[.NET Data Parallelism and PLINQ]]

# Parallel For

`Parallel.For` partitions an integer index range so iterations can be processed by several workers. It fits CPU-bound loops whose iterations are independent or whose shared results can be combined safely.

Iteration order is not sequential, and more iterations may already be in flight when one requests termination. The loop body should avoid hidden shared state and should be benchmarked against the ordinary `for` loop because coordination can dominate inexpensive work.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
