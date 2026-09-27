2026-09-06 20:34

Status: #baby

Tags: [[Entity Framework Core Data Modeling]] [[Entity Framework Core Data Access]]

# Entity Framework Core Entity

An Entity Framework Core entity is a typed class representing persistent, code-driven data in an application model. Its properties describe stored values, keys, and navigation relationships that the mapper associates with database structures.

Entity classes let a controller work with domain objects instead of raw rows. They should not automatically become the public API shape; a [[Data Transfer Object]] can expose only the values that a client needs.

Entity properties can be scalar values mapped to columns or navigation properties representing relationships. A reference navigation points to one related entity, while a collection navigation represents multiple related entities.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[aspnetcore3andangular9_3ed.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]
