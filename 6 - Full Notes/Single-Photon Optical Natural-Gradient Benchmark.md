2026-10-17 14:21

Status: #baby

Tags: [[Natural-Gradient Optimization of Optical Quantum Circuits]]

# Single-Photon Optical Natural-Gradient Benchmark

The first benchmark trains an eight-layer single-mode optical circuit to prepare the Fock state $|1\rangle$. Six real degrees of freedom per [[Gaussian-Kerr Optical Circuit Layer|Gaussian-Kerr layer]] give 48 parameters, and the simulation truncates Fock space at dimension 100.

With separately tuned learning rates, natural-gradient descent reaches near-zero fidelity loss in fewer steps than vanilla gradient descent or Adam and follows a smooth decay. Its layerwise metric blocks are at most $6\times6$, so the paper reports natural-gradient steps with runtime comparable to the other methods in this setting.

The task is deliberately simple and simulated. It establishes that the complex metric implementation works and accelerates this small state-synthesis problem, not that metric inversion remains negligible for multimode or hardware-scale circuits.

# References

[[2021 - Natural Gradient Optimization for Optical Quantum Circuits.pdf]]

