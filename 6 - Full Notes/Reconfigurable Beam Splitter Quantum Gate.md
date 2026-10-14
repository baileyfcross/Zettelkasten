2026-10-14 17:27

Status: #baby

Tags: [[Unary-Encoded Quantum Neural Networks]]

# Reconfigurable Beam Splitter Quantum Gate

A reconfigurable beam splitter (RBS) is a two-qubit gate that leaves $|00\rangle$ and $|11\rangle$ unchanged while rotating the amplitudes of $|01\rangle$ and $|10\rangle$ by an angle $\theta$. On the single-excitation subspace, it is a [[Givens Rotation]] between two coordinates.

Because an RBS conserves Hamming weight, networks of these gates preserve [[Unary Amplitude Encoding]]. The gate can serve both as a data-loading primitive and as a trainable planar rotation inside a [[Quantum Pyramidal Circuit]]. The paper decomposes it into two controlled-Z gates, Hadamards, and opposite $R_y(\theta/2)$ rotations when RBS is not native to the device.

# References

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
