2026-10-14 18:20

Status: #baby

Tags: [[Quantum Optical Neurons]]

# Coincidence-Estimation Photon Complexity

A Hong-Ou-Mandel classifier estimates a coincidence probability from repeated two-photon trials. Under a normal approximation at 95% confidence, the paper writes the uncertainty as $\epsilon=2\sqrt{\tilde p(1-\tilde p)/\tilde n_p}$, where $\tilde p$ is the empirical coincidence rate and $\tilde n_p$ counts input photons across repetitions.

Because $4\tilde p(1-\tilde p)\leq1$, achieving fixed uncertainty requires $O(\epsilon^{-2})$ photons. The count can grow sharply when higher precision is demanded, but it does not depend on the number of spatial cells used to describe the object. This separates precision complexity from resolution complexity: [[Post-Training Resolution-Independent Optical Inference]] is constant in image resolution only while the target statistical uncertainty is treated as fixed.

# References

[[2024 - Quantum optical classifier with superexponential speedup.pdf]]
