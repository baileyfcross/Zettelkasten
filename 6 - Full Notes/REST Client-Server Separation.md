2026-09-27 10:58

Status: #baby

Tags: [[REST Architectural Constraints and Hypermedia]]

# REST Client-Server Separation

The REST client-server constraint separates user-interface and interaction concerns from resource storage and service behavior. Each side depends on the published interface rather than the other's internal implementation.

The boundary allows clients and servers to evolve or deploy independently when they preserve the contract. It does not remove coupling to schemas and semantics, so versioning and compatibility remain deliberate API design work.

In the book's division, the client presents data, captures input, and initiates requests, while the server hosts resources, runs business logic, manages storage, and enforces security. Shared HTTP contracts allow browsers, mobile apps, desktop programs, and IoT devices to use a service implemented with different technologies.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
[[masteringrestapis.epub]]
