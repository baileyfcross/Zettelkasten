2026-09-27 11:43

Status: #baby

Tags: [[C Sharp Code Quality Metrics and Static Analysis]]

# Depth of Inheritance

Depth of inheritance measures how many type levels separate a class from the root of its inheritance hierarchy. Greater depth can increase reuse, but it also makes behavior depend on more inherited definitions and substitution assumptions.

The metric draws attention to hierarchies that may be difficult to understand or change. A shallow hierarchy is not automatically well designed, and a deeper framework hierarchy can be justified when its contracts remain stable and explicit.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
