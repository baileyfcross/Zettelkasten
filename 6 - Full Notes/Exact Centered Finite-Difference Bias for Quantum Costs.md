2026-10-17 14:34

Status: #baby

Tags: [[Quantum Circuit Gradient Rules]]

# Exact Centered Finite-Difference Bias for Quantum Costs

For a two-eigenvalue quantum cost, the centered finite-difference estimator has an exact bias rather than only an asymptotic truncation order:

$$
\operatorname{Bias}\!\left(\widehat g_{\mathrm{cFD}}\right)
=\left[\frac{\sin(2rh)}{2rh}-1\right]f'(\theta).
$$

The factor approaches zero as the shift $h$ shrinks, reproducing the usual small-step approximation. Its finite-shot variance is

$$
\operatorname{Var}\!\left(\widehat g_{\mathrm{cFD}}\right)
=\frac{\sigma_1^2(\theta+h)+\sigma_1^2(\theta-h)}{4h^2},
$$

so smaller shifts reduce bias while amplifying measurement noise by $1/h^2$. The [[Centered Parameter-Shift Rule]] avoids truncation bias by using the generator-dependent sine normalization, but it still inherits finite-shot variance.

# References

[[2021 - Single-component gradient rules for variational quantum algorithms.pdf]]

