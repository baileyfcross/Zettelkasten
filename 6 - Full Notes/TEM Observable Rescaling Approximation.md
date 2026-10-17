2026-10-17 11:34

Status: #baby

Tags: [[Scalable Error-Mitigated Quantum Simulation]]

# TEM Observable Rescaling Approximation

In a non-Clifford circuit, the exact TEM map generally turns one Pauli observable into a sum of many noncommuting Pauli strings. General multi-qubit measurements could estimate all contributions, but current processors more naturally measure the Pauli components already present in the original observable.

A simplified strategy therefore keeps only the diagonal TEM rescaling coefficient for each original Pauli string. Although this omits off-diagonal components of the modified observable, those components have little overlap with the highly noisy output state in the paper's high-complexity model. The resulting systematic error is approximately $\epsilon^2NL/72$, which decreases when hardware improves while the accessible volume grows at fixed $\epsilon NL$.

# References

[[2024 - Scalability of quantum error mitigation techniques from utility to advantage.pdf]]

