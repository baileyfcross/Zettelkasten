2026-10-07 00:46

Status: #baby

Tags: [[Parallel Spectral Feature Selection]]

# Distributed Active-Set Optimization

Distributed active-set optimization keeps a small candidate model centrally while using workers to test it against a much larger collection of variables. Local partitions calculate correlations and Gram-matrix contributions; collective reductions provide the coordinator with the statistics needed to add variables or certify optimality.

The approach is efficient when the active set is much smaller than the complete feature set. It reduces repeated full-model optimization, but global scans of inactive features can still dominate communication if residual correlations are exchanged too often.

# References

[[spectralfeatureselectionfordatamining.pdf]]

