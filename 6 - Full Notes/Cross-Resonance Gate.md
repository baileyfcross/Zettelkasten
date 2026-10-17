2026-10-17 03:20

Status: #baby

Tags: [[Superconducting Qubit Engineering]]

# Cross-Resonance Gate

The cross-resonance gate couples fixed-frequency transmons and drives the control qubit at the target qubit's transition frequency. Because the qubits are always coupled and weakly anharmonic, this off-resonant drive produces a target rotation whose direction depends on the control state, yielding an effective $ZX$ interaction.

The raw driven Hamiltonian also contains unwanted single-qubit and two-qubit terms, including Stark shifts and unconditional target rotations. Echo sequences reverse selected contributions, while calibrated cancellation tones and frame updates suppress the remaining errors. These refinements convert the conditional rotation into a CNOT-equivalent entangling operation.

Cross resonance avoids flux-tuning qubits through crowded frequency regions, but it trades that benefit for longer gates, microwave crosstalk, and residual always-on interaction. Gate speed and fidelity depend on detuning, coupling strength, anharmonicity, drive amplitude, and fabrication variation, so fixed-frequency operation does not eliminate frequency-allocation constraints.

# References

[[2021 - A Quantum Engineers Guide to Superconducting Qubits.pdf]]
