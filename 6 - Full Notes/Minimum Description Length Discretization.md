2026-09-17 09:48

Status: #baby

Tags: [[Big Data Preprocessing]]

# Minimum Description Length Discretization

Minimum description length discretization chooses interval boundaries by balancing the complexity of the discretized representation against how well it explains the data. A split is worthwhile when the added structure produces a shorter combined description.

The source uses an MDL-based discretizer as a case for parallel preprocessing. Distributing candidate evaluation makes the criterion usable when a single-machine scan would be too slow.

# References

[[frontiersofdatascience.pdf]]
