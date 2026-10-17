2026-10-16 21:58

Status: #baby

Tags: [[Experimental Quantum GAN Image Generation]]

# Quantum GAN Parameter-Efficiency Benchmark

On the $2\times2$ gray-scale-bar task, the quantum patch generator uses nine trainable parameters. Classical MLP and convolutional generators with approximately ten parameters obtain worse Frechet Distance scores, while larger classical generators require roughly tens of parameters to match or surpass the quantum results in the reported comparisons.

This supports a narrow parameter-efficiency claim: the tested quantum circuit represents the small target distribution with fewer adjustable generator angles than the selected classical architectures. It is not an end-to-end computational advantage. Quantum parameters require repeated circuit measurements and parameter-shift evaluations, and the quantum and classical parameters do not have equal execution cost.

The comparison also favors the classical baselines in hyperparameter search: learning rates and optimizer settings are grid-searched for the classical GANs but not for the qGAN. That makes the observed quantum result noteworthy, yet five repeated runs on a four-pixel synthetic distribution remain insufficient to infer a broad scaling law or superiority over modern image generators.

# References

[[2021 - Experimental Quantum Generative Adversarial Networks for Image Generation.pdf]]
