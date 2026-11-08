2026-11-06 13:52

Status: #baby

Tags: [[CQRS and Ledger Data Architecture]]

# Event-Based CQRS

Event-based CQRS uses events from the command side to synchronize one or more query-side representations. A command gateway and handler apply a requested change to a domain entity; the resulting event passes through an event bus to handlers that update materialized views, external interfaces, or further commands.

This propagation allows write and read services, stores, and instance counts to be chosen independently. It also means a successful command can precede visibility in every [[CQRS Query Model]], so [[Eventual Consistency]] and recovery of failed event handlers are part of the design. The event bus's publish-subscribe behavior makes new projections extensible without changing the original command handler.

# References

[[practicalmicroservicesarchitecturalpatterns.epub]]
