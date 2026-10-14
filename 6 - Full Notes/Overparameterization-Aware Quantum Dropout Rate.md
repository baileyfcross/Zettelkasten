2026-10-12 18:44

Status: #baby

Tags: [[Quantum Dropout Regularization]]

# Overparameterization-Aware Quantum Dropout Rate

An overparameterization-aware dropout rate limits gate removal so the sampled quantum neural network remains, on average, in its overparameterized regime. If a circuit has $M$ trainable parameters and its average parameter dimension saturates at $D_{\max}$, the paper proposes

$$M_{\mathrm{drop}}^{\max} \leq M-D_{\max},$$

with a corresponding upper drop fraction $M_{\mathrm{drop}}^{\max}/M$. For an $N$-qubit circuit capable of representing the full pure-state manifold, the maximum dimension is $D_{\max}=2^{N+1}-2$.

For the five-qubit regression circuit, $M=150$ and $D_{\max}=62$, so removing about 88 parameterized gates, roughly 59 percent, marks the estimated boundary. The 180-parameter classification circuit gives a nominal allowance of 118 gates, roughly 66 percent, once it becomes overparameterized.

These figures are ceilings, not recommended operating rates. The best empirical settings used effective probabilities of roughly 5–8 percent for the sine task, 6–16 percent for the absolute-value task, and 1–6 percent for classification. The classification architecture also showed altered expressibility and entanglement around 20 percent removal, demonstrating that redundancy structure and gate design can make the practical limit much lower than the dimension count alone suggests.

# References

[[2023 - A General Approach to Dropout in Quantum Neural Networks.pdf]]
