2026-10-18 15:54

Status: #baby

Tags: [[Microservice Boundaries and Data]]

# Business Capability Service Boundary

A business capability service boundary groups the behavior needed to accomplish one recognizable business responsibility. Instead of separating services by technical layers such as user interface, logic, and storage, it places the capability's rules and data authority behind one interface.

The boundary supports independent ownership because one team can change the capability without coordinating changes to another service's internals. It should be discovered with domain experts and expressed in their language, then tested against actual workflows and dependencies. A capability that constantly requires synchronous access to another service's private data may have been split incorrectly. [[Bounded Context to Microservice Mapping]] is one way to align the service with a coherent domain model.

# References

[[artofdecodingmicroservices.epub]]
