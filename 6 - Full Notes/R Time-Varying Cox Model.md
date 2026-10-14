2026-10-04 22:20

Status: #baby

Tags: [[R Multivariate Resampling and Survival Modeling]]

# R Time-Varying Cox Model

An R time-varying Cox model represents follow-up in start-stop intervals so a covariate may change value over time. Each row describes the covariate state during an interval and whether the event occurs at its end, while all intervals belonging to one subject remain connected by an identifier.

The data layout must not use information from after an interval to predict risk within it. Time-varying covariates extend the exposure history, whereas a time-varying coefficient addresses failure of the [[Proportional Hazards Assumption]] and is a different modification.

# References

[[rprimer.pdf]]
