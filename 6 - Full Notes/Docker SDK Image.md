2026-09-27 11:23

Status: #baby

Tags: [[Containerized Microservice Architecture]]

# Docker SDK Image

A .NET Docker SDK image contains the compilers, restore tooling, and command-line SDK needed to build an application. It belongs in a build stage where source is transformed into published artifacts.

Shipping the SDK in the final production image is usually unnecessary. Separating build and runtime stages keeps deployment focused on the files and framework required to execute the service.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
