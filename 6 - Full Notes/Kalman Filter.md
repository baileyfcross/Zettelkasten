2026-09-06 21:47

Status: #baby

Tags: [[Recursive Bayesian Estimation]]

# Kalman Filter

A Kalman filter is a Bayesian filter specialized to linear state transitions and observations with Gaussian uncertainty. Those assumptions allow the belief state to be represented by a mean and covariance and updated analytically.

The prediction step propagates both the estimate and its uncertainty, while the correction step balances that prediction against a measurement. The relative covariances determine how strongly each source influences the posterior.

# References

[[bayesianprogramming.pdf]]
