2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# Measurement-Conditioned Quantum Denoising

Each QuDDPM reverse step couples the data register to ancillas initialized in $|0\rangle$, applies a parameterized unitary, measures the ancillas in the computational basis, and retains the normalized postmeasurement state of the data qubits.

Measurement is essential because denoising must be contractive: many noisy states must move toward a more concentrated target ensemble. A unitary acting only on the data register would preserve inner products and could not supply that contraction, whereas conditioning on an ancilla outcome yields a nonlinear state update while keeping each generated sample pure.

The paper imposes no required ancilla outcome. It collects whichever computational-basis result occurs and uses the corresponding postmeasurement data state as the input to the next denoising step.

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

