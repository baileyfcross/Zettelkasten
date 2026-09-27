2026-09-22 20:53

Status: #baby

Tags: [[Event Sourcing and Projections]]

# Event Sourcing

Event Sourcing persists the ordered [[Domain Event]]s produced by an aggregate instead of storing only its latest state. To load the aggregate, the application reads its [[Event Stream]] and applies each event through the state-transition function, making history the source of truth. New events are appended after command handling. The approach preserves how a state arose and enables replay, but it requires deliberate event schemas, concurrency checks, [[Projection]]s for queries, and acceptance of [[Eventual Consistency]].

The architecture chapter presents event sourcing as persistence of the sequence of domain changes rather than only the latest entity state. Replaying events can reconstruct current state and preserve an audit history, with added complexity in versioning and projections.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[hands-ondomain-drivendesignwithnetcore.pdf]]
