2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Functions Null Safety and Delegation]]

# Kotlin Recursive Function

A recursive Kotlin function calls itself to express a problem in terms of a smaller or otherwise closer-to-complete instance. Each call receives its own parameters and execution frame until one call returns and the pending calls can finish.

The function therefore needs a reachable termination condition. Without it, calls continue until the runtime exhausts the available call stack and raises a stack-overflow failure. The recursive step and base case jointly define the algorithm, not two optional parts of it.

# References

[[masteringkotlinforjavadevelopers.epub]]
