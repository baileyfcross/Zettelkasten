2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Identity Access and Secrets]]

# External Secrets Operator

External Secrets Operator reconciles Kubernetes custom resources with values held in an external secret manager. It authenticates to the provider, retrieves selected values, and materializes or refreshes Kubernetes Secrets according to a declared mapping.

The operator separates secret authority from application manifests and can support provider-side rotation. Its own credentials are consequently high value, and refresh intervals, deletion behavior, namespace scope, provider availability, and access to the generated Secret must all be governed.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

