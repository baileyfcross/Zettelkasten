2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# Second-Order Simultaneous Perturbation Approximation

Second-order SPSA estimates a Hessian by taking a finite difference along two independent Bernoulli directions rather than differentiating every parameter pair. A four-point mixed difference produces a scalar curvature estimate, which is multiplied by the symmetrized outer product of the two directions to form a matrix sample.

The point estimate is noisy and low rank, but its expectation approaches the true Hessian for small perturbations. When combined with the two evaluations needed by the [[Simultaneous Perturbation Gradient Estimator]], a second-order update uses six objective evaluations instead of a number that grows quadratically with the parameter dimension.

The estimator does not make the inverse Hessian unbiased. Practical second-order SPSA therefore smooths many matrix samples and regularizes the result before solving for an update.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

