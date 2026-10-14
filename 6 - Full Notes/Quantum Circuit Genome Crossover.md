2026-10-12 18:49

Status: #baby

Tags: [[Genetic Quantum Circuit Optimization]]

# Quantum Circuit Genome Crossover

Quantum-circuit genome crossover recombines the gate grids of two parent circuits after padding unequal widths or depths with identity gates. GA4QCO can return both resulting children or retain only one, and provides three operators with different exploration and disruption behavior.

Single-point crossover splits both parents at one circuit-depth column and exchanges the resulting suffixes. Multi-point crossover uses several column boundaries, mixing more parental material but increasing the chance of breaking a useful sequence along a qubit wire. Both distribute the original grid contents across their children.

Blockwise crossover adds a row boundary to the column split, exchanging two-dimensional regions. This can separate the cells belonging to a multi-qubit gate, so the framework reconstructs the broken operation in each child. Reconstruction preserves valid executable circuits but can duplicate or otherwise change the aggregate parental gate information, making blockwise crossover a deliberately more disruptive search operator.

# References

[[2023 - GA4QCO Genetic Algorithm for Quantum Circuit Optimization.pdf]]
