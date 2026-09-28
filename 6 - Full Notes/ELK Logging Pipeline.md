2026-09-27 22:21

Status: #baby

Tags: [[Cloud-Native Observability]]

# ELK Logging Pipeline

An ELK logging pipeline centralizes events through Elasticsearch, Logstash, and Kibana. Logstash ingests and transforms records, Elasticsearch indexes and stores them for search and aggregation, and Kibana provides queries and visualizations over the indexed data.

This pipeline replaces host-by-host log inspection when services and containers are distributed or short-lived. A transaction identifier and [[Structured Application Logging|structured fields]] let an operator reconstruct a failure across services, while infrastructure metrics can be correlated with the same time window to distinguish an application error from an exhausted dependency or network.

# References

[[clouddevopsengineersguide.pdf]]

