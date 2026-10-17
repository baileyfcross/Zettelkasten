2026-10-16 23:00

Status: #baby

Tags: [[Quantum Invertible Generative Models]]

# Classical INN Coupling Architecture

A classical invertible neural network constructs a bijection from coupling blocks whose inverses and Jacobian determinants are cheap to evaluate. Each block splits an input vector into two parts, uses one part to predict a transformation of the other, and then rejoins them.

Because the conditioning half is unchanged inside a block, the Jacobian is triangular. Its determinant is therefore the product of easily available diagonal terms rather than the determinant of a dense matrix. Invertible permutations between blocks rotate which variables are transformed without changing the determinant magnitude.

The paper uses [[Affine Coupling Block]] as the simplest illustration and [[Monotone Cubic Spline Coupling]] for the more expressive classical benchmark. These restrictions are the price classical INNs pay for tractable inversion and likelihood evaluation.

# References

[[2023 - Generative Invertible Quantum Neural Networks.pdf]]

