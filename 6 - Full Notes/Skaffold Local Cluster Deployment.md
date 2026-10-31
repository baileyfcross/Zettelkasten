2026-10-30 17:24

Status: #baby

Tags: [[Continuous Integration and Delivery]]

# Skaffold Local Cluster Deployment

Skaffold local cluster deployment builds an image with the workstation's container tooling and applies configured Kubernetes manifests to a local cluster such as Minikube. The same workflow connects a source change to a running pod without a separate sequence of manual build and `kubectl` commands.

Local deployment is a feedback environment rather than proof of production readiness. A production profile can change registry, builder, values, or deployment mechanism while preserving the overall pipeline stages.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

