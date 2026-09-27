2026-09-27 11:39

Status: #baby

Tags: [[Software Quality Attributes and Architecture Tradeoffs]]

# Response Time Requirement

A response time requirement states how long a user or client may wait for a specified operation to produce an observable result. The target should name the operation, workload, percentile or tolerance, and environment in which it will be measured.

Separating this requirement from implementation allows alternative improvements—query design, caching, asynchronous work, or additional capacity—to be evaluated against the same outcome.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
