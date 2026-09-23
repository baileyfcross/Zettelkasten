2026-09-22 20:53

Status: #baby

Tags: [[CQRS Query and Read Model Design]]

# CQRS with One Database

CQRS with one database separates command and query code paths while both use the same physical store. The command side uses the [[Repository Pattern]] to load and persist aggregates; the query side bypasses those repositories and retrieves [[Read Model]]s efficiently from the existing data. This provides conceptual and implementation separation before adding distributed storage. If scale or shape differences later justify separate stores, the established [[Command Query Responsibility Segregation]] boundary makes that change more deliberate.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
