2026-09-14 20:21

Status: #baby

Tags: [[Linear Model Design and Contrasts]]

# Design Matrix

A design matrix places one experimental unit in each row and one modeled term in each column. Its entries encode the intercept, group indicators, continuous predictors, transformations, and interactions used to explain the outcome vector.

The matrix is both a mathematical and scientific specification. Choosing its columns determines which coefficients can be estimated and what each one means; R's `model.matrix` exposes the representation generated from a model formula.

# References

[[dataanalysisforthelifescienceswithr.pdf]]
