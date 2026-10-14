2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Service Networking and Traffic]]

# Kubernetes Network Policy

A Kubernetes NetworkPolicy selects pods and declares permitted ingress, egress, or both. Peer selectors and IP blocks narrow communication, while port rules restrict the protocols and destinations available to the selected workloads.

Policy enforcement depends on a compatible network plugin, and an empty or missing rule has semantics that must be tested carefully. A useful design starts from intended application flows and incrementally establishes default-deny boundaries without accidentally blocking DNS, monitoring, or required control traffic.

Container hardening remains incomplete when every compromised pod can contact every peer. Namespace and pod selectors can express service-to-service boundaries, but policy tests must cover both required flows and prohibited paths because a valid manifest does not guarantee that the installed network plugin enforces it.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[kubernetes_anenterpriseguidethirdedition.pdf]]

