2026-10-03 22:25

Status: #baby

Tags: [[Kubernetes Platform Infrastructure]]

# Kubernetes External Resource Control

Kubernetes external resource control represents cloud or infrastructure services as custom resources and assigns controllers to create and reconcile them. Crossplane-style providers and compositions can turn several low-level resources into a platform capability requested through one Kubernetes-native specification.

The design joins infrastructure and application workflows more tightly than an external infrastructure-as-code pipeline. That can improve discovery and self-service, but it also changes ownership, permissions, drift handling, and deletion semantics. The platform must decide whether resources are defined by users inside the platform or by infrastructure teams outside it and avoid letting both paths manage the same object ambiguously.

# References

[[platformengineeringforarchitects.pdf]]
