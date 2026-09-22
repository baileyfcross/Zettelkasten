2026-09-21 22:12

Status: #baby

Tags: [[CQRS and Ledger Data Architecture]]

# Command Query Responsibility Segregation

Command Query Responsibility Segregation (CQRS) separates operations that change state from operations that retrieve it. An inventory application can use command handlers for saving or deleting a product and query handlers for listing or finding products. Separate models can be optimized for writes and reads, even in different services or stores, but the added coordination is justified only when a simpler shared model is insufficient.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

