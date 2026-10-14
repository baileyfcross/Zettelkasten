2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Cluster Architecture and Resources]]

# Kubernetes API Server

The Kubernetes API server is the control plane's authenticated and authorized entry point. It validates resource requests, applies admission controls, exposes watches, and persists accepted desired state in the [[etcd Cluster State Store]].

Cluster tools and controllers coordinate through this API rather than by editing one another's data directly. That makes API availability, certificates, audit policy, and request authorization central to the reliability and security of every cluster operation.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

