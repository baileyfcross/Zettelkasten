2026-10-12 18:44

Status: #baby

Tags: [[Quantum Dropout Regularization]]

# Single-Gate Quantum Dropout

Single-gate quantum dropout removes one eligible operation without also deleting a connected gate group. Rotation dropout replaces a selected parameterized one-qubit rotation with the identity. Entangling dropout instead removes a selected entangling operation while leaving the rotations in place.

The paper treats rotation dropout as a direct way to keep particular trainable rotations from becoming indispensable. Entangling dropout is included as a special case of the general framework, but the authors argue that it can resemble randomized pruning more than classical dropout: removing an entangler deletes a connection rather than a computational unit, and fixed CNOT entanglers give all such connections equal weight.

This distinction becomes especially important when the entangling gates are themselves parameterized, because removing one then suppresses a trainable parameter directly. The two single-gate variants also serve as simpler baselines for the grouped [[Canonical Quantum Dropout]] and separately controlled [[Independent Quantum Dropout]] strategies.

# References

[[2023 - A General Approach to Dropout in Quantum Neural Networks.pdf]]
