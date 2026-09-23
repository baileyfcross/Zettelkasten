2026-09-22 20:53

Status: #baby

Tags: [[Aggregate Consistency and Persistence]]

# Aggregate

An aggregate is a cluster of domain objects treated as one unit for atomicity and consistency. Child entities cannot meaningfully exist independently of the composition, and all changes enter through an [[Aggregate Root]]. The aggregate protects rules spanning its parts and changes as a whole within one [[Transaction Boundary]]. It should be the smallest structure that can preserve the required [[Aggregate Invariant]]s; unrelated concepts belong in other aggregates and are coordinated outside the transaction.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
