2026-10-04 22:20

Status: #baby

Tags: [[R Multivariate Resampling and Survival Modeling]]

# R Nonparametric Bootstrap

The R nonparametric bootstrap repeatedly samples observations with replacement from the empirical dataset and recalculates a statistic. The resulting distribution approximates sampling variability and can support bias estimates, standard errors, and confidence intervals when an analytic derivation is inconvenient.

The resampling unit must match the independence structure. Resampling individual rows from clustered or serially dependent data breaks that structure, and too few replicates add Monte Carlo noise to the estimated uncertainty.

# References

[[rprimer.pdf]]
