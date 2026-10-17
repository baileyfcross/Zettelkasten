2026-10-17 03:20

Status: #baby

Tags: [[Superconducting Qubit Engineering]]

# iSWAP Gate in Tunable Transmons

Two capacitively coupled transmons have an exchange interaction that moves a single excitation between $|10\rangle$ and $|01\rangle$. When the qubits are tuned into resonance, the interaction generates coherent oscillations in that subspace.

Holding the resonance for the appropriate interval completes a swap while adding a phase of $i$, producing the iSWAP unitary. Shorter interactions generate partial iSWAP gates and entanglement. Deterministic phases accumulated while tuning to and from resonance can be corrected with [[Virtual Z Gate]] updates.

The gate is fast and natural for excitation-preserving simulation, but it requires tunable qubits and careful trajectories through a crowded multilevel spectrum. Nonadiabatic motion, frequency-dependent decoherence, residual coupling, and nearby avoided crossings can create leakage or phase error. In a CNOT-oriented gate set, two iSWAP operations plus single-qubit rotations are generally required, so the best native gate depends on the target workload and hardware connectivity.

# References

[[2021 - A Quantum Engineers Guide to Superconducting Qubits.pdf]]
