2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Lock-Free Synchronization]]

# Read-Modify-Write Atomic Operation

A read-modify-write atomic operation reads a memory location, computes an update, and stores the result as one indivisible action relative to competing atomic accesses. Examples include exchange, compare-and-exchange, fetch-and-add, and test-and-set operations.

These primitives prevent lost updates to a single value and form building blocks for counters, flags, and lock-free algorithms. Their ordering semantics must also be correct: indivisibility alone does not necessarily order accesses to surrounding data, which may require [[Memory Reordering and Barriers]].

# References

[[linuxkernelprogramming_secondedition.pdf]]
