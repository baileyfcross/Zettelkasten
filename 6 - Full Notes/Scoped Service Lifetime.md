2026-09-21 22:12

Status: #baby

Tags: [[.NET Dependency Injection and Service Lifetimes]]

# Scoped Service Lifetime

A scoped .NET service is created once within a defined scope and reused by resolutions in that scope. ASP.NET Core commonly creates a scope for each incoming web request, allowing collaborators in one request to share a context without sharing it with unrelated requests. A scope is a lifetime boundary, not a distributed state mechanism: separate web-server processes or provider instances do not share a scoped object.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

