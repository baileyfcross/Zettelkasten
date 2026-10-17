2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# QN-SPSA Regularization Interpolation

The regularization parameter $\beta$ controls whether a QN-SPSA step behaves more like an exact quantum natural gradient or an ordinary first-order update. Small $\beta$ preserves more anisotropy from the sampled QFIM but can amplify estimation errors; large $\beta$ makes the matrix increasingly proportional to the identity and improves stability.

The paper normalizes the regularized matrix as

$$
\frac{\sqrt{AA}+\beta I}{1+\beta},
$$

so that the update scale does not collapse merely because $\beta$ is large. With this normalization, changing $\beta$ primarily changes the geometry rather than silently shrinking the learning rate.

Regularization therefore defines a continuous interpolation between noisy curvature following and stable Euclidean descent. It must be reported alongside the learning rate and perturbation size because it materially changes the optimizer.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

