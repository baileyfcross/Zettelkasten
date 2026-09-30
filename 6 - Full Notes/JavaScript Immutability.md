2026-09-30 00:32

Status: #baby

Tags: [[Functional JavaScript Programming]]

# JavaScript Immutability

JavaScript immutability is the practice of producing a changed copy instead of modifying the input object or array. `Object.assign` or object spread can replace a field on a copy, while `concat`, `filter`, `map`, or array spread can produce a new array without changing the original.

Keeping the prior value intact makes a transformation easier to inspect and supports [[Pure Function|pure functions]]. It is a programming discipline rather than a guarantee imposed on every JavaScript value: the operation must deliberately avoid methods such as `push`, `splice`, or an in-place `reverse` on the shared input.

# References

[[learningreact1.pdf]]
