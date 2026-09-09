2026-09-08 21:16

Status: #baby

Tags: [[LINQ Query Construction]]

# LINQ Query Provider

A LINQ query provider interprets a query expression for a particular data source. In-memory sequences execute delegates through `IEnumerable<T>`, while `IQueryable<T>` providers inspect expression trees and may translate them into SQL or another remote query language.

This distinction explains why not every .NET method can be used in a database query and why execution behavior varies by source. Provider-backed queries should be evaluated for their generated operations, not assumed to behave like ordinary in-memory loops.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
