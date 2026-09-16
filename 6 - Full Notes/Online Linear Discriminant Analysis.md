2026-09-16 01:28

Status: #baby

Tags: [[Streaming Feature Engineering]]

# Online Linear Discriminant Analysis

Online linear discriminant analysis incrementally updates class-conditioned statistics and a discriminative projection as labeled observations arrive. It aims to preserve separation among classes without storing all earlier examples.

The representation must track both within-class and between-class structure. Small or evolving classes can make covariance estimates unstable, so regularization and adaptive updates are important.

# References

[[featureengineeringformachinelearninganddataanalytics.pdf]]
