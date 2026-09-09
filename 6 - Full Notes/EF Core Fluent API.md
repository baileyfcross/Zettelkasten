2026-09-08 21:16

Status: #baby

Tags: [[Entity Framework Core Data Access]]

# EF Core Fluent API

The EF Core Fluent API configures a model through chained method calls, commonly in `OnModelCreating`. It can define keys, property constraints, relationships, indexes, table mappings, value generation, and behavior that conventions do not capture.

Fluent configuration keeps persistence details out of entity classes and can express mappings unavailable through attributes. When conventions, annotations, and Fluent API configuration conflict, the explicit Fluent configuration has the greatest authority.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
