2026-09-21 22:12

Status: #baby

Tags: [[.NET Dependency Injection and Service Lifetimes]]

# Dependency Implementation Factory

A dependency-injection implementation factory is a registration callback that constructs the service supplied for a contract. It is useful when construction needs configuration or when several interfaces must resolve to the same underlying object. The book registers read and write inventory interfaces through factory functions returning one context instance, preserving shared state while keeping each consumer dependent on only the operations it needs.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

