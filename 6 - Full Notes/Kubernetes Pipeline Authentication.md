2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Identity Access and Secrets]]

# Kubernetes Pipeline Authentication

A deployment pipeline needs a non-human identity whose credentials match its limited automation role. Short-lived tokens issued for a workload identity or a pipeline's external identity reduce the exposure created by copying long-lived service-account tokens or administrator kubeconfig files into CI secrets.

Authentication design should be paired with a narrow Role or ClusterRole, auditable subject naming, credential rotation, and environment separation. Using one permanent cluster-admin credential across pipelines removes attribution and turns compromise of any job into compromise of the platform.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

