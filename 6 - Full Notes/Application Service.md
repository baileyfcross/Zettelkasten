2026-09-22 20:53

Status: #baby

Tags: [[Application Commands and Service Boundaries]]

# Application Service

An application service exposes operations that coordinate domain use cases without owning the business rules. It accepts [[Application Command]]s or explicit parameters, loads an [[Aggregate]] through the [[Repository Pattern]], calls the aggregate's behavior, and commits changes. It can group related operations behind one dependency where separate [[Command Handler]]s would be cumbersome. The service remains thin when decisions about validity and state transitions stay inside the domain model.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
