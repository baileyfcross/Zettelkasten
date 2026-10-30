2026-10-30 16:54

Status: #baby

Tags: [[Java Structured Concurrency and Scoped Context]]

# Java Custom Structured Joiner

A custom Java structured joiner implements application-specific completion and aggregation rules. Its completion callback can collect successful results, count failures, or stop after the first `n` successes, while its result method returns the final protected aggregate.

Completion callbacks may run concurrently, so their state must be thread-safe. A concurrent queue is suitable for frequent parallel writes; a copy-on-write list fits only a small result set. Returning an immutable copy prevents callers from mutating the joiner's internal state after the scope ends.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
