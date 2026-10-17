2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# QN-SPSA Gibbs-State Preparation

A thermal state can be prepared variationally by purifying the maximally mixed state and applying imaginary-time evolution to the system half. Each system qubit is first entangled with an environment qubit in a Bell pair; evolving the system for imaginary time $(2k_BT)^{-1}$ and tracing out the environment yields the target Gibbs state.

QN-SPSA estimates the Fubini-Study metric needed by this [[Variational Quantum Imaginary-Time Evolution]] from state overlaps. The purification keeps the thermal-state preparation within a pure-state circuit model, at the cost of doubling the qubit register and repeatedly solving a regularized stochastic metric equation.

This construction differs from [[QAE-Based Gibbs State Preparation]], which learns a compressed representation. Here the central resource is a variational approximation to thermal imaginary-time dynamics.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

