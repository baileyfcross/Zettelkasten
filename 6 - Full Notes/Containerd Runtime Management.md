2026-10-11 21:26

Status: #baby

Tags: [[Docker Runtime and Container Lifecycle]]

# Containerd Runtime Management

Containerd manages the higher-level runtime work surrounding an isolated process: image transfer and storage, container creation and supervision, and integration with storage and networking. It delegates the low-level creation and start operation to an OCI runtime such as runc.

Docker Engine adds user-facing APIs, network libraries, and plugin support above containerd, while Kubernetes can also use containerd through its runtime integration. Keeping these layers distinct helps locate a failure: an Engine API problem, an image or supervision problem in containerd, and an OCI process-creation problem are different operational conditions.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
