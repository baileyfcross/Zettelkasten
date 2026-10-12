2026-09-27 10:58

Status: #baby

Tags: [[REST Architectural Constraints and Hypermedia]]

# REST Client-Server Separation

The REST client-server constraint separates user-interface and interaction concerns from resource storage and service behavior. Each side depends on the published interface rather than the other's internal implementation.

The boundary allows clients and servers to evolve or deploy independently when they preserve the contract. It does not remove coupling to schemas and semantics, so versioning and compatibility remain deliberate API design work.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
