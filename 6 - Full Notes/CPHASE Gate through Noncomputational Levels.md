2026-10-17 03:20

Status: #baby

Tags: [[Superconducting Qubit Engineering]]

# CPHASE Gate through Noncomputational Levels

A transmon CPHASE gate can use the avoided crossing between the computational state $|11\rangle$ and the noncomputational state $|20\rangle$. Tuning one qubit near this crossing repels the $|11\rangle$ energy level, causing that joint state to accumulate a phase different from the phases of $|00\rangle$, $|01\rangle$, and $|10\rangle$.

An adiabatic excursion that accumulates a relative phase of $\pi$ produces a controlled phase after the single-qubit phases are removed, often with [[Virtual Z Gate]] corrections. The higher level is thus an engineered resource: it supplies a state-dependent energy shift even though the logical state should return to the computational subspace.

Trajectory design balances speed against leakage. Moving too quickly through the avoided crossing populates $|20\rangle$ nonadiabatically; moving too slowly increases exposure to decoherence and flux noise. The protocol also requires control over nearby crossings and frequency crowding, making the full multilevel spectrum—not only the two logical levels—part of gate design.

# References

[[2021 - A Quantum Engineers Guide to Superconducting Qubits.pdf]]
