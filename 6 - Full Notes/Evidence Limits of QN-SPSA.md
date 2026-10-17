2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# Evidence Limits of QN-SPSA

QN-SPSA establishes a constant-overlap estimator for quantum-state geometry and tests it across simulated optimization, one noisy molecular-hardware experiment, imaginary-time Gibbs preparation, and a small QAOA instance. These examples support feasibility and favorable query scaling relative to an explicitly measured QFIM.

They do not establish a universal runtime advantage. State-overlap circuits can add width or depth, the inverse of a random metric remains biased, regularization changes the intended geometry, and repeated sampling may erase the nominal constant-query benefit in trajectory-following applications.

The hardware evidence is limited to four qubits and retains about 200 millihartree of energy error without mitigation. The Boltzmann-machine and MAXCUT studies are also small. The defensible conclusion is that QN-SPSA is a promising stochastic preconditioner whose scaling and robustness require broader hardware comparisons.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

