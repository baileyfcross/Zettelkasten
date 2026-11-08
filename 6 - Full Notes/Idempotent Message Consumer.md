2026-11-06 13:52

Status: #baby

Tags: [[Microservice Communication and Resilience]]

# Idempotent Message Consumer

An idempotent message consumer makes repeated delivery of the same logical message have the same business effect as one delivery. This is necessary when a broker redelivers an unacknowledged message after a failure or when the sender repeats a message whose earlier outcome is uncertain.

One implementation records a sender-assigned unique transaction identifier in the consumer's local store before or with the business update. A later message with that identifier can be recognized and ignored. The check and effect must share a safe local boundary; merely setting a value is not automatically idempotent when concurrent or out-of-order work can change its preconditions.

# References

[[practicalmicroservicesarchitecturalpatterns.epub]]
