2026-10-16 22:46

Status: #baby

Tags: [[Quantum Generative Model Advantage Benchmarking]]

# Generative Model Advantage Race Design

A fair quantum-classical comparison should define the race before tuning the models. The application supplies the dataset, constraints, cost function, problem size, and scarce resources; the evaluation protocol then fixes the allowed track and the metrics that determine a winner.

The race analogy separates a model's general properties from its performance in context. Expressive power, training efficiency, and sampling efficiency characterize a runner, while data scarcity, sampling limits, and expensive objective evaluations act as hurdles. Changing the track can change the winning model even when every architecture remains fixed.

This design discourages post hoc advantage claims based on whichever metric favors a quantum model. [[Sampling-Budget Generative Benchmark Track]] and [[Cost-Evaluation-Budget Generative Benchmark Track]] illustrate two defensible tracks, while [[Practical Quantum Advantage Evidence Tiers]] records how strong a resulting claim can be.

# References

[[2023 - A Framework for Demonstrating Practical Quantum Advantage Racing Quantum against Classical Generative Models.pdf]]

