2026-09-08 21:16

Status: #baby

Tags: [[LINQ Query Construction]]

# LINQ Aggregation

Aggregation reduces a sequence to a summary value. Operators such as `Count`, `Sum`, `Average`, `Min`, and `Max` express common summaries, while `Aggregate` carries a custom accumulator across the elements.

Empty sequences and numeric types affect the behavior of an aggregate, so callers should understand each operator's return and failure rules. With a query provider, aggregation is often translated so the data source computes the result without returning every row.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
