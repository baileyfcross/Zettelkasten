2026-10-16 23:00

Status: #baby

Tags: [[Quantum Invertible Generative Models]]

# Affine Coupling Block

An affine coupling block splits $x=[u,v]^T$ and lets a subnet conditioned on $v$ predict an elementwise scale $s(v)$ and translation $t(v)$ for $u$:

$$\hat u=u\odot e^{s(v)}+t(v),\qquad \hat v=v.$$

The inverse follows directly because the conditioning part is unchanged:

$$u=(\hat u-t(\hat v))\odot e^{-s(\hat v)},\qquad v=\hat v.$$

Its [[Jacobian Matrix]] is triangular, so the [[Jacobian Determinant]] depends only on the scale outputs. This makes the block useful in [[Classical INN Coupling Architecture]], although its elementwise linear transform is less expressive per parameter than a spline coupling.

# References

[[2023 - Generative Invertible Quantum Neural Networks.pdf]]

