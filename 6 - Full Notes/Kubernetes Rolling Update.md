2026-09-27 22:21

Status: #baby

Tags: [[Azure Kubernetes Service Operations]]

# Kubernetes Rolling Update

A Kubernetes rolling update replaces replicas of a [[Kubernetes Deployment]] gradually so a new container image can enter service while older healthy replicas continue handling requests. Rollout status exposes progress, and the deployment controller keeps the transition aligned with the declared workload state.

Availability depends on more than replacement order. Readiness checks should keep an unready new pod out of the [[Kubernetes Service]], and resource settings must allow old and new replicas to overlap. If the release is unhealthy, rollout history supports undoing it to the previous deployment revision.

The `maxSurge` and `maxUnavailable` settings express the capacity and availability tradeoff during replacement. A rollout may be mechanically complete yet operationally unsafe if readiness is superficial, the new version is incompatible with shared data, or the cluster lacks room for overlapping replicas.

A zero-unavailable policy can combine maxUnavailable set to zero with temporary surge capacity, but the guarantee still depends on truthful readiness and adequate cluster resources. A Pod Disruption Budget can protect minimum capacity during voluntary disruptions, while graceful shutdown must let old Jakarta EE instances finish or transfer work before termination.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[clouddevopsengineersguide.pdf]]

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]

