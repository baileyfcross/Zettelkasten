2026-09-08 22:09

Status: #baby

Tags: [[Containerized Microservice Architecture]]

# Service Autonomy

Service autonomy means a service owns its execution and can remain operational without synchronously depending on another service for every action. Inputs may arrive from outside, but their temporary absence should leave the service idle rather than unable to start.

The order worker receives sales orders through an [[Azure Storage Queue]], so the producer and consumer do not need to be available simultaneously. This loose timing relationship is what allows several worker replicas to process the same backlog.

# References

[[c8andnetcore30projectsusingazure.pdf]]
