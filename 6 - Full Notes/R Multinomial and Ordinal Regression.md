2026-10-04 22:20

Status: #baby

Tags: [[R Regression and Longitudinal Modeling]]

# R Multinomial and Ordinal Regression

R multinomial regression models an unordered outcome with more than two categories by comparing category-specific log odds with a reference category. Ordinal regression instead uses the known category order and models cumulative probabilities, commonly under a proportional-odds structure.

The two models answer different questions even when their labels look similar. An ordinal fit gains parsimony from the ordering assumption, so that assumption and the direction of the factor levels must be checked before interpreting coefficients.

# References

[[rprimer.pdf]]
