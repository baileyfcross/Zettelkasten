2026-09-06 18:44

Status: #baby

Tags: [[Survival and Time-to-Event Analysis]] · [[R Multivariate Resampling and Survival Modeling]]

# Kaplan-Meier Estimator

The Kaplan–Meier estimator calculates survival as the product of conditional event-free proportions at observed event times. It is nonparametric because it does not assume a particular distribution for event times.

The estimator incorporates right-censored observations through the changing risk set. Stratified Kaplan–Meier curves provide descriptive group comparisons, while tests or regression are needed for formal inference and confounder adjustment.

In R, observed time and event status are combined into a survival response and supplied to a formula-based fit. The event coding must be verified because the status indicator distinguishes failures from right-censored observations; reversing it changes the risk-set calculation and the resulting curve.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[rprimer.pdf]]
