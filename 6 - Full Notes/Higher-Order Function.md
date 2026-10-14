2026-09-21 22:12

Status: #baby

Tags: [[Functional Programming in C Sharp]] [[Functional JavaScript Programming]]

# Higher-Order Function

A higher-order function accepts a function as an argument or returns one as a result. The book's simplified `Where` method accepts a `Func<T, bool>` criterion and yields only elements for which that criterion succeeds. The traversal stays fixed while the caller supplies the variable behavior, avoiding a separate filtering class for every rule.

JavaScript array methods such as map, filter, and reduce are higher-order because they accept transformation or predicate functions. A returned function can retain an earlier argument, as when a logging factory captures a username and later accepts messages; this supports currying, reusable callbacks, and [[Function Composition|composition]].

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

[[learningreact1.pdf]]
