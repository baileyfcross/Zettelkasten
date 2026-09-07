2026-09-06 21:16

Status: #baby

Tags: [[Augmented Reality Software Architecture]]

# Distributed Scene Graph

A distributed scene graph shares a spatial object hierarchy across multiple processes or computers. Participants can render individual viewpoints or operate separate devices while referring to consistent object identities and transformations.

Updates must be communicated and ordered without assuming zero network delay. The design may replicate selected graph state near each renderer while defining which component owns authoritative changes.

# References

[[augmentedreality_pearson.pdf]]
