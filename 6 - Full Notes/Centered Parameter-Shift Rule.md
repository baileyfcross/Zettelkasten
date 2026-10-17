2026-10-17 14:34

Status: #baby

Tags: [[Quantum Circuit Gradient Rules]]

# Centered Parameter-Shift Rule

For an expectation value controlled by a [[Two-Eigenvalue Quantum Gate Generator|two-eigenvalue generator]], the centered parameter-shift rule computes the exact first derivative from two shifted circuit evaluations:

$$
f'(\theta)=
\frac{r\left[f(\theta+\gamma)-f(\theta-\gamma)\right]}
{\sin(2r\gamma)}.
$$

The shift $\gamma$ may be chosen freely except where $\sin(2r\gamma)=0$. Unlike a [[Central Difference Derivative Formula|centered finite difference]], the identity is exact at the expectation-value level and does not rely on taking a small shift.

A full $n$-parameter gradient therefore needs two expectation evaluations per component, or $2n$ evaluations when no measurements can be reused. Finite shots still introduce estimator variance even though the analytic rule itself is unbiased.

# References

[[2021 - Single-component gradient rules for variational quantum algorithms.pdf]]

