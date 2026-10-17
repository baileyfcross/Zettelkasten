2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# Quantum Denoising Diffusion Probabilistic Model

A quantum denoising diffusion probabilistic model, or QuDDPM, learns to generate individual pure states from an unknown distribution of quantum states. It first constructs intermediate ensembles between structured data and random noise, then trains a reverse process that maps fresh noisy states back through those ensembles.

The forward process applies random scrambling unitaries. The backward process alternates parameterized circuits with ancilla measurements, allowing a contractive denoising map that still outputs pure states. Training proceeds one reverse step at a time so that each circuit solves a shallower ensemble-matching problem.

This is not a direct translation of Gaussian DDPM equations. Quantum diffusion lacks the paper's classical analytic likelihood simplification, so QuDDPM evaluates sample-based distances between state ensembles through measurements such as fidelity-kernel MMD or Wasserstein distance.

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

