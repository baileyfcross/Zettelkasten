2026-09-28 03:19

Status: #baby

Tags: [[Biomedical Image Analysis]]

# Seeded Region Growing

Seeded region growing starts from one or more locations known to lie inside a target and adds neighboring pixels or voxels that satisfy a similarity rule. The procedure turns a sparse detection into a connected region with an estimated boundary.

Its result depends on both the seed and the stopping criterion. A poor seed can grow into the wrong structure, while a permissive similarity threshold can leak across weak boundaries. Confidence-connected variants update region statistics as they grow, allowing the rule to adapt while still requiring spatial continuity.

# References

[[healthcaredataanalytics.pdf]]
