2026-09-27 11:19

Status: #baby

Tags: [[ASP.NET Core Service Observability and API Tooling]]

# Exception Logging Filter

An ASP.NET Core exception logging filter observes an exception raised while an MVC action is executing and records diagnostic context through the application's logger. It can capture controller-level failures at a consistent boundary instead of repeating logging code in every action.

Logging is distinct from deciding the public error response. The filter should avoid disclosing stack traces or sensitive request data, and the pipeline needs one clear owner for marking an exception handled.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
