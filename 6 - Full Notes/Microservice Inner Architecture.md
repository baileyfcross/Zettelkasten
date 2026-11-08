2026-11-06 13:52

Status: #baby

Tags: [[Microservice Architecture Adoption]]

# Microservice Inner Architecture

Microservice inner architecture is the organization of responsibilities inside one independently deployable service. Even though the service is small enough to have its own runtime boundary, it still benefits from separated interfaces, business logic, persistence, and infrastructure concerns.

The book presents several inner forms, from a stateless computation service to a service with its own persistent store, external persistence, or separated command and query paths. The appropriate form depends on the service's state and scaling needs; distribution does not remove the need for clean internal boundaries. [[Ports Adapters and Onion Architecture]] supplies one way to keep technology at those boundaries, while [[Command Query Responsibility Segregation]] can split write and read responsibilities when their models and workloads differ.

# References

[[practicalmicroservicesarchitecturalpatterns.epub]]
