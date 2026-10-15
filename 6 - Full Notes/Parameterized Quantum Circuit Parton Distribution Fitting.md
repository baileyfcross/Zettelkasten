2026-10-15 00:14

Status: #baby

Tags: [[Quantum Computing for High-Energy Physics]]

# Parameterized Quantum Circuit Parton Distribution Fitting

Parton distribution functions describe how a proton's momentum is distributed among quarks and gluons. They encode non-perturbative structure that cannot be calculated throughout the relevant regime by a straightforward perturbative expansion, so their functional forms are fitted to experimental constraints and then used throughout collider predictions.

A parameterized quantum-circuit fit uses measured circuit expectations as the ansatz for the distribution. A classical optimizer adjusts gate parameters to reduce the discrepancy between predicted and observed data, subject to the same physical constraints and uncertainty analysis required of a classical fit. Early demonstrations reproduced established fits on reduced problems, showing representational feasibility rather than quantum advantage.

The distinction matters because the fitted distribution is still a classical function even when a quantum circuit represents it. Any benefit at this stage is computational or statistical, not an automatic recovery of the proton's full quantum state. Strong evaluation must compare expressivity, optimization stability, uncertainty, state-preparation cost, and extrapolation against modern classical parameterizations. [[QUBO Wilson Coefficient Fitting]] applies quantum optimization to a related inference problem with different parameters.

# References

[[2023 - Quantum Computing for High-Energy Physics State of the Art and Challenges Summary of the QC4HEP Working Group.pdf]]
