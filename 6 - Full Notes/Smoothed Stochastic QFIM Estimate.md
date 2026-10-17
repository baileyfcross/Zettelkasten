2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# Smoothed Stochastic QFIM Estimate

QN-SPSA combines successive low-rank metric samples in a running average,

$$
\overline g^{(k)}
=\frac{k}{k+1}\overline g^{(k-1)}
+\frac{1}{k+1}\widehat g^{(k)}.
$$

The accumulated matrix retains information from earlier random directions, allowing its effective rank and geometric fidelity to improve over time. Extra samples can also be averaged within a single iteration when the application requires a more accurate local path.

Although each point estimate is asymptotically unbiased, inverting the smoothed random matrix does not produce an unbiased estimate of the inverse true metric. Smoothing reduces variance but does not remove this nonlinear inverse bias, which is one reason [[Positive-Definite QFIM Sample Regularization]] remains necessary.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

