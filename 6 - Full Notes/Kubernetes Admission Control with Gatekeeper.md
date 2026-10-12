2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Policy and Runtime Security]]

# Kubernetes Admission Control with Gatekeeper

Gatekeeper integrates OPA policy with Kubernetes admission. It observes constraint definitions and asks a validating admission webhook to evaluate incoming resource requests before the API server persists them.

Admission policy can require labels, approved registries, non-privileged security contexts, or other properties that RBAC cannot express. Webhook availability, audit mode, exemptions, rollout sequencing, and a tested recovery path matter because a faulty policy can block both applications and the administrators trying to repair them.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

