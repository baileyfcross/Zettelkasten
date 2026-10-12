2026-09-21 22:12

Status: #baby

Tags: [[.NET Dependency Injection and Service Lifetimes]]

# Service Locator Pattern

A service locator returns an implementation when a component asks for a service by contract. It centralizes construction, but a component that calls the locator directly can hide its real dependencies from its constructor and complicate isolated tests. The book contrasts lookup through a provider with constructor injection, where required collaborators are visible in the type's creation contract. Direct resolution is most defensible at an application composition boundary.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

