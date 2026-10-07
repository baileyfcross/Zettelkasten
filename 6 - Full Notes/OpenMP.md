2026-10-07 17:18

Status: #baby

Tags: [[Parallel Statistical Computing]]

# OpenMP

OpenMP is a directive-based API for shared-memory parallel programming. Compiler pragmas mark regions or loops whose work can be divided among threads, while runtime functions report thread identifiers and control the thread team.

A parallel region follows a fork-join structure: the initial thread creates a team, the team executes the region, and the threads synchronize when the region ends. Data-sharing clauses such as private, shared, and firstprivate determine whether each thread receives its own variable or accesses common storage, making those declarations part of the program's correctness.

# References

[[statisticalcomputingincplusplusandr.pdf]]
