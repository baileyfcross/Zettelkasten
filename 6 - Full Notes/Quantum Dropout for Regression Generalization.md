2026-10-12 18:44

Status: #baby

Tags: [[Quantum Dropout Regularization]]

# Quantum Dropout for Regression Generalization

The paper evaluates quantum dropout on noisy sine and absolute-value regression with a five-qubit, ten-layer data-reuploading circuit containing 150 trainable rotations. Each dataset has only 20 examples, split 75 percent for the [[Training Dataset]] and 25 percent for the [[Test Dataset]], making it easy for the expressive circuit to interpolate training noise.

On the sine task, training without dropout drove training mean-squared error nearly to zero while test error rose to about 0.111. The best [[Independent Quantum Dropout]] configuration produced an average test error near 0.032 across ten runs, a reported reduction of about 71.4 percent. The effective operation probabilities were small even though the circuit's parameter count allowed a much larger theoretical removal fraction.

The absolute-value task showed the same qualitative benefit: every dropout strategy reduced the train-test discrepancy, and independent dropout had the lowest mean test error, about 10.2 percent below entangling dropout. Predictions near the sampled interval boundaries had high variability because the learned Fourier representation exhibited Gibbs behavior there, so the paper does not interpret that variance as a dropout-specific failure.

These results are evidence from noiseless simulation with a tiny sample, not a hardware or scaling demonstration. They show that stochastic subcircuits can improve generalization in the tested setting without establishing that the same ranking holds for larger problems.

# References

[[2023 - A General Approach to Dropout in Quantum Neural Networks.pdf]]
