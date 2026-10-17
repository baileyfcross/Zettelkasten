2026-10-17 14:21

Status: #baby

Tags: [[Natural-Gradient Optimization of Optical Quantum Circuits]]

# Hex-GKP Optical Natural-Gradient Benchmark

The harder benchmark prepares a Hex-GKP state with $d=2$, $\mu=1$, and $\delta=0.3$. It uses 25 single-mode Gaussian-Kerr layers, 150 real degrees of freedom, and a Fock-space cutoff of 50.

Vanilla gradient descent displays a rugged, oscillatory loss trajectory and settles far above the natural-gradient result. Adam is smoother but slower. Natural-gradient descent at learning rate $0.02$ reaches a low loss rapidly and remains smooth, whereas the selected learning rates for both alternatives are $0.001$.

The result supports geometry-aware updates on a more difficult continuous-variable state-synthesis landscape. It remains a noiseless simulation of one target state, so the curve does not demonstrate general GKP-source performance on optical hardware.

# References

[[2021 - Natural Gradient Optimization for Optical Quantum Circuits.pdf]]

