2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# Error-Mitigation Exponential Resource Transfer

The concentration theorem in [[Exponential Estimator Concentration for Error Mitigation]] creates a resource trilemma. If the estimator uses only polynomially many terms, coefficients, and state copies, its parameter-dependent signal remains exponentially close to a fixed point and needs exponentially many shots to resolve.

One can enlarge the linear-combination coefficients or number of terms exponentially, but then the measurement outcomes inherit exponentially large statistical uncertainty. Alternatively, one can use exponentially many copies of the noisy state, as in an extreme multi-copy protocol. Each route moves rather than removes the exponential cost.

The conclusion is an asymptotic statement about a broad class of end-of-circuit mitigation methods under local Pauli noise and linear-or-greater depth. It allows useful constant-factor improvements at small scale, and it leaves open mitigation that uses qualitatively different resources during circuit execution.

Large-circuit resource estimates make the transfer explicit through the total error count $\epsilon NL$. Holding the target precision fixed, sampling-optimal mitigation still requires overhead of order $e^{\epsilon NL}$, while PEC can require $e^{2\epsilon NL}$. TEM reaches the smaller exponent by spending classical tensor-network contraction, and its compression bias falls as hardware error decreases. Mitigation can therefore shift work among shots, classical computation, and model accuracy, but it does not remove exponential dependence on the relevant accumulated noise.

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]

[[2024 - Scalability of quantum error mitigation techniques from utility to advantage.pdf]]
