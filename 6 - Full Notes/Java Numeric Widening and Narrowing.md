2026-10-30 15:57

Status: #baby

Tags: [[Java Values Strings and Core Types]]

# Java Numeric Widening and Narrowing

A widening primitive conversion moves a value to a type whose accepted range generally contains the source range and is often implicit, such as assigning an `int` to a `long`. A narrowing conversion requires an explicit cast because the target may not represent the original value.

Narrowing can discard high-order bits, change sign, or lose fractional information. Widening an integer to a floating-point type can also lose precision even when its magnitude fits. A cast therefore states permission to perform a conversion, not proof that the resulting value preserves the original meaning.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
