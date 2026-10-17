2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# Stochastic Natural-Gradient Convergence Region

A two-parameter benchmark maps which initial points converge under quantum natural gradient, QN-SPSA, SPSA, and vanilla gradient descent. The ansatz contains a global-phase direction and a controlled rotation, while the diagonal Hamiltonian creates stationary axes and a saddle-shaped region.

Exact quantum natural gradient fails where the loss gradient vanishes. Vanilla gradient descent also leaves a diamond-shaped nonconvergent region near the saddle. Stochastic perturbations probe mixed parameter directions and can escape some cases where individual coordinate derivatives vanish.

Across the tested grid, QN-SPSA converges from the largest set of initial conditions. The result illustrates a mechanism rather than a general guarantee: random directions can enlarge the empirical basin of attraction, but success was defined over repeated trials on a specially constructed two-qubit landscape.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

