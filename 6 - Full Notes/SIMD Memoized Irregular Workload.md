2026-10-31 22:04

Status: #baby

Tags: [[SIMD Algorithm Reformulation Patterns]]

# SIMD Memoized Irregular Workload

A SIMD memoized irregular workload stops a lane when its evolving state reaches a previously solved state, then adds the cached remainder of the computation. The method trades random reads and storage for the elimination of potentially long dependent trajectories.

In the Collatz problem, each processed starting value stores its orbit length. Later lanes use [[Java Vector Gather Operation|gather]] to retrieve a known suffix when their intermediate value enters the computed range. This lowered arithmetic so much that simple memoization dominated more elaborate vector scheduling, illustrating that reducing total work can matter more than maximizing lane occupancy.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
