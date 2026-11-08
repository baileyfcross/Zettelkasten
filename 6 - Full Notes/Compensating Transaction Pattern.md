2026-09-21 22:12

Status: #baby

Tags: [[Cloud Scalability and Resilience Patterns]]

# Compensating Transaction Pattern

A compensating transaction reverses the business effect of a completed step when a later step in a distributed workflow fails. In the book's order example, creating an order is followed by debiting funds; if the debit fails, a new action removes or cancels the order. Compensation is not a database rollback across all services, so its design must specify what happens if the compensating action itself fails or if other observers have already seen the first step.

Within a [[Saga Transaction]], compensation is paired with each local transaction and is run for completed steps when a later step fails. The action must be idempotent because the coordinator may deliver it at least once, and it must be semantically valid even though time has passed and external observers may already have reacted to the original action.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]
[[practicalmicroservicesarchitecturalpatterns.epub]]

