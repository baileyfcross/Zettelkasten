2026-10-12 19:52

Status: #baby

Tags: [[Hierarchical Multigrid Variational Quantum Algorithms]]

# Multigrid MaxCut VQE

Multigrid MaxCut VQE builds a graph problem one vertex at a time. At each level, the hierarchy includes the edges connecting the newly admitted vertex to vertices already present, optimizes the corresponding cut Hamiltonian, and transfers the circuit parameters to the next subgraph.

The inverse MaxCut Hamiltonian is a sum of pairwise Z products and constants. Because all terms commute in the computational basis, one register measurement can supply every edge contribution for a shot, followed by classical evaluation of the cut value. The paper compares approximation ratios against exact brute-force optima.

In noiseless 1,000-shot simulations of 15-vertex Erdos-Renyi graphs with edge probabilities 0.3, 0.6, and 0.9, the multigrid method maintains higher and more stable approximation ratios than the static Efficient SU(2) baseline, particularly as graphs grow. It also uses substantially more optimizer calls. Vertices are added in a naive library-generated order, and zero-edge subgraphs are omitted because their approximation ratio is undefined.

# References

[[2023 - Hierarchical Multigrid Ansatz for Variational Quantum Algorithms.pdf]]
