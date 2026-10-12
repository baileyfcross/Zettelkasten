2026-09-22 20:53

Status: #baby

Tags: [[Event Sourcing and Projections]]

# Event-Sourced Aggregate

An event-sourced aggregate records each accepted state transition as one or more [[Domain Event]]s and derives its current state from those events. A command method checks [[Aggregate Invariant]]s, emits an event, and applies it to the in-memory state. Historical events use the same transition logic during [[Aggregate Rehydration]] but are not marked as new changes. The aggregate version advances with applied events and supports [[Optimistic Concurrency]] when new events are appended.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
