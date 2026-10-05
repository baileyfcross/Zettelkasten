2026-10-04 22:20

Status: #baby

Tags: [[R Multivariate Resampling and Survival Modeling]]

# R Principal Component Regression

R principal component regression first replaces correlated predictors with a smaller set of principal-component scores and then regresses the response on those scores. The component construction ignores the response, so directions with high predictor variance are not guaranteed to be the most predictive.

The retained component count should be chosen by [[Cross-Validation]] rather than by in-sample fit alone. Centering and scaling affect the components and must be carried consistently into prediction for new observations.

# References

[[rprimer.pdf]]
