2026-09-22 20:53

Status: #baby

Tags: [[Aggregate Consistency and Persistence]]

# Transaction Boundary

A transaction boundary identifies the state changes that must succeed or fail together. In a domain-centered model, an [[Aggregate]] defines this boundary rather than allowing each controller or database routine to choose an arbitrary group of records. A command begins with a valid aggregate and must finish with either a valid new state or the original state. Keeping the boundary small reduces unrelated write conflicts and prevents one business operation from locking an excessive object graph.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
