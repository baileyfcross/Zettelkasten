2026-10-16 22:51

Status: #baby

Tags: [[Quantum Generative Architecture Performance]]

# KL-Only Quantum Generator Evaluation Limitation

The performance study selects models by Kullback-Leibler divergence between a histogram of generated samples and the training-data histogram. This measures how closely the learned distribution fits the observed empirical distribution and supports controlled architecture comparisons.

Training fit is not the same as generative generalization. KL alone does not determine whether a model produces useful unseen samples, preserves privacy, covers rare modes, or improves an application objective; those questions require evaluation such as [[Discrete Generative Generalization Framework]].

The study also uses only two- and three-dimensional data and noiseless state-vector circuits. Its low KL and parameter-count results should therefore be read as representation and optimization characterization, not evidence that the same models generalize or scale on realistic hardware.

# References

[[2023 - A performance characterization of quantum generative models.pdf]]

