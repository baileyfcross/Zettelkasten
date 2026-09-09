2026-09-08 21:16

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]]

# Atomic Operations

An atomic operation appears indivisible to competing threads: no observer sees it half-complete. .NET's `Interlocked` operations provide atomic increments, exchanges, additions, and compare-and-swap behavior for selected primitive locations.

Atomic primitives avoid a full lock for small state transitions, but they do not automatically protect a larger invariant spanning several values. Correct lock-free design requires the entire algorithm, not just one assignment, to remain valid under every interleaving.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
