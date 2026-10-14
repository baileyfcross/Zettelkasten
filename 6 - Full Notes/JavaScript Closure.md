2026-10-14 01:16

Status: #baby

Tags: [[JavaScript Core Semantics]]

# JavaScript Closure

A JavaScript closure lets a function continue to access variables from the [[JavaScript Lexical Scope|lexical scope]] in which it was created after the enclosing function has finished running. Returning an inner function therefore preserves the particular outer values captured by that invocation.

Calling the outer function multiple times creates separate retained environments. An adder factory can return one function that remembers `1` and another that remembers `10`, even though both functions share the same code. This retained private state is the foundation of the [[JavaScript Module Pattern]].

# References

[[youdontknowjs_upandgoing.pdf]]
