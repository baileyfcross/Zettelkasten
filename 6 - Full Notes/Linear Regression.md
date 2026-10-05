2026-09-06 18:44

Status: #baby

Tags: [[Linear Regression Analysis]] · [[Linear Model Design and Contrasts]] · [[R Regression and Longitudinal Modeling]]

# Linear Regression

Linear regression models a continuous outcome as an intercept plus weighted contributions from one or more explanatory variables. Each coefficient describes the expected change in the outcome for a one-unit predictor change, holding the other modeled variables constant.

Valid interpretation depends on the variable coding, residual behavior, and study design. A statistically significant coefficient describes an adjusted association on the outcome scale; it does not by itself establish causation.

The source writes the full model as $Y=X\beta+\epsilon$, where the design matrix expresses the experimental comparison and least squares estimates the coefficient vector. This same formulation accommodates transformed predictors, several factors, and interaction terms without changing the core fitting principle.

Regression can describe an association or generate predictions, but both uses require checks of residual pattern, variance, influential observations, and the domain over which the fitted form is credible. Extrapolation beyond observed predictor values adds structural assumptions that a small in-sample error cannot validate.

In R, `lm` combines a formula and data frame to fit the model, and `summary` exposes coefficients, their standard errors and tests, residual summaries, and fit statistics. The formula can omit the intercept, include transformed variables, or add interactions, but those syntactic choices change the model and must be interpreted rather than treated as formatting.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]

[[researchmethodsforinformationsystems.pdf]]

[[rprimer.pdf]]
