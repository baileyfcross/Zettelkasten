2026-10-14 17:27

Status: #baby

Tags: [[Unary-Encoded Quantum Neural Networks]]

# RBS Angle-Space Backpropagation

RBS angle-space backpropagation differentiates a [[Quantum Pyramidal Circuit]] with respect to its rotation angles rather than the entries of its equivalent weight matrix. A forward pass stores the unary activation vector after each circuit timestep; the backward pass propagates an error vector through the transposed planar rotations in reverse order.

At one RBS gate, the angle derivative depends only on the two activation components entering the gate, the two error components leaving it, and the sine and cosine of that gate's angle. Each gradient is therefore computed with constant local work, avoiding the parameter-shift rule and preserving the circuit's exact orthogonal parameterization after every gradient update.

# References

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
