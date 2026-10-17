2026-10-17 14:34

Status: #baby

Tags: [[Quantum Circuit Gradient Rules]]

# Quantum Circuit Gradient Rule

A quantum circuit gradient rule specifies which shifted parameter points to evaluate and how to combine their measured expectation values into a derivative estimate. For the $i$th parameter of a cost $F(\boldsymbol{\theta})$, it selects shifts $\mathbf{s}_1,\ldots,\mathbf{s}_k$ and a function $g$ such that

$$
g\!\left(F(\boldsymbol{\theta}+\mathbf{s}_1),\ldots,F(\boldsymbol{\theta}+\mathbf{s}_k)\right)
=\frac{\partial F}{\partial\theta_i}.
$$

On hardware, each expectation value is replaced by a finite-shot estimator, so a rule determines both the circuit settings and the statistical estimator. Reapplying a rule can recover a [[Higher-Order Derivative]], but its circuit cost and variance depend on the chosen shifts and combination.

This definition separates a gradient rule from the classical optimizer that consumes it. [[Gradient Descent]] may use derivatives obtained from finite differences, exact parameter shifts, or simultaneous perturbations without changing its update equation.

# References

[[2021 - Single-component gradient rules for variational quantum algorithms.pdf]]

