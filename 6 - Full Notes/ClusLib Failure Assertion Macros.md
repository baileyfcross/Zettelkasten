2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Build and Testing]]

# ClusLib Failure Assertion Macros

The FAIL macro always throws a ClusLib Error, while ASSERT throws only when its condition is false. Both capture the current source file, line, and enclosing function and append a caller-supplied message.

These macros centralize diagnostic formatting and keep parameter checks concise. They should enforce programmer and input invariants, not replace recoverable control flow whose alternatives belong in ordinary code.

# References

[[dataclusteringincplusplus.pdf]]

