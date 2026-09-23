2026-09-22 20:53

Status: #baby

Tags: [[EventStorming Collaborative Modeling]]

# Domain Event

A domain event is a fact that changed the state of the domain. It describes something that happened, not something an actor wanted to do, so EventStorming names it with a subject and a past-tense verb such as “Order Confirmed.” Events are placed on an [[Event Timeline]] to reveal causal and temporal relationships. In implementation, the same fact can become an object raised by a [[Domain Entity]] or [[Aggregate]] and later stored through [[Event Sourcing]].

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
