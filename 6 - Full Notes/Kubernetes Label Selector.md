2026-09-27 22:21

Status: #baby

Tags: [[Azure Kubernetes Service Operations]]

# Kubernetes Label Selector

A Kubernetes label selector identifies objects by key-value labels rather than by unstable instance names or addresses. A [[Kubernetes Deployment]] uses a selector to recognize the pods it manages, and a [[Kubernetes Service]] uses one to choose the pods that receive traffic.

The label applied by a pod template must match the controller and service selectors that depend on it. This loose coupling allows replicas to appear and disappear while retaining the same logical role. A mismatched label can leave healthy pods unmanaged or unreachable even when their containers are running correctly.

# References

[[clouddevopsengineersguide.pdf]]

