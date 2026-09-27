2026-09-27 11:23

Status: #baby

Tags: [[Containerized Microservice Architecture]]

# Multi-Stage Docker Build

A multi-stage Docker build uses one image with the .NET SDK to restore, compile, test, and publish an application, then copies only the published output into a separate runtime image. Build tools and intermediate files do not become part of the deployed container.

The result is smaller and has a narrower attack surface while retaining a reproducible build recipe. Stage ordering also affects cache reuse, so stable dependency inputs are commonly copied before frequently changing source files.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
