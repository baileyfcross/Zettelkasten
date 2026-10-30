2026-10-30 16:54

Status: #baby

Tags: [[Java Structured Concurrency and Scoped Context]]

# Java Structured Task Scope

A Java structured task scope bounds a group of concurrent subtasks by the lexical lifetime of a block. Work is started with `fork`, coordinated with `join`, and cannot continue beyond the enclosing scope once the scope closes.

Each fork normally runs in a virtual thread and returns a typed subtask rather than an unstructured future. A [[Java Structured Concurrency Joiner]] defines when the scope has enough results, how failures affect siblings, and what `join` returns.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
