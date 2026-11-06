2026-10-03 17:11

Status: #baby

Tags: [[Cloud-Native Reliability and Service Objectives]]

# SLO-Based Incident Prioritization

SLO-based incident prioritization ranks anomalies by whether they threaten a defined user or business objective. A technically abnormal queue or internal service can be lower priority when the critical transaction remains healthy, while a smaller deviation may require immediate response when it consumes a customer-facing error budget.

This approach asks whether customers are affected, revenue is at risk, or a contractual commitment is endangered. It reduces alert fatigue by connecting technical evidence to impact instead of treating every detected anomaly as equally urgent.

The legacy-systems source emphasizes that one transaction crosses layers with different responsibilities. Frontend objectives can use session and user-experience evidence, APIs need availability and latency, message systems need queue depth and subscriber lag, databases need errors and slow queries, and batch systems need completion status. Prioritization should connect these layer-specific objectives through the critical business path rather than force every component into one generic SLO template.

# References

[[observabilityintheai-nativeera.pdf]]
[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
