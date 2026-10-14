2026-10-12 18:44

Status: #baby

Tags: [[Quantum Dropout Regularization]]

# Quantum Dropout Expressibility and Entanglement

Successful quantum dropout need not improve generalization by reducing a circuit's expressibility or its average multipartite entanglement. The paper estimates expressibility from the Kullback–Leibler divergence between circuit-state fidelity distributions and the Haar-random distribution, and measures entanglement with concentrable entanglement over 15,000 sampled states.

For the ten-layer regression circuit, even approximately 50 percent dropout leaves the saturated expressibility and average entanglement essentially unchanged across strategies. Its mean concentrable entanglement is about 0.539, close to the five-qubit Haar expectation of about 0.53977 and within the genuinely multipartite-entangled range.

The classification circuit is more sensitive to removal. Around the useful 3 percent operating rate, dropout strategies have approximately the same expressibility and entanglement as the full circuit. Around 20 percent, both quantities are reduced and convergence is delayed beyond the studied twenty layers, yet classification performance is worse. The better-performing setting is therefore the one that preserves these circuit properties.

This evidence favors an ensemble-like mechanism: successive updates sample related subarchitectures and limit gate co-adaptation while the shared full model remains expressive. It also qualifies [[Overparameterization-Aware Quantum Dropout Rate]] by showing that parameter-count redundancy alone does not predict every architecture's sensitivity.

# References

[[2023 - A General Approach to Dropout in Quantum Neural Networks.pdf]]
