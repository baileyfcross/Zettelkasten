2026-09-22 20:53

Status: #baby

Tags: [[Aggregate Consistency and Persistence]]

# Aggregate

An aggregate is a cluster of domain objects treated as one unit for atomicity and consistency. Child entities cannot meaningfully exist independently of the composition, and all changes enter through an [[Aggregate Root]]. The aggregate protects rules spanning its parts and changes as a whole within one [[Transaction Boundary]]. It should be the smallest structure that can preserve the required [[Aggregate Invariant]]s; unrelated concepts belong in other aggregates and are coordinated outside the transaction.

The DDD chapter treats an aggregate as an entity hierarchy reached through one aggregate root. External operations pass through that root so invariants and the transaction boundary are not bypassed by direct modification of internal parts.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[hands-ondomain-drivendesignwithnetcore.pdf]]
