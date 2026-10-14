2026-10-14 01:16

Status: #baby

Tags: [[JavaScript Core Semantics]]

# JavaScript Lexical Scope

JavaScript lexical scope determines variable access from the nested structure of source code. A function can use names declared in its own scope and in enclosing outer scopes, but an outer function cannot reach variables declared only inside a nested function.

Each function creates its own scope, and ES6 `let` declarations can create finer-grained block scope. This one-way lookup explains how a nested function can retain outer data through a [[JavaScript Closure]] while keeping its own internal variables unavailable to surrounding code.

# References

[[youdontknowjs_upandgoing.pdf]]
