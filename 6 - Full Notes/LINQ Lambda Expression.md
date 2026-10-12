2026-09-08 21:16

Status: #baby

Tags: [[LINQ Query Construction]] [[Functional Programming in C Sharp]]

# LINQ Lambda Expression

A lambda expression is a compact anonymous function commonly supplied to LINQ operators as a predicate, selector, key function, or accumulator. Its parameters represent items flowing through the query, and its body describes the operation to apply.

The same syntax may compile to a delegate for in-memory execution or to an expression tree for provider translation. That contextual conversion is central to LINQ's ability to present one query style across very different data sources.

The inventory example passes a lambda as a product-price criterion to a filtering operation. The filtering mechanism remains unchanged while the lambda expresses the caller's selected business rule, illustrating a functional form of strategy selection.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
[[hands-ondesignpatternswithcandnetcore.pdf]]
