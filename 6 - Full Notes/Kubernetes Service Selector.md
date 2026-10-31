2026-10-30 17:24

Status: #baby

Tags: [[Kubernetes Service Networking and Traffic]]

# Kubernetes Service Selector

A Kubernetes Service selector is a label query that connects a stable Service to the pods eligible to receive its traffic. Deployment-managed pods can be replaced or replicated while retaining the labels that place them behind the same endpoint.

Selector and pod labels form a runtime contract. A mismatch leaves the Service with no endpoints even when the application pods are healthy, while an overly broad selector can route traffic to an unintended workload.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

