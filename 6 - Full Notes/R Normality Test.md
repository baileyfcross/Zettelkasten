2026-10-04 22:20

Status: #baby

Tags: [[R Statistical Testing and Model Validation]]

# R Normality Test

An R normality test compares a sample with a normal distribution through statistics such as Shapiro-Wilk or Anderson-Darling. A small p-value supplies evidence against normality, but a large p-value does not prove the distribution normal, especially when the sample is too small to reveal relevant departures.

Formal testing should be paired with a [[Quantile-Quantile Plot]]. In a model, the relevant object is commonly the residual distribution rather than the raw response, and practical consequences depend on the inferential procedure being protected.

# References

[[rprimer.pdf]]
