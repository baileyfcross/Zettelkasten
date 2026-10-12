2026-10-12 02:08

Status: #baby

Tags: [[Quantum Convolutional Neural Networks]]

# QCNN Rydberg-Atom Implementation Estimate

The paper outlines a possible implementation of its exact cluster-state QCNN with neutral Rydberg atoms. Long-range blockade interactions supply controlled multi-qubit gates without routing them through chains of SWAP operations, while single-qubit rotations change the control basis needed by the circuit.

For input size (N) and depth (d), the stated resource count is linear in (N) for fixed depth, plus (4d) layers of parallel single-qubit rotations. Using assumed coupling strengths and a 200-microsecond coherence time limited by the Rydberg-state lifetime, the authors estimate that a depth-four circuit on roughly 100 qubits could be feasible.

This is a resource analysis, not an experimental realization reported by the paper. The estimate also omits potential improvements from pulse shaping and parallel multi-qubit operations, so it should be read as a platform-specific feasibility argument rather than measured performance.

# References

[[2019 - Quantum Convolutional Neural Networks.pdf]]
