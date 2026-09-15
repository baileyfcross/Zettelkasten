2026-09-15 10:20

Status: #baby

Tags: [[Scalable Hierarchical Search]]

# Baire Longest-Common-Prefix Distance

The Baire distance compares digit or symbol sequences by the length of their longest common prefix. Two decimal values sharing three initial digits are closer in this distance than values sharing only one. With base b, a prefix of length k can be assigned distance b to the negative k; no shared first digit receives the largest distance.

This distance is ultrametric. The shared-prefix relation immediately defines nested groups, so clustering can follow the representation's digits rather than repeatedly computing all ordinary pairwise distances. Its meaning depends on the scaling and precision of the values being encoded.

# References

[[datasciencefoundations_geometry.pdf]]
