2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# QN-SPSA Evaluation-Cost Accounting

In the paper's optimization accounting, a QN-SPSA step uses seven circuit-function evaluations, compared with three for ordinary SPSA. The added work comes from the four overlaps used to update the metric; neither count grows with parameter dimension.

This constant-factor comparison should not be confused with physical runtime. A loss evaluation may require many Hamiltonian measurement groups, while a fidelity evaluation may require a deeper compute-uncompute circuit or a wider SWAP-test circuit. Batching, shot counts, and hardware latency can change which primitive dominates.

QN-SPSA's claimed scaling benefit is therefore clearest against an exact QFIM whose element count grows quadratically. Against first-order SPSA, it pays a fixed additional measurement cost in exchange for stochastic geometric preconditioning.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

