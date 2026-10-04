2026-09-08 22:39

Status: #baby

Tags: [[Cloud Computing Foundations]]

# Service Level Agreement

A service level agreement is the contract between a service consumer and supplier that states the value the service is expected to deliver. Its terms describe matters such as scope, quality, availability, response, delivery time, and consequences when commitments are not met.

An SLA should express outcomes that matter to the consumer rather than exposing every internal infrastructure metric. More specific [[Service Level Objective]]s give the provider measurable targets that support the overall agreement.

The agreement is an external commitment and may define consequences when the promise is missed. This distinguishes it from an internal objective used to steer engineering. A useful chain therefore runs from a measured [[Service Level Indicator]], to a target SLO, to the subset of promises and remedies formalized in the SLA.

Internal SLOs can be more stringent or more technically specific than an SLA so they provide early warning before a contractual promise is breached. Incident analysis should therefore show which objective is threatened and whether that threat can propagate to the agreement's customer-facing commitment.

# References

[[cloudcomputing_mit.epub]]
[[clouddevopsengineersguide.pdf]]

[[observabilityintheai-nativeera.pdf]]
