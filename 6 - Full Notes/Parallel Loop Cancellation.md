2026-09-27 00:11

Status: #baby

Tags: [[.NET Data Parallelism and PLINQ]]

# Parallel Loop Cancellation

A parallel loop can receive a cancellation token through its options and cooperatively stop when the token source requests cancellation. This lets an external owner withdraw the entire operation rather than embedding application-specific stop flags in every iteration.

Cancellation is observed at safe scheduling boundaries, so some iterations may already be running. Loop bodies still need to leave shared results consistent, and callers should treat the resulting cancellation outcome separately from an algorithmic fault.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
