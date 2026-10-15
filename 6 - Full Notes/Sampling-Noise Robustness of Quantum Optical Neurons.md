2026-10-14 18:20

Status: #baby

Tags: [[Quantum Optical Neurons]]

# Sampling-Noise Robustness of Quantum Optical Neurons

Finite coincidence counts replace the exact optical score with an empirical frequency. The paper tests this effect by sampling the Hong-Ou-Mandel output with 100 and 1,000 repetitions per estimate during simulated training. The sampled curves fluctuate around the ideal trajectories, with more variation at the lower repetition count.

For MNIST zero-versus-one, the model's predictability and convergence remain essentially unchanged. CIFAR-10 cat-versus-dog is more sensitive: accuracy and loss fluctuate visibly, yet their asymptotic trends remain compatible with the noiseless optimization and with the classical baselines. The result is evidence of robustness for these two simulations, not a general noise guarantee. It addresses shot sampling only and does not model every experimental imperfection, detector inefficiency, or state-preparation error considered by a broader [[Quantum Classifier Sampling and Systematic Error]] analysis.

# References

[[2024 - Quantum optical classifier with superexponential speedup.pdf]]
