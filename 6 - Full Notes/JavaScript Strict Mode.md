2026-10-14 01:16

Status: #baby

Tags: [[JavaScript Core Semantics]]

# JavaScript Strict Mode

JavaScript strict mode opts code into a more restrictive set of language rules with the `"use strict"` directive. Placing the directive inside a function limits it to that function and nested code, while placing it at file scope applies it across the file.

One important restriction is that assigning to an undeclared name throws a `ReferenceError` instead of silently creating a global property. Strict mode therefore exposes unsafe assumptions, supports more predictable optimization, and changes some call behavior, including making `this` undefined for an unbound plain function call.

# References

[[youdontknowjs_upandgoing.pdf]]
