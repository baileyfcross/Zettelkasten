2026-10-08 01:04

Status: #baby

Tags: [[R Software Testing]]

# R Complex Object Testing

R complex object testing verifies a structured result through several focused expectations rather than one opaque whole-object comparison. A useful sequence checks the object's class, required element names or shape, important values, and invariants that relate its components.

This approach makes failures more informative because each [[R testthat Expectation]] identifies which part of the contract changed. Comparing against a serialized reference object can be concise, but it reports only that the objects differ and can make intentional structural changes cumbersome. Reference comparison is best reserved for cases where the entire representation is genuinely the contract and the loss of [[Test Failure Localization]] is acceptable.

# References

[[testingrcode.pdf]]
