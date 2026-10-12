2026-09-27 11:11

Status: #baby

Tags: [[.NET Microservice Communication and Workers]]

# Worker Service

A .NET worker service is a long-running process built on the generic host without an HTTP request pipeline. It uses the same dependency injection, configuration, and logging infrastructure as other hosted .NET applications while performing background work.

Worker services suit queue consumers, schedulers, and continuous processors. Their work loops must respond to cancellation and avoid allowing one unhandled failure to silently end required processing.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
