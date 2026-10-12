2026-09-16 00:09

Status: #baby

Tags: [[Predictive Data Partitioning]]

# Partition Index Vector

A partition index vector records which rows belong to training, validation, or test subsets. Saving the indices makes the split auditable and permits identical partitions across competing models.

Indices should remain aligned with stable record identifiers so row reordering cannot silently change membership.

# References

[[essentialsofdatascience.pdf]]

