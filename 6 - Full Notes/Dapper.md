2026-09-06 20:52

Status: #baby

Tags: [[Dapper Data Access]] [[ASP.NET Core Service Layers and Mapping]]

# Dapper

Dapper is a lightweight .NET data-access library that executes SQL and maps parameters and result columns to typed objects. The application retains direct control over its queries instead of expressing them through a larger object-relational model.

This makes SQL visible and concise while still removing repetitive command and mapping code. The repository remains responsible for query design, connection use, and the shape returned to the application.

Within a layered ASP.NET Core API, Dapper can implement repository operations that need explicit SQL while the service and controller continue to depend on stable application-facing interfaces.

# References

[[aspnetcore3andreact.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
