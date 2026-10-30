2026-10-30 16:54

Status: #baby

Tags: [[Java Structured Concurrency and Scoped Context]]

# Java Scoped Value Inheritance

Scoped-value inheritance makes a binding available to child threads created within its active scope, including subtasks in structured concurrency. Children observe the same immutable context without allocating and copying a separate mapping entry for every thread.

This model fits large virtual-thread populations because memory grows primarily with active bindings and scopes rather than with `threads × thread-locals`. A nested scope may rebind a key for its own descendants without modifying the outer binding.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
