2026-09-06 22:09

Status: #baby

Tags: [[Scalable Social Data Processing]]

# High-Level Dataflow System

A high-level dataflow system lets a user describe transformations while a compiler constructs the lower-level parallel execution plan. Parsing, semantic checks, logical optimization, and physical planning separate the requested data operations from the runtime that performs them.

This abstraction makes large workflows easier to express and maintain. Its performance still depends on generated jobs, storage scans, data movement, caching, and whether repeated computations are visible to the runtime.

# References

[[bigdataincomplexandsocialnetworks.pdf]]
