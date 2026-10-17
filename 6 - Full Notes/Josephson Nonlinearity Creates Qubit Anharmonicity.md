2026-10-17 03:20

Status: #baby

Tags: [[Superconducting Qubit Engineering]]

# Josephson Nonlinearity Creates Qubit Anharmonicity

A linear LC oscillator has evenly spaced energy levels. A drive resonant with the ground-to-first-excited-state transition is therefore also resonant with transitions into higher levels, so the lowest two states cannot be addressed as an isolated computational subspace.

Replacing the linear inductance with a Josephson junction changes the potential energy from a parabola to a cosine. The resulting unequal level spacings create anharmonicity: the $|0\rangle\leftrightarrow|1\rangle$ transition can be driven selectively because it differs in frequency from $|1\rangle\leftrightarrow|2\rangle$. The junction therefore turns a superconducting resonator into an artificial atom whose spectrum is set by circuit parameters.

Anharmonicity is finite rather than absolute isolation. Short, spectrally broad pulses can still populate noncomputational levels, which is why [[DRAG Pulse Control]] is needed for fast gates. Qubit design must balance strong transition selectivity against sensitivity to environmental noise, as illustrated by the [[Transmon Charge-Noise and Anharmonicity Tradeoff]].

# References

[[2021 - A Quantum Engineers Guide to Superconducting Qubits.pdf]]
