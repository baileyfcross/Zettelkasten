2026-10-14 09:01

Status: #baby

Tags: [[Quantum Convolutional Neural Networks]]

# QCNN Ground-State Preparation Strategies

A [[Hidden Ground-State Feature Map]] requires a physical or simulated process that prepares a Hamiltonian's parameter-dependent ground state. The paper describes three routes: adiabatic evolution along a suitable Hamiltonian path, low-temperature preparation approximated by quantum imaginary-time evolution, and a preoptimized variational circuit.

For the cluster model, the variational route uses a Hamiltonian variational ansatz with alternating exponentials of the cluster interaction and transverse-field terms. With enough depth and separately optimized angles for each feature value, this QAOA-like construction can approximate or, for suitable integrable models, exactly prepare the desired ground states.

The preparation choice determines circuit depth, ancillary-qubit demands, and the quality of the resulting model. Imperfect ground-state preparation can make the otherwise smooth basis functions noisy near the critical point, so the embedding's apparent learning advantage must be evaluated together with its state-preparation cost.

# References

[[2023 - What can we learn from quantum convolutional neural networks.pdf]]
