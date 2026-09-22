2026-09-21 22:12

Status: #baby

Tags: [[Cloud Scalability and Resilience Patterns]]

# Compensating Transaction Pattern

A compensating transaction reverses the business effect of a completed step when a later step in a distributed workflow fails. In the book's order example, creating an order is followed by debiting funds; if the debit fails, a new action removes or cancels the order. Compensation is not a database rollback across all services, so its design must specify what happens if the compensating action itself fails or if other observers have already seen the first step.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

