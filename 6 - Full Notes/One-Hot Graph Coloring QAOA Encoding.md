2026-10-17 17:30

Status: #baby

Tags: [[Constraint-Preserving QAOA]]

# One-Hot Graph Coloring QAOA Encoding

For a graph with $n$ vertices and $\kappa$ colors, a one-hot encoding assigns bit $x_{u,j}$ to “vertex $u$ has color $j$.” Each vertex must satisfy

$$
\sum_{j=1}^{\kappa}x_{u,j}=1,
$$

so the representation uses $n\kappa$ qubits and excludes both uncolored and multiply colored vertices.

The Max-$\kappa$-colorable-subgraph objective rewards edges whose endpoints take different colors. Rather than penalizing invalid one-hot rows, an [[XY Mixer for One-Hot Constraints]] swaps the active color within each vertex register while preserving Hamming weight one.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

