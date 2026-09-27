2026-09-21 22:12

Status: #baby

Tags: [[Cloud Scalability and Resilience Patterns]] [[.NET Microservice Communication and Workers]]

# Event-Driven Architecture

Event-driven architecture reacts to facts that have occurred, such as a customer being created or an order being placed. A producer publishes the event without calling each consumer directly, allowing independently deployed services to respond through messaging. This loose coupling supports scale and change, but event meaning, delivery, ordering, retries, and consistency become explicit service contracts.

Azure Functions in the case study react to queue events instead of polling or remaining continuously active. This makes triggers and message contracts the architecture boundary between producers and independently scaled computation.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[hands-ondesignpatternswithcandnetcore.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
