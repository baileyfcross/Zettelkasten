2026-11-06 12:32

Status: #baby

Tags: [[Kubernetes Service Networking and Traffic]]

# Cilium Hubble Network Observability

Cilium Hubble network observability uses eBPF-derived flow data to show Kubernetes communication at network and application layers. Cilium associates a connection with workload labels and service identities rather than relying on an ephemeral Pod IP, while Hubble exposes flows, drops, request rates, latency, and service relationships through command-line, relay, user-interface, and metrics paths.

Its service map complements a trace-derived map. Network observation can include DNS, TCP, Kafka, OpenSearch, external endpoints, and failed paths that never produced a complete span, while a [[Distributed Request Trace]] remains better for following one instrumented transaction. Operators can use Hubble to locate the failing segment and then drill into traces or packet-level tools for detail.

The same evidence helps validate a [[Kubernetes Network Policy]]. A Layer 3 or Layer 4 denial appears as a dropped connection, while a Layer 7 rule can surface as an HTTP error or timeout; correlating that result with workload identity prevents an application symptom from being mistaken for an unexplained service failure.

# References

[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
