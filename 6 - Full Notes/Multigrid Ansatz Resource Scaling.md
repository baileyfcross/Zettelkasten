2026-10-12 19:52

Status: #baby

Tags: [[Hierarchical Multigrid Variational Quantum Algorithms]]

# Multigrid Ansatz Resource Scaling

Starting from an m-qubit seed with a fixed number of parameters, the paper's one-qubit-at-a-time multigrid construction adds i new parameters when refining an i-qubit circuit. The total parameter count is therefore the seed count plus the sum from i = m through n - 1, which grows quadratically with the final qubit count n.

The all-to-all [[Constant-Interpolation Quantum Refinement Layer]] likewise produces a quadratic total two-qubit-gate cost. If the unitary transformations used in the Hamiltonian's Pauli decomposition have polynomial-depth implementations, each VQE circuit remains polynomial in the number of qubits. In state-preparation language, this is polylogarithmic in the number of amplitudes represented by the register.

Circuit scaling is not the entire runtime. [[Coarse-to-Fine Variational Parameter Transfer]] performs a separate classical optimization at each hierarchy level, so the maximum cumulative optimizer iterations grows with the number of refinements. The paper suggests larger seed circuits for larger problems as one way to reduce the number of stages, but it does not establish an end-to-end complexity advantage.

# References

[[2023 - Hierarchical Multigrid Ansatz for Variational Quantum Algorithms.pdf]]
