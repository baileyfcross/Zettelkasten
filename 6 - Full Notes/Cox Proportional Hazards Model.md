2026-09-06 18:44

Status: #baby

Tags: [[Survival and Time-to-Event Analysis]] · [[R Multivariate Resampling and Survival Modeling]]

# Cox Proportional Hazards Model

The Cox proportional hazards model relates predictors to an event hazard without specifying the baseline hazard's parametric shape. It is semiparametric: coefficients determine multiplicative hazard ratios while the baseline remains unspecified.

This flexibility avoids choosing a full event-time distribution, but the predictor effects are assumed to remain proportional over time. The [[Proportional Hazards Assumption]] must therefore be examined before the hazard ratios are accepted.

R expresses the survival response and covariates through a model formula, with exponentiated coefficients interpreted as hazard ratios. The primer also shows that covariates changing during follow-up require a start-stop representation in an [[R Time-Varying Cox Model]] rather than a single baseline row per subject.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[rprimer.pdf]]
