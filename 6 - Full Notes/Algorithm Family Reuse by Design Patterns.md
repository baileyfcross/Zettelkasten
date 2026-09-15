2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Design Patterns]]

# Algorithm Family Reuse by Design Patterns

An algorithm family can reuse architecture when its invariant steps are separated from its variable mathematics. Template Method provides the shared sequence, Strategy supplies replaceable collaborators, and factory-like or prototype operations construct polymorphic components.

The Lance-Williams classes demonstrate this arrangement: all agglomerative variants build and merge the same forest, while each subclass changes only the recurrence used to update intercluster distance.

# References

[[dataclusteringincplusplus.pdf]]

