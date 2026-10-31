2026-10-30 17:24

Status: #baby

Tags: [[Microservice Architecture Adoption]]

# Decentralized Microservice Transaction

A decentralized microservice transaction is completed through the local work of several autonomous services rather than by one process controlling a global transaction. A booking service can record a booking and publish an event that an inventory service handles independently.

No single service determines the complete outcome at one instant. Reliability depends on message delivery, local transaction boundaries, failure handling, and eventual convergence across the participating data stores.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

