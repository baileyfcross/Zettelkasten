2026-10-15 10:43

Status: #baby

Tags: [[Randomized Compiling and Zero-Noise Extrapolation]]

# Identity-Insertion Noise Magnification

Identity insertion raises the effective noise strength without changing the ideal circuit operation. For a target operation $U$, a logically neutral pair $U^\dagger U$ can be inserted before $U$; for the Hermitian CNOT gate, replacing one CNOT by three, five, or another odd number of repeated CNOTs preserves the ideal unitary while adding faulty gate applications.

Measurements at the original and magnified noise levels supply the points used by zero-noise extrapolation. In the first-order two-level case, the coefficients cancel the leading error term but amplify any uncertainty in the measured expectation values, connecting the technique to [[Error-Mitigation Variance Cost]].

The construction has a practical depth cost. Replacing every entangling gate by at least three gates is poorly suited to current noisy hardware, and a deep circuit whose baseline signal has already vanished can encounter [[Deep-Circuit ZNE Signal Collapse]]. Selectively magnifying only some entangling gates is a possible alternative, but it is not evaluated in this paper.

# References

[[2022 - Synergetic quantum error mitigation by randomized compiling and zero-noise extrapolation for the variational quantum eigensolver.pdf]]
