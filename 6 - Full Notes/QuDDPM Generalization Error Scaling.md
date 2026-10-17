2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# QuDDPM Generalization Error Scaling

QuDDPM generalization error is defined as the difference between the population ensemble loss and the corresponding empirical loss evaluated on finite target and terminal-noise samples after training.

In a four-qubit clustered-state simulation, the measured error scales approximately as

$$E_{\mathrm{gen}}=O\!\left(\frac{1}{TN}\right),$$

where $T$ is the number of diffusion steps and $N$ is the training-set size. Separate parameter sweeps produce fitted exponents near one for both variables.

This is numerical evidence, not a theorem. The authors explicitly leave a proof open, and the reported scaling comes from one small task and architecture. It should not be assumed to hold unchanged for other state ensembles, losses, ansatzes, or noisy hardware.

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

