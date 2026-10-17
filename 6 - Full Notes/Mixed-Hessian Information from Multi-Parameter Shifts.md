2026-10-17 14:34

Status: #baby

Tags: [[Quantum Circuit Gradient Rules]]

# Mixed-Hessian Information from Multi-Parameter Shifts

Shifting two gate parameters together can expose a known linear combination of diagonal and mixed entries of the [[Hessian Matrix]]. The paper gives an example combining evaluations at jointly positive and negative shifts with a half-period-shifted evaluation to produce weighted access to

$$
\frac{\partial^2 f}{\partial\theta_1\partial\theta_2},
\qquad
\frac{\partial^2 f}{\partial\theta_1^2},
\qquad
\frac{\partial^2 f}{\partial\theta_2^2}.
$$

The circuit data need not identify each Hessian entry separately to be useful. An optimization method could act directly on the available combination, potentially using fewer evaluations than explicit element-by-element reconstruction.

This is a proposed extension of the single-component analysis rather than a complete multi-parameter shift rule. It complements the random directional Hessian samples of [[Second-Order Simultaneous Perturbation Approximation]] with a spectrum-based deterministic construction.

# References

[[2021 - Single-component gradient rules for variational quantum algorithms.pdf]]

