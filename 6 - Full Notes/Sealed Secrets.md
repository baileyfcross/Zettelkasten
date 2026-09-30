2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Identity Access and Secrets]]

# Sealed Secrets

Sealed Secrets converts secret data into ciphertext that can be stored alongside deployment manifests. Only the controller holding the matching private key can decrypt the sealed object and create the ordinary Kubernetes Secret consumed by a workload.

This supports Git-based delivery without committing plaintext, but it shifts critical recovery responsibility to the controller key. Key backup, rotation, namespace or name scoping, RBAC around the resulting Secret, and review of who can submit sealed objects remain part of the design.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

