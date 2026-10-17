2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# QN-SPSA Lithium-Hydride Hardware Benchmark

The hardware experiment applies QN-SPSA to a variational energy calculation for lithium hydride at a bond distance of $2.5$ Å. Active-space reduction, parity mapping, and qubit tapering reduce the problem to four qubits, and a 16-parameter hardware-efficient ansatz is compiled to the heavy-hex connectivity of ibmq_montreal.

The first two iterations average 100 QFIM point samples to establish a stable metric; later iterations average two. Across five 300-iteration runs, QN-SPSA descends faster and reaches lower measured energies than ordinary SPSA.

The final energy remains roughly 200 millihartree above the exact value, and the experiment applies no error mitigation. It therefore supports noisy-hardware feasibility and relative optimizer performance, not chemically accurate ground-state estimation.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

