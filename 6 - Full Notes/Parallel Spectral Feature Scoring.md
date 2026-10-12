2026-10-07 00:46

Status: #baby

Tags: [[Parallel Spectral Feature Selection]]

# Parallel Spectral Feature Scoring

Parallel spectral feature scoring decomposes each feature's graph-based quadratic forms across sample partitions. Workers compute degree-weighted norms, centered sums, and partial matrix-vector products; reductions assemble the scalars or vectors needed for the final score.

Combining normalization and scoring avoids extra transfers between workers and the coordinator. The difficult term is often $f^TSf$, because each partition of a feature must interact with the distributed similarity matrix. Collective reduction and scatter operations can compute it without centralizing the original data.

# References

[[spectralfeatureselectionfordatamining.pdf]]

