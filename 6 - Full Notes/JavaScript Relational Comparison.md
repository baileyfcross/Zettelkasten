2026-10-14 01:16

Status: #baby

Tags: [[JavaScript Core Semantics]]

# JavaScript Relational Comparison

JavaScript's `<`, `>`, `<=`, and `>=` operators perform relational comparisons. When both operands are strings, ordering is lexicographic; when either operand is not a string, the operation converts both values to numbers and compares the numeric results.

There is no strict, noncoercing form of these operators. A value that cannot become a valid number produces `NaN`, and `NaN` is neither less than nor greater than another value. Code can consequently observe both `a < b` and `a > b` as false without the values being equal.

# References

[[youdontknowjs_upandgoing.pdf]]
