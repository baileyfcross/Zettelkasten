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

An empirical optimizer review illustrates the resource advantage on an eight-qubit, 64-parameter excited-state classifier. Over 1,000 optimization steps with 1,000 shots per expectation, SPSA used 2,000,000 shots while a parameter-shift method used 128,000,000. The factor-of-64 gap follows from SPSA's two evaluations per gradient estimate versus two shifted evaluations per parameter.

The same benchmark also shows the tradeoff: SPSA was one of the strongest black-box choices but did not match the final-loss quality of Adam and its variants under an equal-iteration budget. Its value is therefore clearest when quantum queries, rather than classical update count, are the scarce resource.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]
[[2022 - An Empirical Review of Optimization Techniques for Quantum Variational Circuits.pdf]]

