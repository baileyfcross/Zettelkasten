2026-09-21 22:12

Status: #baby

Tags: [[Functional Programming in C Sharp]]

# Functional Strategy Pattern

A functional strategy supplies an interchangeable algorithm as a function value rather than as an object implementing a strategy interface. In the book's product filter, a higher-order function receives a criterion such as `p => p.ProductPrice > price` and applies it at runtime. This retains the [[Strategy Pattern]]'s separation between selection mechanism and policy while reducing class scaffolding for a small stateless behavior.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

