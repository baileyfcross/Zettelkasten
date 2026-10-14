2026-10-14 01:16

Status: #baby

Tags: [[JavaScript Core Semantics]]

# JavaScript typeof Operator

The JavaScript `typeof` operator returns a string describing the type of a value. Applied to a variable, it reports the type of the value currently stored there rather than a fixed type belonging to the variable itself.

Its categories have important limits. Functions report `"function"`, while arrays report `"object"`; `null` also reports `"object"` because of a long-standing language bug. The operator is therefore useful for broad classification but cannot by itself distinguish every JavaScript value shape.

# References

[[youdontknowjs_upandgoing.pdf]]
