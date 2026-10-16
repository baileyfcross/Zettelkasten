2026-10-16 17:48

Status: #baby

Tags: [[Quantum Risk Analysis of Derivative Portfolios]]

# Quantum Scenario Preparation Bottleneck

Quantum derivative-risk algorithms require a probability-weighted superposition of joint market scenarios. Loading $N$ sampled scenarios through a generic classical-data block encoding can have logarithmic T-depth but $O(N)$ T-count and potentially large constants. Because the samples retain classical Monte Carlo error, this route limits the end-to-end error scaling even when later processing is fully coherent.

An analytic multivariate density, a reparameterized stochastic model, or a scalable quantum copula could instead prepare a discretized distribution directly and reduce scenario error with more qubits. Whether that is practical depends on the number of risk factors, their granularity and correlations, and the circuit required by the particular distribution. [[Aggregate-Risk Quantum Advantage Threshold]] therefore treats scenario-preparation T-depth as a free cost parameter rather than assuming it is negligible.

# References

[[2024 - Quantum Risk Analysis of Financial Derivatives.pdf]]
