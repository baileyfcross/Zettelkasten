2026-09-29 19:17

Status: #baby

Tags: [[Sparse and Structured Regression]]

# Square-Root Lasso

Square-root Lasso minimizes the residual norm rather than the squared residual norm, together with an $\ell_1$ penalty. This change makes the theoretically calibrated penalty independent of the unknown noise variance and gives the estimator [[Scale-Invariant Estimation|scale invariance]].

It can also be written as a joint convex problem for coefficients and a residual-scale estimate. Alternating updates then solve an ordinary Lasso at the current scale and recompute that scale from the residuals. Scale independence does not eliminate tuning entirely because the risk-optimal penalty can still depend on the unknown signal.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
