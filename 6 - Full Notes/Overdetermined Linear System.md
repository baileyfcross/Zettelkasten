2026-09-06 19:44

Status: #baby

Tags: [[Linear System Structure]] · [[R Matrix Systems and Scientific Models]]

# Overdetermined Linear System

An overdetermined linear system has more equations than unknowns. Measurement data commonly produce such systems, and an exact solution may not exist.

A [[Least Squares Approximation]] chooses the vector whose predicted right-hand side is closest to the observed one, using a [[Normal Equation]], [[QR Decomposition]], or [[Singular Value Decomposition]].

The Old Faithful example in the student companion treats many observed eruption pairs as more equations than the two line parameters can satisfy exactly. The least-squares system selects the intercept and slope that minimize their collective prediction error.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[rstudentcompanion.pdf]]
