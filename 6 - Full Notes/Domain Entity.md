2026-09-22 20:53

Status: #baby

Tags: [[Domain Model Building Blocks]]

# Domain Entity

A domain entity represents a unique object whose identity persists while its attributes and state change. Two entities with identical current property values can still be different because they have different [[Entity Identity]] values. The entity exposes behavior in the [[Ubiquitous Language]] and protects transitions with [[Entity Invariant]]s. This meaning is distinct from a generic database row or a named entity extracted from language: its defining concern is continuity of identity through a life cycle.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
