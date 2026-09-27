2026-09-27 00:11

Status: #baby

Tags: [[.NET Distributed Memory and Message Passing]]

# Torus Network Topology

A torus topology adds wraparound links to a ring or multidimensional mesh, so nodes at opposite edges become neighbors. The extra connections reduce maximum path length and remove the special boundary behavior of an open mesh.

Routing must account for multiple directions and possible contention around each dimension. The regular structure suits grid-shaped parallel computations, but additional links increase implementation cost and do not eliminate congestion from an imbalanced communication pattern.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
