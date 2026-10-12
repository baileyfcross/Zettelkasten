2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Policy and Runtime Security]]

# Kubernetes Container Least Privilege

Container least privilege removes authority that an application does not need: root identity, added Linux capabilities, privilege escalation, writable system paths, host mounts, and unrestricted network access. Kubernetes security contexts express several of these requirements in the pod specification.

The objective is to reduce what a compromised process can reach, not to assume the container boundary is absolute. Admission controls can reject unsafe declarations, while runtime enforcement and node hardening constrain behavior that static configuration alone cannot predict.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

