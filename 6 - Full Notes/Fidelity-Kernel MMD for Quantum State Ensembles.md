2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# Fidelity-Kernel MMD for Quantum State Ensembles

The squared overlap

$$F(|\phi\rangle,|\psi\rangle)=|\langle\phi|\psi\rangle|^2$$

is a symmetric positive-definite kernel on pure states. It therefore defines a maximum mean discrepancy between two distributions of quantum states through their within-ensemble and cross-ensemble mean fidelities:

$$D_{\mathrm{MMD}}(E_1,E_2)=\bar F(E_1,E_1)+\bar F(E_2,E_2)-2\bar F(E_1,E_2).$$

Finite sets of states approximate these expectations using pairwise overlap measurements. This gives QuDDPM a directly measurable loss without reconstructing every state classically.

Kernel validity does not guarantee distributional identifiability. Whether fidelity distinguishes the ensembles is problem-dependent, as demonstrated by [[Fidelity-Kernel MMD Identifiability Failure]].

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

