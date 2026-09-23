2026-09-22 20:53

Status: #baby

Tags: [[Domain Model Building Blocks]]

# Value Object Equality

Value object equality compares the constituent values that define a [[Value Object]], not an object reference or independent identity. Two money values with the same amount and currency are equal even when constructed separately. A reusable value base type can enumerate equality components and derive equality and hashing consistently. Every property that participates in the concept's meaning must participate in equality; otherwise collections and comparisons can treat meaningfully different values as interchangeable.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
