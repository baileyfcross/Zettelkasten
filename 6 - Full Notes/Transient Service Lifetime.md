2026-09-21 22:12

Status: #baby

Tags: [[.NET Dependency Injection and Service Lifetimes]]

# Transient Service Lifetime

A transient .NET service registration creates a fresh instance whenever the container resolves the service. This suits lightweight collaborators that do not need identity or mutable state to persist between resolutions. The inventory example registers interface and command-related services as transient while reserving a shared lifetime for the in-memory context whose state must survive between commands.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

