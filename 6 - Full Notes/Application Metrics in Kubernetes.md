2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Monitoring and Log Operations]]

# Application Metrics in Kubernetes

Application metrics expose behavior that node and container measurements cannot infer, such as request counts, latency distributions, queue depth, domain failures, and completed business work. A Prometheus-compatible endpoint lets the cluster monitoring system discover and scrape those measurements.

Metric names and labels form a long-lived interface. Labels should describe useful bounded dimensions rather than individual users or requests, and service objectives should determine which measurements become alerts instead of collecting every available value without an operational question.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

