2026-10-11 21:34

Status: #baby

Tags: [[Kubernetes Cluster Architecture and Resources]]

# Kubernetes Readiness Probe

A Kubernetes readiness probe asks whether a pod should currently receive traffic. When it fails, the pod can remain running while its address is removed from matching Service endpoints, allowing startup, overload, or temporary dependency problems to be isolated without forcing a restart.

Readiness should represent the work the service promises to accept. A shallow process check can route traffic before initialization is complete, while a probe coupled to every optional dependency can unnecessarily remove otherwise useful capacity.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
