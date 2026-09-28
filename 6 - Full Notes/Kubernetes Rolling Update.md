2026-09-27 22:21

Status: #baby

Tags: [[Azure Kubernetes Service Operations]]

# Kubernetes Rolling Update

A Kubernetes rolling update replaces replicas of a [[Kubernetes Deployment]] gradually so a new container image can enter service while older healthy replicas continue handling requests. Rollout status exposes progress, and the deployment controller keeps the transition aligned with the declared workload state.

Availability depends on more than replacement order. Readiness checks should keep an unready new pod out of the [[Kubernetes Service]], and resource settings must allow old and new replicas to overlap. If the release is unhealthy, rollout history supports undoing it to the previous deployment revision.

# References

[[clouddevopsengineersguide.pdf]]

