2026-09-13 10:25

Status: #baby

Tags: [[Outlier Detection and DBSCAN]]

# Mahalanobis Distance

Mahalanobis distance measures multivariate separation after accounting for the variance and covariance among attributes. It scales a difference vector by the inverse covariance matrix rather than treating every direction as equally variable.

Squared distance from the mean has a chi-square relationship under multivariate normal assumptions. Outliers can distort both the mean and covariance used in the calculation.

When direct covariance estimation is unreliable because the sample is small, external feature-similarity knowledge can supply an alternative covariance model. A commute-time embedding of a feature graph can be converted into that covariance and then used to derive sample similarities, making the distance a bridge from feature knowledge to [[Multi-Source Spectral Feature Selection]].

# References

[[clusteranalysisanddatamining.pdf]]

[[spectralfeatureselectionfordatamining.pdf]]
