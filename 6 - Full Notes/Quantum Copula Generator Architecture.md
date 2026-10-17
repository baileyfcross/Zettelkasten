2026-10-16 22:51

Status: #baby

Tags: [[Quantum Generative Architecture Performance]]

# Quantum Copula Generator Architecture

A quantum copula generator is a discrete circuit constrained to represent dependencies among variables whose marginals are uniform. It first prepares a maximally entangled state across equal-sized variable registers and then applies variational unitaries separately within each register, with no later gates coupling the registers.

Because local unitaries cannot change the entanglement across the register partition, every reduced register remains maximally mixed. Computational-basis measurements therefore retain uniform marginals while trainable within-register operations reshape the joint correlations, as formalized by [[Maximally Entangled Copula Marginals]].

The architectural constraint matches data processed by [[Probability Integral Transform for Quantum Generation]]. This alignment reduces the structure the optimizer must discover and is the main reason the copula circuit outperforms the standard discrete circuit on several benchmark distributions.

# References

[[2023 - A performance characterization of quantum generative models.pdf]]

