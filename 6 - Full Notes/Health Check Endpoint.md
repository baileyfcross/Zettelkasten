2026-09-27 11:19

Status: #baby

Tags: [[ASP.NET Core Service Observability and API Tooling]]

# Health Check Endpoint

A health check endpoint maps the application's registered probes to an HTTP route that infrastructure can poll. Its status code and optional response body summarize whether the service and selected dependencies are ready or healthy.

Readiness and liveness answer different questions: one indicates whether traffic can be served, while the other indicates whether the process should be restarted. Combining them indiscriminately can cause a temporary dependency failure to trigger harmful restart loops.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
