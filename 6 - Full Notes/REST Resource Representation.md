2026-09-27 10:58

Status: #baby

Tags: [[REST Architectural Constraints and Hypermedia]]

# REST Resource Representation

A REST resource is the conceptual target identified by a URI, while a representation is the transferred description of its current or proposed state. JSON, XML, or another media type can represent the same resource without being the resource itself.

Clients manipulate a resource by sending and receiving representations through HTTP methods. Separating identity from representation lets the server change internal storage while preserving the public address and agreed message semantics.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
