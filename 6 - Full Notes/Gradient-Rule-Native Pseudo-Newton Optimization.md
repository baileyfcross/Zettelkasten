2026-10-17 14:34

Status: #baby

Tags: [[Quantum Circuit Gradient Rules]]

# Gradient-Rule-Native Pseudo-Newton Optimization

An asymmetric quantum shift naturally returns a fixed combination of first- and second-order derivatives. A gradient-rule-native optimizer would use that measured combination directly rather than spending circuit evaluations to separate the gradient and [[Hessian Matrix|Hessian]] before forming a conventional Newton step.

The same idea can extend to joint parameter shifts that expose mixtures of cross-derivatives. Classical control patterns could then be designed around the derivative combinations that the quantum circuit produces most economically.

The paper presents this as a research direction, not a tested optimizer. A practical pseudo-Newton method would still need rules for step construction, conditioning, finite-shot uncertainty, and convergence when the available derivative mixture changes with the selected shifts.

# References

[[2021 - Single-component gradient rules for variational quantum algorithms.pdf]]

