2026-09-08 22:09

Status: #baby

Tags: [[Containerized Microservice Architecture]] [[Microservice Boundaries and Data]]

# Distributed Transaction Limitation

A distributed transaction limitation appears when one business operation changes state owned by separate services or databases that cannot participate in one ordinary local transaction. At a particular instant, one part may have committed while another has not.

The order-processing discussion contrasts this with a single database transaction that can update an order and stock together. Distributed designs need asynchronous coordination and explicit recovery or compensation rather than assuming every component changes atomically.

The microservices source connects this limitation to database-per-service ownership. Eventual consistency accepts that service-owned views may converge after a delay, while a saga coordinates a sequence of local changes and invokes compensating actions when a later step fails. Both approaches make partial progress and recovery part of the business workflow instead of pretending that a network-spanning operation is one local commit.

# References

[[c8andnetcore30projectsusingazure.pdf]]
[[artofdecodingmicroservices.epub]]
