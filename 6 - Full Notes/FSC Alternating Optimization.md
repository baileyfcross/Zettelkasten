2026-09-14 22:06

Status: #baby

Tags: [[C++ Specialized Clustering Implementations]]

# FSC Alternating Optimization

The FSC implementation initializes centers and memberships, then alternates dimension-weight, center, and fuzzy-membership updates. Each stage holds the other variables fixed while improving the shared objective until convergence or the iteration limit.

Because the joint problem is nonconvex, starting centers affect the final subspaces and partition. Repeated runs retain the solution with the lowest objective and summarize average performance.

# References

[[dataclusteringincplusplus.pdf]]

