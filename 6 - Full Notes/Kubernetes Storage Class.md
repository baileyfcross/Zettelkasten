2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Cluster Architecture and Resources]]

# Kubernetes Storage Class

A Kubernetes StorageClass describes a class of storage that a provisioner can create for a PersistentVolumeClaim. It can encode the driver, performance or topology parameters, reclaim policy, binding behavior, and expansion capability behind an application-facing request.

Dynamic provisioning separates an application's claim from provider-specific volume creation, but the class remains an operational contract. A restore into another cluster succeeds only if a compatible class and driver exist or the manifests are deliberately mapped to alternatives.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

