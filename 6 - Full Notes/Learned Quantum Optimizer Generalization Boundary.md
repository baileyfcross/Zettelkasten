2026-10-17 11:48

Status: #baby

Tags: [[Meta-Learned Variational Quantum Optimization]]

# Learned Quantum Optimizer Generalization Boundary

The learned optimizers generalize from smaller to larger problem instances only under a controlled interface: the problem distribution and ansatz family remain fixed, and the number of variational parameters does not change. The reported tests therefore demonstrate extrapolation in physical system size, not universal optimization.

Changing QAOA depth, adopting an ansatz whose parameter count grows with qubit number, or moving to a new Hamiltonian family would change the recurrent network's input-output problem. Handling those cases would require retraining or an optimizer architecture designed for variable-size parameter structures.

The empirical scope is narrower still because all circuits were classically simulated and only scalar Gaussian cost noise was added. The results justify a reusable initialization strategy for related workloads, while arbitrary task transfer, device-level robustness, and scaling beyond classically verified optima remain open.

# References

[[2019 - Learning to learn with quantum neural networks via classical neural networks.pdf]]

