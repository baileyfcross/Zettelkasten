2026-10-11 21:34

Status: #baby

Tags: [[Kubernetes Cluster Architecture and Resources]]

# Kubernetes ReplicaSet

A Kubernetes ReplicaSet keeps a specified number of matching pod replicas running. Its selector identifies the pods it owns, and its pod template defines the replacement instances created when the observed count falls below the desired count.

ReplicaSets are normally managed through a [[Kubernetes Deployment]] rather than edited directly. Each Deployment revision can create a new ReplicaSet, allowing the controller to shift replicas between old and new pod templates during a rolling update and retain revision history for rollback.

The book places ReplicaSet between a Deployment's desired replica count and the replaceable microservice pods. When a pod disappears, the controller creates another from the template so instance loss does not reduce the declared capacity indefinitely.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
[[javamicroservicesandcontainersinthecloud.epub]]
