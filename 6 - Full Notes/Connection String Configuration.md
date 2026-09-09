2026-09-06 20:52

Status: #baby

Tags: [[Cloud Application Deployment]] [[Entity Framework Core Data Access]]

# Connection String Configuration

Connection string configuration tells the deployed backend how to reach and authenticate to its database. App Service supplies the environment-specific value so the same application artifact can connect differently in development, staging, and production.

The value is operational configuration and may contain sensitive credentials. It should not be hard-coded into the repository or exposed to the React client.

# References

[[aspnetcore3andreact.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]
