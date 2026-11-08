2026-09-08 22:09

Status: #baby

Tags: [[Containerized Microservice Architecture]] [[Microservice Boundaries and Data]]

# Distributed Transaction Limitation

A distributed transaction limitation appears when one business operation changes state owned by separate services or databases that cannot participate in one ordinary local transaction. At a particular instant, one part may have committed while another has not.

The order-processing discussion contrasts this with a single database transaction that can update an order and stock together. Distributed designs need asynchronous coordination and explicit recovery or compensation rather than assuming every component changes atomically.

The microservices source connects this limitation to database-per-service ownership. Eventual consistency accepts that service-owned views may converge after a delay, while a saga coordinates a sequence of local changes and invokes compensating actions when a later step fails. Both approaches make partial progress and recovery part of the business workflow instead of pretending that a network-spanning operation is one local commit.

The telecom case study makes compensation observable as domain behavior. A revision may require undoing an earlier action, redoing it with changed input, leaving it untouched, or performing an amended action after compensation completes. Traces and business identifiers must preserve the order, outcome, and affected component for each step because a technically successful message exchange can still leave the overall order inconsistent.

The practical architecture source contrasts three responses to this limitation. [[Two-Phase Commit Protocol|Two-phase commit]] coordinates a strong decision across resource managers but adds round trips, longer locks, and failure recovery. [[BASE Transaction|BASE]] propagates smaller local commits asynchronously, while a [[Saga Transaction|saga]] coordinates local work and semantic compensation. The correct choice depends on which temporary states and failure windows the business can tolerate.

# References

[[c8andnetcore30projectsusingazure.pdf]]
[[artofdecodingmicroservices.epub]]
[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
[[practicalmicroservicesarchitecturalpatterns.epub]]
