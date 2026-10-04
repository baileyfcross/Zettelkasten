2026-10-03 17:11

Status: #baby

Tags: [[Self-Service Observability Platforms]]

# Kustomize Metadata Injection

Kustomize metadata injection applies labels or annotations to selected Kubernetes resources through declarative transformers. The rule lives with the configuration and can modify a directory of manifests consistently without copying the same metadata into every object.

A platform team can use this mechanism to attach ownership, environment, priority, or routing context needed by the observability system. Centralized transformation reduces deployment failures and inconsistent telemetry caused by manual repetition.

# References

[[observabilityintheai-nativeera.pdf]]
