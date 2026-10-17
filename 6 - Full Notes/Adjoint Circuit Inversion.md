2026-10-16 23:00

Status: #baby

Tags: [[Quantum Invertible Generative Models]]

# Adjoint Circuit Inversion

A unitary circuit $U=U_L\cdots U_1$ is inverted by applying the adjoints of its layers in reverse order:

$$U^\dagger=U_1^\dagger\cdots U_L^\dagger.$$

For the hardware-efficient QINN ansatz, a three-angle rotation is inverted by negating and reversing its angles, while a CNOT gate is its own inverse. The variational part of the model is consequently reversible without imposing the triangular coupling architecture used by a classical INN.

Circuit reversibility does not by itself make the complete classical-to-classical model invertible. The expectation measurement after $U$ discards state information, producing the separate [[Quantum Measurement Inversion Problem]].

# References

[[2023 - Generative Invertible Quantum Neural Networks.pdf]]

