2026-09-22 20:53

Status: #baby

Tags: [[Domain Model Building Blocks]]

# Anemic Domain Model

An anemic domain model contains data structures and relationships but leaves most behavior elsewhere, often in services, SQL, or database procedures. It can closely mirror a persistence schema while revealing little about what the system actually does. A data model is appropriate when persistence is the only need, but calling it a [[Domain Model]] obscures the absence of domain behavior. Behavior-rich entities instead keep state transitions and [[Entity Invariant]]s near the state they protect.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
