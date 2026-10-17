2026-10-17 14:40

Status: #baby

Tags: [[Variational Quantum Optimizer Benchmarking]]

# Variational Quantum Optimizer Benchmark Suite

An optimizer benchmark for variational quantum circuits compared 46 optimizer configurations across problems ranging from two-qubit circuits with fewer than ten parameters to 25-qubit circuits with 200 parameters. The candidate set combined nine parameter-shift gradient optimizers at four learning rates with derivative-free or approximate-gradient methods such as Nelder-Mead, Powell, COBYLA, and SPSA.

Most experiments shared a ceiling of 1,000 optimizer iterations, a convergence tolerance of $10^{-4}$, three random initializations, and 1,000 shots per expectation estimate. This common protocol makes final losses comparable under an optimization-step budget, but it does not equalize circuit evaluations or total shots.

The suite therefore supports empirical optimizer selection under its protocol rather than a resource-normalized winner. [[Fixed-Iteration versus Fixed-Shot Optimizer Budgets]] is needed to interpret the recommendations for hardware use.

# References

[[2022 - An Empirical Review of Optimization Techniques for Quantum Variational Circuits.pdf]]

