2026-10-04 22:20

Status: #baby

Tags: [[R Regression and Longitudinal Modeling]]

# R Generalized Linear Mixed Model

An R generalized linear mixed model extends generalized linear modeling to clustered non-normal outcomes by combining a response distribution and link function with random effects. It can model, for example, binary or count measurements repeated within subjects while allowing subject-specific heterogeneity.

Its coefficients are conditional on the random effects, which distinguishes their interpretation from the population-averaged effects of an [[R Generalized Estimating Equation]]. Approximation and convergence diagnostics matter because the likelihood integrates over the random-effects distribution.

# References

[[rprimer.pdf]]
