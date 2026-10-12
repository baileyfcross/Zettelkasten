2026-09-27 11:19

Status: #baby

Tags: [[ASP.NET Core Service Observability and API Tooling]]

# ASP.NET Core Logging Abstraction

ASP.NET Core logging exposes category-based `ILogger` instances through dependency injection. Application code writes structured events through the abstraction while one or more configured providers decide where those events are recorded.

This separation lets the same service write to the console during development and to centralized infrastructure in production. Message templates and contextual properties make logs more useful than concatenated text when many requests and services interleave.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
