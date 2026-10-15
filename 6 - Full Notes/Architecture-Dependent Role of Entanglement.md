2026-10-15 00:05

Status: #baby

Tags: [[Quantum and Hybrid Convolutional Image Classification]]

# Architecture-Dependent Role of Entanglement

Entanglement did not have one uniform effect across the hybrid classifiers. In HQNN-Quanvolution, configurations without entanglement in either encoding or ansatz were consistently weaker than entangled alternatives, suggesting that correlations inside a local image patch helped form useful early features. In HQNN-Parallel, a non-entangling ansatz could match or outperform entangling choices after classical feature extraction.

The difference reflects accessible context. Each parallel circuit saw only eight of 768 prepared features, so the study expects larger registers to change the value of long-range quantum correlations. The evidence also comes from ideal simulation. On hardware, entangling gates increase depth and error exposure, creating a tradeoff between correlation capacity and decoherence. Entanglement should therefore be justified by architecture, observable, register size, and noise budget rather than included as an unconditional marker of model quality.

# References

[[2025 - Practical insights on the effect of different encodings ansatze and measurements in quantum and hybrid convolutional neural networks.pdf]]
