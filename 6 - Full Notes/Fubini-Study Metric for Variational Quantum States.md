2026-10-17 14:21

Status: #baby

Tags: [[Natural-Gradient Optimization of Optical Quantum Circuits]]

# Fubini-Study Metric for Variational Quantum States

For a normalized parameterized state $|\psi_\theta\rangle$, the Fubini-Study metric measures the locally distinguishable change of the physical quantum state rather than the raw change of its amplitudes. Its real-coordinate components are

$$g_{ij}=\operatorname{Re}\langle\partial_i\psi|\partial_j\psi\rangle-\langle\partial_i\psi|\psi\rangle\langle\psi|\partial_j\psi\rangle.$$

The second term removes motion parallel to the state itself, including a change of global phase. The resulting tensor supplies the geometry used by a quantum natural gradient to rescale derivatives of an energy or fidelity loss.

Because the metric depends on the current circuit output, it can become singular where a parameter direction no longer changes the physical state. Metric-aware optimization must therefore handle redundancy as part of the update rule.

# References

[[2021 - Natural Gradient Optimization for Optical Quantum Circuits.pdf]]

