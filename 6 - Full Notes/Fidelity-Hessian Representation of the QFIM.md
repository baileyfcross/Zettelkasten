2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# Fidelity-Hessian Representation of the QFIM

For a pure parameterized state, the quantum Fisher information matrix is four times the [[Fubini-Study Metric for Variational Quantum States]]. The metric can be recovered from the curvature of the fidelity

$$F(\theta',\theta)=|\langle\psi(\theta')|\psi(\theta)\rangle|^2$$

by fixing the first argument and differentiating the second:

$$
g_{ij}(\theta)=
-\frac{1}{2}
\left.
\frac{\partial^2 F(\theta',\theta)}
{\partial\theta_i\,\partial\theta_j}
\right|_{\theta'=\theta}.
$$

This identity turns metric estimation into a black-box second-derivative problem. A quantum device need only prepare nearby states and estimate their overlap; it does not need a separate analytic derivative circuit for every entry of the matrix.

The representation is the bridge that allows [[Quantum Natural SPSA]] to adapt a stochastic Hessian estimator to quantum-state geometry.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

