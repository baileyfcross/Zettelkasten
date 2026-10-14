2026-09-30 00:32

Status: #baby

Tags: [[Modern JavaScript Language Features]]

# JavaScript Block-Scoped Variable

ES6 adds `const` and `let` as alternatives to `var`. A `const` binding cannot be reassigned, while a `let` binding is limited to the nearest brace-delimited block rather than leaking from an `if` statement or loop into the surrounding function or global scope.

Block scoping also changes what a callback captures during a loop. Declaring the loop counter with `let` gives each iteration its own scoped value, so later click handlers observe the index from the iteration that created them instead of the final value of one shared `var` binding.

# References

[[learningreact1.pdf]]
