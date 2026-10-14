2026-10-12 18:44

Status: #baby

Tags: [[Quantum Dropout Regularization]]

# Quantum Dropout Parameter Rescaling

Classical dropout commonly compensates for missing training units by scaling activations or weights, but the paper finds no corresponding benefit from scaling trained quantum-circuit parameters. Multiplying the retained angles by the classical factor $1-p$ generally leaves performance unchanged or makes it worse across the sine, absolute-value, and Moons experiments.

The authors also test a weaker family of factors,

$$s=(1-p)^{1/k},$$

where increasing $k$ moves $s$ toward one. Average performance tends to improve as $k$ grows, so the best trend approaches the unscaled parameter values. Small exceptions in individual regression settings are not statistically significant across the ten runs.

The paper proposes entanglement and qubit reuse as possible reasons that a changed gate angle propagates through a quantum circuit differently from a scaled classical weight. This remains a hypothesis: the relation between rescaling, entanglement, and circuit architecture is identified as an open theoretical problem rather than established as the mechanism of [[Quantum Neural Network Dropout]].

# References

[[2023 - A General Approach to Dropout in Quantum Neural Networks.pdf]]
