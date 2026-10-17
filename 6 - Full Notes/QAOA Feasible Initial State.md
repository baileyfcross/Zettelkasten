2026-10-17 17:30

Status: #baby

Tags: [[Constraint-Preserving QAOA]]

# QAOA Feasible Initial State

Constraint-preserving QAOA must begin inside the feasible subspace because its mixer is designed to keep the state there, not to repair an invalid initialization. A simple option is one known classical feasible assignment; a broader option is a superposition over feasible assignments.

For one-hot coloring, all vertices assigned one color is easy to prepare, while a per-vertex W state covers all colors symmetrically. The W state may improve early exploration but costs additional entangling gates. On noisy hardware, that preparation depth must be balanced against the number and depth of later QAOA layers.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

