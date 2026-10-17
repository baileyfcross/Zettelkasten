2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# QuDDPM Many-Body Phase Learning

The many-body benchmark trains QuDDPM on four-qubit ground states of the transverse-field Ising model with field strengths sampled uniformly from $g\in[0.2,0.4)$. These states lie on the ferromagnetic side of the model's critical point at $g=1$.

The generated ensemble is assessed by the magnetization

$$M=\frac{1}{n}\sum_i Z_i.$$

Most training and test outputs remain concentrated near the ordered phase, sharply separated from Haar-like noise. The reported magnetization summary is 1 for the data, 0.9 for generated training states, and 0.96 for generated test states.

This is evidence that the diffusion model can preserve a phase-level property of a small state ensemble. It does not test scaling toward a thermodynamic phase transition or robustness to hardware noise.

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

