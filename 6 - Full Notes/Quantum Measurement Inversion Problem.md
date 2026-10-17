2026-10-16 23:00

Status: #baby

Tags: [[Quantum Invertible Generative Models]]

# Quantum Measurement Inversion Problem

Expectation-value measurement is not generally invertible: many quantum states can produce the same vector of measured expectations. A unitary circuit may therefore be exactly reversible at the state level while the complete map from classical input to measured classical output is not.

A QINN only visits an $n$-dimensional subset of the $2^n$-dimensional state space when it begins from $n$ real input features. Its measured map can still be bijective if no two states on that reachable subset share the same output vector, but the inverse also needs a way to reconstruct an appropriate state from each output.

The paper addresses both requirements by jointly training the forward circuit and a [[Learnable Hybrid Inverse State Preparation]] module under an explicit invertibility loss.

# References

[[2023 - Generative Invertible Quantum Neural Networks.pdf]]

