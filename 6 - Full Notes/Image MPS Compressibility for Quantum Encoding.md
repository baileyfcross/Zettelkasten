2026-10-14 17:55

Status: #baby

Tags: [[Variational Quantum Image Classification]]

# Image MPS Compressibility for Quantum Encoding

Many natural images have rapidly decaying Fourier coefficients, so their [[Flexible Representation of Quantum Images|FRQI states]] can be approximated by matrix product states with modest bond dimension under bounded error. This low-entanglement structure explains why shallow local circuits can reproduce image states much better than they could reproduce arbitrary states of the same qubit count.

An exact sequential preparation of an MPS with bond dimension $\chi$ uses gates supported on roughly $\lceil\log_2\chi\rceil+1$ qubits, but compiling those multiqubit gates may create long native circuits. A layered staircase PQC is a heuristic subset of MPSs with maximum bond dimension $2^l$ after $l$ layers, chosen to reduce compilation overhead rather than reproduce every MPS of that bond dimension.

# References

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]
