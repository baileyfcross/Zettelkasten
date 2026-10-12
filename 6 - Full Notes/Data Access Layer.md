2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Service Layers and Mapping]]

# Data Access Layer

A data access layer contains the code that reads and writes durable storage while presenting an application-facing contract. It keeps controllers and domain services from embedding provider configuration, SQL, connection handling, or change-tracking details.

The layer can use Entity Framework Core, Dapper, or another mechanism according to the workload. The abstraction should not pretend those mechanisms are identical; transaction behavior, query shape, and database capabilities still influence correctness and performance.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
