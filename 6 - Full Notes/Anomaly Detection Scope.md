2026-10-03 17:11

Status: #baby

Tags: [[AIOps Incident Intelligence]]

# Anomaly Detection Scope

Anomaly detection scope defines the entities, signals, dimensions, and time range over which abnormal behavior is evaluated. A narrow view of one endpoint can expose a local deviation, but it can also miss the dependency, neighboring workload, or external event that actually produced it.

Expanding scope increases both explanatory power and the risk of false associations. A useful detector narrows analysis with service context, topology, ownership, and business relevance so millions of possible data points do not become millions of independent alerts.

The legacy-systems source adds collection cost and recurrence to the scoping decision. Kernel events, traces, metrics, and profiles often need preprocessing, so it recommends targeting important services, resources with recurring failures, unresolved prior incidents, and newly configured components instead of continuously analyzing every host and event. On-demand windows and sampling can preserve useful evidence without making the detector itself an operational burden.

# References

[[observabilityintheai-nativeera.pdf]]
[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
