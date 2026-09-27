2026-09-27 11:19

Status: #baby

Tags: [[ASP.NET Core Service Observability and API Tooling]]

# OpenAPI API Convention

An ASP.NET Core API convention applies recurring metadata about controller actions and their possible responses. Convention methods reduce repeated response annotations and help OpenAPI generation describe common create, read, update, and delete behavior consistently.

A convention is documentation metadata, not runtime enforcement. The actual controller must still return the described status codes and representations or the generated contract will mislead clients.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
