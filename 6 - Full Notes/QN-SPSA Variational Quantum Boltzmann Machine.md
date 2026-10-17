2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# QN-SPSA Variational Quantum Boltzmann Machine

A variational quantum Boltzmann machine represents a classical probability distribution with the diagonal of a Gibbs state whose Hamiltonian parameters are learned. The paper alternates an outer SPSA update of a two-qubit Ising Hamiltonian with inner [[QN-SPSA Gibbs-State Preparation]].

The target is a Bell-like distribution $(0.5,0,0,0.5)$. Ten Euler steps approximate each imaginary-time preparation, ten stochastic metric samples are averaged per time step, and ten prepared Gibbs states are averaged for each Hamiltonian update.

Across ten simulated runs, the learned distribution approaches the target about as well as a model using exact imaginary-time evolution. The example demonstrates end-to-end compatibility, but its four-qubit purification and extensive resampling do not establish a practical speedup for larger [[Restricted Boltzmann Machine|Boltzmann-machine]] models.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

