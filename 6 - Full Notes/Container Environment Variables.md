2026-09-27 11:23

Status: #baby

Tags: [[Containerized Microservice Architecture]]

# Container Environment Variables

Container environment variables provide deploy-time configuration without rebuilding an application image. ASP.NET Core's configuration system can map them into settings such as service addresses, connection strings, or environment names when a container starts.

This separates one immutable image from the environments that run it. Secrets still require protected storage and delivery; placing them in a plain Compose file or committed configuration merely changes where they are exposed.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
