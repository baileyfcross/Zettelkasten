2026-10-31 13:15

Status: #baby

Tags: [[Java Numeric Utilities and Arbitrary Precision]]

# Java Pseudorandom Number Scaling

`Math.random()` returns a pseudorandom double from zero inclusive to one exclusive. Multiplying that value by a positive limit and casting the product to `int` produces one of the integers from zero through `limit - 1`.

An application can then add an offset to move the interval, such as adding one for a guessing game numbered from one through the limit. The cast discards the fractional portion after scaling, so the order of multiplication and conversion determines the resulting range.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
