2026-10-12 19:52

Status: #baby

Tags: [[Hierarchical Multigrid Variational Quantum Algorithms]]

# Hierarchical Multigrid Quantum Ansatz

A hierarchical multigrid quantum ansatz grows a parameterized circuit while moving through a sequence of increasingly large versions of the target problem. Each coarse circuit is optimized first, then embedded into a refined circuit whose inherited parameters begin at their previously optimized values.

The construction is intended for problems with a natural [[Variational Quantum Problem Hierarchy]]. Its refinement layer adds a qubit and new entangling parameters without discarding the state-preparation work from the preceding level. The resulting [[Coarse-to-Fine Variational Parameter Transfer]] is the main distinction from applying a fixed hardware-efficient ansatz independently at every size.

The paper reports better average simulated solution quality than a static Efficient SU(2) ansatz for a Dirichlet Laplacian eigensolver, MaxCut, and Maximum Exact k-SAT. These are noiseless simulations rather than hardware experiments or a proof of quantum speedup, and the method pays for its additional exploration with more optimizer calls.

# References

[[2023 - Hierarchical Multigrid Ansatz for Variational Quantum Algorithms.pdf]]
