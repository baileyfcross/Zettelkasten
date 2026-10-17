2026-10-17 11:34

Status: #baby

Tags: [[Scalable Error-Mitigated Quantum Simulation]]

# Observable-Aware and Observable-Agnostic Error Mitigation

Probabilistic error cancellation is observable-agnostic: it samples a signed quasiprobability decomposition of inverse noise so that the circuit's output state is unbiased before a particular observable is chosen. This Schrödinger-picture correction pays for reconstructing components that may not affect the eventual measurement.

Zero-noise extrapolation and tensor-network error mitigation are observable-aware. ZNE infers the zero-noise value from a chosen observable's response to amplified noise, while TEM propagates inverse noise onto that observable in the Heisenberg picture. For realistic sparse Pauli-Lindblad noise, this focus changes the leading sampling overhead from PEC's $e^{2\epsilon NL}$ to approximately $e^{\epsilon NL}$ for ZNE and TEM, although ZNE retains an additional polynomial prefactor.

# References

[[2024 - Scalability of quantum error mitigation techniques from utility to advantage.pdf]]

