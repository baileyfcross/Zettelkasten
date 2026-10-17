2026-10-17 14:21

Status: #baby

Tags: [[Natural-Gradient Optimization of Optical Quantum Circuits]]

# Complex Quantum Natural-Gradient Update

Let $\xi$ contain every real optical-circuit parameter and, for each complex parameter, both the parameter and its conjugate. With Hermitian Fubini-Study metric $f$, the mixed-parameter natural-gradient update is

$$\xi\leftarrow\xi-\epsilon f^{-1}\frac{\partial L}{\partial\xi^*}.$$

The derivative for a complex coordinate is taken with respect to its conjugate, as required for steepest descent of a real-valued non-holomorphic loss. If a coordinate is real, the expression collapses to the usual real natural-gradient rule.

This update combines [[Wirtinger Calculus for Optical Quantum Parameters]] with the physical geometry of quantum-state space. It changes the optimization direction, not merely the scalar learning rate.

# References

[[2021 - Natural Gradient Optimization for Optical Quantum Circuits.pdf]]

