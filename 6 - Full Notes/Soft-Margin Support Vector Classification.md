2026-09-14 21:00

Status: #baby

Tags: [[Support Vector Classification]]

# Soft-Margin Support Vector Classification

Soft-margin support vector classification introduces nonnegative slack variables for observations that enter the margin or cross the separating boundary. The objective balances a wide margin against the total penalty for these violations.

The regularization constant controls this tradeoff. A large penalty prioritizes training fit, while a smaller penalty tolerates more violations to obtain a smoother boundary that may generalize better when labels overlap or contain noise.

The slack-variable formulation is equivalent to minimizing regularized [[Hinge Loss]]. Observations beyond the required margin incur no hinge loss; observations inside it or on the wrong side contribute linearly. Kernelization changes the scoring space without changing this loss–regularization tradeoff.

# References

[[dataclassification.pdf]]

[[introductiontohigh-dimensionalstatistics.pdf]]
