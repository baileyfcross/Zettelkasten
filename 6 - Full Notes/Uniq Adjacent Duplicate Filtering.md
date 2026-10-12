2026-10-12 00:45

Status: #baby

Tags: [[Unix Text Stream Filters]]

# Uniq Adjacent Duplicate Filtering

The `uniq` utility compares adjacent lines and can collapse repeated runs, display only duplicates or unique lines, and prefix groups with counts. It does not discover equal lines that are separated elsewhere in the input.

When the goal is to count all identical records, the input is commonly normalized and passed through [[Sort Text Ordering]] first. That pipeline changes original order, so order-preserving deduplication requires a different strategy.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
