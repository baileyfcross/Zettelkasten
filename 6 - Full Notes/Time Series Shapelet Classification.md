2026-09-14 21:00

Status: #baby

Tags: [[Sequence and Network Classification]] · [[Time-Series Feature Engineering]]

# Time Series Shapelet Classification

Time series shapelet classification uses short subsequences whose presence or close match is highly discriminative of a class. A candidate shapelet is compared with every possible window in a series, and the minimum distance becomes a feature or split criterion.

Shapelets provide localized explanations because the prediction can identify the characteristic segment. Searching the enormous space of possible subsequences requires pruning, sampling, or other acceleration.

The minimum distance from a candidate shapelet to all same-length windows in a series can become a derived feature. A shapelet transform therefore converts variable temporal structure into a conventional tabular representation while preserving a discriminative local form.

# References

[[dataclassification.pdf]]

[[featureengineeringformachinelearninganddataanalytics.pdf]]
