2026-10-08 01:04

Status: #baby

Tags: [[R Software Testing]]

# R Test Equality Tolerance

R test equality tolerance defines how much numerical difference an [[R testthat Expectation]] accepts between an actual and expected result. Floating-point calculations can introduce small rounding differences, so exact identity is usually inappropriate for computed numeric values.

The comparison must use a scale suited to the claim. Absolute error is easier to reason about when a fixed numerical deviation matters, while relative error is necessary when the magnitude of the expected value should determine what counts as close. Very small expected values can expose the difference: a permissive absolute tolerance may accept an underflowed zero even when the relative error is complete.

# References

[[testingrcode.pdf]]
