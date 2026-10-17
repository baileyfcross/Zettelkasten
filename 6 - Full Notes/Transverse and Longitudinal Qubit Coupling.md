2026-10-17 03:20

Status: #baby

Tags: [[Superconducting Qubit Engineering]]

# Transverse and Longitudinal Qubit Coupling

The axis of a qubit-qubit interaction determines what the coupling does. A transverse interaction contains operators such as $\sigma_x\sigma_x$ or exchange terms $\sigma_+\sigma_-+\sigma_-\sigma_+$. Near resonance it swaps excitations between qubits, providing the mechanism for an [[iSWAP Gate in Tunable Transmons]].

A longitudinal interaction is diagonal in the qubit energy basis, with a form such as $\sigma_z\sigma_z$. It changes the phase of a joint state without directly exchanging excitations, making conditional-phase operations natural. Longitudinal coupling can also support measurement and control schemes that reduce unwanted transitions.

Real circuits often contain several terms at once. Which term dominates depends on circuit topology, matrix elements, detuning, drive frequency, and the frame used to describe the dynamics. Gate engineering therefore requires both a physical coupler and a protocol that selects the intended interaction while averaging, detuning, or echoing away the others.

# References

[[2021 - A Quantum Engineers Guide to Superconducting Qubits.pdf]]
