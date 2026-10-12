2026-09-27 11:43

Status: #baby

Tags: [[C Sharp Code Quality Metrics and Static Analysis]]

# Class Coupling

Class coupling measures the number of other types a class directly depends on through parameters, fields, return types, inheritance, calls, or construction. Broad coupling increases the number of changes that may affect the class and the setup needed to test it.

The goal is purposeful dependency, not zero dependency. Stable abstractions and cohesive collaborators can be reasonable, while unrelated knowledge gathered into one class signals a boundary that deserves review.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
