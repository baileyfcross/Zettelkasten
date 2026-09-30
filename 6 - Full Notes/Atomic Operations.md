2026-09-08 21:16

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]] [[.NET Synchronization and Thread Coordination]] [[Linux Kernel Lock-Free Synchronization]]

# Atomic Operations

An atomic operation appears indivisible to competing threads: no observer sees it half-complete. .NET's `Interlocked` operations provide atomic increments, exchanges, additions, and compare-and-swap behavior for selected primitive locations.

Atomic primitives avoid a full lock for small state transitions, but they do not automatically protect a larger invariant spanning several values. Correct lock-free design requires the entire algorithm, not just one assignment, to remain valid under every interleaving.

Interlocked operations also establish the memory-order boundary required for other threads to observe the transition consistently. That ordering guarantee is part of their synchronization role, not merely a faster spelling of arithmetic.

Linux supplies atomic integer, bitwise, exchange, and compare-exchange APIs along with specialized [[Reference Counting in the Linux Kernel|reference-count operations]]. They safely update one location, but a compound invariant across several fields still needs a lock or a proven lock-free protocol with explicit ordering.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
[[linuxkernelprogramming_secondedition.pdf]]
