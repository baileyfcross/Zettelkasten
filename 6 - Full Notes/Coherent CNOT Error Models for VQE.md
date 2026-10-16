2026-10-15 10:43

Status: #baby

Tags: [[Randomized Compiling and Zero-Noise Extrapolation]]

# Coherent CNOT Error Models for VQE

Four stationary coherent-error models expose different ways that imperfect CNOT gates can corrupt a deep VQE circuit. The models apply a small over-rotation after the intended gate, an unwanted $X$ rotation on the control qubit before the gate, an unwanted $Z$ rotation on the target qubit, or a parasitic $ZZ$ interaction between each CNOT qubit and its nearest neighbors.

The first three models isolate local calibration errors, while the fourth represents coherent crosstalk in a one-dimensional periodic layout. In the main simulations, single-qubit gates are ideal and relaxation and SPAM errors are omitted, allowing the comparison to focus on coherent two-qubit error near a $10^{-3}$ rate.

Despite their different generators, all four models produce the same qualitative result: [[RC-ZNE VQE Energy Error Reduction]] is much stronger than randomized compiling or zero-noise extrapolation alone. The range of models therefore tests mechanism-level robustness, not full hardware realism.

# References

[[2022 - Synergetic quantum error mitigation by randomized compiling and zero-noise extrapolation for the variational quantum eigensolver.pdf]]
