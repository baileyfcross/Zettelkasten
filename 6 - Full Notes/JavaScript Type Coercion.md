2026-10-14 01:16

Status: #baby

Tags: [[JavaScript Core Semantics]]

# JavaScript Type Coercion

JavaScript type coercion converts a value from one type to another. Explicit coercion makes the conversion visible through operations such as `Number(value)` or `String(value)`, while implicit coercion occurs as a side effect of another operation whose operands require compatible representations.

Coercion follows language rules rather than arbitrary guesswork. Multiplication can turn a numeric string into a number, a conditional can convert a value through [[JavaScript Truthiness]], and loose equality can convert operands before comparison. Understanding which conversion an operation requests is therefore more reliable than treating all implicit coercion as unpredictable.

# References

[[youdontknowjs_upandgoing.pdf]]
