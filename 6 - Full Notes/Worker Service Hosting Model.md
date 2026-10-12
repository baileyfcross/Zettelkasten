2026-09-27 11:11

Status: #baby

Tags: [[.NET Microservice Communication and Workers]]

# Worker Service Hosting Model

The worker service hosting model starts a generic host, builds configuration and the dependency injection container, then runs registered hosted services until cancellation. It supplies application lifetime, logging, and environment behavior without requiring a web server.

This separates a background consumer from the API process while preserving a consistent composition model. Each process can be deployed, restarted, and scaled according to its own workload.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
