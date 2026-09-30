2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Service Networking and Traffic]]

# Kubernetes Network Policy

A Kubernetes NetworkPolicy selects pods and declares permitted ingress, egress, or both. Peer selectors and IP blocks narrow communication, while port rules restrict the protocols and destinations available to the selected workloads.

Policy enforcement depends on a compatible network plugin, and an empty or missing rule has semantics that must be tested carefully. A useful design starts from intended application flows and incrementally establishes default-deny boundaries without accidentally blocking DNS, monitoring, or required control traffic.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

