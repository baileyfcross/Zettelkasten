2026-10-17 14:21

Status: #baby

Tags: [[Natural-Gradient Optimization of Optical Quantum Circuits]]

# Layerwise Block-Diagonal Quantum Natural Gradient

A full quantum natural-gradient step builds and inverts one metric over every trainable circuit parameter. A layerwise approximation instead retains metric couplings among parameters in the same layer and discards couplings between different layers.

The resulting block-diagonal matrix can be inverted one small block at a time. This greatly reduces classical linear-algebra cost and lets the optical experiments use natural-gradient updates whose runtime is comparable to ordinary gradient methods for a single-mode circuit.

The approximation assumes that cross-layer geometric correlations are not essential to a useful descent direction. The paper adopts it based on earlier evidence that layerwise blocks perform similarly to the full metric, rather than presenting a new full-versus-block ablation of its own.

# References

[[2021 - Natural Gradient Optimization for Optical Quantum Circuits.pdf]]

