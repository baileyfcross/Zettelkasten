2026-09-21 22:12

Status: #baby

Tags: [[CQRS and Ledger Data Architecture]] [[CQRS Query and Read Model Design]]

# CQRS Query Model

A CQRS query model supplies data without changing application state. The book models requests for all products and for one product as distinct query types with handlers that retrieve their responses. A read model may use different fields, indexing, or even a separate store from the command side, giving callers a representation suited to retrieval rather than to write validation.

Query models should be shaped around the information a user or external system needs to make a decision. They can join information from multiple aggregates, use a [[Read Model Ubiquitous Language]], and return the stored representation directly. This avoids loading behavioral aggregates solely to display data.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]
[[hands-ondomain-drivendesignwithnetcore.pdf]]
