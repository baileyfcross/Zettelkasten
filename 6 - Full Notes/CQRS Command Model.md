2026-09-21 22:12

Status: #baby

Tags: [[CQRS and Ledger Data Architecture]] [[CQRS Query and Read Model Design]]

# CQRS Command Model

A CQRS command model represents a requested change and the rules for applying it. The book's product API constructs save and delete commands, sends them to corresponding handlers, and returns an outcome indicating success or failure. The command side can enforce invariants and use a write-optimized repository without shaping itself around every report or page that reads the data.

Within a domain-centered design, a command expresses [[Command Intent]] and is processed against the current state of an [[Aggregate]]. Successful handling changes state and may emit [[Domain Event]]s. The model does not need to return a read representation; information retrieval belongs to the [[CQRS Query Model]].

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]
[[hands-ondomain-drivendesignwithnetcore.pdf]]
