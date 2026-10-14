2026-10-14 17:27

Status: #baby

Tags: [[Unary-Encoded Quantum Neural Networks]]

# Unary-Subspace Orthogonal Matrix Multiplication

When a [[Quantum Pyramidal Circuit]] acts on a unary state, each input excitation can follow several paths to each output qubit. Products of gate sines and cosines give the amplitude of a path, and interference sums those paths into an element $W_{ij}$ of a real matrix $W$.

The full $n$-qubit circuit is a $2^n\times2^n$ unitary, but the single-excitation subspace is invariant and only $n$ dimensional. Within it, the circuit implements $|x\rangle\mapsto|Wx\rangle$ for an $n\times n$ [[Orthogonal Matrix|orthogonal matrix]]. This correspondence lets one quantum layer reproduce a norm-preserving classical dense layer while remaining classically simulable in $O(n^2)$ time on unary inputs.

# References

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
