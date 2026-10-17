2026-10-17 17:30

Status: #baby

Tags: [[Constraint-Preserving QAOA]]

# Maximum Independent Set QAOA Encoding

Maximum independent set assigns one bit $x_u$ to each graph vertex, with $x_u=1$ meaning that $u$ is selected. Feasible strings never select adjacent vertices, and the objective maximizes set size:

$$
C(x)=\sum_{u\in V}x_u.
$$

The empty set $|0\cdots0\rangle$ is an easy feasible initial state. Instead of penalizing selected edges, a controlled mixer permits a vertex bit to rotate only when every neighboring vertex is currently unselected, so every reachable basis state remains independent.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

