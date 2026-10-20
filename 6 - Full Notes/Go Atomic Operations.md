2026-10-19 01:48

Status: #baby

Tags: [[Go Concurrency and Coordination]]

# Go Atomic Operations

Go's atomic package performs indivisible loads, stores, additions, swaps, and comparisons on supported values shared between goroutines. These operations can maintain a simple counter or state flag without exposing an intermediate update.

Atomicity applies only to the particular operation and does not make a larger invariant automatically safe. When several fields or steps must change together, a [[Go Mutex]] or ownership through channels provides a clearer coordination boundary.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
