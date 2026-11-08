2026-09-22 20:53

Status: #baby

Tags: [[CQRS Query and Read Model Design]]

# CQRS with One Database

CQRS with one database separates command and query code paths while both use the same physical store. The command side uses the [[Repository Pattern]] to load and persist aggregates; the query side bypasses those repositories and retrieves [[Read Model]]s efficiently from the existing data. This provides conceptual and implementation separation before adding distributed storage. If scale or shape differences later justify separate stores, the established [[Command Query Responsibility Segregation]] boundary makes that change more deliberate.

The Micronaut source depicts one data store containing both a write model and a read model. Commands pass through validation, domain logic, and persistence, while queries generate consumer-oriented data-transfer objects from the read side. The separation therefore begins with responsibility and model shape; a second physical store is an optional escalation for workloads that justify its synchronization cost.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]

[[prorestfulapiswithmicronaut.epub]]
