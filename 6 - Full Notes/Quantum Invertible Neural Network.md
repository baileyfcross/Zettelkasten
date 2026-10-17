2026-10-16 23:00

Status: #baby

Tags: [[Quantum Invertible Generative Models]]

# Quantum Invertible Neural Network

A quantum invertible neural network is a hybrid normalizing flow whose central transformation is a parameterized unitary circuit. Classical inputs are angle encoded, the variational circuit transforms the resulting state, and expectation measurements produce a classical output vector.

The state preparation and unitary circuit can be reversed algebraically, but the expectation-value measurement is many-to-one. The model therefore adds a [[Learnable Hybrid Inverse State Preparation]] module and an auxiliary reconstruction objective so that outputs reached during training map back to suitable premeasurement states.

Once effective invertibility is established, the network can use the [[Normalizing-Flow Change-of-Variables Objective]] for density estimation. Its distinctive promise is access to the full input Jacobian through parameter-shift evaluations rather than only the determinant made tractable by classical coupling restrictions.

# References

[[2023 - Generative Invertible Quantum Neural Networks.pdf]]

