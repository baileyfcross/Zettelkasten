2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Service Networking and Traffic]]

# Kubernetes Network Policy

A Kubernetes NetworkPolicy selects pods and declares permitted ingress, egress, or both. Peer selectors and IP blocks narrow communication, while port rules restrict the protocols and destinations available to the selected workloads.

Policy enforcement depends on a compatible network plugin, and an empty or missing rule has semantics that must be tested carefully. A useful design starts from intended application flows and incrementally establishes default-deny boundaries without accidentally blocking DNS, monitoring, or required control traffic.

Container hardening remains incomplete when every compromised pod can contact every peer. Namespace and pod selectors can express service-to-service boundaries, but policy tests must cover both required flows and prohibited paths because a valid manifest does not guarantee that the installed network plugin enforces it.

The Cilium case study turns enforcement into observable evidence. Label-selected Layer 3 and Layer 4 rules can produce explicit connection drops, while a Layer 7 restriction may appear to the caller as an HTTP error or timeout. [[Cilium Hubble Network Observability]] can show the source, destination, protocol, policy result, and failing segment so a deliberate denial is not misdiagnosed as an unexplained application outage.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[kubernetes_anenterpriseguidethirdedition.pdf]]

[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]

