2026-09-22 20:53

Status: #baby

Tags: [[CQRS Query and Read Model Design]]

# Read Model

A read model is a data representation shaped for a specific information need. An [[Application Query]] retrieves it without invoking state-changing domain behavior, and the API can often return the stored shape directly without mapping it through an [[Aggregate]]. Read models can combine fields from several aggregates and use indexes or denormalization suited to their consumers. In event-sourced systems, a [[Projection]] builds and updates them from domain events.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
