2026-10-17 03:20

Status: #baby

Tags: [[Superconducting Qubit Engineering]]

# Transmon Charge-Noise and Anharmonicity Tradeoff

A transmon shunts a Josephson junction with a large capacitance so that the ratio $E_J/E_C$ is typically at least about 50. In this regime the qubit's energy levels become exponentially less sensitive to offset charge, strongly suppressing charge-noise dephasing.

The protection has a cost. Increasing $E_J/E_C$ reduces anharmonicity only by a power law, leaving the transmon as a weakly anharmonic oscillator with several physically relevant levels. Typical devices retain enough anharmonicity—often roughly 100–300 MHz in magnitude—to select the computational transition, but fast pulses can still leak into $|2\rangle$.

The transmon is therefore an engineering compromise rather than a perfectly protected two-level system. Its large capacitance trades some spectral separation for a much larger reduction in charge sensitivity. Control methods such as [[DRAG Pulse Control]] address the remaining leakage, while split-junction variants add the tunability described in [[Split-Transmon Flux Tunability]].

# References

[[2021 - A Quantum Engineers Guide to Superconducting Qubits.pdf]]
