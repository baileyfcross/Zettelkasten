2026-10-17 11:34

Status: #baby

Tags: [[Scalable Error-Mitigated Quantum Simulation]]

# TEM Sampling-Overhead Optimality

For a typical high-weight Pauli observable under weak sparse Pauli-Lindblad noise, TEM has sampling overhead $\Gamma\approx\gamma\approx e^{\epsilon NL}$. Its random error with $M$ shots is consequently $e^{\epsilon NL/2}/\sqrt{M}$, assuming an exact noise model and compression-free tensor network.

Quantum estimation theory supplies a universal lower bound on the shots required by any unbiased mitigation estimator without restricting classical post-processing. TEM asymptotically saturates that bound for large random circuits with weak sparse Pauli-Lindblad noise and, more generally, weak Pauli noise when the unitary layers form a 2-design. TEM is therefore sampling-optimal within those assumptions; the remaining practical constraint moves to classical contraction and compression.

# References

[[2024 - Scalability of quantum error mitigation techniques from utility to advantage.pdf]]

