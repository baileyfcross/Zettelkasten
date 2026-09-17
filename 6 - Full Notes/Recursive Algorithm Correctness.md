2026-09-16 22:54

Status: #baby

Tags: [[Proof Methods and Recursive Definitions]]

# Recursive Algorithm Correctness

An induction proof can mirror the execution of a recursive algorithm. The induction base case verifies the branch that returns without another call, while the inductive case assumes smaller recursive calls are correct and proves that the surrounding computation produces the correct larger result.

The proof also reveals the termination structure: every recursive call must move toward a base case. [[Strong Induction]] is especially useful when a call operates on substructures whose sizes can be any value below the original size.

# References

[[FoundationsOfComputation_2.3.2.pdf]]
