2026-10-16 17:54

Status: #baby

Tags: [[Variational Quantum Wasserstein Anomaly Detection]]

# Commuting Z-Expectation Generator Readout

After the parameterized circuit acts on the latent state, the QWGAN-GP generator measures the Pauli-$Z$ expectation of every qubit. These $N$ expectation values form a classical vector that feeds the generator's dense upscaling layer, which produces an output in the data space.

All of the measured Pauli-$Z$ operators commute, so one batch of computational-basis bitstrings can estimate every output coordinate. A sample of circuit shots therefore yields an entire latent feature vector rather than requiring a distinct measurement basis for each coordinate. [[Hybrid Quantum Generator Gradient Estimation]] differentiates these expectations when training the circuit parameters.

Expectation readout also constrains the information passed to the classical network. For example, a final $Z$ rotation cannot change a $Z$ expectation by itself, which helps explain why circuits with randomly chosen rotation axes can benefit from additional layers. The output is a learned classical feature vector, not a direct sample of the 29-dimensional transaction distribution.

# References

[[2021 - Anomaly detection with variational quantum generative adversarial networks.pdf]]
