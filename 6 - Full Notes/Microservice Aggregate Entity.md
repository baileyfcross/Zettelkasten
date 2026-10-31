2026-10-30 17:24

Status: #baby

Tags: [[Microservice Boundaries and Data]]

# Microservice Aggregate Entity

A microservice aggregate entity represents a reusable domain model within the service's application core. Controllers, message listeners, repositories, and external clients interact around it rather than embedding the entity's business meaning in those adapters.

More complex processes may coordinate several aggregates through a service or process model. The aggregate remains owned by the microservice boundary even when different REST, GraphQL, persistence, or messaging adapters expose it.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

