2026-10-30 16:54

Status: #baby

Tags: [[Java Structured Concurrency and Scoped Context]]

# Java Nested Structured Concurrency

Nested structured concurrency places a task scope inside one of another scope's subtasks. Each nested scope owns its own children, join policy, and error handling, while its lifetime remains inside the lifetime of the outer operation.

A trip-planning operation can require both hotel and car-search branches at the outer level while each branch races or collects several providers internally. If an inner all-successful scope fails, that failure propagates through its subtask to the outer scope, keeping the hierarchy's outcome deterministic.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
