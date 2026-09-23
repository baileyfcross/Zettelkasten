2026-09-22 20:53

Status: #baby

Tags: [[CQRS Query and Read Model Design]]

# Application Query

An application query expresses a request for information without changing domain state. It names the user's retrieval intent and returns a purpose-specific [[Read Model]]. Unlike an [[Application Command]], it does not need to load an aggregate or enforce state-transition invariants. A query can access storage through an efficient read path, including joins across aggregate data, while still using the [[Ubiquitous Language]] of the decision or screen it supports.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
