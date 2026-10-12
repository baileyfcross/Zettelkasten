2026-09-21 22:12

Status: #baby

Tags: [[Functional Programming in C Sharp]] [[Functional JavaScript Programming]]

# Pure Function

A pure function produces the same result for the same arguments and has no externally observable side effects. The book's discount calculation depends on price and discount inputs rather than changing inventory state, so it can be tested with ordinary input-output examples. Purity does not prove that the inputs are valid business values; that separate concern can be represented through validation or a constrained input type.

In JavaScript, purity also means treating arguments as [[JavaScript Immutability|immutable data]] and returning a new value rather than changing a shared object, global variable, or DOM node. This makes the required inputs controllable in a test and keeps the transformation separate from the code that performs external effects.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

[[learningreact1.pdf]]
