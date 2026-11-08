2026-11-08 16:00

Status: #baby

Tags: [[REST API Versioning Documentation and Governance]]

# API Design Strategy Spectrum

An API can be introduced through a bolt-on, greenfield, iterative, or façade strategy. Bolt-on exposes capability from an existing application; greenfield makes the interface a first-order boundary before the backend exists; an iterative strategy refines the contract through feedback before publication; and a façade reshapes existing systems behind a preferred external design.

The choice determines which constraints are inherited and when consumers can validate the contract. Greenfield design has the most freedom, whereas a bolt-on must respect existing behavior. A façade can combine a consumer-oriented interface with legacy backends, but it must mediate between the two rather than merely rename existing operations.

# References

[[prorestfulapiswithmicronaut.epub]]
