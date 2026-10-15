2026-10-15 00:14

Status: #baby

Tags: [[Quantum Computing for High-Energy Physics]]

# Collective Neutrino SWAP-Network Simulation

The neutrino-neutrino term in a collective oscillation model couples every neutrino pair, whereas many gate-based processors provide only local two-qubit connectivity. A SWAP network resolves this mismatch by moving logical neutrinos through neighboring hardware positions so every required pair becomes adjacent once during a structured sequence.

For $N$ neutrinos, the construction uses $N$ layers containing about $N/2$ nearest-neighbor two-qubit interactions per layer. Combined with a first-order product formula, the report gives a cost of $3N(N-1)/2$ CNOT operations and depth $3N$ per time step; a second-order step costs more gates and roughly doubles the depth. All-to-all platforms avoid routing constraints but still perform a comparable number of entangling operations.

This organization makes the hardware-connectivity cost explicit and supplies a reproducible benchmark across architectures. It also shows why larger systems are not enough by themselves: useful simulations require enough fidelity for many repeated two-qubit operations and enough time steps to resolve collective behavior. [[Trotter Step Noise-Discretization Tradeoff]] captures the resulting balance between shorter numerical steps and accumulated device error.

# References

[[2023 - Quantum Computing for High-Energy Physics State of the Art and Challenges Summary of the QC4HEP Working Group.pdf]]
