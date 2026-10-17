2026-10-17 03:20

Status: #baby

Tags: [[Superconducting Qubit Engineering]]

# DRAG Pulse Control

Derivative Removal by Adiabatic Gate, or DRAG, reduces errors when controlling a weakly anharmonic qubit such as a transmon. A short in-phase pulse has spectral weight near the $|1\rangle\leftrightarrow|2\rangle$ transition, causing leakage, and off-resonant coupling also produces phase error through level repulsion.

DRAG adds an out-of-phase quadrature proportional to the time derivative of the main pulse, scaled by the inverse anharmonicity. The added quadrature cancels unwanted excitation pathways. One coefficient is theoretically optimal for leakage suppression and another for phase suppression, so practical calibration often combines an intermediate DRAG amplitude with a small drive-frequency shift or [[Virtual Z Gate]] correction.

The method does not make higher levels irrelevant; it uses their known dynamics to keep the intended evolution inside the computational subspace. Its performance depends on waveform distortion, anharmonicity, pulse duration, and calibration at the qubit, not merely the programmed generator envelope.

# References

[[2021 - A Quantum Engineers Guide to Superconducting Qubits.pdf]]
