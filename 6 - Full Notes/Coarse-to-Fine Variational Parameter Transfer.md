2026-10-12 19:52

Status: #baby

Tags: [[Hierarchical Multigrid Variational Quantum Algorithms]]

# Coarse-to-Fine Variational Parameter Transfer

Coarse-to-fine variational parameter transfer initializes a refined quantum optimization with the optimized parameters from the preceding, smaller problem. Only the parameters introduced by the [[Constant-Interpolation Quantum Refinement Layer]] begin at zero, so the finer search starts from a state that already represents the coarse solution.

The multigrid VQE repeats this transfer after every problem refinement. In the paper's Laplacian experiment, retaining earlier angles gives consistently better BFGS results than building the same final circuit hierarchy while reinitializing every angle to zero. The comparison isolates parameter reuse from the mere presence of a larger multigrid-shaped circuit.

Transfer is useful only when adjacent levels share meaningful structure. The paper supplies smooth Laplacian ground states, nested subgraphs, and nested Boolean formulas as examples; it does not claim that arbitrary problem orderings preserve useful information. [[Variational Quantum Problem Hierarchy]] therefore belongs to the algorithm design, not just its input formatting.

# References

[[2023 - Hierarchical Multigrid Ansatz for Variational Quantum Algorithms.pdf]]
