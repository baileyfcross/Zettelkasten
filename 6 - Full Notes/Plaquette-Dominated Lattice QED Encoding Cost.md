2026-10-15 00:14

Status: #baby

Tags: [[Quantum Computing for High-Energy Physics]]

# Plaquette-Dominated Lattice QED Encoding Cost

Encoding a quantum-link formulation of lattice QED turns each Hamiltonian term into a sum of Pauli strings. The mass, fermion-hopping, Wilson, electric, and magnetic plaquette terms scale differently with lattice size, spatial dimension, spinor components, and the finite dimension chosen for each truncated gauge field.

The plaquette term dominates this decomposition because it multiplies four link operators around each elementary loop. For a general logarithmic encoding, the report gives scaling proportional to $n_s d d_S^8$ in the gauge-field dimension $d_S$; perfectly representable logarithmic and linear encodings reduce the exponent to $d_S^4$. Even modest increases in local gauge resolution can therefore multiply the number of Pauli terms far more strongly than the other parts of the Hamiltonian.

A logarithmic encoding minimizes both qubit use and, in the favorable representable case, Pauli-string count, but a power-of-two local dimension can omit the zero electric-field eigenvalue and create an unphysical ground-state degeneracy. Resource selection must therefore balance circuit cost against faithful local spectra rather than minimizing qubits alone. This constraint qualifies the apparent scale of the [[Two-Plus-One-Dimensional QED Quantum Benchmark]].

# References

[[2023 - Quantum Computing for High-Energy Physics State of the Art and Challenges Summary of the QC4HEP Working Group.pdf]]
