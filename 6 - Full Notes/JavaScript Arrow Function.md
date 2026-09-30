2026-09-30 00:32

Status: #baby

Tags: [[Modern JavaScript Language Features]]

# JavaScript Arrow Function

A JavaScript arrow function is a concise function expression written with `=>`. A single expression can be returned implicitly, one parameter can omit parentheses, and a multi-statement body uses braces and an explicit `return` when a result is needed.

Arrow functions preserve the surrounding `this` binding rather than creating their own. That makes an arrow callback useful inside a method when the callback must retain the method receiver, but it also means an arrow should not replace a regular method when the method itself needs a dynamically bound `this`.

# References

[[learningreact1.pdf]]
