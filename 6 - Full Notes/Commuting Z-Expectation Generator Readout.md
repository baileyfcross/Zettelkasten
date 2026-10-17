2026-10-16 22:03

Status: #baby

Tags: [[Variational Quantum Wasserstein Anomaly Detection]] · [[Style-qGAN Monte Carlo Event Generation]]

# Commuting Z-Expectation Generator Readout

After the parameterized circuit acts on the latent state, the QWGAN-GP generator measures the Pauli-$Z$ expectation of every qubit. These $N$ expectation values form a classical vector that feeds the generator's dense upscaling layer, which produces an output in the data space.

All of the measured Pauli-$Z$ operators commute, so one batch of computational-basis bitstrings can estimate every output coordinate. A sample of circuit shots therefore yields an entire latent feature vector rather than requiring a distinct measurement basis for each coordinate. [[Hybrid Quantum Generator Gradient Estimation]] differentiates these expectations when training the circuit parameters.

Expectation readout also constrains the information passed to the classical network. For example, a final $Z$ rotation cannot change a $Z$ expectation by itself, which helps explain why circuits with randomly chosen rotation axes can benefit from additional layers. The output is a learned classical feature vector, not a direct sample of the 29-dimensional transaction distribution.

The style-qGAN uses the same commuting measurement family without a dense upscaler. It assigns one continuous output component to each qubit as $x_i=-\langle\sigma_z^i\rangle$, so an $n$-qubit circuit directly produces a point in $[-1,1]^n$ before classical inverse preprocessing. Other commuting multi-qubit observables could define more elaborate sample components, but the collider benchmark uses one local expectation per feature.

# References

[[2021 - Anomaly detection with variational quantum generative adversarial networks.pdf]]

[[2022 - Style-based quantum generative adversarial networks for Monte Carlo events.pdf]]
