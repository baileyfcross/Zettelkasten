2026-10-14 01:16

Status: #baby

Tags: [[JavaScript Core Semantics]]

# Immediately Invoked Function Expression

An immediately invoked function expression, or IIFE, is a function expression followed directly by `()` so it executes as soon as it is created. Surrounding parentheses force the function to be parsed as an expression rather than as an ordinary declaration.

Because the invoked function creates a scope, an IIFE can hold variables without adding them to the surrounding scope. It can also return a value to the larger expression. This older organizational pattern uses the same [[First-Class Function|first-class function]] behavior that allows a function reference to participate in an expression.

# References

[[youdontknowjs_upandgoing.pdf]]
