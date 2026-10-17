2026-10-17 14:21

Status: #baby

Tags: [[Natural-Gradient Optimization of Optical Quantum Circuits]]

# Fidelity-Loss Optical State Preparation

An optical state-preparation circuit can be trained by minimizing one minus its fidelity with a target pure state:

$$L(\xi)=1-|\langle\psi_{\mathrm{target}}|U_\xi|0\rangle|^2.$$

The loss is zero when the prepared state matches the target up to a global phase. It therefore evaluates the physical state produced by the mixed real-complex parameter vector $\xi$ without penalizing an unobservable phase convention.

Locally, the second-order change of the same fidelity defines the [[Fubini-Study Metric for Variational Quantum States]]. The objective and natural-gradient geometry are thus aligned: both compare rays in quantum-state space rather than raw coordinate vectors.

The simulations initialize circuit parameters randomly and optimize this loss for a single photon and a Hex-GKP target.

# References

[[2021 - Natural Gradient Optimization for Optical Quantum Circuits.pdf]]

