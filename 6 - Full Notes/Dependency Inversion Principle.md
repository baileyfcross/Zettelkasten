2026-09-21 22:12

Status: #baby

Tags: [[Software Design Principles]]

# Dependency Inversion Principle

The dependency inversion principle directs high-level behavior to depend on abstractions rather than concrete details. An inventory command can require an `IInventoryReadContext` contract instead of constructing a particular database or in-memory repository. [[Dependency Injection]] is one way to provide the implementation, but the principle concerns the dependency direction itself: changing storage should not require rewriting the command's business rule.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

