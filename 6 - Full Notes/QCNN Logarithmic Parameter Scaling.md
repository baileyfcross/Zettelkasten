2026-10-12 02:08

Status: #baby

Tags: [[Quantum Convolutional Neural Networks]]

# QCNN Logarithmic Parameter Scaling

A translationally invariant QCNN for an (N)-qubit input can use (O(\log N)) variational parameters. Each convolution-pooling scale has a constant-size collection of shared unitaries, while repeated pooling reduces the active register geometrically and therefore requires only logarithmically many scales.

The parameter count is much smaller than that of a generic unconstrained quantum-circuit classifier. This structural restriction can reduce training demands and overfitting, as illustrated by the paper's phase-recognition model generalizing from a small line of solvable training points to a two-dimensional phase diagram.

Logarithmic parameter scaling does not imply that the circuit uses only logarithmically many gates. Shared unitaries must still be applied across many locations, and the paper's experimental resource estimate has a multi-qubit operation count that grows with the input size.

# References

[[2019 - Quantum Convolutional Neural Networks.pdf]]
