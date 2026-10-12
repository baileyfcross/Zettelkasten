2026-09-22 20:53

Status: #baby

Tags: [[Bounded Context and Organizational Design]]

# Single Model Trap

The single model trap is the attempt to represent every business capability with one shared model. As the system grows, terms acquire incompatible meanings, objects collect properties with unrelated rates of change, and teams must coordinate modifications across one codebase and database. Generalization then increases ambiguity instead of reuse. Dividing the system into [[Bounded Context]]s allows each model to express the language and rules of its capability without becoming a [[Big Ball of Mud]].

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
