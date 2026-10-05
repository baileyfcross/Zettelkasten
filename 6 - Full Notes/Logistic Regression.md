2026-09-06 18:44

Status: #baby

Tags: [[Logistic Regression Analysis]] · [[R Regression and Longitudinal Modeling]]

# Logistic Regression

Logistic regression models the probability of a binary outcome by expressing its log odds as a linear combination of predictors. It keeps fitted probabilities within the interval from zero to one while allowing adjustment for several covariates.

The raw coefficients are [[Log Odds|log-odds]] changes. Health research commonly exponentiates them into [[Odds Ratio|odds ratios]], which compare the odds of the outcome with those in a defined reference group.

The R fit is specified as a generalized linear model with a binomial family. Its summary reports log-odds coefficients and Wald tests; exponentiating an estimate and its confidence limits converts that result to the odds-ratio scale, while nested model comparisons can test the contribution of terms without dropping required lower-order components.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[rprimer.pdf]]
