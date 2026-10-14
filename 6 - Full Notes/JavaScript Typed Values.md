2026-10-14 01:16

Status: #baby

Tags: [[JavaScript Core Semantics]]

# JavaScript Typed Values

JavaScript assigns types to values rather than permanently assigning a type to each variable. The same variable can therefore hold a string, number, boolean, object, or another kind of value at different points in a program.

This dynamic typing makes a variable a general container for program state, but operations still depend on the type of its current value. [[JavaScript typeof Operator|`typeof`]] observes that current value, while [[JavaScript Type Coercion|coercion]] converts a value when an operation requires another representation.

# References

[[youdontknowjs_upandgoing.pdf]]
