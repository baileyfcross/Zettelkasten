2026-10-15 00:14

Status: #baby

Tags: [[Quantum Computing for High-Energy Physics]]

# Quantum-Assisted Jet Clustering

Jet clustering groups measured collision products into structures associated with an initiating quark or gluon. A useful algorithm must preserve infrared and collinear safety: adding an arbitrarily soft particle or replacing one particle by a collinear pair should not change the physical jet assignment.

Quantum proposals attack different parts of the task. A thrust-based QUBO maps a two-hemisphere partition to quantum annealing, while gate-based subroutines estimate particle distances or accelerate a search for a maximum. Quantum versions of $k$-means, affinity propagation, and the $k_T$ clustering algorithm can reproduce classical-quality assignments in small simulated examples and offer polynomial speedups for selected subroutines under their access assumptions.

The end-to-end advantage remains conditional. Dense QUBOs require connectivity that present annealers lack, and several digital algorithms assume QRAM-like parallel access to particle data. Classical geometric reformulations already reduce some clustering routines from cubic to quadratic or near $N\log N$ scaling. A quantum benchmark must therefore include data access, connectivity, and the best classical jet implementation, not compare only an isolated distance calculation.

# References

[[2023 - Quantum Computing for High-Energy Physics State of the Art and Challenges Summary of the QC4HEP Working Group.pdf]]
