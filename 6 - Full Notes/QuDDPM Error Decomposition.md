2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# QuDDPM Error Decomposition

The paper organizes total QuDDPM learning error into three conceptually different contributions:

$$E\simeq E_{\mathrm{diff}}+E_M+E_{\mathrm{gen}}.$$

$E_{\mathrm{diff}}$ measures how far the terminal scrambling ensemble remains from ideal random noise. $E_M$ represents finite-repetition error in estimating overlap-based losses. $E_{\mathrm{gen}}$ is the difference between the population loss and the loss computed from finite training and noise samples.

The decomposition prevents improvement in one component from being mistaken for total scalability. More diffusion steps reduce the modeled scrambling error, more measurements improve fidelity estimates, and more training samples improve generalization, but each resource addresses a different failure mode.

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

