2026-10-17 14:21

Status: #baby

Tags: [[Natural-Gradient Optimization of Optical Quantum Circuits]]

# Wirtinger Calculus for Optical Quantum Parameters

Wirtinger calculus treats a complex variable $z$ and its conjugate $z^*$ as formally independent coordinates. Their derivatives are related to derivatives of $z_R=\operatorname{Re}z$ and $z_I=\operatorname{Im}z$ by

$$\partial_z=\tfrac12(\partial_{z_R}-i\partial_{z_I}),\qquad
\partial_{z^*}=\tfrac12(\partial_{z_R}+i\partial_{z_I}).$$

This representation is useful for optical circuits because fidelity losses are real-valued and generally non-holomorphic: they depend on both complex amplitudes and their conjugates. Ordinary complex differentiation alone would not describe their full variation.

The paper uses block-diagonal basis transformations to apply the same rule to a vector containing real and complex gate parameters. Real parameters retain a one-dimensional identity block, while each complex parameter contributes a two-dimensional block.

# References

[[2021 - Natural Gradient Optimization for Optical Quantum Circuits.pdf]]

