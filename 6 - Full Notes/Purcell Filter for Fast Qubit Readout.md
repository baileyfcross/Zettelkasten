2026-10-17 03:20

Status: #baby

Tags: [[Superconducting Qubit Engineering]]

# Purcell Filter for Fast Qubit Readout

A readout resonator connects a qubit to a transmission line strongly enough to measure it, but that same path lets the qubit radiate energy into the environment. In the dispersive regime the associated Purcell decay rate scales approximately as $(g/\Delta)^2\kappa$, linking qubit lifetime to coupling, detuning, and resonator linewidth.

Simply narrowing the resonator reduces this loss but slows ring-up and ring-down, degrading measurement speed. A Purcell filter inserts a frequency-selective network between the readout resonator and the line. It transmits near the resonator frequency while presenting a suppressive impedance near the qubit frequency.

The filter partially separates two objectives that a bare resonator ties together: rapid escape of readout photons and weak spontaneous emission from the qubit. Its effectiveness depends on the realized filter response, qubit and resonator placement, parasitic modes, and the full multiport environment. It protects [[Dispersive Superconducting-Qubit Readout]] without removing other $T_1$ mechanisms.

# References

[[2021 - A Quantum Engineers Guide to Superconducting Qubits.pdf]]
