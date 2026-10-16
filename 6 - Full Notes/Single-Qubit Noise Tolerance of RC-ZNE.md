2026-10-15 10:43

Status: #baby

Tags: [[Randomized Compiling and Zero-Noise Extrapolation]]

# Single-Qubit Noise Tolerance of RC-ZNE

Randomized compiling inserts and merges additional single-qubit Pauli operations, so its benefit depends on those operations being substantially cleaner than the entangling gates whose noise is being tailored. A simulation with coherent crosstalk on both gate classes tests this assumption directly.

With the entangling-gate error fixed near $10^{-3}$, combined RC and ZNE still produces a significant energy improvement when the single-qubit error rate is one tenth or one half of the entangling-gate rate. When the rates become equal, the added single-qubit errors prevent the protocol from reducing the VQE energy error.

The result supplies a relative hardware criterion rather than an absolute threshold: the easy gates used to dress noisy cycles must remain appreciably cleaner than the hard gates. It also bounds the ideal-single-qubit assumption used in [[Coherent CNOT Error Models for VQE]].

# References

[[2022 - Synergetic quantum error mitigation by randomized compiling and zero-noise extrapolation for the variational quantum eigensolver.pdf]]
