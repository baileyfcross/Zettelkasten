2026-09-08 22:09

Status: #baby

Tags: [[Containerized Microservice Architecture]] [[Cloud Scalability and Resilience Patterns]]

# Microservice

A microservice is a small, independently operated process responsible for a bounded capability. The order-processing example treats autonomy as the defining property: the worker can continue running even when no new orders arrive and does not require another application process to remain alive.

Independent deployment and scaling can isolate change, but dividing one system into many services adds network, versioning, logging, and data-consistency problems. The book cautions that a microservice architecture is useful only when those costs solve a real need.

The design-patterns source frames a microservice as a small unit built around one business capability, loosely coupled by an explicit service contract, independently maintainable, and responsible for isolated state. Those boundaries permit different services and their data stores to scale or deploy at different rates, rather than merely splitting a monolith into smaller processes that still share one database.

# References

[[c8andnetcore30projectsusingazure.pdf]]
[[hands-ondesignpatternswithcandnetcore.pdf]]
