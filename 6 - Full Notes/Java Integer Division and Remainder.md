2026-10-30 15:57

Status: #baby

Tags: [[Java Operators and Pattern Matching]]

# Java Integer Division and Remainder

When both operands are integer primitives, Java division produces an integer result and discards the fractional part toward zero. To retain a fraction, at least one operand must participate as a floating-point value before the division is evaluated.

The remainder operator `%` returns the portion left after division and follows the dividend's sign. Integer division or remainder by zero throws `ArithmeticException`; floating-point division instead follows IEEE 754 behavior and can produce infinity or NaN.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
