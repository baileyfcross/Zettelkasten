2026-09-22 20:53

Status: #baby

Tags: [[Event Sourcing and Projections]]

# Event Sourcing

Event Sourcing persists the ordered [[Domain Event]]s produced by an aggregate instead of storing only its latest state. To load the aggregate, the application reads its [[Event Stream]] and applies each event through the state-transition function, making history the source of truth. New events are appended after command handling. The approach preserves how a state arose and enables replay, but it requires deliberate event schemas, concurrency checks, [[Projection]]s for queries, and acceptance of [[Eventual Consistency]].

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
