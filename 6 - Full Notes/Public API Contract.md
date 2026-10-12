2026-09-22 20:53

Status: #baby

Tags: [[Application Commands and Service Boundaries]]

# Public API Contract

A public API contract is the explicit data shape accepted or returned at an application boundary. In a web API, strongly typed request [[Data Transfer Object]]s collectively define what outside clients can send without exposing internal domain objects. Contracts favor serializable values and can be versioned independently of a [[Domain Model]]. The [[Application Layer]] converts them into domain-specific values or commands, making transport compatibility a deliberate boundary concern.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
