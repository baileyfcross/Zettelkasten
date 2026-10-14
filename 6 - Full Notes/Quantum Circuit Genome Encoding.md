2026-10-12 18:49

Status: #baby

Tags: [[Genetic Quantum Circuit Optimization]]

# Quantum Circuit Genome Encoding

A quantum circuit genome can encode an $n$-qubit circuit of depth $m$ as an $n \times m$ two-dimensional list. Rows identify qubit wires and columns identify gate positions, so changing the row or column count changes circuit width or depth within the same representation.

Each gate record stores its name, qubit identifier, affected qubits, optional rotation parameters, and control and target qubits. Parameters without a fixed value are initialized randomly in $[-\pi,\pi]$. This metadata lets an encoded individual be converted into an executable circuit while keeping the relationships belonging to controlled and other multi-qubit gates explicit.

Parents with different dimensions are padded with identity gates before recombination. The grid therefore supports variable-size evolution, but its operators must still treat a multi-qubit operation consistently across the cells that represent it; [[Quantum Circuit Genome Crossover]] and [[Quantum Circuit Genome Mutation]] supply those circuit-aware transformations.

# References

[[2023 - GA4QCO Genetic Algorithm for Quantum Circuit Optimization.pdf]]
