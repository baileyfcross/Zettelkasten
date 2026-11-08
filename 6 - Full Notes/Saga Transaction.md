2026-11-06 13:52

Status: #baby

Tags: [[Microservice Boundaries and Data]]

# Saga Transaction

A saga transaction coordinates a multi-step workflow as a sequence of local transactions, each paired with a compensating action. If a later step fails, the saga invokes compensations for earlier completed steps so their business effects are eventually neutralized rather than rolled back by one global database transaction.

A distributed saga records progress in a durable saga log and uses a process manager or execution coordinator to decide the next step. Request and response correlation, message sequence, and guaranteed delivery make the workflow recoverable after a coordinator failure. Compensation is semantic rather than physical rollback: canceling a hotel reservation is a new business action, so it must be designed for repeat delivery and for the possibility that observers already saw the reservation. See [[Compensating Transaction Pattern]] and [[Message Correlation Identifier]].

# References

[[practicalmicroservicesarchitecturalpatterns.epub]]
