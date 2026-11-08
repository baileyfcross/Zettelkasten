2026-10-18 15:54

Status: #baby

Tags: [[Microservice Communication and Resilience]]

# Microservice API Gateway

A microservice API gateway provides one external entry point that routes a request to the appropriate service. It can also aggregate several service responses and apply shared behavior such as authentication, authorization, rate limiting, caching, logging, and protocol translation.

Centralizing these concerns simplifies clients and keeps internal service locations private, but the gateway becomes a critical operational component. Poorly bounded logic can turn it into a new monolith, and insufficient capacity or resilience can make it a bottleneck or single point of failure. The gateway should remain focused on edge concerns, scale independently, and use [[Service Registry|service discovery]] rather than hard-coded instances. Client-specific requirements may justify a [[Backend for Frontend Pattern]].

The practical architecture source emphasizes aggregation as well as routing. A gateway can turn several fine-grained internal calls into one coarse client request, transform the result for a device type, and shield clients from internal service relocation or version changes. That convenience makes gateway availability, capacity, and contract evolution part of the public API design.

# References

[[artofdecodingmicroservices.epub]]
[[practicalmicroservicesarchitecturalpatterns.epub]]
