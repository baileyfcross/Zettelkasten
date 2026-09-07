2026-09-06 00:13

Status: #baby

Tags: [[Optimization and Differentiation]]

# Gradient

A gradient is a [[Vector]] containing all the [[Partial Derivative|partial derivatives]] of a multivariable function. It indicates the local direction in which the function increases most directly.

To reduce neural-network loss, a [[Neural Network Parameter Update]] changes each weight and bias in the direction opposite its corresponding gradient component. This generalizes using the opposite of a single slope to move downhill.

For any unit direction $u$, the [[Directional Derivative]] is $\nabla f\cdot u$. The gradient therefore points in the direction of steepest local increase, its negative points toward steepest decrease, and a zero gradient identifies a [[Stationary Point]].

# References

[[algorithms.epub]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]
