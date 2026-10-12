2026-10-04 22:20

Status: #baby

Tags: [[R Data Transformation and Reshaping]]

# R Vector Membership Test

An R vector membership test asks, for each element of one object, whether it occurs in another set of values. It produces a logical vector suitable for filtering or validation and differs from equality comparison because the candidate may match any member of the reference set.

Membership is especially useful for retaining approved categories or finding unexpected codes during [[R Data Frame Subsetting]]. Missing values and mismatched types should be handled deliberately so that apparent nonmembership is not merely a coercion artifact.

# References

[[rprimer.pdf]]
