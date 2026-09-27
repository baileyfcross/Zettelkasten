2026-09-27 11:19

Status: #baby

Tags: [[ASP.NET Core Service Observability and API Tooling]]

# Custom Health Check

A custom ASP.NET Core health check implements application-specific logic for a dependency or operating condition not covered by a standard registration. It returns a healthy, degraded, or unhealthy result together with concise diagnostic information.

The check should honor cancellation and complete quickly because monitoring systems may call it often. It reports current evidence; it should not repair state or perform substantial business work as part of the probe.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
