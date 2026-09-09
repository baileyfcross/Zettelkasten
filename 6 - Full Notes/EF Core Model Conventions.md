2026-09-08 21:16

Status: #baby

Tags: [[Entity Framework Core Data Access]]

# EF Core Model Conventions

EF Core conventions infer a database model from ordinary .NET types. Names and type patterns can identify entity keys, required or optional properties, relationships, and table mappings without configuration for every detail.

Conventions reduce repetitive mapping, while data annotations and the Fluent API override them when the inferred model does not match the intended schema. Understanding the defaults is important because an apparently small class change can alter the resulting model.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
