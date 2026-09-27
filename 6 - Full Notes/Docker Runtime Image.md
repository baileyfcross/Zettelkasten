2026-09-27 11:23

Status: #baby

Tags: [[Containerized Microservice Architecture]]

# Docker Runtime Image

A .NET Docker runtime image contains the runtime components required to execute a previously published application but omits the full build toolchain. It forms the base of the final stage for an ASP.NET Core service or worker container.

Selecting the correct runtime family and version is part of the deployment contract. The application must be published for a compatible target, and security updates require rebuilding the derived image against an updated base.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
