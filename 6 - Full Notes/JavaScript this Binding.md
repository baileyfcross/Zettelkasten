2026-10-14 01:16

Status: #baby

Tags: [[JavaScript Core Semantics]]

# JavaScript this Binding

JavaScript determines a function's `this` value from how the function is called, not from where the function was written and not from the function itself. Understanding `this` therefore requires examining the call site.

The source introduces four call forms: a plain call uses the global object in non-strict mode and `undefined` in [[JavaScript Strict Mode|strict mode]]; a method call binds the receiver object; `call` can supply an object explicitly; and a call with `new` binds a newly created object. The same function can consequently observe different `this` values at different calls.

# References

[[youdontknowjs_upandgoing.pdf]]
