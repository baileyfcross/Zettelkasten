2026-10-17 11:34

Status: #baby

Tags: [[Scalable Error-Mitigated Quantum Simulation]]

# Data-Driven TEM Compression Error Estimation

The exact TEM map has exponentially large bond dimension, so its full singular-value spectrum cannot be computed for large systems. Compression error must instead be estimated from quantities available while the approximate map is being built.

At each layer, one can compute the relative Frobenius distance between the uncompressed update and its bond-dimension-$\chi$ approximation. Summing the squared relative distances across layers and taking the square root defines an error indicator $\mathcal{E}(\chi,L)$. Numerical experiments show that it tracks the median observable bias and works with either singular-value or variational compression, making it an operational diagnostic for [[TEM Bond-Dimension Compression Bias]].

# References

[[2024 - Scalability of quantum error mitigation techniques from utility to advantage.pdf]]

