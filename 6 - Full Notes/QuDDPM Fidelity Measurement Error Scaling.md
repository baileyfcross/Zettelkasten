2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# QuDDPM Fidelity Measurement Error Scaling

Estimating a fidelity $F_{ij}$ from $m$ repeated SWAP-test measurements has standard error

$$\operatorname{SE}(F_{ij})=\sqrt{\frac{1-F_{ij}}{m}}.$$

When two empirical ensembles each contain $N$ states and the loss averages all $N^2$ pairwise fidelities, the paper combines the independent variances to obtain mean-fidelity error scaling

$$E_M=O\!\left(\frac{1}{N\sqrt m}\right).$$

This scaling describes statistical error in the averaged quantity, not the number of circuit executions required to obtain all pairs. Directly measuring a dense $N\times N$ overlap matrix still creates a substantial experimental workload, especially when every SWAP test operates on two state registers plus an ancilla.

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

