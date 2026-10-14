2026-10-14 17:55

Status: #baby

Tags: [[Variational Quantum Image Classification]]

# Variational FRQI State Preparation

Variational FRQI state preparation assigns each image its own parameterized quantum circuit. A classical optimizer starts from random angles and minimizes infidelity, $1-|\langle\widetilde\psi|\psi\rangle|^2$, between the circuit output and the target [[Flexible Representation of Quantum Images|FRQI state]].

Repeating a nearest-neighbor staircase ansatz gives depth linear in the number of qubits and layers rather than the exponentially deep worst case for exact arbitrary-state preparation. The method is approximate and its preprocessing is substantial: the study optimizes every image circuit classically for 10,000 Adam epochs. It therefore creates deployable quantum inputs without demonstrating an efficient end-to-end quantum loading process.

# References

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]
