2026-09-08 22:09

Status: #baby

Tags: [[Entity Framework Core Data Access]]

# EF Core SQL Server Provider

The EF Core SQL Server provider translates Entity Framework Core operations for Microsoft SQL Server. The web-research project installs it, supplies a SQL Server connection string, and registers the database context with the ASP.NET Core service container.

Provider configuration links the abstract context and entity model to a concrete database engine. Queries and schema behavior must therefore be tested against SQL Server even when an in-memory provider is convenient during automated tests.

# References

[[c8andnetcore30projectsusingazure.pdf]]
