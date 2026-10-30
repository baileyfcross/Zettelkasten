2026-10-30 16:54

Status: #baby

Tags: [[Java Structured Concurrency and Scoped Context]]

# Java Scoped Value vs ThreadLocal

A Java `ThreadLocal` stores a mutable mapping on each thread and normally requires explicit cleanup, whereas a [[Java Scoped Value]] exposes an immutable binding with a bounded lifetime. Inheritable thread-local context also copies mappings into child threads; scoped values share a binding through the task scope.

The difference becomes significant with hundreds of thousands of virtual threads. Per-thread mappings multiply memory and leak risk, while scoped values suit read-only request context. Thread-local storage remains appropriate only when the application truly requires thread-specific mutable state and manages its removal deliberately.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
