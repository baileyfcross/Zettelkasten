2026-10-14 01:16

Status: #baby

Tags: [[JavaScript Core Semantics]]

# JavaScript Truthiness

JavaScript truthiness describes how a non-boolean value behaves when an operation coerces it to a boolean. The falsy values are the empty string, `0`, `-0`, `NaN`, `null`, `undefined`, and `false`; values outside that set are truthy.

Truthiness applies only when a boolean conversion actually occurs, as in an `if` test or a logical condition. Empty arrays and empty objects are therefore truthy despite appearing to contain nothing, because their object references are not members of the falsy set.

# References

[[youdontknowjs_upandgoing.pdf]]
