2026-09-21 22:12

Status: #baby

Tags: [[Functional Programming in C Sharp]]

# Func Delegate

`Func<TInput, TResult>` is a C# delegate type for a callable value that accepts inputs and returns a result. A filtering helper can receive `Func<decimal, bool>` as a criterion, then apply it to each discount value without knowing how the criterion was written. Passing such values makes behavior configurable at a call site and supports higher-order functions.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

