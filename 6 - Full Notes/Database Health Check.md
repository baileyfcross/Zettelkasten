2026-09-27 11:19

Status: #baby

Tags: [[ASP.NET Core Service Observability and API Tooling]]

# Database Health Check

A database health check performs a small bounded operation that determines whether an application can reach the database it depends on. Its result contributes to a service health report exposed to orchestration or monitoring systems.

The probe should be cheap enough to run repeatedly and time out promptly. A successful network connection may not prove that every business query works, so the check's name and interpretation should match what it actually tests.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
