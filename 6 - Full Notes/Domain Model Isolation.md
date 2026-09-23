2026-09-22 20:53

Status: #baby

Tags: [[Application Commands and Service Boundaries]]

# Domain Model Isolation

Domain model isolation keeps communication protocols, persistence libraries, serialization, and execution infrastructure outside the [[Domain Model]]. The model remains focused on business behavior and can be tested without a database, web server, or mocking of technical services. Interfaces for required [[Domain Service]]s may live inside the model while their implementations live outside it. This structure contains [[Accidental Complexity]] and prevents transport or storage constraints from defining the business rules.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
