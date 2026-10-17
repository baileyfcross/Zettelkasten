2026-10-16 21:58

Status: #baby

Tags: [[Experimental Quantum GAN Image Generation]]

# Frechet Distance Evaluation for Quantum GANs

The quantum GAN benchmark uses a Frechet Distance score to compare the distribution of generated gray-scale bars with the known real distribution. The score corresponds to a 2-Wasserstein distance, so lower values indicate that the generated samples more closely match the target distribution.

Every 50 training iterations, the experiment draws 1,000 generated examples and computes the score. Each model setting is repeated five times, and box plots report the distribution of scores as well as the best observed values. This exposes adversarial-training variability that would be hidden by reporting only one final run.

The score is meaningful because the synthetic target distribution is explicit and can supply unlimited test samples. It should not be confused with a general proof of perceptual image quality: the benchmark has four pixels and a highly constrained pattern. [[Quantum GAN Parameter-Efficiency Benchmark]] uses these scores to compare models at different parameter budgets.

# References

[[2021 - Experimental Quantum Generative Adversarial Networks for Image Generation.pdf]]
