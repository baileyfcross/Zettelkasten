2026-10-15 00:14

Status: #baby

Tags: [[Quantum Computing for High-Energy Physics]]

# Hamiltonian Escape from the Lattice Sign Problem

Euclidean path-integral Monte Carlo becomes inefficient when its statistical weights acquire rapidly oscillating phases. In lattice field theory this sign problem appears in real-time evolution, finite fermion density, and theories with topological terms; cancellations then make the sampling cost grow exponentially with lattice size.

The Hamiltonian formulation changes the computational representation. It evolves a many-body state directly and therefore does not estimate an oscillatory path integral. A quantum computer can encode the tensor-product Hilbert space using a number of qubits that grows linearly with the number of discretized degrees of freedom, whereas explicitly storing a general state vector on a classical computer grows exponentially.

Avoiding the sign problem does not make the calculation easy. The field variables must still be truncated and encoded, a physical initial state must be prepared, the evolution must fit within available depth, and observables must be measured accurately. The opportunity is therefore a change in the dominant obstacle, not a guarantee of practical advantage. [[Quantum Lattice Gauge Theory Dimension Roadmap]] organizes increasingly realistic tests of that opportunity.

# References

[[2023 - Quantum Computing for High-Energy Physics State of the Art and Challenges Summary of the QC4HEP Working Group.pdf]]
