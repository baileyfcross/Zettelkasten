2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# Fidelity-Kernel MMD Identifiability Failure

A fidelity-kernel MMD can assign zero distance to different quantum-state distributions. The paper's counterexample compares a uniform one-qubit ring in the $X$-$Z$ plane with the Haar-random distribution over the Bloch sphere.

For these ensembles, the mean fidelity within the ring, within the Haar distribution, and across the two distributions is $1/2$. Substitution into the MMD expression gives $1/2+1/2-2(1/2)=0$ even though the distributions have different topology and support.

The failure is caused by the kernel representation, not by insufficient optimization. More samples only estimate the same nonidentifying population quantity more accurately. QuDDPM therefore uses [[Quantum State-Ensemble Wasserstein Distance]] for the circular-state experiment.

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

