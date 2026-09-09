2026-09-08 21:16

Status: #baby

Tags: [[LINQ Query Construction]]

# LINQ Where Filtering

The LINQ `Where` operator selects sequence elements that satisfy a Boolean predicate. It preserves the element type and returns a query that yields only matching values when enumerated.

Multiple filters may be chained or combined into a single predicate. With a remote provider, predicates can be translated and applied near the data source, which can greatly reduce the amount of data returned to the application.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
