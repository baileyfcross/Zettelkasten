2026-10-03 17:11

Status: #baby

Tags: [[Observability Signals and Semantic Context]]

# Metric Cardinality and Privacy

A metric's cardinality is the number of distinct label combinations it can produce. Dimensions such as arbitrary usernames or IP addresses can create billions of series, making storage, querying, and anomaly detection expensive even when the metric itself is simple.

High-cardinality labels can also expose personal or confidential data to anyone with access to technical dashboards. Metric design should therefore use bounded, operationally meaningful dimensions and keep identity-level investigation in access-controlled signals better suited to that purpose.

# References

[[observabilityintheai-nativeera.pdf]]
