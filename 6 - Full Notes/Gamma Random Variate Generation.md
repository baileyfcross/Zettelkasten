2026-10-07 17:18

Status: #baby

Tags: [[Pseudorandom Number Generation Methods]]

# Gamma Random Variate Generation

Gamma random variate generation transforms uniform values into samples from a gamma density. For shape parameters greater than one, the book develops a rejection construction by bounding a region related to the target density and accepting a ratio of uniform coordinates when it satisfies the density test.

A gamma generator also supplies chi-square values through a scale transformation, which in turn supports simulation from related $t$ and $F$ distributions. The method's validity depends on the acceptance region, while its efficiency depends on how tightly the proposal bounds the target.

# References

[[statisticalcomputingincplusplusandr.pdf]]
