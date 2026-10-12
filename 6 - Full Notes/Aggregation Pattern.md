2026-09-27 00:11

Status: #baby

Tags: [[.NET Server Concurrency and Parallel Patterns]]

# Aggregation Pattern

The aggregation pattern combines partial results produced by independent parallel operations into one result. Sum, count, minimum, and grouped summaries are common examples when the combining operation can be applied incrementally.

Efficient aggregation keeps intermediate state local to workers and performs a controlled reduction instead of locking one shared accumulator for every input. Associativity makes regrouping safe; order-sensitive or nonassociative operations require a more explicit merge plan.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
