2026-09-22 20:53

Status: #baby

Tags: [[Application Commands and Service Boundaries]] [[OSI Layers Packets and Network Streams]]

# Application Layer

The application layer coordinates a use case around an isolated [[Domain Model]]. It receives a [[Public API Contract]] or message, obtains the required aggregate or services, invokes domain behavior, and persists the resulting changes. It can implement infrastructure-facing interfaces declared by the domain, but it should not reimplement [[Entity Invariant]]s. The layer is an outer boundary: it translates between delivery mechanisms and the domain while keeping business decisions in domain objects.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
