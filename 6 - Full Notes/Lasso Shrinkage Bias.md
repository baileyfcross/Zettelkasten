2026-09-29 19:17

Status: #baby

Tags: [[Sparse and Structured Regression]]

# Lasso Shrinkage Bias

Lasso shrinkage bias is the systematic pull of selected coefficients toward zero caused by the $\ell_1$ penalty. The same penalty that creates exact zeros also reduces the magnitude of coefficients that remain active.

In an orthonormal design, the effect is explicit: each selected response correlation is reduced by a fixed threshold. This can improve prediction by controlling variance but attenuate strong signals. Refitting ordinary least squares on the selected support yields the [[Gauss-Lasso]], while the [[Adaptive Lasso]] uses data-dependent weights to reduce shrinkage selectively.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
