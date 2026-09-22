2026-09-21 22:12

Status: #baby

Tags: [[CQRS and Ledger Data Architecture]]

# CQRS Command Model

A CQRS command model represents a requested change and the rules for applying it. The book's product API constructs save and delete commands, sends them to corresponding handlers, and returns an outcome indicating success or failure. The command side can enforce invariants and use a write-optimized repository without shaping itself around every report or page that reads the data.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

