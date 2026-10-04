2026-10-03 22:25

Status: #baby

Tags: [[Platform Security and Software Supply Chain]]

# Platform Audit Log

A platform audit log records security-relevant actions with enough context to answer who did what, where, when, and with what result. Kubernetes API audit records, source-control changes, pipeline actions, registry access, and policy decisions together form evidence across the platform lifecycle.

Audit collection must omit credentials and protect sensitive personal information while preserving useful request context. Known user journeys can define anomalous patterns such as repeated denials, unusual clients, or impossible session locations. Alerts require tuning and human review because excessive false signals create fatigue and make genuine incidents easier to miss.

# References

[[platformengineeringforarchitects.pdf]]
