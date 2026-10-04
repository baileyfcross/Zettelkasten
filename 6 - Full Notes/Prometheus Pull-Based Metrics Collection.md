2026-09-27 22:21

Status: #baby

Tags: [[Cloud-Native Observability]]

# Prometheus Pull-Based Metrics Collection

Prometheus collects time-series metrics by periodically scraping configured HTTP endpoints, commonly `/metrics`. The application exposes current measurements, and Prometheus pulls them on a schedule into its time-series store rather than requiring every service to push observations independently.

Scrape configuration identifies targets and intervals, while labels make related series distinguishable. The pull model works well for numeric health signals such as latency, throughput, resource use, and error counts. A compatible managed store such as [[Amazon Managed Service for Prometheus]] can preserve the same collection and query model while operating the scalable backend.

Prometheus also evaluates alerting rules and forwards notifications to Alertmanager for grouping, inhibition, silencing, and routing. Its local time-series store can integrate with remote storage, and its labeled multidimensional model makes historical trends and real-time health queries accessible through PromQL.

# References

[[clouddevopsengineersguide.pdf]]

[[observabilityintheai-nativeera.pdf]]
