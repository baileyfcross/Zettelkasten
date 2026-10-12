2026-09-22 20:53

Status: #baby

Tags: [[CQRS Query and Read Model Design]]

# Read-to-Write Mismatch

Read-to-write mismatch occurs when one representation and storage design cannot serve state changes and information retrieval equally well. Write models favor short transactions and invariant protection, while screens and reports may need joins, indexes, or fields drawn from several [[Aggregate]]s. Optimizing one side can degrade the other. [[Command Query Responsibility Segregation]] accepts this asymmetry by allowing the [[CQRS Command Model]] and [[CQRS Query Model]] to use different shapes without requiring separate databases immediately.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
