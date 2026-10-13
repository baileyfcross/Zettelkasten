2026-10-12 19:52

Status: #baby

Tags: [[Hierarchical Multigrid Variational Quantum Algorithms]]

# Multigrid Maximum Exact k-SAT VQE

Multigrid Maximum Exact k-SAT VQE grows a Boolean optimization problem by adding variables in generation order. A clause enters a level only after every variable it contains has been admitted, producing a nested formula hierarchy for [[Coarse-to-Fine Variational Parameter Transfer]].

Each clause becomes a diagonal local Hamiltonian that penalizes the assignment satisfying its negation. Replacing the true and false projectors with combinations of identity and Pauli-Z operators yields at most order m times 2 to the k Pauli terms for m clauses. Because these terms commute, one computational-basis circuit execution per shot can provide the bits used to evaluate all included clauses.

The paper tests noiseless, 1,000-shot random Maximum Exact 2-SAT and 3-SAT instances with 15 variables, using m = 3n and m = 6n clauses respectively. Multigrid VQE retains higher approximation ratios than the static Efficient SU(2) baseline while requiring more optimizer calls. Empty subformulas are excluded where their approximation ratios are undefined, and exact brute force is used only to score these small benchmarks.

# References

[[2023 - Hierarchical Multigrid Ansatz for Variational Quantum Algorithms.pdf]]
