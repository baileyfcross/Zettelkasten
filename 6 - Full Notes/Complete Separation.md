2026-09-06 18:44

Status: #baby

Tags: [[Logistic Regression Analysis]]

# Complete Separation

Complete separation occurs in logistic regression when a predictor or combination of predictors perfectly divides observations with and without the outcome. Ordinary maximum-likelihood coefficients then move toward infinite magnitude and the model may fail to converge.

The pattern reflects strong sample separation but does not yield a usable conventional estimate. Penalized approaches such as [[Firth Logistic Regression]] can produce finite coefficients, while the data and coding should also be checked for sparse or deterministic categories.

# References

[[analyzinghealthdatainrforsasusers.pdf]]
