2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Identity Access and Secrets]]

# Kubernetes Secret Threat Model

A Kubernetes Secret separates sensitive values from an ordinary workload manifest, but base64 encoding is not encryption and broad API or node access can still reveal the material. Threats exist at rest in etcd or repositories, in transit to nodes and applications, and in process memory, files, logs, and environment variables during use.

Protection therefore combines encryption at rest, TLS, narrow RBAC, node security, controlled injection, rotation, and avoidance of plaintext Git history. An external manager can improve lifecycle control, but the workload ultimately needs some usable form of the secret and must protect that delivery path.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

