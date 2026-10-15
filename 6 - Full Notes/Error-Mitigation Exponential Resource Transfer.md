2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# Error-Mitigation Exponential Resource Transfer

The concentration theorem in [[Exponential Estimator Concentration for Error Mitigation]] creates a resource trilemma. If the estimator uses only polynomially many terms, coefficients, and state copies, its parameter-dependent signal remains exponentially close to a fixed point and needs exponentially many shots to resolve.

One can enlarge the linear-combination coefficients or number of terms exponentially, but then the measurement outcomes inherit exponentially large statistical uncertainty. Alternatively, one can use exponentially many copies of the noisy state, as in an extreme multi-copy protocol. Each route moves rather than removes the exponential cost.

The conclusion is an asymptotic statement about a broad class of end-of-circuit mitigation methods under local Pauli noise and linear-or-greater depth. It allows useful constant-factor improvements at small scale, and it leaves open mitigation that uses qualitatively different resources during circuit execution.

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]
