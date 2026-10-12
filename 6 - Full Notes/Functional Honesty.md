2026-09-21 22:12

Status: #baby

Tags: [[Functional Programming in C Sharp]]

# Functional Honesty

Functional honesty means a function's contract reveals the conditions under which it can produce a valid result. The book revises a discount calculation to accept a `ValidDiscount` value rather than an arbitrary decimal, moving a business constraint into the input contract. This is distinct from purity: a function can deterministically compute a result from an invalid percentage while still being a poor representation of the domain rule.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

