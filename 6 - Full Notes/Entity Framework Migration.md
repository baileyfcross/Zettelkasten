2026-09-06 20:34

Status: #baby

Tags: [[Entity Framework Core Data Modeling]] [[ASP.NET Core Service Layers and Mapping]]

# Entity Framework Migration

An Entity Framework migration records a change between versions of a code-first data model and expresses the database operations needed to apply or reverse it. Migrations let schema history evolve alongside the application source.

After entities, relationships, or identity structures change, a new migration can be generated and applied to update the database. A migration changes schema; moving existing production data safely may require additional data-migration planning.

The REST service workflow uses migrations to turn the persistence model configured in the data layer into a reproducible database schema before the API begins serving repository operations.

The software-architecture workflow treats migrations as versioned transformations from the configured EF Core model to a deployable physical schema, allowing database evolution to accompany application releases rather than rely on manual drift.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[aspnetcore3andangular9_3ed.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
