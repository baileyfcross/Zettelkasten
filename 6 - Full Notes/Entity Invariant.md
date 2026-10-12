2026-09-22 20:53

Status: #baby

Tags: [[Domain Model Building Blocks]]

# Entity Invariant

An entity invariant is a condition that must hold whenever a [[Domain Entity]] completes an operation. Individual [[Value Object]]s can ensure that each input is valid, but the entity must check rules involving combinations of values and its current life-cycle state. For example, an item entering review may require a nonempty title, text, and nonzero price. The operation either produces a valid new state or is rejected, so callers cannot bypass the rule by setting fields directly.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
