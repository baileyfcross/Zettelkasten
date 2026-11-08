2026-11-06 13:52

Status: #baby

Tags: [[Microservice Communication and Resilience]]

# Out-of-Order Message Handling

Out-of-order message handling prevents a later-delivered older event from overwriting the effect of a newer one. Delivery sequence can diverge from business sequence when messages take different paths, are retried, or are processed concurrently, even if no message is lost.

A consumer needs ordering evidence such as a source sequence, entity version, or timestamp together with an explicit rule for stale work. It can reject an older transition, buffer it until a predecessor arrives, or reconcile from an authoritative record. [[Idempotent Message Consumer|Idempotence]] addresses duplicate identity, but it does not by itself determine whether two distinct messages arrived in the intended order.

# References

[[practicalmicroservicesarchitecturalpatterns.epub]]
