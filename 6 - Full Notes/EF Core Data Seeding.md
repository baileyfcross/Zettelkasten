2026-09-08 21:16

Status: #baby

Tags: [[Entity Framework Core Data Access]]

# EF Core Data Seeding

Data seeding places known rows into a database as part of the model's managed state. In EF Core, seed data can be described during model configuration so migrations can insert, update, or remove those rows as the model evolves.

Seed data works best for stable reference values whose identities are known in advance. Operational or environment-specific initialization often needs a separate process because model-based seeding is not a general replacement for application workflows.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
