2026-09-08 21:16

Status: #baby

Tags: [[Entity Framework Core Data Access]] [[ASP.NET Core Service Layers and Mapping]]

# EF Core Fluent API

The EF Core Fluent API configures a model through chained method calls, commonly in `OnModelCreating`. It can define keys, property constraints, relationships, indexes, table mappings, value generation, and behavior that conventions do not capture.

Fluent configuration keeps persistence details out of entity classes and can express mappings unavailable through attributes. When conventions, annotations, and Fluent API configuration conflict, the explicit Fluent configuration has the greatest authority.

In the book's service architecture, fluent configuration is part of the data-access layer and defines the database-facing model without moving those details into the HTTP or application-service layers.

This source uses `OnModelCreating` to complete mappings that conventions or annotations do not express cleanly, keeping database-oriented relationship and key configuration within the data-layer composition boundary.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
