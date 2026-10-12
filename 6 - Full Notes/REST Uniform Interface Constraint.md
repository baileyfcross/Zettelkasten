2026-09-27 10:58

Status: #baby

Tags: [[REST Architectural Constraints and Hypermedia]]

# REST Uniform Interface Constraint

The REST uniform-interface constraint gives clients a consistent way to identify and manipulate resources regardless of their internal implementation. Resource identifiers, representations, self-descriptive messages, and hypermedia controls make that interface understandable without a private operation protocol for every resource type.

Uniformity reduces coupling but can sacrifice an interface tailored to one implementation. The service gains evolvability by making its public semantics depend on shared HTTP and representation rules rather than internal method names.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
