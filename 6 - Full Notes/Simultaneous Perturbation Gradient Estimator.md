2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# Simultaneous Perturbation Gradient Estimator

Simultaneous perturbation stochastic approximation estimates an entire gradient from two evaluations of a scalar objective, independent of the number of parameters. For a random direction $\Delta\in\{-1,+1\}^d$ with independent components,

$$
\widehat{\nabla f}(\theta)=
\frac{f(\theta+\epsilon\Delta)-f(\theta-\epsilon\Delta)}
{2\epsilon}\Delta.
$$

The random direction perturbs every coordinate at once, replacing coordinate-by-coordinate derivatives with a noisy vector estimate. Averaging over directions recovers the local gradient as $\epsilon$ becomes small, but any single estimate contains variance from both the random direction and measurement noise.

This constant evaluation cost makes SPSA useful when a variational quantum objective has many parameters. Its advantage is therefore query scaling rather than exactness: the perturbation size, learning rate, and number of repeated samples still determine whether the optimizer is stable.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

