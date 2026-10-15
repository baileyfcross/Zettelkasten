2026-10-14 18:20

Status: #baby

Tags: [[Quantum Optical Neurons]]

# Multiclass Extension of a Binary Optical Neuron

The Hong-Ou-Mandel optical neuron produces one binary decision because a single trained probe supplies one overlap score followed by a scalar threshold-like readout. Multiclass use therefore requires multiple learned probe settings and a decision scheme that combines their outputs rather than a single native $K$-class measurement.

The paper proposes one-versus-one and one-versus-rest strategies, with a resource overhead reported as either $O(K)$ or $O(K^2)$ operations depending on the scheme for $K$ classes. The per-comparison overlap can retain its resolution-independent implementation, but the number of comparisons grows with the label set. This distinction prevents the binary neuron's constant-in-resolution cost from being mistaken for constant cost in both image resolution and number of classes.

# References

[[2024 - Quantum optical classifier with superexponential speedup.pdf]]
