2026-09-22 20:53

Status: #baby

Tags: [[CQRS Query and Read Model Design]]

# Cross-Aggregate Read Model

A cross-aggregate read model combines information owned by more than one [[Aggregate]] for a particular retrieval use case. A listing might show an item's public details together with selected owner profile fields even though those states have separate consistency boundaries. The query side can join or precompute this view without introducing object references between the aggregates. Under [[Event Sourcing]], projections can consume events from several streams to maintain the combined representation.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
