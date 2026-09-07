2026-09-06 20:34

Status: #baby

Tags: [[Entity Framework Core Data Modeling]]

# Database Context

A database context is the Entity Framework Core object that represents a session with the database and coordinates entity sets, mappings, queries, and saved changes. An application-specific context declares the entities that belong to its model.

The context is configured with a database provider and connection information, then supplied to controllers or services through [[Dependency Injection]]. Tests can replace the production configuration with an [[In-Memory Database Provider]].

# References

[[aspnetcore3andangular9_3ed.pdf]]
