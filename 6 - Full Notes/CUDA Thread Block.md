2026-10-03 16:51

Status: #baby

Tags: [[CUDA and NVIDIA GPU Architecture]]

# CUDA Thread Block

A CUDA thread block is a cooperating group of [[CUDA Thread|threads]] within one [[CUDA Grid]]. Threads in a block can coordinate through block-scoped synchronization and on-chip resources while processing a shared tile or related portion of the problem.

A block is assigned to one [[Streaming Multiprocessor]] for its execution, although an SM can hold several resident blocks when registers, shared memory, and other resources permit. Blocks are the scheduling units that let one kernel scale across GPUs with different SM counts.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

