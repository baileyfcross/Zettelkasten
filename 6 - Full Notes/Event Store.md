2026-09-22 20:53

Status: #baby

Tags: [[Event Sourcing and Projections]]

# Event Store

An event store is a persistence system designed to append and retrieve ordered events in [[Event Stream]]s. It supports transactional appends, expected stream versions, reading historical slices, and subscriptions for new or existing events. The store preserves the event history used by [[Event Sourcing]]; it is not itself the user-facing query model. [[Projection]]s consume its streams to construct data structures optimized for filtering and display.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
