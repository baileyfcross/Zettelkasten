2026-09-06 20:31

Status: #baby

Tags: [[HTTP API Integration]] [[Distributed Network Caching Monitoring and Inspection]] [[ASP.NET Core Service Observability and API Tooling]]

# Health Check

A health check evaluates whether an application or one of its dependencies is available and able to perform an expected operation. It produces a result suitable for monitoring rather than ordinary business data.

Useful outcomes distinguish healthy, degraded, and unhealthy states and can include messages describing the evaluated dependency. A health endpoint exposes those results through an [[HTTP Response]] for a browser or monitoring system.

MicroProfile separates three lifecycle questions. Liveness asks whether an instance should continue or be replaced, readiness asks whether it can currently perform its task and may recover without restart, and startup asks whether initialization has advanced far enough for the other two checks to be meaningful.

# References

[[aspnetcore3andangular9_3ed.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
