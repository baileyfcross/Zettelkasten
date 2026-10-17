2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# Diffusion-Staged Barren Plateau Avoidance

QuDDPM uses diffusion steps to divide an expressive deep circuit into locally trained shallow circuits. For an $n$-qubit problem, the paper argues that expressivity requires a total depth linear in $n$, but the circuit can be divided into $T\in\Omega(n/\log n)$ reverse tasks so that each trained block has depth on the order of $\log n$.

With a local loss, keeping each optimization problem at logarithmic depth avoids the random-circuit regime associated with [[Barren Plateau Gradient Scaling]]. The intermediate ensembles provide meaningful targets, rather than asking one deep randomly initialized circuit to transport Haar-like noise directly to the data.

This is a theoretical trainability design supported by small simulated benchmarks. It does not prove that every ansatz, loss, noise model, or large-scale implementation of QuDDPM remains free of barren plateaus.

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

