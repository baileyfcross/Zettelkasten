2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GenAI Deployment Architecture]]

# Kubernetes Model Inference Deployment

A Kubernetes model inference Deployment maintains replicated pods that load a trained model and answer real-time requests through a stable Service or Ingress. Resource limits, accelerator requests, readiness probes, and rollout strategy determine when a replica can safely receive traffic.

Model startup can be much slower than ordinary application startup because weights must be downloaded and loaded into accelerator memory. Readiness should reflect actual inference availability, while liveness should avoid repeatedly killing a healthy pod during a long initialization.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

