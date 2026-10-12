2026-09-22 20:53

Status: #baby

Tags: [[Domain Model Building Blocks]]

# Event-Applied State Transition

An event-applied state transition changes entity state by first creating a [[Domain Event]] and then applying that event through a dedicated transition function. This couples the fact of change to the state it produces instead of mutating fields and publishing a separate notification that might diverge. Newly raised events are recorded as pending changes, while historical events can use the same transition function during [[Aggregate Rehydration]] without being raised again.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
