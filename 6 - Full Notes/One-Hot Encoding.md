2026-09-16 01:05

Status: #baby

Tags: [[Feature Engineering Foundations]]

# One-Hot Encoding

One-hot encoding converts a categorical feature into a collection of binary indicators, one for each category. Exactly one indicator is active for an ordinary single-valued category, so the representation preserves identity without imposing an artificial numerical order.

The method increases dimensionality, especially for high-cardinality features. It is appropriate when an algorithm needs numerical vectors, but the expanded representation may require sparse storage or feature selection.

# References

[[featureengineeringformachinelearninganddataanalytics.pdf]]
