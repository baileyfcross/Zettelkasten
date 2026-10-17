2026-10-17 14:34

Status: #baby

Tags: [[Quantum Circuit Gradient Rules]]

# Generalized Parameter-Shift Rule

The generalized parameter-shift rule compares two potentially unequal displacements around a parameter:

$$
g_{\mathrm{gPSR}}(\theta,\gamma_1,\gamma_2)
=r\left[f(\theta+\gamma_1)-f(\theta-\gamma_2)\right].
$$

For a two-eigenvalue generator, this quantity is exactly

$$
\frac{\sin(2r\gamma_1)+\sin(2r\gamma_2)}{2}f'(\theta)
-\frac{\cos(2r\gamma_1)-\cos(2r\gamma_2)}{4r}f''(\theta).
$$

Equal shifts cancel the second-derivative coefficient and recover the [[Centered Parameter-Shift Rule]]. Setting one shift to zero recovers a scaled forward or backward finite difference, while a half-period choice isolates the second derivative.

The rule unifies these methods as different selections from the same exact first- and second-derivative mixture rather than treating them as unrelated circuit recipes.

# References

[[2021 - Single-component gradient rules for variational quantum algorithms.pdf]]

