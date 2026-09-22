2026-09-21 22:12

Status: #baby

Tags: [[Object-Oriented Design Patterns]]

# Singleton Pattern

The singleton pattern constrains a class to one instance within a chosen application boundary. The book uses a single inventory context so commands observe the same in-memory book collection, then shows how a .NET service container can manage that lifetime. One instance is not the same as thread safety: concurrent mutation still requires coordination. A singleton can also hide global state and create a bottleneck, so it should be used only when shared identity is a real requirement.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

