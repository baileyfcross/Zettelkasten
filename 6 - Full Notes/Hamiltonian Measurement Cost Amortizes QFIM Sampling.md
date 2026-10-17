2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# Hamiltonian Measurement Cost Amortizes QFIM Sampling

The relative cost of QN-SPSA depends on how expensive it is to measure the optimization loss. A molecular energy can contain many noncommuting Pauli terms, so each nominal loss evaluation may require many measurement bases, whereas one stochastic QFIM sample still requires four state overlaps.

In the lithium-hydride experiment, an energy evaluation uses 25 measurement bases with 1,024 shots per basis. Under that accounting, the extra metric evaluations are a small fraction of the total measurement burden even though QN-SPSA uses more circuit calls than ordinary SPSA.

This amortization is problem dependent. For a simple diagonal Hamiltonian or cheaply measured objective, the overlap circuits can be a substantial constant-factor overhead; for a complex Hamiltonian, their cost may be negligible relative to measuring the loss.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

