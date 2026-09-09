2026-09-08 21:16

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]]

# Sequential and Concurrent Tasks

Sequential tasks finish one unit of work before starting the next, preserving an obvious order and simple access to shared state. Concurrent tasks make progress during overlapping periods and can improve throughput or responsiveness when their work is independent.

Concurrency is useful only when the workload and dependencies permit it. Coordination, scheduling, and contention add costs, so independent operations should be identified explicitly and performance should be measured rather than inferred from the number of tasks.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
