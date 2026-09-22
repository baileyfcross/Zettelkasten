2026-09-06 20:37

Status: #baby

Tags: [[Front-End Service Design]] [[.NET Dependency Injection and Service Lifetimes]]

# Singleton Service

A singleton service has one shared instance within an application. Angular can provide a service at the application root so every injected consumer receives that same instance.

This avoids creating redundant service objects and is the common arrangement for stateless API access or intentionally shared state. A service need not be a singleton, so its provider scope remains a design decision.

.NET Core's `AddSingleton` registration similarly provides one service instance per built service provider. The book's inventory tests show why the provider boundary matters: building a new provider for every resolution produces a new singleton in each provider. A shared instance may still need synchronization when several threads mutate it.

# References

[[aspnetcore3andangular9_3ed.pdf]]
[[hands-ondesignpatternswithcandnetcore.pdf]]
