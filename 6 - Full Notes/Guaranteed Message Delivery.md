2026-09-09 00:00

Status: #baby

Tags: [[Cloud Integration and Messaging]] [[Microservice Communication and Resilience]]

# Guaranteed Message Delivery

Guaranteed message delivery is a service promise that a message will be delivered under stated conditions even if the sender or receiver becomes temporarily unavailable. Persistence retains the message while it is in transit or awaiting reception.

The book describes this level as once-and-once-only delivery. An implementation must make the scope of that promise explicit, including how it identifies a message and what happens if a receiver fails after beginning work.

In the distributed-saga design, a send is considered successful only after the message is stored durably, and one stored copy remains until the next node has stored and acknowledged it. That protects against a transient node failure, but business correctness still requires [[Idempotent Message Consumer|idempotent consumption]] because uncertainty after delivery can cause a retry.

# References

[[cloudcomputing_mit.epub]]
[[practicalmicroservicesarchitecturalpatterns.epub]]
