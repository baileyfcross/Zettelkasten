2026-10-04 22:20

Status: #baby

Tags: [[R Multivariate Resampling and Survival Modeling]]

# R Partial Least Squares Regression

R partial least squares regression constructs latent predictor components while using the response to guide their direction. This distinguishes it from [[R Principal Component Regression]], whose components are selected solely from predictor variation.

The number of latent components controls the model's complexity and should be selected with resampled prediction error. Loadings and scores can help describe the fitted representation, but interpretation must account for scaling and the fact that each component combines many original variables.

# References

[[rprimer.pdf]]
