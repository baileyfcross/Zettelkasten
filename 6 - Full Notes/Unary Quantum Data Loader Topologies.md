2026-10-14 17:27

Status: #baby

Tags: [[Unary-Encoded Quantum Neural Networks]]

# Unary Quantum Data Loader Topologies

A unary quantum data loader prepares [[Unary Amplitude Encoding]] with $d-1$ [[Reconfigurable Beam Splitter Quantum Gate|RBS gates]] after classically converting a normalized $d$-component vector into rotation angles. Different layouts trade circuit depth against hardware connectivity.

The parallel topology has depth $O(\log d)$ but needs long-range connections. A diagonal nearest-neighbor cascade has depth $d-1$, while the semidiagonal arrangement reduces depth to roughly $d/2$ and still fits limited-connectivity hardware. The logarithmic version can reduce the ideal depth for 1,024 features from about 1,024 steps to 10, but only when the processor can execute its required parallel interactions.

# References

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
