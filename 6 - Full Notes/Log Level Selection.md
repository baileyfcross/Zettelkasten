2026-09-27 11:19

Status: #baby

Tags: [[ASP.NET Core Service Observability and API Tooling]]

# Log Level Selection

Log level selection assigns diagnostic events a severity that reflects their operational meaning. Trace and debug describe detailed execution, information records expected milestones, warning identifies recoverable concern, and error or critical signals failed behavior requiring attention.

Choosing levels consistently enables production filtering without discarding important evidence. Expected client mistakes should not flood error monitoring, while a failed dependency or lost operation should not be hidden at an informational level.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
