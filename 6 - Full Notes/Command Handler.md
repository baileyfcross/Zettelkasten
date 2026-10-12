2026-09-22 20:53

Status: #baby

Tags: [[Application Commands and Service Boundaries]]

# Command Handler

A command handler is a class or function dedicated to one [[Application Command]] type. It loads or creates the relevant [[Aggregate]], invokes domain behavior, and coordinates persistence. One handler per command supports the [[Single Responsibility Principle]] and makes dependencies explicit, but a large API can create many injected handlers. An [[Application Service]] is an alternative grouping when several related commands share coordination needs; neither pattern is universally superior.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
