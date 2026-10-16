2026-10-16 17:27

Status: #baby

Tags: [[Quantum Chebyshev Modeling]]

# Exponential-Degree Chebyshev Amplitude Encoding

An $N$-qubit [[Orthonormal Chebyshev Quantum State]] contains amplitudes proportional to $T_k(x)$ for indices through $k=2^N-1$. The highest accessible polynomial degree therefore grows exponentially with the register width, even though the state occupies only $N$ data qubits.

The [[Orthonormal Chebyshev Feature Map]] generates these degrees through phase rotations whose frequency scales double with qubit position, rather than by evaluating every polynomial with a separate arithmetic circuit. This gives the representation high functional capacity, but capacity alone is not a learning advantage: a useful model must still be trainable, have an appropriate adjustable circuit, and expose its learned distribution through a practical readout such as the [[Quantum Chebyshev Transform]].

# References

[[2023 - Quantum Chebyshev Transform Mapping Embedding Learning and Sampling Distributions.pdf]]
