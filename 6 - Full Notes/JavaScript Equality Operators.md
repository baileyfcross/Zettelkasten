2026-10-14 01:16

Status: #baby

Tags: [[JavaScript Core Semantics]]

# JavaScript Equality Operators

JavaScript's `==` operator compares values while allowing type coercion, whereas `===` compares without allowing coercion. The paired non-equality forms are `!=` and `!==`; the distinction is therefore coercing versus noncoercing equality, not simply value versus value-and-type equality.

Loose equality is safest when the possible operand types are understood. The source recommends strict equality when either side may be boolean or may contain troublesome coercion cases such as `0`, an empty string, or an empty array. For objects and arrays, both forms reduce to [[JavaScript Reference Equality|reference comparison]].

# References

[[youdontknowjs_upandgoing.pdf]]
