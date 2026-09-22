2026-09-21 22:12

Status: #baby

Tags: [[CQRS and Ledger Data Architecture]]

# CQRS Query Model

A CQRS query model supplies data without changing application state. The book models requests for all products and for one product as distinct query types with handlers that retrieve their responses. A read model may use different fields, indexing, or even a separate store from the command side, giving callers a representation suited to retrieval rather than to write validation.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

