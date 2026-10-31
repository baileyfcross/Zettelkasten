2026-09-08 22:09

Status: #baby

Tags: [[Containerized Microservice Architecture]] [[Microservice Architecture Adoption]]

# Service Autonomy

Service autonomy means a service owns its execution and can remain operational without synchronously depending on another service for every action. Inputs may arrive from outside, but their temporary absence should leave the service idle rather than unable to start.

The order worker receives sales orders through an [[Azure Storage Queue]], so the producer and consumer do not need to be available simultaneously. This loose timing relationship is what allows several worker replicas to process the same backlog.

The microservices source extends autonomy from runtime independence to lifecycle ownership. A team needs authority over the service's model, data, technology, deployment, scaling, monitoring, and maintenance if it is to change without continuous coordination. Autonomy therefore depends on explicit contracts and automated operations; placing code in a separate process while retaining a shared database or lockstep release does not create an independent service.

The Java source adds an availability consequence: a service should remain useful even when another service in the end-to-end flow is unhealthy. Replacing a mandatory synchronous call with a message channel lets the provider resume later, while the producing service completes the part of the transaction it owns.

# References

[[c8andnetcore30projectsusingazure.pdf]]
[[artofdecodingmicroservices.epub]]
[[javamicroservicesandcontainersinthecloud.epub]]
