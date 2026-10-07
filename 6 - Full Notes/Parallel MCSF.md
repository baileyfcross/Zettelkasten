2026-10-07 00:46

Status: #baby

Tags: [[Parallel Spectral Feature Selection]]

# Parallel MCSF

Parallel MCSF distributes the feature-score calculations of [[Matrix Comparison Spectral Feature Selection]]. The initial score $f^TSf$ is computed from partitions of the sample-similarity matrix, and later iterations update each score using correlations with the most recently selected feature.

This recurrence avoids storing or communicating a dense residual similarity matrix after every selection. The first similarity-based pass is usually the dominant cost; subsequent updates require only feature correlations and a global choice of the largest remaining score.

# References

[[spectralfeatureselectionfordatamining.pdf]]

