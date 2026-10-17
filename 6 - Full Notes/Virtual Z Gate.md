2026-10-17 03:20

Status: #baby

Tags: [[Superconducting Qubit Engineering]]

# Virtual Z Gate

A virtual $Z$ gate changes the phase reference used for subsequent microwave pulses instead of applying a separate physical pulse to the qubit. Because the phase of an $X$-$Y$ drive determines its rotation axis in the equatorial plane, shifting that phase is mathematically equivalent to rotating the qubit's control frame about $Z$.

The update is performed in the waveform generator or control software. It has effectively zero duration, introduces no additional physical exposure to decoherence, and is therefore nominally perfect apart from frame bookkeeping and calibration errors elsewhere in the sequence.

Virtual $Z$ operations make a physical $X_{\pi/2}$ pulse sufficient for arbitrary single-qubit gates when combined with phase updates. They also cancel deterministic single-qubit phases accumulated during two-qubit protocols such as [[CPHASE Gate through Noncomputational Levels]]. The technique is best understood as a reference-frame transformation whose consequences must be propagated through every later drive and measurement.

# References

[[2021 - A Quantum Engineers Guide to Superconducting Qubits.pdf]]
