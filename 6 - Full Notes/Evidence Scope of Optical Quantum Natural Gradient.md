2026-10-17 14:21

Status: #baby

Tags: [[Natural-Gradient Optimization of Optical Quantum Circuits]]

# Evidence Scope of Optical Quantum Natural Gradient

The paper demonstrates complex quantum natural-gradient optimization on two simulated single-mode state-preparation tasks: a single photon and a Hex-GKP state. Both use the same Gaussian-Kerr layer family, fidelity loss, layerwise metric approximation, and empirically tuned regularization.

The comparisons show smoother convergence and fewer update steps than tuned vanilla gradient descent and Adam. For these single-mode blocks, the authors also report similar per-step runtime because the metric matrices are only $6\times6$.

The evidence does not include a physical photonic processor, sampling noise, imperfect gates, multimode scaling, or a direct full-metric ablation. Since dense metric inversion grows rapidly with mode count, the small-block runtime result and noiseless convergence curves should not be read as an end-to-end hardware advantage.

# References

[[2021 - Natural Gradient Optimization for Optical Quantum Circuits.pdf]]

