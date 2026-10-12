2026-09-22 20:53

Status: #baby

Tags: [[Aggregate Consistency and Persistence]]

# Aggregate Root

An aggregate root is the parent entity and public entry point of an [[Aggregate]]. Outside code invokes behavior on the root rather than modifying child entities directly. The root coordinates state changes across its children, checks [[Aggregate Invariant]]s, and supplies the identity used to load or persist the aggregate. Hiding internal children prevents callers from creating partial updates that leave the aggregate's overall state inconsistent.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
