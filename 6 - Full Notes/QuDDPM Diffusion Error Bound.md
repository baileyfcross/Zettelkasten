2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# QuDDPM Diffusion Error Bound

When the forward scrambling circuit approaches an approximate quantum $K$-design, the paper bounds its deviation from ideal random-state noise by a term that decays exponentially with the number of diffusion steps:

$$E_{\mathrm{diff}}\sim 2^{nK}e^{-T/A(K)}C.$$

$A(K)$ is polynomial in the design order and $C$ depends on the single-step circuit. For fixed problem and design parameters, this gives the summarized behavior $E_{\mathrm{diff}}=O(e^{-T})$.

The exponential decay in $T$ does not remove the dimension- and design-dependent prefactor. The bound isolates how additional scrambling steps improve terminal-noise quality; it is not a claim that the entire QuDDPM training and measurement cost is independent of system size.

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

