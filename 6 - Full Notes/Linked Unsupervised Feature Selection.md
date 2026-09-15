2026-09-14 21:34

Status: #baby

Tags: [[Unsupervised Feature Selection for Clustering]]

# Linked Unsupervised Feature Selection

Linked unsupervised feature selection couples feature choice to both local data geometry and the global cluster structure inferred from that geometry. Rather than completing selection and clustering as isolated stages, it lets each refine the other.

The link can improve consistency between representation and partition, especially when labels are absent. It also creates a nonconvex joint problem whose outcome may depend on initialization, graph construction, and the relative weight placed on selection versus clustering.

# References

[[dataclustering.pdf]]

