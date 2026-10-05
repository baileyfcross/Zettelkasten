2026-10-04 22:20

Status: #baby

Tags: [[R Regression and Longitudinal Modeling]]

# R Generalized Estimating Equation

An R generalized estimating equation fits population-averaged regression effects for correlated responses. The analyst specifies a working correlation structure for observations within a cluster, while robust standard errors can remain useful even when that working structure is not exactly correct.

Cluster identifiers and observation order must reflect the study design. Unlike an [[R Generalized Linear Mixed Model]], the method does not use subject-specific random effects to explain the dependence and therefore answers a marginal rather than conditional question.

# References

[[rprimer.pdf]]
