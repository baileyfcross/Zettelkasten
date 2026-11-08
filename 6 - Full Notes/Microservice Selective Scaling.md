2026-10-30 17:24

Status: #baby

Tags: [[Microservice Testing Deployment and Scaling]]

# Microservice Selective Scaling

Microservice selective scaling changes the instance count or resources of one service according to its workload without scaling the whole application. A heavily used provider can gain replicas while unrelated services retain their current capacity.

This is one of the architectural benefits of independent deployment, but downstream databases, brokers, and partitions must support the added concurrency. Scaling only the visible bottleneck can shift saturation to another boundary.

Read-heavy and write-heavy paths can also scale orthogonally. In a high look-to-book workload, [[CQRS Independent Scaling]] can multiply query replicas without multiplying the authoritative write service to the same degree. Scaling writers is more difficult because concurrent instances can attempt to change the same entity and need a consistency mechanism such as [[Optimistic Concurrency]].

# References

[[javamicroservicesandcontainersinthecloud.epub]]
[[practicalmicroservicesarchitecturalpatterns.epub]]

