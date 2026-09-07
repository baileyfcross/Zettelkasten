2026-09-06 20:37

Status: #baby

Tags: [[Front-End Service Design]]

# Singleton Service

A singleton service has one shared instance within an application. Angular can provide a service at the application root so every injected consumer receives that same instance.

This avoids creating redundant service objects and is the common arrangement for stateless API access or intentionally shared state. A service need not be a singleton, so its provider scope remains a design decision.

# References

[[aspnetcore3andangular9_3ed.pdf]]
