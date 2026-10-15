2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# Exponential Estimator Concentration for Error Mitigation

Many mitigation protocols estimate linear combinations of quantities formed from one or more copies of a noisy state, a measurement operator, and clean ancillary qubits added after the noisy computation. Under local Pauli noise, each such quantity approaches a state-independent fixed point with a bound proportional to

$$
\lVert X\rVert_\infty M\sqrt{n}\,q^{c(L+1)},
$$

where $M$ is the number of state copies, $L$ is the noisy circuit depth, $q<1$ characterizes the noise, and $c=1/(2\ln 2)$.

For depth linear in the qubit count, the residual parameter dependence is exponentially small unless another resource grows exponentially. The result covers the estimator structures used by zero-noise extrapolation, virtual distillation, probabilistic error cancellation, and linear-regression mitigation.

Clean ancillas appended at the end do not change the contraction of the already-prepared noisy states. The theorem does not rule out protocols that intervene during the computation, which is why its conclusion differs from full quantum error correction.

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]
