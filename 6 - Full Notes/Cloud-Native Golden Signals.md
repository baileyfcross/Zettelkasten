2026-10-03 17:11

Status: #baby

Tags: [[Cloud-Native Reliability and Service Objectives]]

# Cloud-Native Golden Signals

Cloud-native golden signals are latency, traffic or throughput, errors, and saturation interpreted at each layer of a dynamic platform. They shift attention from isolated CPU and memory values toward whether a resource, orchestrator, workload, shared service, application, or business transaction can fulfill its role.

Automation changes what deserves an alert. A restarted Pod may be ordinary self-healing, while repeated failed restarts or rising scheduling latency indicate that the recovery mechanism is failing. The signal must therefore reflect the layer's responsibility and the behavior users depend on.

The networking case study applies the same reasoning to connectivity. Request rate, errors, and latency can be observed at Layer 7, while round-trip time, retransmission, and drops expose lower-layer failure. Cilium and Hubble associate those values with Kubernetes service identity, making it possible to correlate a user-facing error with the workload and network segment that produced it.

# References

[[observabilityintheai-nativeera.pdf]]
[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
